# -*- coding: utf-8 -*-
"""Les références d'Yves décortiquées : recruter des business partners et vendre en ligne. Format EXPLICATION.
Usage : python3 strategie.py"""
import os, sys
sys.path.insert(0, os.path.expanduser('~/Documents/crm-heyfuture/docs/chantier-skills/formats'))
import explication as X

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))

cfg = dict(
    onglet='Concurrents oméga-3',
    oeil='Les références envoyées par Yves · 16 novembre 2026',
    titre='Comment ses références recrutent des business partners et vendent en ligne',
    chapo=('Yves nous a envoyé neuf références sur WhatsApp. Nous avons ouvert chacune : site, Instagram, publications, liens en bio, '
           'pages partenaires et boutiques. Voici, référence par référence, comment elles trouvent des business partners et comment elles vendent, '
           'puis ce qu’on reprend pour son nouveau site.'),
    logo=os.path.join(RACINE, 'assets/images/eqology-logo.png'),
    polices=dict(titre='Space Grotesk', texte='DM Sans',
                 lien='https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700&family=Space+Grotesk:wght@500;600;700&display=swap'),
    couleurs=dict(rouge='#B4483A', vert='#3D8691', jaune='#9A7A45'),
    variables={'marque': '#335075'},
    parties=[
        dict(
            court='Le principe',
            etiquette='Comprendre',
            titre='Un distributeur Eqology gagne sur deux tableaux : ses ventes et son équipe',
            intro=['Eqology le dit sur sa page « Devenir Business Partner » : on peut se contenter de vendre à son réseau, '
                   'mais « les avantages financiers sont encore plus importants » quand on monte une équipe de partenaires qui vendent à leur tour.',
                   'Côté vente, le distributeur n’a ni stock ni panier. Chaque lien vers la boutique Eqology porte son code de partenaire, '
                   'et toute commande passée par ce lien lui revient. Côté recrutement, le nouveau partenaire achète un Business Kit, '
                   'suit la formation d’Eqology et rejoint l’équipe de celui qui l’a fait entrer.'],
            schema=X.flux([('Site d’Yves', 'vitrine', 'note'), ('Lien codé', 'son code', 'ok'),
                           ('Eqology', 'panier, envoi', 'neutre'), ('Commission', 'pour Yves', 'ok'),
                           ('Équipe', 'ses recrues', 'note')],
                          legende='Le site vend avec des liens codés et recrute pour l’équipe'),
            donc='le site d’Yves a deux missions : faire acheter via ses liens codés et faire entrer des business partners dans son équipe. Toutes ses références jouent sur l’une ou l’autre.',
        ),
        dict(
            court='Les vrais chiffres',
            etiquette='Vérification',
            titre='Leurs audiences Instagram sont petites : le chiffre vient de l’équipe, pas des abonnés',
            intro=['Yves dit que ses références « font plein de chiffres grâce à Instagram ». Nous avons relevé leurs comptes le 16/11/2026. '
                   'Leur chiffre d’affaires n’est pas public, donc on ne peut pas le vérifier. En revanche, leurs audiences, elles, se mesurent.'],
            comparatif=dict(
                colonnes=['Abonnés', 'J’aime par publication', 'Ce qui recrute vraiment'],
                lignes=[
                    ('Falko Krismayr', '5 123', '—', ('Les rencontres en face à face (il le dit dans la presse)', '')),
                    ('eqologybusiness (officiel)', '3 573', '—', ('Kick Off, Convention : les événements Eqology', '')),
                    ('Boost Your Health', '1 876', '14 à 79 (une vidéo de leur chat : 21 000)', ('Le site, l’appel de 15 min, les pros recrutés', 'ok')),
                    ('Robert Kontriner', '657', '2 à 36', ('Rien de visible en ligne', 'mal')),
                    ('Eqology Sicilia', '51', '—', ('Les soirées en présentiel', '')),
                    ('eqologywithaga', '4', '0 publication', ('Rien pour l’instant', 'mal')),
                ]),
            points=[
                dict(titre='Comment on fait du chiffre avec 1 800 abonnés', ton='ok',
                     texte='En vente en réseau, le volume se fait dans l’équipe. Boost Your Health ne vend pas seulement à ses abonnés : '
                           'ils recrutent des professionnels qui ont déjà leur clientèle (coach, thérapeute, salle de sport). Chacun revend à ses propres clients, '
                           'puis recrute à son tour. Instagram sert de vitrine et de preuve de vie. Le recrutement se fait en message privé, en rendez-vous et en soirée.',
                     exemple='La thérapeute de Poepgoed.nl raconte qu’elle a d’abord proposé Eqology à ses clients, puis l’a ouvert à ses propres thérapeutes. Une recrue amène toute une équipe.'),
            ],
            donc='Yves a raison sur le principe, mais pas sur le mécanisme. Ces partenaires ne gagnent pas grâce à leur audience Instagram : ils gagnent en recrutant des gens qui ont déjà des clients. C’est ce profil que le site et les pubs doivent aller chercher.',
        ),
        dict(
            court='Recruter',
            etiquette='Objectif 1 · Trouver des business partners',
            titre='Pour recruter, chaque référence a sa méthode, et aucune n’utilise la publicité',
            points=[
                dict(titre='Boost Your Health (Dennis & Anne Sied, Pays-Bas) : la référence la plus complète', ton='ok',
                     texte='Leur site boostyourhealth.eu demande dès l’accueil « Où veux-tu commencer ? » avec deux portes : « Améliorer ma santé » et « Entreprendre dans la santé ». '
                           'Tout mène à un appel découverte gratuit de 15 minutes sur Calendly. Ils recrutent surtout des professionnels qui intègrent Eqology à leur activité : '
                           'une coach en nutrition, une thérapeute de l’eczéma, une spécialiste des intestins, une salle de sport. '
                           'Leurs témoignages racontent tous la même chose : « J’ai d’abord proposé les produits à mes clients, puis j’ai monté une équipe. » '
                           'Sur Instagram, ils montrent leur vie (sport, école à la maison, voyages, leur chat) et glissent une publication épinglée : '
                           '« Et si une seule décision te donnait plus de liberté que tu ne l’imaginais ? »',
                     exemple='Leur vidéo d’accueil s’intitule « Eqology First Look ». Leur page « Test don’t guess » explique le test avant/après 120 jours, puis renvoie vers le rendez-vous.'),
                dict(titre='Eqology Business Partner Sicilia : des soirées de recrutement en présentiel',
                     texte='Leur compte Instagram est petit (51 abonnés) et sert à annoncer des soirées. Celle du 4 novembre à Catane, de 19 h à 21 h, '
                           'promettait « Transforme ta passion pour le bien-être en une nouvelle profession », avec des dirigeants d’Eqology et des « présidentes » du réseau au micro.',
                     exemple='Leur bio : « Le plus beau cadeau pour toi et ta famille, c’est ta santé. Des opportunités de business éthiques avec Eqology. »'),
                dict(titre='Falko Krismayr : le recrutement par l’autorité, entièrement hors ligne',
                     texte='Ancien coach olympique devenu « mentor business » (5 100 abonnés, compte certifié). Sa bio promet un cours gratuit. '
                           'L’article de presse en lien dans sa bio (The UBJ, 28/09/2026) explique que lui et Esther Wilhelm ont bâti leur organisation « uniquement hors ligne » : '
                           'Instagram sert leur image, les rencontres en face à face font le recrutement.',
                     exemple='Ses stories à la une : Expertise, Testimonials, Pro Sport, About Me. Il vend un parcours avant de vendre une opportunité.'),
                dict(titre='Le livre « Oméga-3, le verdict de la science » : l’approche des professionnels par LinkedIn',
                     texte='Un distributeur Eqology écrit à ses « chers confrères » et leur offre les pages de synthèse de son livre, vendu sur Amazon, qui « ne cite aucun produit ». '
                           'Une fois la confiance installée, un QR code propose « une autre orientation professionnelle, un complément de revenu ».',
                     exemple='Attention : le livre promet « -45 % de mort subite » et « -49 % de démence ». On garde l’approche, pas ces promesses, interdites en publicité.'),
                dict(titre='Robert Kontriner : la page partenaire et un Instagram personnel',
                     texte='Il n’a que la page partenaire fournie par Eqology et un compte Instagram de 657 abonnés, où ses publications font de 2 à 36 j’aime. '
                           'Sa publication épinglée répond à l’objection qu’on lui fait : « On croit que je fais ce nouveau projet seulement pour gagner de l’argent. »',
                     exemple='C’est le niveau zéro du recrutement en ligne : pas de site, pas de rendez-vous, pas de formulaire.'),
                dict(titre='eqologywithaga : un compte qui démarre',
                     texte='Quatre abonnés, aucune publication, une bio courte et un lien d’inscription client Eqology. On voit ici ce qu’Eqology fournit de base à un nouveau partenaire, et la limite de ce minimum.'),
                dict(titre='Le compte officiel eqologybusiness : le matériel prêt à partager',
                     texte='Eqology anime son propre compte « business » (Oslo, 3 573 abonnés) avec des stories Products, Kick Off, Opportunity et Convention, '
                           'et reposte les déballages de ses clientes. Les partenaires reprennent ce matériel pour recruter.'),
            ],
            donc='les recrutements qui marchent passent par une histoire de vie, un rendez-vous et des soirées ou des visios. Aucune référence d’Yves ne recrute avec la publicité Meta : c’est la place à prendre.',
        ),
        dict(
            court='Vendre en ligne',
            etiquette='Objectif 2 · L’e-commerce',
            titre='Un distributeur fait de l’e-commerce avec des liens codés vers la boutique Eqology',
            points=[
                dict(titre='Le Linktree de Boost Your Health est un catalogue complet', ton='ok',
                     texte='linktr.ee/boostyourhealth.eu liste 22 produits rangés par familles : oméga-3, packs avantage, vitamines et minéraux, beauté. '
                           'Chaque lien ouvre la fiche Eqology avec leur code partenaire dans l’adresse (eqology.com/nl/__s31ef49s__/produit). '
                           'Le client paie chez Eqology, la vente leur revient.',
                     exemple='« Omega 3 + vit K2/D3 + Multivitaminen » mène directement au pack Pure Nordic Health, avec leur code.'),
                dict(titre='La page partenaire de Robert Kontriner est une mini-boutique',
                     texte='partner.eqology.com/omegarob affiche son nom, ses produits conseillés, ses articles et ses vidéos. '
                           'Tous les liens vers le catalogue portent son identifiant (?sid=…) : le panier, le compte client et même la page « Devenir Business Partner ».'),
                dict(titre='Norway Omega : le modèle de la boutique de marque',
                     texte='Une boutique Shopify de 12 produits seulement, avec des formules à l’année (jusqu’à 1 755 €) et un « Team Pack » de 30 flacons pour les clubs sportifs. '
                           'Leurs ambassadeurs sont des sportifs de haut niveau (Tarjei Bø en biathlon, Barnabé Delarze en aviron). La publicité offre 20 € sur la première commande (code OCEANDEEP).'),
                dict(titre='IM8 : le modèle de la fiche produit pensée pour l’abonnement',
                     texte='La pub vue par Yves mène à une page « Dr James » qui renvoie vers la fiche produit, avec l’abonnement de 90 jours présélectionné. '
                           'Elle met en avant -30 %, un kit de bienvenue offert, la garantie « satisfait ou remboursé » de 90 jours, 22 104 avis, un essai clinique, '
                           'et un programme de masterclasses avec des experts réservé aux abonnés.',
                     exemple='Le prix est affiché « par jour » (3,03 € par portion) plutôt que par mois.'),
            ],
            donc='Yves peut avoir un vrai site e-commerce, avec catalogue, fiches produits, packs et abonnement mis en avant comme chez IM8, dont chaque bouton « Acheter » ouvre le panier Eqology avec son code. Paiement, livraison et service client restent chez Eqology.',
        ),
        dict(
            court='Ce qu’on reprend',
            etiquette='Recommandation',
            titre='Le nouveau site : la structure de Boost Your Health, les fiches d’IM8, le recrutement par rendez-vous',
            intro=['Pour chaque brique du site, voici la référence d’Yves dont elle s’inspire.'],
            comparatif=dict(
                colonnes=['On le prend chez', 'Sur le site d’Yves'],
                lignes=[
                    ('Deux portes dès l’accueil', 'Boost Your Health', ('« Je veux le produit » / « Je veux l’activité »', 'ok')),
                    ('Catalogue avec liens codés', 'Linktree Boost, page Kontriner', ('Toute la gamme, chaque bouton vers Eqology avec son code', 'ok')),
                    ('Fiches produits et abonnement', 'IM8', ('Prix par jour, garantie, avis, test avant/après', 'ok')),
                    ('Packs et formules à l’année', 'Norway Omega', ('Packs Eqology mis en avant, offre pour les clubs et cabinets', 'ok')),
                    ('Témoignages de professionnels', 'Boost Your Health', ('Praticiens et sportifs qui utilisent Eqology', 'ok')),
                    ('Recrutement', 'Boost, Sicilia, Falko', ('Formulaire, appel de 15 min, puis visio de groupe', 'ok')),
                    ('Porte d’entrée pour les pros de santé', 'Le livre (LinkedIn)', ('Un guide gratuit sourcé, sans promesse interdite', 'ok')),
                    ('Publicité Meta par porte', 'Aucune référence ne le fait', ('Une campagne « produit » et une campagne « activité »', 'ok')),
                ]),
            donc='on construit un seul site qui vend toute la gamme avec les liens codés d’Yves et qui recrute avec un rendez-vous. Chaque porte a sa propre campagne Meta.',
        ),
        dict(
            court='À vérifier',
            etiquette='Avant de commencer',
            titre='Deux points à vérifier avec Yves avant de construire',
            deux=[
                dict(titre='Son code partenaire', ton='ok',
                     texte='Il nous faut son identifiant Eqology (EQ ID ou lien de page partenaire) pour coder chaque bouton « Acheter », comme Boost Your Health le fait sur ses 22 produits.'),
                dict(titre='Les règles d’Eqology', ton='mal',
                     texte='Nous n’avons trouvé aucun règlement public d’Eqology sur les sites et la publicité de ses partenaires. '
                           'Yves doit vérifier son contrat : usage du nom Eqology, des photos produits, et pubs Meta qui citent la marque.'),
            ],
            donc='avec ces deux réponses, on peut lancer la maquette du site.',
        ),
    ],
    glossaire=[
        ('Business Partner', 'Un distributeur indépendant Eqology. Il touche une commission sur ses ventes et sur celles de l’équipe qu’il recrute.'),
        ('Business Kit', 'Le pack de démarrage qu’achète un nouveau partenaire : produits et outils de vente.'),
        ('Lien codé', 'Un lien vers la boutique Eqology qui contient l’identifiant du partenaire (?sid=… ou __code__ dans l’adresse). La commande lui est attribuée.'),
        ('Page partenaire', 'La copie du site Eqology au nom d’un partenaire (partner.eqology.com/nom), avec ses produits conseillés.'),
        ('Linktree', 'Une page de liens qu’on met en bio Instagram. Boost Your Health s’en sert comme catalogue.'),
        ('Calendly', 'Un outil de prise de rendez-vous en ligne.'),
    ],
    decision='On construit le nouveau site sur ce modèle (deux portes, catalogue avec liens codés, recrutement par rendez-vous et visio) : oui ou non ? '
             'Si oui, il nous faut le code partenaire d’Yves.',
    pied='Sources : captures WhatsApp d’Yves (08 au 15/11/2026), sites, Instagram et Linktree consultés le 16/11/2026. Détail dans veille/yves-2026-11/.',
)

with open(os.path.join(ICI, 'strategie-concurrents.html'), 'w') as f:
    f.write(X.page(cfg))
print('ok')
