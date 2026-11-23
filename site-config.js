// ============================================================
// RÉGLAGES DU SITE — le seul fichier à modifier pour les liens
// ============================================================
window.SITE = {
  // Lien partenaire d'Yves (boutique Eqology codée à son identifiant).
  // À FOURNIR par Yves avant la mise en ligne : sans lui, les ventes ne lui sont pas attribuées.
  lienBoutique: '',
  // Repli tant que le lien partenaire n'est pas renseigné
  boutiqueParDefaut: 'https://eqology.com/fr/our-products',
  // Comment ajouter l'identifiant partenaire à un lien produit Eqology.
  // {url} = page produit, {code} = identifiant. À ajuster quand Yves aura donné son lien.
  codePartenaire: '',
  modeleLienProduit: '{url}',
  // Identifiant du pixel Meta (vide = pas de pixel chargé)
  pixelMeta: '',
  // Page Trustpilot d'Eqology (avis publics, sans note affichée)
  trustpilot: 'https://fr.trustpilot.com/review/eqology.com',
};

// Lien de commande d'un produit (avec l'identifiant partenaire quand il sera connu)
window.lienCommande = function (url) {
  var S = window.SITE;
  if (!S.codePartenaire) return url;
  return S.modeleLienProduit.replace('{url}', url).replace('{code}', S.codePartenaire);
};

(function () {
  var S = window.SITE;
  var lien = S.lienBoutique || S.boutiqueParDefaut;
  // Tous les boutons « Commander » pointent vers la boutique partenaire
  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('[data-boutique]').forEach(function (a) {
      a.href = lien;
      a.target = '_blank';
      a.rel = 'noopener';
    });
    document.querySelectorAll('[data-trustpilot]').forEach(function (a) { a.href = S.trustpilot; });
  });
  // Pixel Meta, seulement s'il est renseigné
  if (S.pixelMeta) {
    !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');
    fbq('init', S.pixelMeta);
    fbq('track', 'PageView');
  }
})();
