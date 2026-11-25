// Mécanismes d'interface partagés (inspirés de patch.io) : carrousel, étapes en orbite, onglets à progression,
// texte qui s'éclaire au défilement, barre d'action mobile.
window.MECA = (function () {
  var reduit = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Carrousel horizontal aligné sur la colonne de contenu, avec flèches
  function carrousel(el, html, prec, suiv) {
    el.innerHTML = html;
    el.classList.add('rail');
    var p = document.getElementById(prec), s = document.getElementById(suiv);
    if (s) s.onclick = function () { el.scrollBy({ left: 320, behavior: 'smooth' }); };
    if (p) p.onclick = function () { el.scrollBy({ left: -320, behavior: 'smooth' }); };
  }

  // Étapes qui avancent seules + schéma en orbite (#etapes, #liens, #noeuds)
  function orbite(E, opts) {
    opts = opts || {};
    var ol = document.getElementById('etapes'); if (!ol) return;
    var clair = !ol.closest('.bg-navy-900');
    ol.innerHTML = E.map(function (e, i) {
      return '<li class="etape cursor-pointer pt-4 pb-4" data-i="' + i + '"><div class="progres mb-4"><i></i></div><p class="text-lg"><span class="' + (clair ? 'text-navy-400' : 'text-glacier-300') + ' mr-2 text-sm">0' + (i + 1) + '</span>' + e[0] + '</p><p class="texte hidden mt-2 ' + (clair ? 'text-navy-600' : 'text-cream-200') + ' max-w-[42ch] leading-relaxed">' + e[1] + '</p></li>';
    }).join('');
    var cx = 300, cy = 300, r = 200, n = E.length;
    var pts = E.map(function (e, i) { var a = -Math.PI / 2 + i * 2 * Math.PI / n; return [cx + r * Math.cos(a), cy + r * Math.sin(a)]; });
    var li = '';
    pts.forEach(function (p, i) { var q = pts[(i + 2) % n]; li += '<line x1="' + p[0] + '" y1="' + p[1] + '" x2="' + q[0] + '" y2="' + q[1] + '"/><line x1="' + p[0] + '" y1="' + p[1] + '" x2="' + cx + '" y2="' + cy + '" stroke-dasharray="2 5"/>'; });
    var L = document.getElementById('liens'), N = document.getElementById('noeuds');
    if (L) L.innerHTML = li;
    if (N) N.innerHTML = pts.map(function (p, i) { var h = p[1] < cy, lib = '0' + (i + 1) + ' · ' + E[i][0], w = Math.round(24 + lib.length * 7.4); return '<g><circle cx="' + p[0] + '" cy="' + p[1] + '" r="18" fill="#0F2030" stroke="rgba(129,207,216,.6)"/><rect x="' + (p[0] - w / 2) + '" y="' + (p[1] + (h ? -58 : 28)) + '" width="' + w + '" height="28" rx="6" fill="#fff"/><text x="' + p[0] + '" y="' + (p[1] + (h ? -39 : 47)) + '" text-anchor="middle" fill="#0B1D2E" font-size="13" font-family="Albert Sans, system-ui, sans-serif">' + lib + '</text></g>'; }).join('');
    var actif = 0, t;
    function etape(i) {
      actif = i;
      ol.querySelectorAll('.etape').forEach(function (el, k) { var on = k === i; el.classList.toggle('actif', on); el.querySelector('.texte').classList.toggle('hidden', !on); el.querySelector('p').style.opacity = on ? 1 : .5; var b = el.querySelector('.progres i'); b.style.animation = 'none'; b.offsetWidth; b.style.animation = ''; });
      if (N) N.querySelectorAll('circle').forEach(function (c, k) { c.setAttribute('fill', k === i ? '#E3262F' : '#0F2030'); });
      clearTimeout(t); if (!reduit) t = setTimeout(function () { etape((actif + 1) % n); }, opts.duree || 6000);
    }
    ol.querySelectorAll('.etape').forEach(function (el) { el.onclick = function () { etape(+el.dataset.i); }; });
    etape(0);
  }

  // Onglets à progression qui changent l'image (#onglets, #onglet-img, #onglet-tag)
  function onglets(O, sombre) {
    var box = document.getElementById('onglets'); if (!box) return;
    box.innerHTML = O.map(function (o, i) {
      return '<div class="onglet cursor-pointer" data-i="' + i + '" style="--d:7s"><div class="progres mb-5"><i></i></div><p class="text-xl">' + o.t + '</p><p class="mt-2 ' + (sombre ? 'text-cream-300' : 'text-navy-600') + ' leading-relaxed">' + o.d + '</p>' + (o.lien ? '<a href="' + o.lien + '" class="inline-block mt-3 text-sm underline underline-offset-4 ' + (sombre ? 'text-white/80 hover:text-white' : 'text-navy-700 hover:text-navy-900') + '">En savoir plus</a>' : '') + '</div>';
    }).join('');
    var im = document.getElementById('onglet-img'), tag = document.getElementById('onglet-tag'), oa = 0, t;
    function onglet(i) {
      oa = i;
      if (im) { im.style.opacity = 0; setTimeout(function () { im.src = O[i].img; im.style.opacity = 1; }, 250); }
      if (tag) tag.textContent = O[i].tag || '';
      box.querySelectorAll('.onglet').forEach(function (el, k) { var on = k === i; el.classList.toggle('actif', on); el.style.opacity = on ? 1 : .5; var b = el.querySelector('.progres i'); b.style.animation = 'none'; b.offsetWidth; b.style.animation = ''; });
      clearTimeout(t); if (!reduit) t = setTimeout(function () { onglet((oa + 1) % O.length); }, 7000);
    }
    box.querySelectorAll('.onglet').forEach(function (el) { el.onclick = function (e) { if (e.target.tagName !== 'A') onglet(+el.dataset.i); }; });
    onglet(0);
  }

  // Texte qui s'éclaire mot à mot au défilement
  var aEclairer = [];
  function eclaire(el) {
    if (!el) return;
    el.innerHTML = el.textContent.trim().split(/\s+/).map(function (w) { return '<span style="transition:opacity .3s">' + w + '</span>'; }).join(' ');
    aEclairer.push(el); maj();
  }
  function maj() {
    aEclairer.forEach(function (el) {
      var mots = el.querySelectorAll('span'), b = el.getBoundingClientRect(), h = innerHeight;
      var t = reduit ? 1 : Math.min(1, Math.max(0, (h * 0.85 - b.top) / (h * 0.6)));
      var n = Math.round(t * mots.length); mots.forEach(function (s, k) { s.style.opacity = k < n ? 1 : .18; });
    });
  }

  // Barre d'action mobile : visible après le premier écran, cachée sur le pied de page
  var barres = [];
  function barreMobile(barre, hero) { if (barre) { barres.push([barre, hero]); majBarres(); } }
  function majBarres() {
    var pied = document.querySelector('body > footer');
    barres.forEach(function (b) {
      var bas = b[1] ? b[1].getBoundingClientRect().bottom : 0;
      var fin = pied && pied.getBoundingClientRect().top < innerHeight;
      b[0].style.transform = (bas < 0 && !fin) ? 'translateY(0)' : '';
    });
  }
  addEventListener('scroll', function () { maj(); majBarres(); }, { passive: true });

  return { carrousel: carrousel, orbite: orbite, onglets: onglets, eclaire: eclaire, barreMobile: barreMobile };
})();
