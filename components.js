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
  ];
  const catActive = new URLSearchParams(location.search).get('cat');
  const ico = {
    loupe: '<svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path stroke-linecap="round" d="m20 20-3.5-3.5"/></svg>',
    sac: '<svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linejoin="round" d="M5 8h14l-1 12H6L5 8Z"/><path stroke-linecap="round" d="M9 8V6a3 3 0 0 1 6 0v2"/></svg>',
    panier: '<svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="1.8" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M3 4h2l2.2 10.2a1.5 1.5 0 0 0 1.5 1.2h8.6a1.5 1.5 0 0 0 1.5-1.1L20.5 8H6.1"/><circle cx="9.5" cy="19.5" r="1.4"/><circle cx="17" cy="19.5" r="1.4"/></svg>',
    equipe: '<svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true"><circle cx="9" cy="8" r="3.2"/><path stroke-linecap="round" d="M3.5 19c.8-3 3-4.6 5.5-4.6s4.7 1.6 5.5 4.6"/><path stroke-linecap="round" d="M16 5.5a3 3 0 0 1 0 5.6M18 14.8c1.3.7 2.1 2 2.5 4.2"/></svg>',
  };

  // Deux modes : la vitrine (tout le site) et la page d'atterrissage partenaire (pubs), sans fuite
  const isLP = currentPage === 'partenaire.html' || currentPage === 'merci.html';

  function getBandeau() { return ''; }

  const fleche = '<svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M5 12h14m-6-6 6 6-6 6"/></svg>';
  const marque = (lien) => `<a href="${lien}" class="flex items-center gap-2.5 shrink-0" aria-label="Accueil"><img src="assets/images/eqology-eq.png" alt="Eqology" style="height:24px;width:auto"><span class="block text-[11px] sm:text-[12.5px] leading-tight text-nuit/75 border-l border-nuit/15 pl-2 sm:pl-2.5">Yves Coignard<br>distributeur indépendant</span></a>`;

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
        <p class="truncate hidden sm:block"><span class="text-glacier-300">Livraison offerte par Eqology</span> dès deux produits de plus de 60&nbsp;€<span class="hidden lg:inline"> · Paiement sécurisé sur la boutique officielle</span></p>
        <span class="shrink-0 flex items-center gap-5"><a href="tel:+33675242626" class="hover:text-white">Conseil gratuit&nbsp;: <span class="text-white">06 75 24 26 26</span></a><a href="partenaire.html" class="hover:text-white"><span class="sm:hidden">Partenaire →</span><span class="hidden sm:inline">Devenir partenaire →</span></a></span>
      </div>
    </div>
    <div class="entete-verre text-nuit">
      <div class="wrap h-16 lg:h-[76px] flex items-center gap-3 lg:gap-8">
        <button id="mobile-menu-btn" class="lg:hidden -ml-2 w-11 h-11 grid place-items-center rounded-[8.5px] hover:bg-sable" aria-label="Ouvrir le menu" aria-expanded="false" aria-controls="mobile-menu">
          <svg width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" d="M4 8h16M4 16h16"/></svg>
        </button>
        ${marque('index.html')}
        <form action="boutique.html" class="hidden md:flex flex-1 max-w-xl items-center gap-2 h-11 px-4 rounded-full verre focus-within:!border-glacier-500" role="search">
          <span class="text-nuit/50">${ico.loupe}</span>
          <input name="q" type="search" placeholder="Rechercher un produit : oméga-3, vitamine D, test…" class="flex-1 bg-transparent outline-none text-[15px] placeholder:text-nuit/50" aria-label="Rechercher un produit">
        </form>
        <div class="ml-auto flex items-center gap-1 sm:gap-2">
          
          <a href="boutique.html" class="md:hidden w-11 h-11 grid place-items-center rounded-[8.5px] hover:bg-sable" aria-label="Rechercher">${ico.loupe}</a>
          <button type="button" data-panier-ouvrir class="relative w-11 h-11 grid place-items-center rounded-full hover:bg-sable" aria-label="Ouvrir le panier">${ico.panier}<span data-panier-nombre class="hidden absolute top-0.5 right-0.5 min-w-[19px] h-[19px] px-1 rounded-full bg-glacier-500 text-nuit text-[11px] font-medium leading-[19px] text-center">0</span></button>
          <a href="boutique.html" aria-label="La boutique" class="hidden sm:inline-flex btn !min-h-[44px] !px-4 bg-nuit text-white hover:bg-nuit-2">${ico.sac}<span class="hidden sm:inline">La boutique</span></a>
        </div>
      </div>
      <div class="hidden lg:block border-t border-nuit/10">
        <div class="wrap h-12 flex items-center gap-1 text-[15px]">
          ${CATS.map(rayon).join('')}
          <span class="mx-2 h-4 w-px bg-nuit/15"></span>
          <a href="le-test.html" class="px-3 py-1.5 rounded-[8.5px] text-nuit/80 hover:bg-sable">Comprendre le test</a>
          <a href="${ancreYves}" class="px-3 py-1.5 rounded-[8.5px] text-nuit/80 hover:bg-sable">Qui suis-je</a>
          <a href="partenaire.html" class="ml-auto inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-glacier-500 text-nuit hover:bg-glacier-300 transition-colors">${ico.equipe}Devenir partenaire</a>
        </div>
      </div>
    </div>
    <div id="mobile-menu" class="hidden lg:hidden absolute inset-x-2 top-full mt-2 verre !bg-white/80 rounded-[14px] text-nuit max-h-[78vh] overflow-y-auto">
      <div class="wrap py-4">
        <form action="boutique.html" class="flex items-center gap-2 h-12 px-4 rounded-full verre mb-3" role="search">
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


  // En-tête de la page d'atterrissage des pubs (data-entete="lp") : logo, téléphone, rappel. Aucune fuite.
  function getNavLPPro() {
    return `
    <div class="bg-nuit text-white/85 text-[13px]">
      <div class="wrap h-9 flex items-center justify-between gap-4">
        <p class="truncate">Distributeur indépendant Eqology<span class="hidden sm:inline"> · Rappel sous 48 heures, sans engagement</span></p>
        <a href="tel:+33675242626" class="shrink-0 hover:text-white">06 75 24 26 26</a>
      </div>
    </div>
    <div class="entete-verre text-nuit">
      <div class="wrap h-16 lg:h-[72px] flex items-center justify-between gap-4">
        ${marque('#')}
        <div class="flex items-center gap-3 sm:gap-5">
          <a href="tel:+33675242626" class="hidden md:inline-flex items-center gap-2 text-[15px] hover:opacity-70"><svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.8" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linejoin="round" d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></svg>06 75 24 26 26</a>
          <a href="#premier-pas" id="nav-cta" class="btn btn-plein !min-h-[44px]"><span>Être rappelé<span class="hidden sm:inline"> par Yves</span></span></a>
        </div>
      </div>
    </div>`;
  }

  function getFooterLP() {
    return `<div class="wrap py-10 grid gap-6 text-sm text-white/65">
      <div class="flex flex-col md:flex-row md:items-center justify-between gap-5">
        <img src="assets/v2/eqology-logo-blanc.png" alt="Eqology" class="w-[150px] h-auto" loading="lazy" width="1300" height="205">
        <p class="max-w-[70ch] md:text-right">Yves Coignard est distributeur indépendant Eqology. Les revenus d'un partenaire dépendent de son activité&nbsp;: aucun revenu n'est garanti. Le plan de rémunération officiel d'Eqology est présenté avant tout engagement.</p>
      </div>
      <div class="border-t border-white/10 pt-6 flex flex-col sm:flex-row justify-between gap-3">
        <p>© 2026 ZENCO SAS · SIREN 504 495 946</p>
        <div class="flex gap-5"><a href="mentions-legales.html" class="hover:text-white">Mentions légales</a><a href="confidentialite.html" class="hover:text-white">Confidentialité</a></div>
      </div>
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
      <div class="border-t border-white/10 py-8 flex flex-col md:flex-row md:items-center justify-between gap-6">
        <img src="assets/v2/eqology-logo-blanc.png" alt="Eqology" class="w-[180px] h-auto opacity-95" loading="lazy" width="1300" height="205">
        <p class="text-sm text-white/60 max-w-[62ch] md:text-right">Les compléments alimentaires ne se substituent pas à une alimentation variée et équilibrée ni à un mode de vie sain. Tenir hors de portée des enfants. Ne pas dépasser la dose journalière recommandée.</p>
      </div>
      <div class="border-t border-white/10 py-6 flex flex-col md:flex-row justify-between gap-3 text-sm text-white/60">
        <p>© 2026 ZENCO SAS · SIREN 504 495 946 · Yves Coignard, distributeur indépendant Eqology</p>
        <p>Commandes, paiement et livraison assurés par Eqology · <a href="mentions-legales.html" class="underline underline-offset-4 hover:text-white">Mentions légales</a></p>
      </div>
    </div>`;
  }

  // Inject nav and footer
  const nav = document.querySelector('nav#entete') || document.querySelector('nav.fixed');
  if (nav) {
    const mode = document.body.dataset.entete;
    const enteteBoutique = mode === 'boutique' || mode === 'lp';
    nav.innerHTML = mode === 'lp' ? getNavLPPro() : enteteBoutique ? getNavBoutique() : getNav();
    nav.className = enteteBoutique ? 'sticky top-0 z-50' : 'fixed top-0 inset-x-0 z-50 px-3 pt-3 sm:px-6 sm:pt-5';
    if (nav.id === 'entete') {
      const main = document.querySelector('main');
      if (main && !document.querySelector('[data-plein]') && !document.body.dataset.entete) main.style.paddingTop = '88px';
    }
  }

  const footer = document.querySelector('body > footer');
  if (footer) { footer.innerHTML = document.body.dataset.entete === 'lp' ? getFooterLP() : getFooter(); if (nav && nav.id === 'entete') footer.className = 'bg-nuit text-white border-t border-white/10 pt-16'; }
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


  // ============ Panier : panneau latéral, compteur, ajout depuis n'importe quelle page ============
  if (window.PANIER) {
    const P = window.PANIER;
    const tiroir = document.createElement('div');
    tiroir.id = 'panier-tiroir';
    tiroir.className = 'fixed inset-0 z-[70] invisible';
    tiroir.setAttribute('role', 'dialog'); tiroir.setAttribute('aria-modal', 'true'); tiroir.setAttribute('aria-labelledby', 'panier-titre');
    tiroir.innerHTML = `
      <div data-panier-fermer class="absolute inset-0 bg-nuit/50 backdrop-blur-[2px] opacity-0 transition-opacity duration-300"></div>
      <aside class="absolute right-0 top-0 h-full w-full max-w-[440px] bg-white text-nuit shadow-2xl flex flex-col translate-x-full transition-transform duration-300">
        <div class="flex items-center justify-between px-5 sm:px-6 h-16 border-b border-nuit/10 shrink-0">
          <p id="panier-titre" class="text-lg">Votre panier <span data-panier-compte class="text-nuit/60"></span></p>
          <button type="button" data-panier-fermer class="w-10 h-10 grid place-items-center rounded-full hover:bg-sable" aria-label="Fermer le panier"><svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.8" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" d="M6 6l12 12M18 6 6 18"/></svg></button>
        </div>
        <div data-panier-lignes class="flex-1 overflow-y-auto px-5 sm:px-6"></div>
        <div data-panier-pied class="border-t border-nuit/10 p-5 sm:p-6 shrink-0"></div>
      </aside>`;
    document.body.appendChild(tiroir);

    window.panierLignes = function (cible, compact) {
      const l = P.lire();
      if (!l.length) { cible.innerHTML = `<div class="py-14 text-center"><p class="text-lg">Votre panier est vide.</p><p class="text-nuit/65 mt-2">Parcourez la boutique et ajoutez les produits qui vous intéressent.</p><a href="boutique.html" class="btn btn-plein mt-6">Voir la boutique</a></div>`; return; }
      cible.innerHTML = '<ul class="divide-y divide-nuit/10">' + l.map(function (i) {
        const p = window.produit(i.slug);
        const prix = p.prix ? P.euros(p.prix * i.qte) : window.prixTexte(p);
        return `<li class="py-5 flex gap-4">
          <a href="produit.html?p=${p.slug}" class="shrink-0 w-20 h-20 ${compact ? '' : 'sm:w-24 sm:h-24'} rounded-[10px] bg-sable grid place-items-center"><img src="assets/v2/produits/${p.slug}.webp" alt="" class="w-full h-full object-contain p-2" width="96" height="96" loading="lazy"></a>
          <div class="flex-1 min-w-0">
            <div class="flex justify-between gap-3"><a href="produit.html?p=${p.slug}" class="leading-snug hover:underline underline-offset-4">${p.nom}</a><span class="shrink-0">${prix}</span></div>
            <p class="text-sm text-nuit/60 mt-0.5">${p.detail}</p>
            <div class="mt-3 flex items-center justify-between">
              <div class="inline-flex items-center rounded-full border border-nuit/15">
                <button type="button" data-panier-moins="${p.slug}" class="w-9 h-9 grid place-items-center" aria-label="Retirer un ${p.nom}">−</button>
                <span class="w-7 text-center text-[15px]" aria-live="polite">${i.qte}</span>
                <button type="button" data-panier-plus="${p.slug}" class="w-9 h-9 grid place-items-center" aria-label="Ajouter un ${p.nom}">+</button>
              </div>
              <button type="button" data-panier-retirer="${p.slug}" class="text-sm text-nuit/60 underline underline-offset-4 hover:text-nuit">Retirer</button>
            </div>
          </div>
        </li>`;
      }).join('') + '</ul>';
    };

    function majPied() {
      const pied = tiroir.querySelector('[data-panier-pied]');
      if (!P.lire().length) { pied.innerHTML = ''; pied.classList.add('hidden'); return; }
      pied.classList.remove('hidden');
      pied.innerHTML = `
        <div class="flex justify-between text-lg"><span>Sous-total</span><span>${P.euros(P.total())}</span></div>
        ${P.aPrixVariable() ? '<p class="text-sm text-nuit/60 mt-1">Hors produits en abonnement, dont le prix est confirmé par Eqology.</p>' : ''}
        <p class="text-sm text-nuit/65 mt-2">Livraison offerte par Eqology dès deux produits de plus de 60&nbsp;€. Paiement sécurisé sur la boutique officielle.</p>
        <a href="panier.html" class="btn btn-plein w-full !min-h-[50px] mt-5">Valider mon panier</a>
        <button type="button" data-panier-fermer class="w-full mt-3 text-[15px] underline underline-offset-4">Continuer mes achats</button>`;
    }
    function majCompteurs() {
      const n = P.nombre();
      document.querySelectorAll('[data-panier-nombre]').forEach(function (b) { b.textContent = n; b.classList.toggle('hidden', !n); });
      document.querySelectorAll('[data-panier-ouvrir]').forEach(function (b) { b.setAttribute('aria-label', n ? 'Ouvrir le panier (' + n + ' article' + (n > 1 ? 's' : '') + ')' : 'Ouvrir le panier'); });
      const c = tiroir.querySelector('[data-panier-compte]'); if (c) c.textContent = n ? '(' + n + ')' : '';
    }
    function maj() { window.panierLignes(tiroir.querySelector('[data-panier-lignes]'), true); majPied(); majCompteurs(); }
    let dernierFocus = null;
    function ouvrir() {
      dernierFocus = document.activeElement; maj();
      tiroir.classList.remove('invisible');
      requestAnimationFrame(function () { tiroir.querySelector('aside').classList.remove('translate-x-full'); tiroir.firstElementChild.classList.remove('opacity-0'); });
      document.documentElement.style.overflow = 'hidden';
      setTimeout(function () { const f = tiroir.querySelector('[data-panier-fermer].w-10'); if (f) f.focus(); }, 50);
    }
    function fermer() {
      tiroir.querySelector('aside').classList.add('translate-x-full'); tiroir.firstElementChild.classList.add('opacity-0');
      document.documentElement.style.overflow = '';
      setTimeout(function () { tiroir.classList.add('invisible'); if (dernierFocus) dernierFocus.focus(); }, 300);
    }
    window.ouvrirPanier = ouvrir;
    document.addEventListener('click', function (e) {
      const t = e.target.closest('[data-ajouter],[data-panier-ouvrir],[data-panier-fermer],[data-panier-plus],[data-panier-moins],[data-panier-retirer]');
      if (!t) return;
      if (t.hasAttribute('data-ajouter')) {
        e.preventDefault(); e.stopPropagation();
        const slug = t.getAttribute('data-ajouter'), q = parseInt(t.getAttribute('data-quantite') || '1', 10), p = window.produit(slug);
        P.ajouter(slug, q);
        if (window.suivre && p) window.suivre('AddToCart', { content_ids: [slug], content_name: p.nom, value: p.prix || 0, currency: 'EUR' });
        ouvrir(); return;
      }
      if (t.hasAttribute('data-panier-ouvrir')) { ouvrir(); return; }
      if (t.hasAttribute('data-panier-fermer')) { fermer(); return; }
      const l = P.lire();
      const slug = t.getAttribute('data-panier-plus') || t.getAttribute('data-panier-moins') || t.getAttribute('data-panier-retirer');
      const x = l.find(function (i) { return i.slug === slug; }); if (!x) return;
      if (t.hasAttribute('data-panier-plus')) P.changer(slug, x.qte + 1);
      else if (t.hasAttribute('data-panier-moins')) { if (x.qte > 1) P.changer(slug, x.qte - 1); else P.retirer(slug); }
      else P.retirer(slug);
    });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !tiroir.classList.contains('invisible')) fermer(); });
    document.addEventListener('panier', maj);
    window.addEventListener('storage', function (e) { if (e.key === 'panier') maj(); });
    maj();
  }



  // ============ Avis clients Eqology (Trustpilot, relevés le 26/11/2026, extraits non modifiés) ============
  const AVIS = [
    { nom: 'Odile', pays: 'Autriche', date: '21 janvier 2026', etoiles: 5, texte: "J'ai essayé plusieurs huiles de leur gamme et je les intègre très facilement à mes repas, car délicieuses.", url: 'https://fr.trustpilot.com/reviews/6970d5afdb0f2d2770d17967' },
    { nom: 'Françoise V.', pays: 'Belgique', date: '19 janvier 2025', etoiles: 4, texte: "Service après vente très appréciable. Mr Wolanin a pu directement m'aider.", url: 'https://fr.trustpilot.com/reviews/678d16f788fd832eae353daa' },
    { nom: 'MoRi', pays: 'Suisse', date: '19 novembre 2026', etoiles: 5, texte: "J'aime vraiment le goût.", note: "Traduit de l'anglais", url: 'https://www.trustpilot.com/reviews/6aff364aa3a53849c2acfa83' },
  ];
  const etoiles = (n) => '<span class="inline-flex gap-0.5" aria-label="' + n + ' étoiles sur 5">' + [1,2,3,4,5].map((i) => `<span class="w-5 h-5 grid place-items-center rounded-[3px] ${i <= n ? 'bg-[#00B67A]' : 'bg-nuit/15'}"><svg width="12" height="12" viewBox="0 0 24 24" fill="#fff" aria-hidden="true"><path d="M12 2l2.9 6.9 7.1.6-5.4 4.7 1.7 7-6.3-3.9-6.3 3.9 1.7-7L2 9.5l7.1-.6z"/></svg></span>`).join('') + '</span>';
  document.querySelectorAll('[data-avis]').forEach(function (el) {
    const titre = el.getAttribute('data-avis') || "Ce que disent les clients d'Eqology.";
    el.innerHTML = `
      <div class="flex flex-col lg:flex-row lg:items-end justify-between gap-6">
        <div><span class="oeil">Avis clients</span><h2 class="h2 mt-6 max-w-[20ch]">${titre}</h2></div>
        <a href="https://fr.trustpilot.com/review/eqology.com" target="_blank" rel="noopener" class="self-start lg:self-auto inline-flex items-center gap-3 rounded-full bg-white text-nuit border border-nuit/10 pl-4 pr-5 h-12 hover:-translate-y-0.5 transition-transform"><img src="assets/v2/trustpilot.webp" alt="Trustpilot" width="320" height="79" class="h-6 w-auto"><span class="text-[15px]">Tous les avis →</span></a>
      </div>
      <div class="mt-10 grid gap-4 lg:grid-cols-[0.9fr_1fr_1fr_1fr] rail-mobile">
        <div class="rounded-[14px] bg-nuit text-white p-6 sm:p-7 flex flex-col justify-between gap-6">
          <div><p class="text-sm text-white/65">Sur Trustpilot, Eqology est noté</p><p class="text-3xl font-light mt-1">Excellent</p></div>
          <dl class="grid gap-4">
            <div><dt class="text-sm text-white/65">Avis publiés</dt><dd class="text-2xl font-light">1&nbsp;886</dd></div>
            <div><dt class="text-sm text-white/65">Avis sur les 12 derniers mois</dt><dd class="text-2xl font-light">862</dd></div>
          </dl>
        </div>
        ${AVIS.map((a) => `
        <figure class="rounded-[14px] bg-white text-nuit border border-nuit/10 p-6 sm:p-7 flex flex-col">
          ${etoiles(a.etoiles)}
          <blockquote class="mt-5 text-[17px] leading-relaxed flex-1">« ${a.texte} »</blockquote>
          <figcaption class="mt-6 pt-4 border-t border-nuit/10 text-sm">
            <span class="font-medium">${a.nom}</span><span class="text-nuit/60"> · ${a.pays} · ${a.date}</span>
            ${a.note ? `<span class="block text-xs text-nuit/55 mt-0.5">${a.note}</span>` : ''}
            <a href="${a.url}" target="_blank" rel="noopener" class="block mt-2 text-xs text-nuit/60 underline underline-offset-4 hover:text-nuit">Lire l'avis sur Trustpilot ↗</a>
          </figcaption>
        </figure>`).join('')}
      </div>
      <p class="rail-indice" aria-hidden="true">Faites glisser pour voir la suite →</p>
      <p class="mt-4 text-xs opacity-60">Avis publics sur la marque Eqology, relevés sur Trustpilot le 26 novembre 2026. Extraits non modifiés.</p>`;
  });

})();
