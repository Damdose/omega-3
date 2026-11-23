# -*- coding: utf-8 -*-
"""Plan du nouveau site d'Yves (variante V2), format EXPLICATION.  python3 -I mission/plan_site_v2.py"""
import os, sys
ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser('~/Documents/crm-heyfuture/docs/chantier-skills/formats'))
import explication as X

L = 'http://127.0.0.1:8140/'

cfg = dict(
    onglet='Plan du site V2 · Yves',
    oeil='Yves Coignard · site V2 · 23 novembre 2026',
    titre='Une vraie boutique en vitrine, le recrutement en coulisses',
    chapo='Le site a l’allure d’un e-commerce (24 produits, prix, fiches, coffrets de Noël) ; les pubs, elles, envoient sur « Rejoindre l’équipe ». Ce qui est fait, et les cinq éléments à obtenir d’Yves.',
    logo=os.path.join(ICI, '..', 'assets', 'images', 'eqology-eq.png'),
    polices=dict(titre='Space Grotesk', texte='DM Sans',
                 lien='https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,600;9..40,700&family=Space+Grotesk:wght@500;600;700&display=swap'),
    couleurs=dict(rouge='#335075', vert='#3d8691', jaune='#A88C5C'),
    variables={'fond': '#FAFAF8', 'trait': '#ECEAE4', 'vert-pale': '#EEF8F9'},
    parties=[
        dict(
            titre='Le site sert à obtenir un numéro de téléphone',
            court='Objectif',
            intro=['Yves cherche des partenaires, pas des ventes en ligne. Chaque page pousse vers un seul geste : laisser son numéro pour être rappelé. La boutique existe parce qu’elle a été facturée et qu’elle rend service, mais aucune publicité ne l’envisage comme destination.'],
            schema=X.flux([('Pub Meta', 'story Instagram', 'neutre'), ('Page équipe', 'atterrissage', 'fort'),
                           ('Formulaire', '1 minute', 'fort'), ('Appel d’Yves', 'sous 48 h', 'ok'), ('Visio équipe', 'puis kit', 'ok')],
                          legende='Le parcours d’un futur partenaire'),
            exemple='Une naturopathe voit la story, arrive sur « Rejoindre l’équipe », coche « Praticien de santé », choisit « l’après-midi ». Yves reçoit un e-mail « À rappeler — Claire M. · L’après-midi » avec son métier et la pub d’origine.',
            donc='la page « Rejoindre l’équipe » est la page la plus importante du site ; l’accueil et la boutique y renvoient.',
        ),
        dict(
            titre='Les directives : cinq pages, deux publics, aucune promesse',
            court='Directives',
            points=[
                dict(titre='Deux publics, dans cet ordre', texte='D’abord les praticiens de santé (naturopathes, micronutritionnistes, diététiciens, kinés, ostéos), ensuite les particuliers de 35 à 70 ans qui cherchent un complément de revenu. Les médecins ne voient que le test et la science.'),
                dict(titre='Une boutique complète', texte='Accueil en vitrine (bannières, catégories illustrées, meilleures ventes, coffrets de Noël) · boutique filtrable par rayon · une fiche par produit avec prix et bouton « Commander chez Eqology » · Le test · Rejoindre l’équipe. Le paiement et la livraison restent chez Eqology.'),
                dict(titre='Ce qui est interdit', texte='Plus de FENA, pas d’IFOS, pas de note Trustpilot affichée, aucun témoignage inventé, aucun montant de revenu. Toujours « distributeur indépendant Eqology ».'),
                dict(titre='La charte reste', texte='Bleu nuit, bleu glacier, crème, Space Grotesk et DM Sans. Même espace en haut et en bas de chaque section, réglé une seule fois dans site.css.'),
                dict(titre='Zéro technique pour Yves', texte='Il reçoit un e-mail par contact (bientôt un SMS ou WhatsApp) et rappelle. Le lien partenaire et le pixel se règlent dans un seul fichier, site-config.js.'),
            ],
            donc='tout ce qui touche à l’argent se dit pendant la visio, avec le plan officiel d’Eqology, jamais sur le site.',
        ),
        dict(
            titre='La boutique est construite et vérifiée sur mobile et ordinateur',
            court='Fait',
            intro=[f'Elle vit sur une branche à part (site-v2) : le site en ligne n’a pas bougé. Pages à ouvrir : <a href="{L}index.html">accueil</a>, <a href="{L}boutique.html">boutique</a>, <a href="{L}produit.html?p=pure-arctic-oil-gold">une fiche produit</a>, <a href="{L}rejoindre-l-equipe.html">rejoindre l’équipe</a>, <a href="{L}le-test.html">le test</a>.'],
            deux=[dict(titre='Fait, vérifié à 390 et 1440 px', texte='24 produits Eqology avec photo officielle et prix relevé le 23/11 · accueil vitrine · rayons filtrables et recherche · fiches produit · page « Rejoindre l’équipe » et son formulaire relié à /api/lead · les 24 liens « Commander » vérifiés.'),
                  dict(titre='En attente', ton='mal', texte='Photo et vidéo d’Yves · lien partenaire Eqology · pixel Meta · alerte SMS ou WhatsApp · relances e-mail à J0, J2 et J5.')],
            donc='le squelette et les textes sont prêts ; ce qui manque dépend d’Yves ou des accès Meta.',
        ),
        dict(
            titre='Cinq éléments d’Yves bloquent la mise en ligne',
            court='Bloquants',
            points=[
                dict(titre='1. Son lien partenaire Eqology', texte='Sans lui, une commande passée depuis le site ne lui est pas attribuée. C’est le seul bloquant absolu.'),
                dict(titre='2. Une photo portrait', texte='Verticale, lumière du jour. Elle remplace le cadre « à fournir » de l’accueil.'),
                dict(titre='3. La vidéo de 10 minutes', texte='Son histoire, l’activité, comment on démarre. Filmée au téléphone, ça suffit. En attendant, le cadre peut disparaître.'),
                dict(titre='4. SMS ou WhatsApp', texte='Pour l’alerte « nouveau contact ». Aujourd’hui, l’e-mail part déjà vers son adresse Gmail.'),
                dict(titre='5. L’accès Meta Business', texte='L’invitation sur damien.growth@gmail.com, pour poser le pixel et l’événement « Lead » avant le lancement des pubs.'),
            ],
            donc_ton='mal', donc_mot='Attention',
            donc='la date promise (site lundi 23/11, pubs mercredi 25/11) ne tient que si le lien partenaire arrive aujourd’hui ou demain.',
        ),
        dict(
            titre='La suite : finir, vérifier, puis mettre en ligne à ton feu vert',
            court='Suite',
            schema=X.etapes_num([('Tes retours', 'corrections'), ('Yves', 'lien, photo'),
                                 ('Pixel, alertes', 'Lead, SMS'), ('Contrôles', 'Lighthouse ≥ 90'), ('En ligne', 'à ton feu vert')],
                                resultat='Puis les pubs'),
        ),
    ],
    decision='On garde cette variante comme base (je corrige d’après tes retours), ou je te prépare une seconde direction pour comparer ?',
)

sortie = os.path.join(ICI, 'plan-site-v2.html')
open(sortie, 'w').write(X.document(cfg))
print(sortie)
