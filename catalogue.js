// ============================================================
// CATALOGUE — une ligne par produit, alimente l'accueil, la boutique et les fiches.
// Prix relevés sur eqology.com/fr le 23/11/2026 (achat unique, TTC).
// Le prix affiché chez Eqology au moment de la commande fait foi.
// ============================================================
window.CATEGORIES = [
  { id: 'omega3', nom: 'Oméga-3', image: 'assets/v2/cat-omega3.webp', accroche: "Huiles de Norvège et version végane" },
  { id: 'tests', nom: 'Tests à domicile', image: 'assets/v2/testkit-detail.webp', accroche: 'Mesurer avant de compléter' },
  { id: 'programmes', nom: 'Programmes', image: 'assets/v2/cat-programmes.webp', accroche: 'Huile, complément et test réunis' },
  { id: 'vitamines', nom: 'Vitamines et forme', image: 'assets/v2/cat-vitamines.webp', accroche: 'K2 + D3, Nordic Energy Booster' },
  { id: 'beaute', nom: 'Beauté', image: 'assets/v2/produits/ocean-miracle-plumping-serum.webp', produitImg: true, accroche: 'La ligne Ocean Miracle' },
  { id: 'coffrets', nom: 'Coffrets de Noël', image: 'assets/v2/produits/christmas-pack-large.webp', produitImg: true, accroche: 'Des cadeaux prêts à offrir' },
];

window.PRODUITS = [
  // --- Oméga-3 ---
  { slug: 'pure-arctic-oil', cat: 'omega3', nom: 'Pure Arctic Oil', detail: 'Citron ou orange · 300 ml', prix: 55, badge: 'Meilleure vente', top: 1,
    texte: "L'huile de référence d'Eqology : des oméga-3 de morue sauvage pêchée en Arctique, de l'huile d'olive vierge extra biologique et de la vitamine D3.",
    points: ['Oméga-3 à spectre complet, EPA et DHA', "Huile d'olive vierge extra biologique pressée à froid", 'Vitamine D3', 'Pêche certifiée MSC, flacon en verre'],
    usage: 'Environ 0,15 ml par kilo de poids par jour, de préférence au repas. Au réfrigérateur après ouverture.' },
  { slug: 'pure-arctic-oil-natural', cat: 'omega3', nom: 'Pure Arctic Oil Natural', detail: 'Sans arôme ajouté · 300 ml', prix: 57,
    texte: "La même huile, au goût naturel de l'Arctique : 1 500 mg d'EPA et de DHA pour 10 ml, avec huile d'olive biologique et vitamine D.",
    points: ["1 500 mg d'EPA et de DHA pour 10 ml", 'Sans arôme ajouté', "Huile d'olive vierge extra biologique", 'Vitamine D'],
    usage: 'Environ 0,15 ml par kilo de poids par jour. Au réfrigérateur après ouverture.' },
  { slug: 'pure-arctic-oil-gold', cat: 'omega3', nom: 'Pure Arctic Oil Gold', detail: 'Lutéine, vitamines A et D · 300 ml', prix: 87, top: 3,
    texte: "Plus d'EPA et de DHA par dose quotidienne, enrichie en lutéine, vitamine A et vitamine D. Le DHA contribue au fonctionnement normal du cerveau et au maintien d'une vision normale.",
    points: ["Plus d'EPA et de DHA par dose", 'Lutéine et vitamine A', 'Vitamine D', 'Arôme citron frais'],
    usage: 'Une dose par jour au repas. Au réfrigérateur après ouverture.' },
  { slug: 'pure-arctic-oil-heart-energy', cat: 'omega3', nom: 'Pure Arctic Oil Heart & Energy', detail: 'Avec ubiquinol (CoQ10) · 300 ml', prix: 87, top: 4,
    texte: "Les oméga-3 de Pure Arctic Oil enrichis en Kaneka Ubiquinol®, la forme active de la coenzyme Q10. L'EPA et le DHA contribuent à une fonction cardiaque normale (250 mg par jour).",
    points: ['Oméga-3 à spectre complet', 'Ubiquinol Kaneka® (CoQ10)', 'Formule primée', 'Pêche certifiée MSC'],
    usage: 'Une dose par jour au repas. Au réfrigérateur après ouverture.' },
  { slug: 'pure-vegan-oil', cat: 'omega3', nom: 'Pure Vegan Oil', detail: "Oméga-3 d'algues · 300 ml", prix: 88, badge: 'Végan', top: 5,
    texte: "Des oméga-3 issus de microalgues cultivées durablement, avec de l'huile d'olive biologique, de la lutéine et de la vitamine D : 1 500 mg d'EPA et de DHA pour 10 ml.",
    points: ['100 % végan, sans poisson', "1 500 mg d'EPA et de DHA pour 10 ml", '10 mg de lutéine', 'Vitamine D'],
    usage: 'Une dose par jour au repas. Au réfrigérateur après ouverture.' },
  { slug: 'pure-arctic-oil-for-kids', cat: 'omega3', nom: 'Pure Arctic Oil For Kids', detail: 'Citron · 150 ml', prix: 40,
    texte: "Une huile pensée pour les enfants : 900 mg d'EPA et de DHA pour 5 ml, avec vitamine D3 et un arôme frais de citron.",
    points: ["900 mg d'EPA et de DHA pour 5 ml", 'Vitamine D3', 'Arôme citron', 'Poisson sauvage pêché en Arctique'],
    usage: "Selon l'âge et le poids de l'enfant, au repas. Au réfrigérateur après ouverture." },

  // --- Tests ---
  { slug: 'omega-3-test-kit', cat: 'tests', nom: 'Test oméga-3', detail: 'À domicile · résultats en ligne', prix: 88, badge: 'Pour commencer', top: 2,
    texte: "Une goutte de sang prélevée chez vous, analysée par un laboratoire indépendant : le profil de 11 acides gras, le rapport oméga-6 / oméga-3 et l'indice oméga-3.",
    points: ['Test à domicile en sept étapes', '11 acides gras analysés', 'Rapport oméga-6 / oméga-3 et indice oméga-3', 'Résultats anonymes en ligne sous 20 à 25 jours ouvrés'],
    usage: "Faites un premier test, puis un second après environ quatre mois de prise d'huile pour comparer." },
  { slug: 'vitamin-k2d3-test', cat: 'tests', nom: 'Test vitamines K2 et D3', detail: 'À domicile · résultats en ligne', prix: 115,
    texte: 'Un test à faire chez soi pour connaître sa concentration sanguine en vitamine K2 (MK7) et en vitamine D3.',
    points: ['Test à domicile', 'Vitamine K2 (MK7) et vitamine D3', 'Résultats en ligne'],
    usage: 'Idéal avant de commencer une supplémentation, puis quelques mois après.' },

  // --- Programmes (abonnement Eqology) ---
  { slug: 'pure-nordic-health', cat: 'programmes', nom: 'Programme Pure Nordic Health', detail: 'Huile + K2 + D3 + Booster + test', parMois: 41,
    texte: 'Le programme le plus complet : Pure Arctic Oil, vitamines K2 + D3, Nordic Energy Booster et un test pour suivre vos résultats.',
    points: ['Une huile Pure Arctic Oil au choix', 'Vitamines K2 + D3', 'Nordic Energy Booster', 'Test inclus'],
    usage: "Programme sur abonnement Eqology : lisez la durée d'engagement sur la page de commande." },
  { slug: 'pure-k2d3-valuepack', cat: 'programmes', nom: 'Programme Pure K2 + D3', detail: 'Huile + K2 + D3 + test', parMois: 41,
    texte: "Pure Arctic Oil et les vitamines K2 + D3, réunies dans un pack plus avantageux, avec un test pour mesurer.",
    points: ['Pure Arctic Oil', 'Vitamines K2 + D3', 'Test inclus'],
    usage: "Programme sur abonnement Eqology : lisez la durée d'engagement sur la page de commande." },
  { slug: 'pure-energy-booster', cat: 'programmes', nom: 'Programme Pure Energy Booster', detail: 'Huile + Booster + test', parMois: 41,
    texte: 'Une huile Pure Arctic Oil au choix et le Nordic Energy Booster, pour compléter une alimentation équilibrée.',
    points: ['Une huile Pure Arctic Oil au choix', 'Nordic Energy Booster', 'Test inclus'],
    usage: "Programme sur abonnement Eqology : lisez la durée d'engagement sur la page de commande." },
  { slug: 'pure-marine-collagen', cat: 'programmes', nom: 'Programme Pure Marine Collagen', detail: 'Huile + collagène marin + test', parMois: 41,
    texte: 'Pure Arctic Oil associée au collagène marin Premium+, avec un test oméga-3.',
    points: ['Pure Arctic Oil', 'Marine Collagen Premium+', 'Test inclus'],
    usage: "Programme sur abonnement Eqology : lisez la durée d'engagement sur la page de commande." },
  { slug: 'family-pack', cat: 'programmes', nom: 'Family Pack', detail: 'Adultes + enfants',
    texte: 'Un flacon de Pure Arctic Oil et un flacon de Pure Arctic Oil For Kids, pour toute la famille.',
    points: ['Pure Arctic Oil (300 ml)', 'Pure Arctic Oil For Kids (150 ml)'],
    usage: 'Le prix et les conditions sont indiqués sur la page de commande Eqology.' },

  // --- Vitamines et forme ---
  { slug: 'vitamin-k2-d3', cat: 'vitamines', nom: 'Vitamines K2 + D3', detail: 'Gélules', prix: 38, top: 6,
    texte: "De la vitamine K2 (ménaquinone-7) et de la vitamine D3. La vitamine D contribue au maintien d'une ossature normale.",
    points: ['Vitamine K2 (MK-7)', 'Vitamine D3', 'Une gélule par jour'],
    usage: 'Une gélule par jour, au repas.' },
  { slug: 'vitamin-k2d3-drops', cat: 'vitamines', nom: 'Vitamines K2 + D3 en gouttes', detail: 'Flacon compte-gouttes', prix: 43,
    texte: 'Les vitamines K2 et D3 en gouttes, faciles à doser pour toute la famille. La vitamine D contribue au fonctionnement normal du système immunitaire.',
    points: ['Vitamine K2 naturelle', 'Vitamine D3', 'Format gouttes'],
    usage: 'Quelques gouttes par jour, selon la notice.' },
  { slug: 'vitamin-k2d3-gold', cat: 'vitamines', nom: 'K2 + D3 Gold', detail: 'Avec astaxanthine', prix: 48,
    texte: "Vitamine K2 MenaQ7®, vitamine D3 et astaxanthine naturelle Astalif®, un antioxydant d'origine nordique.",
    points: ['Vitamine K2 MenaQ7®', 'Vitamine D3', 'Astaxanthine Astalif®'],
    usage: 'Une gélule par jour, au repas.' },
  { slug: 'nordic-energy-booster', cat: 'vitamines', nom: 'Nordic Energy Booster', detail: 'Vitamines, minéraux, antioxydants', prix: 51,
    texte: "Un complexe de vitamines, de minéraux et d'antioxydants à forte biodisponibilité, doux pour l'estomac.",
    points: ['Vitamines et minéraux', 'Antioxydants', "Doux pour l'estomac"],
    usage: 'Selon la notice, au repas.' },
  { slug: 'pure-vegan-shake', cat: 'vitamines', nom: 'Pure Vegan Shake', detail: 'Protéines de riz et de pois', prix: 49,
    texte: 'Un substitut de repas végétal à base de protéines de riz et de pois.',
    points: ['Protéines de riz et de pois', '100 % végétal'],
    usage: 'À mélanger avec une boisson, selon la notice.' },

  // --- Beauté ---
  { slug: 'ocean-miracle-plumping-serum', cat: 'beaute', nom: 'Ocean Miracle, sérum repulpant', detail: '30 ml', prix: 92, badge: 'Primé',
    texte: "Un sérum léger, sans huile, qui pénètre vite. La pièce maîtresse de la ligne de soins Ocean Miracle d'Eqology.",
    points: ['Texture légère, sans huile', 'Pénètre rapidement', 'Flacon de 30 ml'],
    usage: 'Matin et soir sur peau propre.' },
  { slug: 'ocean-miracle-cleansing-gel', cat: 'beaute', nom: 'Ocean Miracle, gel nettoyant', detail: '150 ml', prix: 52,
    texte: 'Un gel doux qui démaquille et nettoie la peau sans la dessécher.',
    points: ['Démaquille et nettoie', 'Respecte l’hydratation de la peau', 'Tube de 150 ml'],
    usage: 'Matin et soir, puis rincer.' },

  // --- Coffrets de Noël ---
  { slug: 'christmas-pack-large', cat: 'coffrets', nom: 'Coffret Immune Shield', detail: 'Grand coffret de Noël', prix: 189, badge: 'Noël',
    texte: 'Le grand coffret de Noël : Pure Arctic Oil Gold, Pure Arctic Oil Heart & Energy, un test oméga-3, Nordic Energy Booster et vitamine D3 en gouttes.',
    points: ['Pure Arctic Oil Gold', 'Pure Arctic Oil Heart & Energy', 'Test oméga-3', 'Nordic Energy Booster', 'Vitamine D3 en gouttes'],
    usage: 'Édition limitée de Noël, dans la limite des stocks Eqology.' },
  { slug: 'christmas-pack-vegan', cat: 'coffrets', nom: 'Coffret Immune Shield végan', detail: 'Grand coffret de Noël', prix: 199, badge: 'Noël',
    texte: 'La version végane du grand coffret : Pure Vegan Oil, un test oméga-3, Nordic Energy Booster et vitamines K2 + D3 en gouttes.',
    points: ['Pure Vegan Oil', 'Test oméga-3', 'Nordic Energy Booster', 'Vitamines K2 + D3 en gouttes'],
    usage: 'Édition limitée de Noël, dans la limite des stocks Eqology.' },
  { slug: 'christmas-pack-medium', cat: 'coffrets', nom: 'Coffret Winter Glow', detail: 'Coffret beauté de Noël', prix: 149, badge: 'Noël',
    texte: 'Le coffret beauté : gel nettoyant, crème jour et nuit, sérum repulpant Ocean Miracle et Nordic Energy Booster.',
    points: ['Ocean Miracle gel nettoyant', 'Ocean Miracle crème jour et nuit', 'Ocean Miracle sérum repulpant', 'Nordic Energy Booster'],
    usage: 'Édition limitée de Noël, dans la limite des stocks Eqology.' },
  { slug: 'christmas-pack-small', cat: 'coffrets', nom: 'Coffret Eqology', detail: 'Petit coffret de Noël', prix: 109, badge: 'Noël',
    texte: "L'essentiel pour découvrir Eqology : Pure Arctic Oil, vitamines K2 + D3 et un test oméga-3.",
    points: ['Pure Arctic Oil', 'Vitamines K2 + D3', 'Test oméga-3'],
    usage: 'Édition limitée de Noël, dans la limite des stocks Eqology.' },
];

// Utilitaires communs
window.produit = (slug) => window.PRODUITS.find((p) => p.slug === slug);
window.prixTexte = (p) => p.prix ? p.prix.toLocaleString('fr-FR') + ' €' : (p.parMois ? 'dès ' + p.parMois + ' € / mois' : 'Prix chez Eqology');
window.lienEqology = (p) => window.lienCommande('https://eqology.com/fr/eqology-' + p.slug);

window.carteProduit = (p) => `
  <article class="group relative flex flex-col rounded-lg bg-sable text-nuit overflow-hidden transition-transform duration-300 hover:-translate-y-0.5">
    <a href="produit.html?p=${p.slug}" class="absolute inset-0 z-10" aria-label="${p.nom}"></a>
    <div class="relative aspect-square bg-white">
      ${p.badge ? `<span class="absolute top-3 left-3 z-[1] text-[11px] font-medium px-2.5 py-1 rounded-md ${p.badge === 'Noël' ? 'bg-rouge text-white' : 'bg-nuit text-white'}">${p.badge}</span>` : ''}
      <img src="assets/v2/produits/${p.slug}.webp" alt="${p.nom}" class="absolute inset-0 w-full h-full object-contain p-5 sm:p-7 group-hover:scale-[1.04] transition-transform duration-500" width="720" height="720" loading="lazy" decoding="async">
    </div>
    <div class="flex flex-col flex-1 p-4 sm:p-5">
      <h3 class="text-[16px] sm:text-xl font-light leading-snug">${p.nom}</h3>
      <p class="text-xs sm:text-sm text-nuit/60 mt-1">${p.detail}</p>
      <div class="mt-auto pt-4 flex items-center justify-between gap-2">
        <span class="text-base sm:text-lg leading-tight">${p.prix ? window.prixTexte(p) : (p.parMois ? 'dès ' + p.parMois + '&nbsp;€<span class="block text-xs text-nuit/60">par mois</span>' : '<span class="text-sm">Prix chez Eqology</span>')}</span>
        <button type="button" data-ajouter="${p.slug}" class="relative z-20 shrink-0 inline-flex items-center gap-1.5 h-10 sm:h-9 px-3 rounded-full bg-nuit text-white text-[13px] hover:bg-glacier-600 transition-colors" aria-label="Ajouter ${p.nom} au panier"><svg width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linejoin="round" d="M5 8h14l-1 12H6L5 8Z"/><path stroke-linecap="round" d="M9 8V6a3 3 0 0 1 6 0v2"/></svg><span class="hidden sm:inline">Ajouter</span></button>
      </div>
    </div>
  </article>`;

// Pas de coffrets de Noël sur le site (décision du 25/11) : rayon et produits retirés partout
window.CATEGORIES = window.CATEGORIES.filter(function (c) { return c.id !== 'coffrets'; });
window.PRODUITS = window.PRODUITS.filter(function (p) { return p.cat !== 'coffrets'; });

// ============ Panier (gardé dans le navigateur ; paiement et livraison chez Eqology) ============
window.PANIER = {
  lire: function () { try { return JSON.parse(localStorage.getItem('panier') || '[]').filter(function (l) { return window.produit(l.slug); }); } catch (e) { return []; } },
  ecrire: function (l) { try { localStorage.setItem('panier', JSON.stringify(l)); } catch (e) {} document.dispatchEvent(new CustomEvent('panier')); },
  ajouter: function (slug, q) { var l = this.lire(), x = l.find(function (i) { return i.slug === slug; }); if (x) x.qte = Math.min(20, x.qte + (q || 1)); else l.push({ slug: slug, qte: q || 1 }); this.ecrire(l); },
  changer: function (slug, q) { var l = this.lire(); l.forEach(function (i) { if (i.slug === slug) i.qte = Math.max(1, Math.min(20, q)); }); this.ecrire(l); },
  retirer: function (slug) { this.ecrire(this.lire().filter(function (i) { return i.slug !== slug; })); },
  vider: function () { this.ecrire([]); },
  nombre: function () { return this.lire().reduce(function (n, i) { return n + i.qte; }, 0); },
  total: function () { return this.lire().reduce(function (t, i) { var p = window.produit(i.slug); return t + (p && p.prix ? p.prix * i.qte : 0); }, 0); },
  aPrixVariable: function () { return this.lire().some(function (i) { var p = window.produit(i.slug); return p && !p.prix; }); },
  euros: function (n) { return n.toLocaleString('fr-FR', { minimumFractionDigits: n % 1 ? 2 : 0, maximumFractionDigits: 2 }) + '\u00a0€'; },
  texte: function () { return this.lire().map(function (i) { var p = window.produit(i.slug); return i.qte + ' × ' + p.nom + ' (' + window.prixTexte(p) + ')'; }).join('\n'); }
};
