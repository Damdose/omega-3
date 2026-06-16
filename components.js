// Shared nav and footer for all pages
(function() {
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';

  function isActive(page) {
    if (page === 'blog.html' && (currentPage === 'blog.html' || currentPage === 'article.html')) return true;
    if (page === 'produits-dropdown' && (currentPage === 'omega-de-confiance.html' || currentPage === 'produit-omega3.html')) return true;
    return currentPage === page;
  }

  const activeClass = 'px-4 py-2 text-sm font-medium text-navy-700 bg-glacier-50 rounded-xl';
  const inactiveClass = 'px-4 py-2 text-sm font-medium text-navy-800 hover:text-glacier-600 hover:bg-glacier-50 rounded-xl transition-all duration-300';
  const dropdownActiveClass = 'block px-4 py-2.5 text-sm text-glacier-600 font-medium bg-glacier-50 rounded-lg';
  const dropdownInactiveClass = 'block px-4 py-2.5 text-sm text-navy-800 hover:bg-glacier-50 rounded-lg transition-all duration-200';
  const mobileActiveClass = 'block px-4 py-3 text-sm font-medium text-navy-700 bg-glacier-50 rounded-xl';
  const mobileInactiveClass = 'block px-4 py-3 text-sm font-medium text-navy-800 hover:bg-glacier-50 rounded-xl';

  function getNav() {
    return `
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-4">
      <div class="bg-white/80 backdrop-blur-xl rounded-2xl border border-glacier-100/50 shadow-sm px-6 py-3">
        <div class="flex items-center justify-between">
          <a href="index.html" class="inline-flex items-center gap-1.5" aria-label="FENA × Eqology">
            <span style="display:inline-block;width:43px;height:48px;background-color:#172847;-webkit-mask:url(assets/images/fena-logo.png) center/contain no-repeat;mask:url(assets/images/fena-logo.png) center/contain no-repeat;"></span>
            <span class="text-glacier-400 text-xl font-light">&times;</span>
            <img src="assets/images/eqology-eq.png" alt="Eqology" style="height:22px;width:auto;display:inline-block;">
          </a>
          <div class="hidden md:flex items-center gap-1">
            <a href="index.html" class="${isActive('index.html') ? activeClass : inactiveClass}">Accueil</a>
            <div class="relative group">
              <button class="${isActive('produits-dropdown') ? 'px-4 py-2 text-sm font-medium text-navy-700 bg-glacier-50 rounded-xl inline-flex items-center gap-1 cursor-pointer' : 'px-4 py-2 text-sm font-medium text-navy-800 hover:text-glacier-600 hover:bg-glacier-50 rounded-xl transition-all duration-300 inline-flex items-center gap-1 cursor-pointer'}">
                Produits
                <svg class="w-3.5 h-3.5 transition-transform duration-300 group-hover:rotate-180" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/></svg>
              </button>
              <div class="absolute top-full left-0 pt-2 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-300">
                <div class="bg-white/95 backdrop-blur-xl rounded-xl border border-glacier-100/50 shadow-lg p-2 min-w-[200px]">
                  <a href="omega-de-confiance.html" class="${isActive('omega-de-confiance.html') ? dropdownActiveClass : dropdownInactiveClass}">Oméga-3 de confiance</a>
                  <a href="produit-omega3.html" class="${isActive('produit-omega3.html') ? dropdownActiveClass : dropdownInactiveClass}">Oméga 3 supérieur</a>
                </div>
              </div>
            </div>
            <a href="a-propos.html" class="${isActive('a-propos.html') ? activeClass : inactiveClass}">À propos</a>
            <a href="blog.html" class="${isActive('blog.html') ? activeClass : inactiveClass}">Blog</a>
          </div>
          <a href="contact.html" class="hidden md:inline-flex items-center gap-2 px-5 py-2.5 bg-navy-700 text-white text-sm font-medium rounded-xl hover:bg-navy-800 transition-all duration-300 cursor-pointer shadow-sm shadow-navy-700/20">
            Nous contacter
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/></svg>
          </a>
          <button id="mobile-menu-btn" class="md:hidden p-2 text-navy-800 cursor-pointer" aria-label="Menu">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/></svg>
          </button>
        </div>
      </div>
    </div>
    <div id="mobile-menu" class="hidden md:hidden px-4 pt-2">
      <div class="bg-white/95 backdrop-blur-xl rounded-2xl border border-glacier-100/50 shadow-lg p-4 space-y-1">
        <a href="index.html" class="${isActive('index.html') ? mobileActiveClass : mobileInactiveClass}">Accueil</a>
        <a href="omega-de-confiance.html" class="${isActive('omega-de-confiance.html') ? mobileActiveClass : mobileInactiveClass}">Oméga-3 de confiance</a>
        <a href="produit-omega3.html" class="${isActive('produit-omega3.html') ? mobileActiveClass : mobileInactiveClass}">Oméga 3 supérieur</a>
        <a href="a-propos.html" class="${isActive('a-propos.html') ? mobileActiveClass : mobileInactiveClass}">À propos</a>
        <a href="blog.html" class="${isActive('blog.html') ? mobileActiveClass : mobileInactiveClass}">Blog</a>
        <a href="contact.html" class="block px-4 py-3 text-sm font-medium text-center bg-navy-700 text-white rounded-xl mt-2">Nous contacter</a>
      </div>
    </div>`;
  }

  function getFooter() {
    return `
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-12 mb-16">
        <div>
          <a href="index.html" class="inline-flex items-center gap-2" aria-label="FENA × Eqology">
            <span style="display:inline-block;width:40px;height:44px;background-color:#ffffff;-webkit-mask:url(assets/images/fena-logo.png) center/contain no-repeat;mask:url(assets/images/fena-logo.png) center/contain no-repeat;"></span>
            <span class="text-glacier-400 text-2xl font-light">&times;</span>
            <img src="assets/images/eqology-eq.png" alt="Eqology" style="height:30px;width:auto;display:inline-block;">
          </a>
          <p class="text-cream-400 text-sm leading-relaxed mt-4">YAC, premier distributeur EQOLOGY en France.<br>Partenaire officiel FENA.</p>
        </div>
        <div>
          <h4 class="font-serif font-bold text-sm mb-4 text-cream-300">Produits</h4>
          <ul class="space-y-3 text-sm"><li><a href="omega-de-confiance.html" class="text-cream-400 hover:text-white transition-colors duration-300 cursor-pointer">Oméga-3 de confiance</a></li><li><a href="produit-omega3.html" class="text-cream-400 hover:text-white transition-colors duration-300 cursor-pointer">Oméga 3 supérieur</a></li></ul>
        </div>
        <div>
          <h4 class="font-serif font-bold text-sm mb-4 text-cream-300">Ressources</h4>
          <ul class="space-y-3 text-sm"><li><a href="blog.html" class="text-cream-400 hover:text-white transition-colors duration-300 cursor-pointer">Blog</a></li><li><a href="index.html#faq" class="text-cream-400 hover:text-white transition-colors duration-300 cursor-pointer">FAQ</a></li></ul>
        </div>
        <div>
          <h4 class="font-serif font-bold text-sm mb-4 text-cream-300">Contact</h4>
          <ul class="space-y-3 text-sm"><li><a href="contact.html" class="text-cream-400 hover:text-white transition-colors duration-300 cursor-pointer">Nous contacter</a></li><li><a href="candidature.html" class="text-cream-400 hover:text-white transition-colors duration-300 cursor-pointer">Rejoindre le programme</a></li></ul>
        </div>
      </div>
      <div class="border-t border-white/10 pt-8 flex flex-col md:flex-row items-center justify-between gap-4">
        <p class="text-cream-400/60 text-sm">&copy; 2025 YAC — EQOLOGY. Tous droits réservés.</p>
        <div class="flex flex-wrap items-center justify-center md:justify-end gap-4 sm:gap-6 text-sm text-cream-400/60">
          <a href="mentions-legales.html" class="hover:text-white transition-colors duration-300 cursor-pointer">Mentions légales</a>
          <a href="confidentialite.html" class="hover:text-white transition-colors duration-300 cursor-pointer">Confidentialité</a>
          <a href="conditions.html" class="hover:text-white transition-colors duration-300 cursor-pointer">Conditions</a>
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
  if (currentPage !== 'contact.html') {
    const fab = document.createElement('a');
    fab.href = 'contact.html';
    fab.setAttribute('aria-label', 'Nous contacter');
    fab.className = 'fixed bottom-4 right-4 sm:bottom-6 sm:right-6 z-50 flex items-center gap-2 bg-glacier-600 hover:bg-glacier-700 text-white p-3.5 sm:pl-5 sm:pr-6 sm:py-3.5 rounded-full shadow-lg shadow-glacier-600/30 hover:shadow-xl hover:shadow-glacier-600/40 transition-all duration-300 hover:scale-105 group cursor-pointer';
    fab.innerHTML = `
      <svg class="w-5 h-5 transition-transform duration-300 group-hover:rotate-12" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"/>
      </svg>
      <span class="text-sm font-medium hidden sm:inline">Nous contacter</span>
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
        } else {
          menu.classList.add('hidden');
          menu.style.display = 'none';
        }
      };
    }
  }, 100);

  // Reveal animations (IntersectionObserver)
  const revealElements = document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .reveal-scale');
  if (revealElements.length) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => { if (entry.isIntersecting) { entry.target.classList.add('visible'); } });
    }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });
    revealElements.forEach(el => observer.observe(el));
  }
})();
