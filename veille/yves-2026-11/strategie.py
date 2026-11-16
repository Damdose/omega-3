# -*- coding: utf-8 -*-
"""Synthèse « stratégie des concurrents » pour Yves, format EXPLICATION. Usage : python3 strategie.py"""
import os, sys
sys.path.insert(0, os.path.expanduser('~/Documents/crm-heyfuture/docs/chantier-skills/formats'))
import explication as X

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))

cfg = dict(
    onglet='Concurrents oméga-3',
    oeil='Veille Eqology · 16 novembre 2026',
    titre='Comment vendent les concurrents d’Yves, et ce qu’on en reprend',
    chapo=('Nous avons passé au crible les 9 comptes envoyés par Yves, 22 autres distributeurs Eqology en Europe '
           'et toutes les publicités Meta qui parlent d’Eqology, de Zinzino et d’oméga-3 en France. '
           'Ce document résume leur méthode, ce qu’il y a au bout de chaque publicité, puis le modèle à suivre pour le nouveau site.'),
    logo=os.path.join(RACINE, 'assets/images/eqology-logo.png'),
    polices=dict(titre='Space Grotesk', texte='DM Sans',
                 lien='https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700&family=Space+Grotesk:wght@500;600;700&display=swap'),
    couleurs=dict(rouge='#B4483A', vert='#3D8691', jaune='#9A7A45'),
    variables={'marque': '#335075'},
    parties=[
        dict(
            court='Le principe',
            etiquette='Comprendre',
            titre='Tous vendent le test avant l’huile',
            intro=['Qu’ils soient distributeurs Eqology, Zinzino ou marques indépendantes (NORSAN), les acteurs qui marchent ouvrent la conversation '
                   'par un test sanguin à faire chez soi : quelques gouttes de sang mesurent l’équilibre entre oméga-6 et oméga-3. '
                   'Le résultat est presque toujours mauvais, et c’est lui qui vend l’huile.',
                   'Chez Eqology, le test est souvent « offert » dans un abonnement de 6 mois, avec un second test à la fin pour montrer le progrès. '
                   'Ensuite vient l’offre « 3 for free » : le client qui fait commander trois proches reçoit ses produits gratuitement. '
                   'Une partie de ces clients devient partenaire à son tour.'],
            schema=X.flux([('Pub', 'ou message', 'note'), ('Test', 'oméga-6/3', 'ok'),
                           ('Résultat', 'souvent bas', 'mal'), ('Huile', '6 mois, 2 tests', 'ok'),
                           ('Partenaire', '3 for free', 'note')],
                          legende='Le parcours type, du premier contact au recrutement'),
            donc='le nouveau site d’Yves doit ouvrir sur le test. C’est le point d’entrée de toute la concurrence.',
        ),
        dict(
            court='Les familles',
            etiquette='Le paysage',
            titre='Trois familles d’acteurs, trois façons de vendre',
            points=[
                dict(titre='Les distributeurs Eqology vendent par la conversation',
                     texte='Ce sont surtout des praticiens (massage, esthétique, nutrition) ou des familles qui vendent leur mode de vie. '
                           'Ils renvoient la commande vers la boutique officielle d’Eqology avec leur identifiant de partenaire (EQ ID). '
                           'Très peu achètent de la publicité : on compte 12 publicités actives qui citent « eqology » dans le monde.',
                     exemple='Boost Your Health (Pays-Bas) : une famille qui vit « où elle veut », un rendez-vous Calendly gratuit de 15 minutes, et « JOIN THE TEAM » dans la bio.'),
                dict(titre='Les distributeurs Zinzino font la même chose, avec plus de sites en français',
                     texte='Zinzino est le concurrent direct d’Eqology : même modèle de vente en réseau, même test sanguin. '
                           'Ses distributeurs français ont déjà des mini-sites et 9 publicités actives en France.',
                     exemple='L’Équilibre, d’Astrid et Bertrand (equilibre-sante.vercel.app) : « La plupart des compléments commencent par une promesse. Zinzino commence par un test. »'),
                dict(titre='Les marques achètent du volume avec une offre d’appel',
                     texte='Norway Omega, IM8, NORSAN ou Frøya vendent sur leur propre boutique. Elles diffusent des dizaines de publicités en même temps '
                           'et attirent le premier achat avec une remise ou un cadeau.',
                     exemple='Norway Omega : « 20 € offerts sur votre première commande avec le code OCEANDEEP ».'),
            ],
            donc='Yves est un distributeur : il ne peut pas jouer les remises comme une marque. En revanche, il peut faire de la publicité, ce que presque aucun distributeur ne fait.',
        ),
        dict(
            court='Les distributeurs',
            etiquette='Distributeur par distributeur',
            titre='Les meilleurs distributeurs ont chacun un levier, aucun n’a tout',
            points=[
                dict(titre='omega3-test.net (Allemagne, site en 5 langues dont le français)',
                     texte='Le modèle le plus abouti. Le site informe avant de vendre : outils gratuits (bilan oméga-3, calculateurs), comparatifs Eqology contre NORSAN, Zinzino ou Nutri&amp;Co, '
                           'et uniquement les allégations santé autorisées par l’EFSA. Le bouton « Commander le test » mène à Eqology, avec un rendez-vous gratuit de 15 minutes à côté.',
                     exemple='Il affiche « Financement transparent : partenaire Eqology ». La confiance passe par l’honnêteté sur le modèle.'),
                dict(titre='Pure Arctic Omega 3 (purearcticomega3.com)',
                     texte='Le seul vrai tunnel de recrutement trouvé. Une page explique pourquoi Eqology, les 4 étapes pour démarrer, le kit de démarrage et la formation. '
                           'Un formulaire déclenche une série d’e-mails, puis une invitation à une présentation de groupe en ligne.',
                     exemple='La page /join/ ne propose aucun produit : elle ne parle qu’à ceux qui cherchent une activité.'),
                dict(titre='Boost Your Health (Dennis &amp; Anne Sied, Pays-Bas)',
                     texte='Le recrutement par le mode de vie : travail à distance, école à la maison, sport, cuisine. Le site boostyourhealth.eu titre « Boost Your Health, Grow Wealth » '
                           'et tout mène à un appel découverte gratuit sur Calendly.',
                     exemple='Leurs stories à la une s’appellent Workouts, Work remote, Home schooling et Food. On achète leur vie avant leur huile.'),
                dict(titre='Gradina Health (Denislav, Bulgarie)',
                     texte='Le seul distributeur qui fait de la publicité en volume vers la France : une vingtaine de variantes testées en une semaine, '
                           '« Testez votre ratio oméga-3 » et « -25 % jusqu’au 10 mars ». Tout mène à sa page partenaire partner.eqology.com.',
                     exemple='Il se présente simplement : « Je m’entraîne régulièrement et je suis informaticien. » Un profil ordinaire rassure.'),
                dict(titre='Lang gesund (Allemagne)',
                     texte='Une publicité qui « recrute 3 participants pour un projet expérience oméga-3 » : 8 semaines d’huile offertes, un test au début et un à la fin, un suivi personnel. '
                           'La candidature se fait sur un formulaire Google.',
                     exemple='En réalité, c’est une prise de contacts. Les 3 places créent l’urgence, et chaque candidat devient un client ou un futur partenaire.'),
                dict(titre='gesundezelle (Allemagne)',
                     texte='Des coffrets de Noël à 109 € et 189 €, test sanguin inclus, sans abonnement. Pour commander, on écrit « SMALL » ou « LARGE » en commentaire, '
                           'puis la vente se fait en message privé.',
                     exemple='« Ce n’est pas une IA qui vous répond, c’est moi. » Le contact humain sert d’argument de vente.'),
                dict(titre='Robert Kontriner, Totaliz, Balz ImPuls : la page partenaire seule',
                     texte='Pas de site à eux, ou une simple page qui renvoie vers la page partenaire officielle d’Eqology. C’est gratuit et rapide à mettre en place, '
                           'mais toutes ces pages se ressemblent et ne gardent aucun contact.',
                     exemple='partner.eqology.com/omegarob : le nom du partenaire en haut, puis le site Eqology standard.'),
                dict(titre='Falko Krismayr et l’auteur du livre « Oméga-3, le verdict de la science »',
                     texte='Le recrutement par l’autorité. Falko se présente comme ancien coach olympique et mentor, et offre un cours gratuit. '
                           'Le livre, lui, sert à aborder des « confrères » sur LinkedIn sans parler de produit, puis glisse « une autre orientation professionnelle, un complément de revenu ».',
                     exemple='Attention : le livre promet « -45 % de mort subite » et « -49 % de démence ». Ces promesses sont interdites en publicité.'),
            ],
            donc='aucun distributeur ne réunit le contenu sérieux d’omega3-test.net, le tunnel de recrutement de Pure Arctic Omega 3 et la publicité de Gradina. C’est la place à prendre.',
        ),
        dict(
            court='Les marques',
            etiquette='Le modèle e-commerce',
            titre='Les marques gagnent sur la pureté, la preuve et l’offre de bienvenue',
            points=[
                dict(titre='Norway Omega (norwayomega.com)',
                     texte='Des publicités sur la pureté : distillation moléculaire, triglycérides naturels, indices d’oxydation. Une boutique multipays et une page « Ambassadors ».',
                     exemple='Story sponsorisée : un flacon dans la glace, « From 62° North », bouton « Start shopping today » et code OCEANDEEP.'),
                dict(titre='IM8 Health (im8health.com)',
                     texte='La preuve par les experts : la marque se présente comme « cofondée par David Beckham avec des experts de la Mayo Clinic et de la NASA ». '
                           'Ses publicités passent par des médias (Sports Illustrated, The Dodo) et chacune mène à une page dédiée à un médecin.',
                     exemple='La pub vue par Yves mène à im8health.com/pages/drjames : une landing par expert.'),
                dict(titre='NORSAN (norsan.fr)',
                     texte='Le vrai concurrent e-commerce en France : « Votre spécialiste en oméga-3 de Norvège ». Test d’index oméga-3 vendu en ligne, '
                           'livraison offerte dès 49 €, -10 % à l’inscription, et un espace pour les professionnels de santé.',
                     exemple='Leur menu « Apprendre » (bienfaits, index oméga-3, webinaires) fait le travail de conviction avant la boutique.'),
                dict(titre='Frøya Organics (froyaorganics.com)',
                     texte='La machine publicitaire : plus de 80 publicités actives, dont beaucoup sont publiées par de fausses pages éditoriales (« Anne’s Skincare Blog », « Nordic Wellness Secrets ») '
                           'ou par des créatrices en partenariat. Promesse de -50 % et garantie de 60 jours.',
                     exemple='Un format à connaître sans le copier : les pages « blog » déguisées posent un vrai risque de confiance.'),
            ],
            donc='des marques, on garde la preuve de pureté, la page par expert et l’idée d’une offre de bienvenue. On laisse de côté les remises et les faux blogs.',
        ),
        dict(
            court='Le bout du tunnel',
            etiquette='Après le clic',
            titre='Au bout de la publicité, cinq destinations possibles',
            intro=['C’est la question d’Yves : « qu’est-ce qu’il y a au bout ? ». Voici ce que nous avons trouvé, de la plus simple à la plus travaillée.'],
            comparatif=dict(
                colonnes=['Qui le fait', 'Ce que ça donne'],
                lignes=[
                    ('Page partenaire Eqology (achat direct)', 'Gradina, Kontriner, Balz ImPuls', ('Simple, mais aucun contact gardé', 'mal')),
                    ('Message privé ou WhatsApp', 'gesundezelle, Pure Omega3, Zinzino FR', ('Bon taux de vente, impossible à grande échelle', '')),
                    ('Formulaire de candidature', 'Lang gesund, Pure Arctic Omega 3', ('Garde le contact, crée l’urgence', 'ok')),
                    ('Rendez-vous gratuit (Calendly)', 'Boost Your Health, omega3-test.net', ('Convertit bien, demande du temps', 'ok')),
                    ('Mini-site test d’abord, puis boutique', 'L’Équilibre, omega3-test.net, NORSAN', ('Informe, rassure et vend, le plus complet', 'ok')),
                ]),
            donc='le meilleur bout de tunnel combine un mini-site qui commence par le test, un formulaire pour garder le contact et un rendez-vous pour ceux qui hésitent.',
        ),
        dict(
            court='La France',
            etiquette='L’opportunité',
            titre='En France, aucun distributeur Eqology n’occupe le terrain',
            deux=[
                dict(titre='Ce qui existe', ton='mal',
                     texte='Aucun site de distributeur Eqology en France : sur Google France, le seul qui sort est l’ancien site d’Yves. '
                           'Sur Meta, les 80 publicités Eqology diffusées en France viennent du siège (en anglais) et d’un distributeur bulgare. '
                           'Zinzino n’a que 9 publicités actives.'),
                dict(titre='Ce que ça permet', ton='ok',
                     texte='Yves peut devenir la référence Eqology en français, en ligne comme en publicité. '
                           'Sa concurrence publicitaire réelle se limite aux marques e-commerce (NORSAN, Nutri&amp;Co, Novoma), qui se battent sur la pureté et le prix.'),
            ],
            donc='le moment est bon : le premier distributeur qui investit sérieusement le français prend une place que personne ne lui dispute.',
        ),
        dict(
            court='Le modèle à suivre',
            etiquette='Recommandation',
            titre='Pour Yves, un site qui commence par le test, avec deux portes',
            intro=['Trois modèles sont possibles. Nous recommandons le premier.'],
            options=[
                dict(nom='A · Site « test d’abord » avec deux portes', reco=True,
                     resume='Un mini-site éditorial en français, sur le modèle d’omega3-test.net et de L’Équilibre, avec deux parcours : « Je veux le produit » et « Je veux l’activité ».',
                     comment=['La page d’accueil présente le test oméga-6/3 et un petit quiz.',
                              'La porte « produit » mène au test puis à la commande sur la boutique Eqology, avec l’EQ ID d’Yves.',
                              'La porte « activité » mène à une page de recrutement, un formulaire, puis un rendez-vous ou une présentation en ligne.',
                              'Des publicités Meta séparées alimentent chaque porte.'],
                     change='Yves garde tous les contacts (clients et candidats), et la publicité mesure ce qui marche porte par porte.',
                     avantages=[('Seul sur le terrain', 'aucun distributeur Eqology ne fait ça en français'),
                                ('Garde les contacts', 'chaque visiteur intéressé laisse ses coordonnées'),
                                ('Conforme', 'contenu limité aux allégations autorisées, comme omega3-test.net')],
                     inconvenients=[('Plus de travail au départ', 'contenus, quiz et deux tunnels à construire'),
                                    ('Le panier reste chez Eqology', 'sauf si le contrat d’Yves autorise une boutique à lui')],
                     quand='Si Yves veut à la fois vendre et recruter avec la publicité Meta, ce qui est son objectif.'),
                dict(nom='B · Boutique en ligne façon marque', verdict='deconseille',
                     resume='Une vraie boutique avec panier, remise de bienvenue et publicités en volume, comme Norway Omega ou NORSAN.',
                     comment=['Yves achète les produits et les revend sur sa boutique.',
                              'Une remise de bienvenue attire le premier achat.'],
                     change='Yves deviendrait commerçant, avec du stock et un service client.',
                     avantages=[('Parcours d’achat court', 'le client paie sans quitter le site')],
                     inconvenients=[('Probablement contraire au contrat', 'Eqology encadre les prix et la revente, à vérifier'),
                                    ('Pas de remise possible', 'l’offre d’appel des marques ne se copie pas'),
                                    ('Rien pour le recrutement', 'une boutique ne recrute pas de partenaires')],
                     quand='Seulement si Eqology l’autorise par écrit, comme pour les quelques praticiens belges, néerlandais et polonais qui ont leur propre panier.'),
                dict(nom='C · Page partenaire Eqology seule', verdict='possible',
                     resume='On fait pointer les publicités directement vers la page partenaire officielle, comme Gradina ou Kontriner.',
                     comment=['La publicité mène à partner.eqology.com au nom d’Yves.',
                              'La vente se fait sur le site Eqology standard.'],
                     change='Rien à construire, mais aucun contact gardé et aucune différence avec les autres partenaires.',
                     avantages=[('Immédiat et gratuit', 'la page existe déjà')],
                     inconvenients=[('Aucune donnée', 'on ne sait pas qui a cliqué sans acheter'),
                                    ('Aucun recrutement', 'rien ne parle de l’activité'),
                                    ('Aucune différence', 'toutes ces pages se ressemblent')],
                     quand='Pour tester un premier budget publicitaire pendant que le site A se construit.'),
            ],
            donc='on construit A, et on peut lancer C dès maintenant pour tester les premières publicités.',
        ),
    ],
    glossaire=[
        ('Bibliothèque publicitaire Meta', 'Le registre public de toutes les publicités Facebook et Instagram. On y voit qui diffuse quoi, depuis quand, et où mène chaque publicité.'),
        ('EQ ID', 'L’identifiant de partenaire Eqology. Placé dans un lien, il attribue la vente au partenaire.'),
        ('Page partenaire', 'La copie du site Eqology au nom d’un partenaire (partner.eqology.com/nom).'),
        ('Tunnel', 'Le parcours d’un visiteur, de la publicité jusqu’à l’achat ou l’inscription.'),
        ('Allégation santé', 'Une phrase sur l’effet d’un produit. Seules celles autorisées par l’EFSA (l’autorité européenne) sont permises, par exemple « le DHA contribue au fonctionnement normal du cerveau ».'),
        ('Landing', 'Une page faite pour une seule publicité ou une seule offre.'),
    ],
    decision='On part sur l’option A, un site « test d’abord » avec deux portes, en lançant l’option C en attendant : oui ou non ? '
             'Avant de commencer, il faut savoir si le contrat d’Yves l’autorise à avoir sa propre boutique.',
    pied='Sources : captures WhatsApp d’Yves (08 au 15/11/2026), Bibliothèque publicitaire Meta et sites consultés le 16/11/2026. Détail dans veille/yves-2026-11/.',
)

with open(os.path.join(ICI, 'strategie-concurrents.html'), 'w') as f:
    f.write(X.page(cfg))
print('ok')
