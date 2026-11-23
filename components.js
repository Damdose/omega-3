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

  function getBandeau() {
    return `<div class="bg-navy-900 text-cream-100 text-[13px]">
      <div class="wrap h-9 flex items-center justify-center sm:justify-between gap-6">
        <p class="truncate"><span class="text-glacier-300 font-semibold">Coffrets de Noël</span> disponibles · Livraison offerte par Eqology dès deux produits de plus de 60 €</p>
        <a href="rejoindre-l-equipe.html" class="hidden sm:inline text-cream-300 hover:text-white whitespace-nowrap">Devenir partenaire →</a>
      </div>
    </div>`;
  }

  function getNav() {
    return `
    <div class="bg-white/95 backdrop-blur border-b border-cream-200">
      <div class="wrap h-16 lg:h-[72px] flex items-center gap-3 lg:gap-8">
        <button id="mobile-menu-btn" class="lg:hidden -ml-2 w-11 h-11 inline-flex items-center justify-center text-navy-900 rounded-xl hover:bg-cream-100" aria-label="Ouvrir le menu" aria-expanded="false" aria-controls="mobile-menu">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-width="2" d="M4 7h16M4 12h16M4 17h16"/></svg>
        </button>
        <a href="index.html" class="inline-flex items-center gap-2.5 shrink-0" aria-label="Accueil">
          <img src="assets/images/eqology-eq.png" alt="Eqology" style="height:26px;width:auto">
          <span class="hidden sm:inline text-[12px] leading-tight text-navy-600 border-l border-cream-300 pl-2.5">Yves Coignard<br><span class="text-navy-400">distributeur indépendant</span></span>
        </a>
        <form action="boutique.html" class="hidden md:flex flex-1 max-w-xl items-center gap-2 h-11 px-4 rounded-full bg-cream-100 border border-transparent focus-within:border-glacier-500 focus-within:bg-white transition-colors" role="search">
          <span class="text-navy-400">${ico.loupe}</span>
          <input name="q" type="search" placeholder="Rechercher un produit : oméga-3, vitamine D, test…" class="flex-1 bg-transparent outline-none text-[15px] placeholder:text-navy-400" aria-label="Rechercher un produit">
        </form>
        <div class="ml-auto flex items-center gap-1 sm:gap-2">
          <a href="rejoindre-l-equipe.html" class="hidden lg:inline-flex items-center gap-2 h-11 px-4 rounded-full text-[15px] font-medium text-navy-800 hover:bg-cream-100">${ico.equipe}Devenir partenaire</a>
          <a href="boutique.html" class="md:hidden w-11 h-11 inline-flex items-center justify-center rounded-full hover:bg-cream-100" aria-label="Rechercher">${ico.loupe}</a>
          <a href="boutique.html" class="inline-flex items-center gap-2 h-11 px-4 sm:px-5 rounded-full bg-navy-900 text-white text-[15px] font-semibold hover:bg-navy-700">${ico.sac}<span class="hidden sm:inline">La boutique</span></a>
        </div>
      </div>
      <div class="hidden lg:block border-t border-cream-200">
        <div class="wrap h-11 flex items-center gap-1 text-[14px] font-medium">
          ${CATS.map(([h, t]) => { const on = h.endsWith('=' + catActive); const noel = t.startsWith('Coffrets');
            return `<a href="${h}" class="px-3 py-1.5 rounded-full ${on ? 'bg-navy-900 text-white' : noel ? 'text-[#B3261E] hover:bg-red-50' : 'text-navy-700 hover:bg-cream-100'}">${t}</a>`; }).join('')}
          <span class="mx-2 h-4 w-px bg-cream-300"></span>
          <a href="le-test.html" class="px-3 py-1.5 rounded-full ${currentPage === 'le-test.html' ? 'bg-navy-900 text-white' : 'text-navy-700 hover:bg-cream-100'}">Comprendre le test</a>
          <a href="index.html#yves" class="px-3 py-1.5 rounded-full text-navy-700 hover:bg-cream-100">Qui suis-je</a>
        </div>
      </div>
    </div>
    <div id="mobile-menu" class="hidden lg:hidden absolute inset-x-0 top-full bg-white border-b border-cream-200 shadow-xl max-h-[80vh] overflow-y-auto">
      <div class="wrap py-4">
        <form action="boutique.html" class="flex items-center gap-2 h-12 px-4 rounded-full bg-cream-100 mb-3" role="search">
          <span class="text-navy-400">${ico.loupe}</span>
          <input name="q" type="search" placeholder="Rechercher un produit" class="flex-1 bg-transparent outline-none text-base" aria-label="Rechercher un produit">
        </form>
        <p class="oeil px-2 mt-4 mb-1">La boutique</p>
        ${CATS.map(([h, t]) => `<a href="${h}" class="block px-2 py-3 text-base font-medium border-b border-cream-100 ${t.startsWith('Coffrets') ? 'text-[#B3261E]' : 'text-navy-800'}">${t}</a>`).join('')}
        <a href="le-test.html" class="block px-2 py-3 text-base font-medium border-b border-cream-100 text-navy-800">Comprendre le test</a>
        <a href="index.html#yves" class="block px-2 py-3 text-base font-medium text-navy-800">Qui suis-je</a>
        <a href="rejoindre-l-equipe.html" class="btn btn-plein w-full mt-4">${ico.equipe}Devenir partenaire</a>
      </div>
    </div>`;
  }

  function getFooter() {
    const l = 'text-cream-300 hover:text-white transition-colors';
    return `
    <div class="wrap">
      <div class="grid gap-10 sm:grid-cols-2 lg:grid-cols-4 mb-14">
        <div>
          <img src="assets/images/eqology-eq.png" alt="Eqology" style="height:28px;width:auto;filter:brightness(0) invert(1)">
          <p class="text-cream-300 text-sm leading-relaxed mt-4 max-w-[30ch]">Yves Coignard, distributeur indépendant Eqology. Les commandes, le paiement et la livraison sont assurés par Eqology.</p>
        </div>
        <div>
          <p class="font-serif font-semibold text-sm mb-4 text-white">L'équipe</p>
          <ul class="space-y-3 text-sm">
            <li><a href="rejoindre-l-equipe.html" class="${l}">Rejoindre l'équipe</a></li>
            <li><a href="rejoindre-l-equipe.html#questions" class="${l}">Questions fréquentes</a></li>
            <li><a href="rejoindre-l-equipe.html#rappel" class="${l}">Être rappelé</a></li>
          </ul>
        </div>
        <div>
          <p class="font-serif font-semibold text-sm mb-4 text-white">La boutique</p>
          <ul class="space-y-3 text-sm">
            ${CATS.map(([h, t]) => `<li><a href="${h}" class="${l}">${t}</a></li>`).join('')}
            <li><a href="le-test.html" class="${l}">Comprendre le test</a></li>
          </ul>
        </div>
        <div>
          <p class="font-serif font-semibold text-sm mb-4 text-white">Contact</p>
          <ul class="space-y-3 text-sm">
            <li><a href="contact.html" class="${l}">Écrire à Yves</a></li>
            <li><a href="science-omega3.html" class="${l}">La science des oméga-3</a></li>
            <li><a href="blog.html" class="${l}">Articles</a></li>
            <li><a data-trustpilot href="#" class="${l}" target="_blank" rel="noopener">Avis clients sur Trustpilot</a></li>
          </ul>
        </div>
      </div>
      <div class="border-t border-white/10 pt-7 flex flex-col md:flex-row items-center justify-between gap-4 text-sm text-cream-400">
        <p>&copy; 2026 ZENCO SAS · distributeur indépendant Eqology</p>
        <div class="flex flex-wrap justify-center gap-5">
          <a href="mentions-legales.html" class="hover:text-white">Mentions légales</a>
          <a href="confidentialite.html" class="hover:text-white">Confidentialité</a>
          <a href="conditions.html" class="hover:text-white">Conditions</a>
        </div>
      </div>
    </div>`;
  }

  // Inject nav and footer
  const nav = document.querySelector('nav#entete') || document.querySelector('nav.fixed');
  if (nav) {
    nav.innerHTML = getNav();
    if (nav.id === 'entete') nav.insertAdjacentHTML('beforebegin', getBandeau());
  }

  const footer = document.querySelector('footer');
  if (footer) footer.innerHTML = getFooter();

  // Cookie consent banner
  if (!localStorage.getItem('cookies_accepted')) {
    const banner = document.createElement('div');
    banner.id = 'cookie-banner';
    banner.className = 'fixed bottom-4 left-4 right-4 sm:right-auto sm:left-6 sm:bottom-6 z-50 sm:max-w-sm bg-white border border-cream-300 rounded-2xl shadow-xl p-5 animate-fade-in';
    banner.innerHTML = `
      <div class="flex items-start gap-3">
        <div class="w-10 h-10 bg-glacier-50 rounded-xl flex items-center justify-center flex-shrink-0 mt-0.5">
          <svg class="w-5 h-5 text-glacier-600" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/>
          </svg>
        </div>
        <div>
          <p class="text-sm font-semibold text-navy-900 mb-1">Cookies & confidentialité</p>
          <p class="text-xs text-navy-500 leading-relaxed mb-3">Ce site utilise des cookies pour améliorer votre expérience. En continuant, vous acceptez notre <a href="confidentialite.html" class="text-glacier-600 hover:underline">politique de confidentialité</a>.</p>
          <div class="flex items-center gap-2">
            <button id="cookie-accept" class="px-4 py-2 bg-navy-700 hover:bg-navy-800 text-white text-xs font-medium rounded-lg transition-colors duration-200 cursor-pointer">Accepter</button>
            <button id="cookie-refuse" class="px-4 py-2 bg-cream-200 hover:bg-cream-300 text-navy-700 text-xs font-medium rounded-lg transition-colors duration-200 cursor-pointer">Refuser</button>
          </div>
        </div>
      </div>
    `;
    document.body.appendChild(banner);

    document.getElementById('cookie-accept').addEventListener('click', function() {
      localStorage.setItem('cookies_accepted', 'true');
      banner.remove();
    });
    document.getElementById('cookie-refuse').addEventListener('click', function() {
      localStorage.setItem('cookies_accepted', 'refused');
      banner.remove();
    });
  }

  // Floating contact button
  if (currentPage !== 'contact.html' && currentPage !== 'rejoindre-l-equipe.html') {
    const fab = document.createElement('a');
    fab.href = 'rejoindre-l-equipe.html#rappel';
    fab.setAttribute('aria-label', 'Être rappelé par Yves');
    fab.className = 'fixed bottom-4 right-4 sm:bottom-6 sm:right-6 z-50 flex items-center gap-2 bg-glacier-600 hover:bg-glacier-700 text-white p-3.5 sm:pl-5 sm:pr-6 sm:py-3.5 rounded-full shadow-lg shadow-glacier-600/30 hover:shadow-xl hover:shadow-glacier-600/40 transition-all duration-300 hover:scale-105 group cursor-pointer';
    fab.innerHTML = `
      <svg class="w-5 h-5 transition-transform duration-300 group-hover:rotate-12" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/>
      </svg>
      <span class="text-sm font-medium hidden sm:inline">Être rappelé</span>
    `;
    document.body.appendChild(fab);
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
