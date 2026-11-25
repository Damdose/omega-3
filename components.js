// Shared nav and footer for all pages
(function() {
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';

  function isActive(page) {
    if (page === 'blog.html' && (currentPage === 'blog.html' || currentPage === 'article.html')) return true;
    if (page === 'produits-dropdown' && (currentPage === 'omega-de-confiance.html' || currentPage === 'produit-omega3.html')) return true;
    return currentPage === page;
  }

  const CATS = [
    ['boutique.html?cat=omega3', 'Oméga-3'],
    ['boutique.html?cat=tests', 'Tests à domicile'],
    ['boutique.html?cat=programmes', 'Programmes'],
    ['boutique.html?cat=vitamines', 'Vitamines et forme'],
    ['boutique.html?cat=beaute', 'Beauté'],
    ['boutique.html?cat=coffrets', 'Coffrets de Noël'],
  ];
  const catActive = new URLSearchParams(location.search).get('cat');
  const ico = {
    loupe: '<svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path stroke-linecap="round" d="m20 20-3.5-3.5"/></svg>',
    sac: '<svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linejoin="round" d="M5 8h14l-1 12H6L5 8Z"/><path stroke-linecap="round" d="M9 8V6a3 3 0 0 1 6 0v2"/></svg>',
    equipe: '<svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true"><circle cx="9" cy="8" r="3.2"/><path stroke-linecap="round" d="M3.5 19c.8-3 3-4.6 5.5-4.6s4.7 1.6 5.5 4.6"/><path stroke-linecap="round" d="M16 5.5a3 3 0 0 1 0 5.6M18 14.8c1.3.7 2.1 2 2.5 4.2"/></svg>',
  };

  // Deux modes : la vitrine (tout le site) et la page d'atterrissage partenaire (pubs), sans fuite
  const isLP = currentPage === 'partenaire.html' || currentPage === 'merci.html';

  function getBandeau() { return ''; }

  const fleche = '<svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M5 12h14m-6-6 6 6-6 6"/></svg>';
  const marque = (lien) => `<a href="${lien}" class="flex items-center gap-2.5 shrink-0" aria-label="Accueil"><img src="assets/images/eqology-eq.png" alt="Eqology" style="height:24px;width:auto"><span class="block text-[11px] sm:text-[12.5px] leading-tight text-nuit/60 border-l border-nuit/15 pl-2 sm:pl-2.5">Yves Coignard<br>distributeur indépendant</span></a>`;

  function getNavLP() {
    return `<div class="max-w-[1400px] mx-auto"><div class="bg-white rounded-lg shadow-[0_8px_30px_rgba(11,29,46,.12)] h-14 sm:h-[58px] flex items-center justify-between pl-4 pr-2 sm:pl-5 sm:pr-3">
      ${marque('#')}
      ${currentPage === 'merci.html' ? '' : `<a href="#rappel" class="btn btn-plein !min-h-[40px] !text-sm">Être rappelé</a>`}
    </div></div>`;
  }

  function getNav() {
    const lien = (h, t) => `<a href="${h}" class="hover:opacity-60 transition-opacity ${(h === currentPage || (h === 'boutique.html' && (currentPage === 'boutique.html' || currentPage === 'produit.html'))) ? 'underline underline-offset-[6px] decoration-1' : ''}">${t}</a>`;
    return `<div class="max-w-[1400px] mx-auto">
      <div class="bg-white rounded-lg shadow-[0_8px_30px_rgba(11,29,46,.12)] h-14 sm:h-[58px] flex items-center justify-between gap-4 pl-4 pr-2 sm:pl-5 sm:pr-3 text-navy-900">
        ${marque('index.html')}
        <div class="hidden lg:flex items-center gap-8 text-[17px] font-normal">
          ${lien('boutique.html', 'Boutique')}${lien('le-test.html', 'Le test')}${lien('index.html#en-bref', 'Qui est Eqology')}${lien('partenaire.html', 'Devenir partenaire')}
        </div>
        <div class="flex items-center gap-1 sm:gap-3">
          <a href="contact.html" class="hidden md:inline text-[17px] font-normal hover:opacity-60">Contact</a>
          ${currentPage === 'partenaire.html' ? `<a href="#rappel" class="btn btn-plein"><span class="sm:hidden">Rappel</span><span class="hidden sm:inline">Être rappelé par Yves</span></a>` : `<a href="le-test.html" class="btn btn-plein"><span class="sm:hidden">Le test</span><span class="hidden sm:inline">Commencer par le test</span></a>`}
          <button id="mobile-menu-btn" class="lg:hidden w-10 h-10 grid place-items-center rounded-lg hover:bg-cream-100" aria-label="Ouvrir le menu" aria-expanded="false" aria-controls="mobile-menu">
            <svg width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" d="M4 8h16M4 16h16"/></svg>
          </button>
        </div>
      </div>
      <div id="mobile-menu" class="hidden lg:hidden mt-2 bg-white rounded-lg shadow-xl p-2 text-navy-900 max-h-[75vh] overflow-y-auto">
        ${[['boutique.html', 'Boutique'], ['le-test.html', 'Le test'], ['index.html#en-bref', 'Qui est Eqology'], ['partenaire.html', 'Devenir partenaire'], ['contact.html', 'Contact']].map(([h, t]) => `<a href="${h}" class="block px-3 py-3.5 text-lg border-b border-cream-200 last:border-0">${t}</a>`).join('')}
        <p class="px-3 pt-4 pb-1 text-sm text-navy-400">Rayons</p>
        ${CATS.map(([h, t]) => `<a href="${h}" class="block px-3 py-2 text-[15px] ${t.startsWith('Coffrets') ? 'text-rouge' : 'text-navy-700'}">${t}</a>`).join('')}
      </div>
    </div>`;
  }

  function getFooterLP() {
    return `<div class="wrap py-8 flex flex-col sm:flex-row items-center justify-between gap-4 text-sm text-cream-400">
      <p>© 2026 ZENCO SAS · Yves Coignard, distributeur indépendant Eqology</p>
      <div class="flex gap-5"><a href="mentions-legales.html" class="hover:text-white">Mentions légales</a><a href="confidentialite.html" class="hover:text-white">Confidentialité</a></div>
    </div>`;
  }

  function getFooter() {
    const col = (titre, liens) => `<div><p class="text-white/50 pb-3 mb-4 border-b border-white/10">${titre}</p><ul class="space-y-3">${liens.map(([h, t]) => `<li><a href="${h === 'data:trustpilot' ? '#' : h}" ${h === 'data:trustpilot' ? 'data-trustpilot target="_blank" rel="noopener"' : ''} class="hover:opacity-60">${t}</a></li>`).join('')}</ul></div>`;
    return `<div class="wrap">
      <div class="flex flex-col md:flex-row md:items-center justify-between gap-5 pb-10 border-b border-white/10">
        <p class="h2">Une question&nbsp;? Yves vous répond.</p>
        <a href="contact.html" class="btn btn-plein self-start">Écrire à Yves</a>
      </div>
      <div class="grid grid-cols-2 md:grid-cols-4 gap-8 py-10 text-[15px]">
        ${col('Boutique', CATS.slice(0, 6))}
        ${col('Comprendre', [['le-test.html', 'Le test oméga-3'], ['science-omega3.html', 'La science'], ['blog.html', 'Articles'], ['index.html#en-bref', 'Qui est Eqology']])}
        ${col('Partenariat', [['partenaire.html', 'Devenir partenaire'], ['partenaire.html#rappel', 'Être rappelé'], ['partenaire.html#questions', 'Questions fréquentes']])}
        ${col('Yves Coignard', [['contact.html', 'Contact'], ['mentions-legales.html', 'Mentions légales'], ['confidentialite.html', 'Confidentialité'], ['data:trustpilot', 'Avis Trustpilot']])}
      </div>
      <div class="border-t border-white/10 py-10"><img src="assets/v2/eqology-logo-blanc.png" alt="Eqology" class="w-full h-auto opacity-95" loading="lazy" width="1300" height="205"></div>
      <div class="border-t border-white/10 py-6 flex flex-col md:flex-row justify-between gap-3 text-sm text-white/50">
        <p>© 2026 ZENCO SAS · Yves Coignard, distributeur indépendant Eqology</p>
        <p>Commandes, paiement et livraison assurés par Eqology.</p>
      </div>
    </div>`;
  }

  // Inject nav and footer
  const nav = document.querySelector('nav#entete') || document.querySelector('nav.fixed');
  if (nav) {
    nav.innerHTML = getNav();
    nav.className = 'fixed top-0 inset-x-0 z-50 px-3 pt-3 sm:px-6 sm:pt-5';
    if (nav.id === 'entete') {
      const main = document.querySelector('main');
      if (main && !document.querySelector('[data-plein]')) main.style.paddingTop = '88px';
    }
  }

  const footer = document.querySelector('body > footer');
  if (footer) { footer.innerHTML = getFooter(); if (nav && nav.id === 'entete') footer.className = 'bg-nuit text-white border-t border-white/10 pt-16'; }
  document.querySelectorAll('[data-trustpilot]').forEach(function (a) { if (window.SITE) a.href = window.SITE.trustpilot; });

  // Cookie consent banner
  if (!localStorage.getItem('cookies_accepted')) {
    const banner = document.createElement('div');
    banner.id = 'cookie-banner';
    banner.className = 'fixed bottom-3 left-3 right-3 sm:right-auto sm:left-5 sm:bottom-5 z-[60] sm:max-w-md bg-nuit-2 text-white border border-white/15 rounded-lg shadow-2xl shadow-black/40 p-4 sm:p-5';
    banner.innerHTML = `
      <p class="text-sm leading-relaxed text-cream-200">Avec votre accord, nous mesurons les visites venues de nos publicités (pixel Meta). Rien n'est déposé si vous refusez. <a href="confidentialite.html" class="underline text-white">En savoir plus</a></p>
      <div class="mt-3 flex gap-2">
        <button id="cookie-accept" class="h-9 px-4 rounded-md bg-white text-navy-900 text-sm font-medium hover:bg-cream-100">Accepter</button>
        <button id="cookie-refuse" class="h-9 px-4 rounded-md border border-white/40 text-sm hover:border-white">Refuser</button>
      </div>
    `;
    document.body.appendChild(banner);

    document.getElementById('cookie-accept').addEventListener('click', function() {
      localStorage.setItem('cookies_accepted', 'true');
      banner.remove();
      if (window.chargerPixel) window.chargerPixel();
    });
    document.getElementById('cookie-refuse').addEventListener('click', function() {
      localStorage.setItem('cookies_accepted', 'refused');
      banner.remove();
    });
  }

  // Mobile menu toggle
  setTimeout(function() {
    var btn = document.getElementById('mobile-menu-btn');
    var menu = document.getElementById('mobile-menu');
    if (btn && menu) {
      btn.onclick = function() {
        if (menu.style.display === 'none' || menu.classList.contains('hidden')) {
          menu.classList.remove('hidden');
          menu.style.display = 'block';
          btn.setAttribute('aria-expanded', 'true');
        } else {
          menu.classList.add('hidden');
          menu.style.display = 'none';
          btn.setAttribute('aria-expanded', 'false');
        }
      };
    }
  }, 100);

  // Reveal animations (IntersectionObserver)
  const revealElements = document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .reveal-scale, .monte');
  if (revealElements.length) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => { if (entry.isIntersecting) { entry.target.classList.add('visible', 'vu'); } });
    }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });
    revealElements.forEach(el => observer.observe(el));
  }
})();
