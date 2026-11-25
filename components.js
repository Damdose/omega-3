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


  // En-tête « boutique » (bandeau, recherche, rayons) : pages en <body data-entete="boutique">
  function getNavBoutique() {
    const ancreYves = document.getElementById('yves') ? '#yves' : 'index.html#yves';
    const rayon = ([h, t]) => { const on = h.endsWith('=' + catActive); const noel = t.startsWith('Coffrets');
      return `<a href="${h}" class="px-3 py-1.5 rounded-[8.5px] transition-colors ${on ? 'bg-nuit text-white' : noel ? 'text-[#A3342C] hover:bg-[#F6EEE9]' : 'text-nuit/80 hover:bg-sable'}">${t}</a>`; };
    return `
    <div class="bg-nuit text-white/85 text-[13px]">
      <div class="wrap h-9 flex items-center justify-between gap-4">
        <p class="truncate"><a href="boutique.html?cat=coffrets" class="text-glacier-300 hover:underline">Coffrets de Noël disponibles</a><span class="hidden sm:inline"> · Livraison offerte par Eqology dès deux produits de plus de 60&nbsp;€</span></p>
        <a href="partenaire.html" class="shrink-0 hover:text-white">Devenir partenaire →</a>
      </div>
    </div>
    <div class="bg-white text-nuit border-b border-nuit/10">
      <div class="wrap h-16 lg:h-[76px] flex items-center gap-3 lg:gap-8">
        <button id="mobile-menu-btn" class="lg:hidden -ml-2 w-11 h-11 grid place-items-center rounded-[8.5px] hover:bg-sable" aria-label="Ouvrir le menu" aria-expanded="false" aria-controls="mobile-menu">
          <svg width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" d="M4 8h16M4 16h16"/></svg>
        </button>
        ${marque('index.html')}
        <form action="boutique.html" class="hidden md:flex flex-1 max-w-xl items-center gap-2 h-11 px-4 rounded-[8.5px] bg-sable border border-transparent focus-within:border-glacier-500 focus-within:bg-white transition-colors" role="search">
          <span class="text-nuit/50">${ico.loupe}</span>
          <input name="q" type="search" placeholder="Rechercher un produit : oméga-3, vitamine D, test…" class="flex-1 bg-transparent outline-none text-[15px] placeholder:text-nuit/50" aria-label="Rechercher un produit">
        </form>
        <div class="ml-auto flex items-center gap-1 sm:gap-2">
          <a href="partenaire.html" class="hidden lg:inline-flex items-center gap-2 h-11 px-3 text-[15px] hover:opacity-70">${ico.equipe}Devenir partenaire</a>
          <a href="boutique.html" class="md:hidden w-11 h-11 grid place-items-center rounded-[8.5px] hover:bg-sable" aria-label="Rechercher">${ico.loupe}</a>
          <a href="boutique.html" class="btn !min-h-[44px] !px-4 bg-nuit text-white hover:bg-nuit-2">${ico.sac}<span class="hidden sm:inline">La boutique</span></a>
        </div>
      </div>
      <div class="hidden lg:block border-t border-nuit/10">
        <div class="wrap h-12 flex items-center gap-1 text-[15px]">
          ${CATS.map(rayon).join('')}
          <span class="mx-2 h-4 w-px bg-nuit/15"></span>
          <a href="le-test.html" class="px-3 py-1.5 rounded-[8.5px] text-nuit/80 hover:bg-sable">Comprendre le test</a>
          <a href="${ancreYves}" class="px-3 py-1.5 rounded-[8.5px] text-nuit/80 hover:bg-sable">Qui suis-je</a>
        </div>
      </div>
    </div>
    <div id="mobile-menu" class="hidden lg:hidden absolute inset-x-0 top-full bg-white text-nuit border-b border-nuit/10 shadow-xl max-h-[80vh] overflow-y-auto">
      <div class="wrap py-4">
        <form action="boutique.html" class="flex items-center gap-2 h-12 px-4 rounded-[8.5px] bg-sable mb-3" role="search">
          <span class="text-nuit/50">${ico.loupe}</span>
          <input name="q" type="search" placeholder="Rechercher un produit" class="flex-1 bg-transparent outline-none text-base" aria-label="Rechercher un produit">
        </form>
        <p class="mono text-nuit/60 px-2 mt-4 mb-1">La boutique</p>
        ${CATS.map(([h, t]) => `<a href="${h}" class="block px-2 py-3 text-base border-b border-nuit/5 ${t.startsWith('Coffrets') ? 'text-[#A3342C]' : ''}">${t}</a>`).join('')}
        <a href="le-test.html" class="block px-2 py-3 text-base border-b border-nuit/5">Comprendre le test</a>
        <a href="${ancreYves}" class="block px-2 py-3 text-base">Qui suis-je</a>
        <a href="partenaire.html" class="btn btn-plein w-full mt-4 !min-h-[48px]">Devenir partenaire</a>
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
    const enteteBoutique = document.body.dataset.entete === 'boutique';
    nav.innerHTML = enteteBoutique ? getNavBoutique() : getNav();
    nav.className = enteteBoutique ? 'sticky top-0 z-50' : 'fixed top-0 inset-x-0 z-50 px-3 pt-3 sm:px-6 sm:pt-5';
    if (nav.id === 'entete') {
      const main = document.querySelector('main');
      if (main && !document.querySelector('[data-plein]') && document.body.dataset.entete !== 'boutique') main.style.paddingTop = '88px';
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
  // Les blocs des sections apparaissent en douceur, en cascade (sauf l'écran d'ouverture et les formulaires)
  if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    const cibles = 'main > section .filet, main > section ol > li, main > section .grid > a, main > section .grid > div, main > section .grid > li, main > section #ventes > *, main > section .rounded-xl.overflow-hidden, main > section ul.grid > li';
    document.querySelectorAll(cibles).forEach(el => {
      if (el.closest('form') || el.closest('header') || el.classList.contains('monte')) return;
      if (el.querySelector('form') || el.getBoundingClientRect().top < window.innerHeight * 0.85) return;
      const freres = Array.from(el.parentElement.children);
      el.classList.add('monte');
      el.style.transitionDelay = Math.min(freres.indexOf(el), 5) * 90 + 'ms';
    });
  }
  const revealElements = document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .reveal-scale, .monte');
  if (revealElements.length) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => { if (entry.isIntersecting) { entry.target.classList.add('visible', 'vu'); } });
    }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });
    revealElements.forEach(el => observer.observe(el));
  }
})();
