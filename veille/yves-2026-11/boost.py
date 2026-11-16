# -*- coding: utf-8 -*-
"""La stratégie de Boost Your Health montrée étape par étape, avec captures. Format EXPLICATION. Usage : python3 boost.py"""
import os, sys, html
sys.path.insert(0, os.path.expanduser('~/Documents/crm-heyfuture/docs/chantier-skills/formats'))
import explication as X

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))


def capture(src, legende, telephone=False):
    largeur = 'max-width:300px;margin-inline:auto' if telephone else ''
    return (f'<figure style="margin:0;display:grid;gap:8px;{largeur}">'
            f'<img src="{src}" alt="{html.escape(legende)}" '
            f'style="width:100%;height:auto;border-radius:14px;border:1px solid var(--trait);display:block">'
            f'<figcaption style="font-size:13.5px;color:var(--encre-2)">{legende}</figcaption></figure>')


def deux_captures(a, b):
    return f'<div class="deux" style="align-items:start">{a}{b}</div>'


cfg = dict(
    onglet='Stratégie Boost Your Health',
    oeil='Une référence envoyée par Yves · 16 novembre 2026',
    titre='Boost Your Health : comment ils trouvent clients et business partners',
    chapo=('Dennis et Anne Sied sont distributeurs Eqology aux Pays-Bas, comme Yves en France. '
           'Nous avons suivi tout leur parcours, d’Instagram jusqu’au rendez-vous. Voici ce que voit un inconnu, étape par étape, et pourquoi ça marche.'),
    logo=os.path.join(RACINE, 'assets/images/eqology-logo.png'),
    polices=dict(titre='Space Grotesk', texte='DM Sans',
                 lien='https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700&family=Space+Grotesk:wght@500;600;700&display=swap'),
    couleurs=dict(rouge='#B4483A', vert='#3D8691', jaune='#9A7A45'),
    variables={'marque': '#335075'},
    parties=[
        dict(
            court='En résumé',
            etiquette='Leur stratégie en une phrase',
            titre='Ils vendent une vie libre, puis proposent un appel de 15 minutes',
            intro=['Leur Instagram montre une famille qui vit et travaille où elle veut. La bio mène à deux endroits : '
                   'un Linktree qui sert de boutique, et un site qui demande « Où veux-tu commencer ? ». '
                   'Quelle que soit la réponse, tout finit par un appel gratuit de 15 minutes. C’est pendant cet appel qu’ils vendent l’huile ou l’activité.',
                   'Ils ne font aucune publicité Meta : nous n’avons trouvé aucune pub à leur nom dans la Bibliothèque publicitaire. Tout est organique.'],
            schema=X.flux([('Instagram', 'leur vie', 'note'), ('Linktree', 'boutique codée', 'ok'),
                           ('Site', 'deux portes', 'ok'), ('Appel 15 min', 'Calendly', 'fort'),
                           ('Client', 'ou partenaire', 'note')],
                          legende='Le parcours d’un inconnu chez Boost Your Health'),
            donc='le cœur de leur stratégie, c’est l’appel. Instagram, le Linktree et le site n’existent que pour y amener les gens.',
        ),
        dict(
            court='1. Instagram',
            etiquette='Étape 1',
            titre='Instagram montre une vie, presque jamais un produit',
            intro=['Le compte s’appelle « Dennis & Anne Sied » et non « Boost Your Health Eqology ». La bio tient en quatre lignes : '
                   '« Nordic Health Concept | mesurer = savoir », « 1 vie. Vis-la ! », « Oméga-3. Absolument essentiel ! », '
                   'et surtout « Travailler où tu veux ? REJOINS L’ÉQUIPE ».',
                   'Les stories à la une s’appellent Workouts, Work remote, Home schooling et Food. Les publications montrent le sport, les voyages, les enfants et leur chat. '
                   'La vidéo du chat a fait 21 000 j’aime, alors que les autres en font entre 14 et 79.'],
            html=deux_captures(
                capture('boost/5-instagram.jpg', 'Leur profil Instagram, tel qu’Yves te l’a envoyé : 1 847 abonnés, « JOIN THE TEAM » dans la bio.', telephone=True),
                '<div class="point ok"><h3>Ce qu’ils publient</h3>'
                '<p><b>La vie</b> : « 1 000 step-ups avec 10 kilos sur la nuque », les vacances, l’école à la maison.</p>'
                '<p><b>Un peu de pédagogie</b> : « Café ou thé tous les jours ? Pourquoi pas les oméga-3 ? »</p>'
                '<p><b>Une publication épinglée pour recruter</b> : « Et si une seule décision te donnait plus de liberté que tu ne l’imaginais ? »</p>'
                '<div class="exemple"><b>À retenir</b>On suit des gens, pas une marque. L’huile arrive en second.</div></div>'),
            donc='Instagram sert à donner envie de leur vie et à créer la confiance. La vente ne se fait pas là.',
        ),
        dict(
            court='2. Le Linktree',
            etiquette='Étape 2 · L’e-commerce',
            titre='Le lien en bio est une boutique de 22 produits, chacun avec leur code',
            intro=['linktr.ee/boostyourhealth.eu range 22 produits par familles : oméga-3, packs avantage, vitamines, beauté. '
                   'Chaque bouton ouvre la fiche produit sur le site d’Eqology avec leur code de partenaire dans l’adresse '
                   '(eqology.com/nl/__s31ef49s__/produit). Le client paie chez Eqology, la vente leur revient.'],
            html=deux_captures(
                capture('boost/6-linktree.jpg', 'Leur Linktree : « Les meilleurs produits pour ta santé ! »', telephone=True),
                '<div class="point ok"><h3>Pourquoi c’est malin</h3>'
                '<p>Zéro stock, zéro paiement à gérer, zéro service client. Ils n’ont pas eu besoin de construire une boutique : '
                'le Linktree en fait office, et Eqology s’occupe du reste.</p>'
                '<div class="exemple"><b>Pour Yves</b>Le nouveau site peut faire la même chose en mieux : de vraies fiches produits en français, '
                'avec chaque bouton « Acheter » vers Eqology et son code.</div></div>'),
            donc='c’est le modèle e-commerce d’un distributeur : une vitrine à soi, un panier chez Eqology.',
        ),
        dict(
            court='3. Le site',
            etiquette='Étape 3',
            titre='Le site pose une seule question : « Où veux-tu commencer ? »',
            intro=['Le titre annonce la couleur : « Boost health, Grow wealth », avec Dennis caché derrière le livre « Réfléchissez et devenez riche ». '
                   'On parle d’argent dès la première seconde.',
                   'Juste en dessous, deux portes : « Améliorer ma santé » mène au test, « Entreprendre dans la santé » mène au rendez-vous. '
                   'Les chiffres d’Eqology rassurent ensuite : 33 pays, plus de 530 000 tests sanguins, +2 400 % de croissance depuis 2015.'],
            html=capture('boost/1-accueil.jpg', 'L’accueil : « Commence ton chemin vers la liberté financière. »')
                 + capture('boost/2-deux-portes.jpg', 'Les deux portes, puis les chiffres d’Eqology.'),
            donc='en une question, le visiteur se range tout seul : futur client ou futur partenaire.',
        ),
        dict(
            court='4. Leur offre',
            etiquette='Étape 4',
            titre='Ils vendent leur accompagnement, pas le produit',
            intro=['La section « Qu’est-ce que je t’offre ? » montre la famille sur une plage. Dennis raconte qu’il a découvert l’opportunité il y a huit ans '
                   'et qu’il travaille « quand et où il veut ». Il promet quatre choses : un accompagnement personnel, un concept éprouvé, '
                   'une équipe qui motive, et la liberté. Il précise à la fin qu’il est « Business Partner indépendant Eqology ».'],
            html=capture('boost/3-famille.jpg', '« Ce n’est pas un emploi classique. C’est une occasion de faire la différence, pour toi et pour les autres. »'),
            donc='on rejoint Dennis et son équipe avant de rejoindre Eqology. La personne est l’argument.',
        ),
        dict(
            court='5. Les témoignages',
            etiquette='Étape 5 · Le recrutement',
            titre='Leurs témoignages sont ceux de professionnels qu’ils ont recrutés',
            intro=['Les sept témoignages viennent presque tous de gens qui ont déjà une activité et une clientèle : '
                   'Fresh Start (coach en nutrition), Restore Your Skin (eczéma et allergies), Poepgoed.nl (santé intestinale), Performance House (sport). '
                   'Chacun raconte la même histoire : il a d’abord proposé Eqology à ses clients, puis il a monté sa propre équipe.'],
            html=capture('boost/4-temoignages.jpg', 'Manouk Deuling, Fresh Start : « Depuis que je travaille avec Eqology et Dennis, mon activité est passée à un autre niveau. »'),
            points=[dict(titre='C’est là que se fait le chiffre', ton='ok',
                         texte='Une coach qui a 200 clients et les met sous oméga-3 vend plus que des centaines d’abonnés Instagram. '
                               'Poepgoed.nl l’a même ouvert à ses propres thérapeutes : une recrue amène toute une équipe.')],
            donc='Boost Your Health ne cherche pas des acheteurs un par un. Ils recrutent des professionnels qui ont déjà des clients.',
        ),
        dict(
            court='6. L’appel',
            etiquette='Étape 6',
            titre='Tout finit par un appel découverte gratuit de 15 minutes',
            intro=['Chaque bouton du site (« Prendre rendez-vous », « Planifier un échange ») ouvre leur Calendly : '
                   '« Échange découverte sans engagement », 15 minutes, en visio. C’est la seule vraie conversion du site.'],
            html=capture('boost/7-calendly.jpg', 'Leur Calendly, tel qu’Yves te l’a envoyé : 15 minutes, en visio, gratuit.', telephone=True),
            donc='le site ne vend rien directement. Il remplit l’agenda de Dennis, et c’est lui qui conclut.',
        ),
        dict(
            court='La pub',
            etiquette='Ce qu’ils ne font pas',
            titre='Boost Your Health ne fait pas de pub, mais d’autres distributeurs recrutent avec',
            intro=['Dans la Bibliothèque publicitaire, environ 90 distributeurs Eqology ont diffusé des pubs qui citent la marque. '
                   'Quelques-uns s’en servent pour recruter, avec la même cible que Boost Your Health.'],
            points=[
                dict(titre='marloes_orthohealthlab (Pays-Bas) : elle vise les coachs et les thérapeutes', ton='ok',
                     texte='« Tu travailles comme coach ou thérapeute et tu veux passer moins de temps sur ton marketing et plus avec tes clients ? '
                           'Alors c’est peut-être pour toi. Rejoins mon équipe chez Eqology. » (février 2026)'),
                dict(titre='Eqology Business Partners Sicilia (Italie) : 31 pubs pour remplir leurs soirées',
                     texte='Des pubs régulières de novembre 2025 à juin 2026, avec des sujets santé, pour faire venir du monde à leurs soirées de présentation.'),
                dict(titre='e.x.m.o.r.t.i.s (Pologne) : une pub pour une soirée « Business Opportunity »',
                     texte='« Le 4 juillet à Łódź, se retrouvent des gens qui en ont assez de faire du surplace. Je n’invite pas tout le monde. »'),
                dict(titre='jurkevicpaulina (Lituanie) : elle répond aux peurs',
                     texte='« Il y a quelques raisons simples pour lesquelles il ne faut pas avoir peur de rejoindre Eqology, surtout si tu envisages une activité en ligne. »'),
            ],
            donc='pour Yves, on prend le parcours de Boost Your Health et on ajoute ce qui leur manque : une pub Meta qui vise les coachs, thérapeutes et salles de sport, comme celle de marloes.',
        ),
    ],
    glossaire=[
        ('Linktree', 'Une page de liens qu’on met en bio Instagram. Boost Your Health s’en sert comme boutique.'),
        ('Lien codé', 'Un lien vers Eqology qui contient le code du partenaire. La commande lui est attribuée.'),
        ('Calendly', 'Un outil de prise de rendez-vous en ligne.'),
        ('Business Partner', 'Un distributeur indépendant Eqology. Il touche une commission sur ses ventes et sur celles de l’équipe qu’il recrute.'),
        ('Bibliothèque publicitaire', 'Le registre public de Meta où l’on voit toutes les pubs Facebook et Instagram, actives ou passées.'),
    ],
    decision='On reproduit ce parcours pour Yves (Instagram de vie, boutique en liens codés, site à deux portes, appel de 15 minutes), '
             'en ajoutant une pub Meta qui vise les coachs, thérapeutes et salles de sport : oui ou non ?',
    pied='Sources : boostyourhealth.eu, linktr.ee/boostyourhealth.eu, Instagram @boostyourhealth.eu, captures envoyées par Yves, Bibliothèque publicitaire Meta. Consultés le 16/11/2026.',
)

with open(os.path.join(ICI, 'boost-strategie.html'), 'w') as f:
    f.write(X.page(cfg))
print('ok')
