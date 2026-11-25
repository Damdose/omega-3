# Design system du site d'Yves Coignard (distributeur indépendant Eqology)

Version 1 du 25/11/2026. Référence vivante : `design-system.html` (exclue de Google).
Inspiration : les mécanismes d'usage de patch.io, appliqués aux produits Eqology et au trafic Meta.

## Principes (trafic Meta, mobile d'abord)
1. Le titre du premier écran reprend l'accroche de la pub (`partenaire.html?cible=pro|visio`).
2. Une seule action en orange par écran : tester, commander, être rappelé. Le reste en contour.
3. L'action est visible sans défiler, puis une barre d'action fixe apparaît sur mobile.
4. Les preuves arrivent tout de suite (bande qui défile) : MSC, GOED, Superior Taste Award, Oslo. Jamais de faux avis.
5. Le prix est dans le bouton (« Commencer par le test · 88 € »).
6. Aucune promesse de revenu ; toujours « distributeur indépendant Eqology » ; pas de FENA ni d'IFOS.

## Fondations
- Couleurs (`tw-config.js`) : `navy-900` #141613 fond, `navy-800` #1E201C cartes sombres, blanc pour les cartes claires,
  `cream-100` #EFEFEA vignettes produit, `rouge` #EE6A2C action, #243B2E bloc partenariat, `navy-300` texte secondaire.
  Le logo Eqology garde son rouge.
- Police : Satoshi (Fontshare) 300 / 400 / 500 / 700. `.geant` 300, `.titre.fin` 300, `.titre` 400.
- Arrondis : 6-8 px pour boutons et étiquettes, 12 px (`rounded-xl`) pour cartes et images, 16 px pour les grands blocs.
- Espacement : `.sec` (même valeur en haut et en bas), `.wrap` (1180 px), `.filet` en tête de chaque section.

## Composants (dans `site.css`, `components.js`, `catalogue.js`)
- Boutons : `.btn` + `.btn-plein` (orange, flèche automatique) / `.btn-clair` (contour blanc) / `.btn-ligne` (contour sombre, sur fond clair).
- En-tête de section : `.filet` > `.oeil` (étiquette à losange) > `h2.titre.fin`.
- Fiche produit : `carteProduit(p)` ; prix via `prixTexte(p)` ; lien de commande via `lienEqology(p)`.
- Navigation flottante et pied de page avec logo géant : `components.js` (version réduite sur `partenaire.html` et `merci.html`).
- Formulaires : carte blanche `text-navy-900`, un seul bouton `.btn-plein`.

## Mécanismes (`assets/v2/mecanismes.js`)
`.defile` (bande de preuves), `MECA.orbite` (étapes qui avancent seules), `MECA.onglets` (arguments à progression),
`MECA.carrousel` + `.rail` (rayons), `MECA.eclaire` (phrase qui s'éclaire), `MECA.barreMobile` (barre d'action).

## Règles de maintenance
- Après toute modification de classes : `npx -y tailwindcss@3.4.17 -c tailwind.config.cjs -i tw-entree.css -o assets/v2/site-tw.css --minify`
  (`tw-entree.css` embarque une copie de `site.css`).
- Une nouvelle page reprend le gabarit vitrine ou le gabarit partenaire décrits dans `design-system.html`.
- Toute zone claire dans une page sombre fixe sa couleur de texte (`text-navy-900`).
