// Shared nav and footer for all pages
(function() {
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';

  function isActive(page) {
    if (page === 'blog.html' && (currentPage === 'blog.html' || currentPage === 'article.html')) return true;
    if (page === 'produits-dropdown' && (currentPage === 'omega-de-confiance.html' || currentPage === 'produit-omega3.html')) return true;
    return currentPage === page;
  }

  const LIENS = [
    ['index.html', 'Accueil'],
    ['rejoindre-l-equipe.html', "Rejoindre l'équipe"],
    ['boutique.html', 'Boutique'],
    ['le-test.html', 'Le test'],
    ['index.html#yves', 'Qui suis-je'],
  ];
  const on = (href) => href === currentPage;
  const cl = (href) => on(href)
    ? 'px-3.5 py-2 text-[15px] font-medium text-navy-900 bg-glacier-50 rounded-xl'
    : 'px-3.5 py-2 text-[15px] font-medium text-navy-700 hover:text-navy-900 hover:bg-cream-100 rounded-xl transition-colors';

  function getNav() {
    return `
    <div class="max-w-7xl mx-auto px-3 sm:px-6 lg:px-8 pt-3">
      <div class="bg-white/85 backdrop-blur-xl rounded-2xl border border-cream-200 shadow-sm pl-4 pr-2 sm:px-5 py-2">
        <div class="flex items-center justify-between gap-3">
          <a href="index.html" class="inline-flex items-center gap-2.5 min-h-[44px]" aria-label="Accueil">
            <img src="assets/images/eqology-eq.png" alt="Eqology" style="height:26px;width:auto">
            <span class="hidden sm:inline text-[13px] leading-tight text-navy-600 border-l border-cream-300 pl-2.5">Yves Coignard<br><span class="text-navy-400">distributeur indépendant</span></span>
          </a>
          <div class="hidden lg:flex items-center gap-0.5">
            ${LIENS.map(([h, t]) => `<a href="${h}" class="${cl(h)}"${on(h) ? ' aria-current="page"' : ''}>${t}</a>`).join('')}
          </div>
          <a href="rejoindre-l-equipe.html#rappel" class="hidden lg:inline-flex btn btn-plein !min-h-[44px] !text-sm">Être rappelé</a>
          <button id="mobile-menu-btn" class="lg:hidden w-11 h-11 inline-flex items-center justify-center text-navy-900 rounded-xl hover:bg-cream-100" aria-label="Ouvrir le menu" aria-expanded="false" aria-controls="mobile-menu">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-width="2" d="M4 7h16M4 12h16M4 17h16"/></svg>
          </button>
        </div>
      </div>
    </div>
    <div id="mobile-menu" class="hidden lg:hidden px-3 pt-2">
      <div class="bg-white rounded-2xl border border-cream-200 shadow-lg p-3 space-y-1">
        ${LIENS.map(([h, t]) => `<a href="${h}" class="block px-4 py-3.5 text-base font-medium rounded-xl ${on(h) ? 'bg-glacier-50 text-navy-900' : 'text-navy-700 hover:bg-cream-100'}">${t}</a>`).join('')}
        <a href="rejoindre-l-equipe.html#rappel" class="btn btn-plein w-full mt-2">Être rappelé par Yves</a>
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
          <p class="text-cream-300 text-sm leading-relaxed mt-4 max-w-[30ch]">Yves Coignard, distributeur indépendant Eqology. Les produits sont vendus et livrés par Eqology.</p>
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
          <p class="font-serif font-semibold text-sm mb-4 text-white">Santé</p>
          <ul class="space-y-3 text-sm">
            <li><a href="boutique.html" class="${l}">Boutique</a></li>
            <li><a href="le-test.html" class="${l}">Le test oméga-3</a></li>
            <li><a href="science-omega3.html" class="${l}">La science des oméga-3</a></li>
            <li><a href="blog.html" class="${l}">Articles</a></li>
          </ul>
        </div>
        <div>
          <p class="font-serif font-semibold text-sm mb-4 text-white">Contact</p>
          <ul class="space-y-3 text-sm">
            <li><a href="contact.html" class="${l}">Écrire à Yves</a></li>
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
  const nav = document.querySelector('nav.fixed');
  if (nav) nav.innerHTML = getNav();

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
