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
  // Prochaine visio de présentation (pubs « invitation », page partenaire.html?cible=visio)
  // Exemple : { jour: 'jeudi 4 décembre', heure: '20 h' } ; vide = message sans date
  prochaineVisio: { jour: '', heure: '' },
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
  // Pixel Meta : chargé seulement s'il est renseigné ET après accord aux cookies (RGPD)
  function chargerPixel() {
    if (!S.pixelMeta || window.fbq) return;
    !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');
    fbq('init', S.pixelMeta);
    fbq('track', 'PageView');
    (window._evenements || []).forEach(function (e) { fbq(e[0], e[1], e[2] || {}); });
  }
  window.chargerPixel = chargerPixel;
  var accord = null; try { accord = localStorage.getItem('cookies_accepted'); } catch (e) {}
  if (accord === 'true') chargerPixel();

  // Suivi d'un événement : envoyé tout de suite si le pixel tourne, sinon gardé jusqu'à l'accord
  window.suivre = function (nom, params, perso) {
    var type = perso ? 'trackCustom' : 'track';
    if (window.fbq) fbq(type, nom, params || {});
    else (window._evenements = window._evenements || []).push([type, nom, params]);
  };

  // Clic sur un bouton de commande Eqology : événement personnalisé ClicCommander
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href*="eqology.com"]');
    if (a) window.suivre('ClicCommander', { lien: a.href }, true);
  });
})();
