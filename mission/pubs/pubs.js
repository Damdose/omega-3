// Les créations Meta : une ligne par pub. Le nom (id) sert aussi d'utm_content.
// Visio : renseigner DATE_VISIO puis relancer node mission/pubs/rendre.mjs
window.DATE_VISIO = { jour: '', heure: '20 h' };
window.PUBS = [
  // A · Praticiens de santé
  { id: 'A1-test-mesure', camp: 'A', badge: 'Praticiens de santé', fond: 'testkit-detail.webp', pos: '50% 40%',
    titre: 'Vos patients vous demandent quels oméga&#8209;3 prendre ?', sous: 'Donnez-leur une mesure, pas un avis.', produit: 'omega-3-test-kit' },
  { id: 'A2-premier-second-test', camp: 'A', badge: 'Praticiens de santé', fond: null,
    titre: 'Un premier test.<br>Un second pour comparer.', sous: 'Le test oméga-3 se fait à la maison, analysé par un laboratoire indépendant.', produit: 'omega-3-test-kit', double: true },
  { id: 'A3-sans-vendre', camp: 'A', badge: 'Praticiens de santé', fond: 'consultation.webp', pos: '62% 50%',
    titre: 'Recommander, sans rien vendre au cabinet.', sous: 'Vos patients commandent seuls chez Eqology.' },
  { id: 'A4-trace-msc', camp: 'A', badge: 'Praticiens de santé', fond: 'peche.webp', pos: '50% 50%',
    titre: 'Une huile tracée jusqu’au bateau.', sous: 'Pêche certifiée MSC : un produit que vous pouvez expliquer.', produit: 'pure-arctic-oil' },
  // B · Complément de revenu
  { id: 'B1-sans-stock', camp: 'B', badge: 'Partenariat Eqology', fond: 'flacon-roche.webp', pos: '50% 55%',
    titre: 'Un complément de revenu, sans stock, à votre rythme.', sous: 'Recommandez des oméga-3 de qualité. Eqology livre.' },
  { id: 'B2-parlez-sante', camp: 'B', badge: 'Partenariat Eqology', fond: 'sante-immunite.webp', pos: '40% 50%',
    titre: 'Vous parlez déjà santé autour de vous ?', sous: 'Ça peut devenir une activité.' },
  { id: 'B3-eqology-livre', camp: 'B', badge: 'Partenariat Eqology', fond: 'fjord.webp', pos: '50% 50%',
    titre: 'Pas de stock.<br>Pas de local.<br>Pas d’horaires.', sous: 'Eqology livre, vous recommandez.', produit: 'pure-arctic-oil-gold' },
  // C · Visio de présentation
  { id: 'C1-visio-date', camp: 'C', badge: 'Visio gratuite', fond: 'nature.webp', pos: '50% 50%', visio: true,
    titre: '{DATE} à {HEURE}', sous: '45 minutes en visio pour comprendre le partenariat Eqology.' },
  { id: 'C2-visio-gratuite', camp: 'C', badge: 'Visio gratuite', fond: 'consultation.webp', pos: '62% 50%',
    titre: 'Gratuit, sans engagement : posez vos questions en direct.', sous: 'Une visio de présentation du partenariat Eqology.' },
  { id: 'C3-visio-questions', camp: 'C', badge: 'Visio gratuite', fond: null,
    titre: 'Stock, temps, démarrage.', sous: 'On répond à tout pendant la visio.', liste: ['Faut-il acheter du stock ?', 'Combien de temps faut-il ?', 'Comment démarre-t-on ?'] },
  { id: 'C4-plus-que-2-jours', camp: 'C', badge: 'Visio gratuite', fond: 'fjord.webp', pos: '50% 50%', visio: true,
    titre: 'Plus que 2 jours.', sous: 'Visio de présentation : {DATE} à {HEURE}.' },
  // D · Reciblage
  { id: 'D1-argent', camp: 'D', badge: 'Partenariat Eqology', fond: null,
    titre: 'D’où vient vraiment l’argent ?', sous: 'Des produits achetés par des clients. Le plan officiel vous est montré ligne par ligne.', produit: 'pure-arctic-oil' },
  { id: 'D2-eqology-fait-le-reste', camp: 'D', badge: 'Partenariat Eqology', fond: 'huile.webp', pos: '80% 50%',
    titre: 'Vous parlez aux gens.<br>Eqology fait le reste.', sous: 'Commande, paiement, livraison, service client.' },
  { id: 'D3-aimez-produits', camp: 'D', badge: 'Partenariat Eqology', fond: 'gamme.webp', pos: '50% 50%',
    titre: 'Vous aimez ces produits ? Recommandez-les.', sous: 'Et faites-en une activité, avec l’équipe d’Yves.' },
];
