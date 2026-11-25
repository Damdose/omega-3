# -*- coding: utf-8 -*-
"""Plan Meta du lancement de l'acquisition d'Yves (26/11/2026), format EXPLICATION.  python3 -I mission/plan_meta.py"""
import os, sys
ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser('~/Documents/crm-heyfuture/docs/chantier-skills/formats'))
import explication as X

SITE = 'https://eqology-omega3.vercel.app/'
UTM = 'utm_source=meta&amp;utm_medium=paid'


def lien(chemin, campagne):
    return f'<code>{SITE}{chemin}{"&amp;" if "?" in chemin else "?"}{UTM}&amp;utm_campaign={campagne}&amp;utm_content={{{{ad.name}}}}</code>'


def src(texte, url):
    return f'<a href="{url}">{texte}</a>'


cfg = dict(
    onglet='Plan Meta · Yves',
    oeil='Yves Coignard · acquisition Meta · lancement le jeudi 26 novembre 2026',
    titre='Trois campagnes vers une seule page, et un contact compté à chaque formulaire',
    chapo='Le plan de lancement des publicités Instagram et Facebook pour recruter des partenaires Eqology : '
          'quelles campagnes, vers quelles adresses, ce qu’on mesure, à qui on parle, quelles stories, quel budget, '
          'et ce qui doit être prêt avant d’appuyer sur « publier » demain.',
    logo=os.path.join(ICI, '..', 'assets', 'images', 'eqology-eq.png'),
    polices=dict(titre='Space Grotesk', texte='DM Sans',
                 lien='https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,600;9..40,700&family=Space+Grotesk:wght@500;600;700&display=swap'),
    couleurs=dict(rouge='#335075', vert='#3d8691', jaune='#A88C5C'),
    variables={'fond': '#FAFAF8', 'trait': '#ECEAE4', 'vert-pale': '#EEF8F9'},
    parties=[
        # 1
        dict(
            titre='Les pubs servent à remplir l’agenda d’Yves, pas la boutique',
            court='Objectif',
            intro=['On recrute des partenaires. D’abord les praticiens de santé (naturopathes, micronutritionnistes, diététiciens, kinés, ostéos), '
                   'qui ont déjà une clientèle, puis les particuliers de 35 à 70 ans qui cherchent un complément de revenu. '
                   'Aucune publicité n’envoie vers la boutique : elle reste la vitrine pour ceux qui viennent par le profil Instagram.',
                   'Yves ne fait qu’une chose : rappeler les contacts. Tout le reste (pubs, page, e-mails, mesure) tourne sans lui.'],
            schema=X.flux([('Story', 'Instagram', 'neutre'), ('Page', 'partenaire', 'fort'),
                           ('Formulaire', 'merci = Lead', 'fort'), ('Appel d’Yves', 'sous 48 h', 'ok'), ('Visio', 'puis le kit', 'ok')],
                          legende='Le parcours d’un futur partenaire'),
            donc='on juge les pubs au coût par contact rappelé, pas au nombre de clics.',
        ),
        # 2
        dict(
            titre='Chaque campagne arrive sur la même page, avec son propre titre',
            court='Campagnes',
            intro=['La page partenaire change son titre selon le paramètre <code>cible</code> : le visiteur retrouve la promesse de la pub qu’il vient de voir. '
                   'Toutes les adresses portent les mêmes UTM : la source de chaque contact s’affiche dans l’e-mail reçu par Yves.'],
            points=[
                dict(titre='A · Praticiens de santé', texte=lien('partenaire.html?cible=pro', 'recrut-praticiens')
                     + '<br>Message : le test oméga-3 comme mesure objective à proposer à ses patients, sans rien vendre au cabinet. Le profil « praticien » est présélectionné dans le formulaire.'),
                dict(titre='B · Complément de revenu', texte=lien('partenaire.html', 'recrut-revenu')
                     + '<br>Message : recommander des oméga-3 de qualité, sans stock, à son rythme.'),
                dict(titre='C · Visio de présentation', texte=lien('partenaire.html?cible=visio', 'recrut-visio')
                     + '<br>Message : la date et l’heure de la prochaine visio. C’est le format des références siciliennes (31 pubs sur 7 mois). La date se règle dans <code>site-config.js</code>.'),
                dict(titre='D · Reciblage (à partir du 4 décembre)', texte=lien('partenaire.html', 'reciblage-partenaire')
                     + '<br>Pour les visiteurs de la page partenaire sans formulaire, les visiteurs de la boutique et les personnes qui ont interagi avec le compte Instagram.'),
            ],
            exemple='<code>utm_content={{ad.name}}</code> est un paramètre dynamique : Meta y écrit le nom de la publicité. '
                    'Nommez les pubs <code>angle-format</code>, par exemple <code>test-mesure-story</code> ou <code>sans-stock-story</code>, '
                    'et l’e-mail d’Yves dira quelle story a apporté le contact.',
            donc='quatre adresses seulement ; les variantes se font dans les pubs, jamais dans des pages en plus.',
        ),
        # 3
        dict(
            titre='On optimise sur le formulaire envoyé, compté sur la page merci',
            court='Mesure',
            intro=['Le pixel ne se charge qu’après l’accord aux cookies. Il compte quatre événements, tous déjà prévus dans le site.'],
            comparatif=dict(colonnes=['Où', 'À quoi il sert'], lignes=[
                ('Lead', 'merci.html, après le formulaire', ('Objectif des campagnes', 'ok')),
                ('PageView', 'toutes les pages', 'Audiences de reciblage'),
                ('ViewContent', 'les fiches produit', 'Audience « intéressés par les produits »'),
                ('ClicCommander', 'les boutons « Commander chez Eqology »', 'Audience boutique, événement personnalisé'),
            ]),
            points=[
                dict(titre='Objectif de campagne : Prospects, conversion « Lead » sur le site',
                     texte='Pas d’objectif « trafic » : Meta enverrait des cliqueurs, pas des gens qui remplissent un formulaire.'),
                dict(titre='Phase d’apprentissage : environ 50 contacts par ensemble de pubs et par semaine',
                     texte='Avec 30 € par jour, on n’y arrivera pas tout de suite : Meta affichera « apprentissage limité ». C’est normal au début. '
                           'Pour aider, on garde peu d’ensembles de pubs et on ne modifie rien pendant les 3 premiers jours.'),
                dict(titre='Plus tard : l’API Conversions côté serveur',
                     texte='<code>/api/lead</code> enverra aussi le Lead à Meta depuis le serveur, avec un identifiant commun pour ne pas le compter deux fois. '
                           'C’est utile parce qu’une partie des visiteurs refuse les cookies.'),
            ],
            donc='le chiffre à suivre chaque matin : coût par Lead, campagne par campagne.',
        ),
        # 4
        dict(
            titre='Un ciblage large et honnête, parce que Meta peut classer ces pubs en « emploi »',
            court='Audiences',
            intro=['Meta oblige à déclarer une « catégorie spéciale » pour les offres d’emploi, de logement et de crédit quand on cible les États-Unis, le Canada ou '
                   '« certaines parties de l’Europe » (' + src('Meta, normes publicitaires', 'https://transparency.meta.com/policies/ad-standards/') + ', '
                   + src('API Marketing, catégorie spéciale', 'https://developers.facebook.com/docs/marketing-api/audiences/special-ad-category') + '). '
                   'Les guides décrivent cette catégorie comme visant les emplois, stages et certifications (' + src('Jon Loomer', 'https://www.jonloomer.com/special-ad-categories-meta-ads/') + ') ; '
                   'une opportunité de partenaire indépendant n’y figure pas noir sur blanc. Je n’ai pas trouvé de règle propre à la France.',
                   'Décision prudente : on lance sans catégorie spéciale, avec un texte qui n’est jamais une offre d’emploi (ni « on recrute », ni « poste », ni « salaire »), '
                   'et un ciblage qui fonctionne encore si Meta impose la catégorie (âge large, pas d’exclusion par âge ou par sexe, rayon d’au moins 25 km).'],
            comparatif=dict(colonnes=['Ciblage de départ', 'Exclusions'], lignes=[
                ('A · Praticiens', 'France, 25-65 ans. Intérêts à tester : naturopathie, micronutrition, diététique, ostéopathie, kinésithérapie, médecines douces.', 'Contacts déjà inscrits (merci.html, 180 jours)'),
                ('B · Revenu', 'France, 35-65 ans et plus. Audience Advantage+, avec en suggestion : entrepreneuriat, travail à domicile, bien-être, compléments alimentaires.', 'Contacts déjà inscrits'),
                ('C · Visio', 'Même base que B. Plus tard, une audience similaire aux inscrits.', 'Contacts déjà inscrits'),
                ('D · Reciblage', 'Visiteurs de partenaire.html (30 jours), visiteurs de la boutique (ViewContent, ClicCommander), interactions Instagram (30 jours).', 'Contacts déjà inscrits'),
            ]),
            points=[
                dict(titre='Les intérêts « santé » ont fondu depuis 2022',
                     texte='Meta a retiré des milliers d’options jugées sensibles, dont des sujets de santé (' + src('Search Engine Land', 'https://searchengineland.com/meta-will-remove-targeting-options-for-sensitive-topics-on-january-19-378095') + '), '
                           'et en a encore retiré en 2024 (' + src('MediaPost', 'https://www.mediapost.com/publications/article/392609/') + '). '
                           'Il faut vérifier dans le gestionnaire que « naturopathie » existe encore. Sinon, c’est la création qui cible : une story qui parle aux praticiens trouve les praticiens.'),
                dict(titre='Ce que Meta interdit pour le marketing de réseau',
                     texte='Pas de promesse d’enrichissement rapide, pas de « sans effort », pas d’offre de revenu vague sans décrire l’activité ; '
                           'les modèles « argent rapide pour peu d’investissement », dont le marketing de réseau, sont visés (' + src('Meta, résultats irréalistes', 'https://transparency.meta.com/policies/ad-standards/deceptive-content/unrealistic-outcomes') + '). '
                           'Donc dans les pubs : aucun montant, aucun « devenez libre financièrement », toujours « distributeur indépendant Eqology » et une description concrète de l’activité.'),
            ],
            donc_ton='mal', donc_mot='Attention',
            donc='si une pub est refusée pour « emploi », on la republie dans la catégorie spéciale plutôt que de contester : le ciblage large est fait pour.',
        ),
        # 5
        dict(
            titre='Une story par jour, quatre angles par campagne, rien d’inventé',
            court='Créations',
            intro=['Format 9:16, 5 à 15 secondes, texte lisible sans le son, sous-titres si on filme. Visuels tirés du kit : flacons et test Eqology, fjord, pêche, huile versée. '
                   'Mention « distributeur indépendant Eqology » dans le texte de la pub. Pas de faux témoignage, pas de chiffre de revenu, pas de FENA, pas d’IFOS, pas de note Trustpilot.'],
            points=[
                dict(titre='A · Praticiens de santé', texte=
                     '1. « Vos patients vous demandent quels oméga-3 prendre ? Donnez-leur une mesure, pas un avis. » (visuel : le test)<br>'
                     '2. « Un repère avant, un repère après : le test oméga-3 se fait à la maison. »<br>'
                     '3. « Recommander sans vendre au cabinet : vos patients commandent seuls chez Eqology. »<br>'
                     '4. « Une huile tracée jusqu’au bateau, pêche certifiée MSC : un produit que vous pouvez expliquer. »'),
                dict(titre='B · Complément de revenu', texte=
                     '1. « Un complément de revenu sans stock, à votre rythme. »<br>'
                     '2. « Vous parlez déjà santé autour de vous ? Ça peut devenir une activité. »<br>'
                     '3. « Pas de stock, pas de local, pas d’horaires : Eqology livre, vous recommandez. »<br>'
                     '4. Yves face caméra, « Ce que je fais, concrètement » (dès que la vidéo existe, avec son accord).'),
                dict(titre='C · Visio de présentation', texte=
                     '1. « [Jour] [date] à 20 h : 45 minutes en visio pour comprendre le partenariat Eqology. »<br>'
                     '2. « Gratuit, sans engagement : posez vos questions en direct. »<br>'
                     '3. « Stock, temps, démarrage : on répond à tout pendant la visio. »<br>'
                     '4. Compte à rebours « Plus que 2 jours » la veille et l’avant-veille.'),
                dict(titre='D · Reciblage', texte=
                     '1. « D’où vient vraiment l’argent ? » (la réponse de la FAQ)<br>'
                     '2. « Vous parlez aux gens, Eqology fait le reste. »<br>'
                     '3. Pour les visiteurs de la boutique : « Vous aimez ces produits ? Recommandez-les. »'),
            ],
            exemple='La photo de la praticienne utilisée sur le site est une illustration générée : on peut s’en servir comme décor, '
                    'jamais avec un prénom ou une phrase qui laisserait croire à une vraie partenaire.',
            donc='l’agent Ads tourne sur ces angles ; on garde ceux qui font des Lead et on remplace les autres chaque semaine.',
        ),
        # 6
        dict(
            titre='30 € par jour pour commencer, une règle de décision à J+3 et à J+7',
            court='Budget',
            intro=['Le budget publicitaire est payé directement à Meta par la carte d’Yves, à part de la prestation. Le travail de Heyfuture, c’est le développement de l’agent Ads : '
                   'campagnes, audiences, créations et règles de décision qu’il applique.',
                   'Le lancement tombe pendant le Black Friday (27 au 30 novembre) : les enchères sont plus chères cette semaine-là. '
                   'On démarre donc prudemment et on juge sur le coût par contact de la semaine suivante.'],
            comparatif=dict(colonnes=['Du 26/11 au 3/12', 'À partir du 4/12'], lignes=[
                ('A · Praticiens', '10 € par jour', 'Selon J+7'),
                ('B · Revenu', '8 € par jour', 'Selon J+7'),
                ('C · Visio', '12 € par jour', 'Selon J+7'),
                ('D · Reciblage', '0 € (audience trop petite)', '5 € par jour, pris sur la moins bonne'),
                ('Total', '30 € par jour', '30 € par jour'),
            ]),
            points=[
                dict(titre='J+3 (dimanche 29/11) : on coupe les pubs, pas les campagnes',
                     texte='Une pub qui a dépensé deux fois le coût par contact visé sans aucun Lead s’arrête. Repère de départ : 15 € par contact, à corriger avec les vrais chiffres.'),
                dict(titre='J+7 (jeudi 3/12) : on déplace le budget',
                     texte='On compare le coût par contact et le taux de contacts joints par Yves. Une campagne à moins de 50 % de joints perd du budget, même si ses contacts sont bon marché.'),
            ],
            donc='aucun changement de budget avant J+3, aucun déplacement entre campagnes avant J+7.',
        ),
        # 7
        dict(
            titre='Après le formulaire, Yves rappelle et la visio fait le reste',
            court='Après le contact',
            schema=X.etapes_num([('Formulaire', 'page merci'), ('E-mail', 'à Yves'), ('Rappel', 'sous 48 h'),
                                 ('Visio', 'avec le parrain'), ('Kit', 'démarrage')], resultat='Un nouveau partenaire'),
            points=[
                dict(titre='Déjà en place', texte='<code>/api/lead</code> enregistre le contact et envoie un e-mail détaillé (profil, métier, créneau, pub d’origine). '
                                                  'À vérifier avant le lancement : la variable <code>LEAD_EMAIL_TO</code> doit contenir l’adresse d’Yves et celle de Damien.'),
                dict(titre='À brancher', texte='Les relances e-mail automatiques : J0 (confirmation), J2 (qui est Eqology), J5 (la date de la visio), et la veille de la visio. '
                                               'L’alerte SMS ou WhatsApp pour Yves, s’il la préfère à l’e-mail.'),
            ],
        ),
        # 8
        dict(
            titre='Neuf choses à cocher avant de publier, dont trois bloquantes',
            court='Avant demain',
            comparatif=dict(colonnes=['Qui', 'Bloquant ?'], lignes=[
                ('Accès Meta Business d’Yves partagé à damien.growth@gmail.com, carte sur le compte pub', 'Yves', ('Oui', 'mal')),
                ('Mise en ligne du site V2', 'Damien (feu vert)', ('Oui', 'mal')),
                ('Identifiant du pixel dans site-config.js, puis test du Lead', 'Heyfuture', ('Oui', 'mal')),
                ('Envoi d’un formulaire de test en production, e-mail reçu par Yves et Damien', 'Heyfuture', 'Le jour même'),
                ('Bandeau cookies : le pixel ne part qu’après « Accepter »', 'Heyfuture', 'Le jour même'),
                ('Vérification du domaine dans Meta (eqology-omega3.vercel.app)', 'Heyfuture', 'Sous 7 jours'),
                ('Lien partenaire Eqology d’Yves dans site-config.js', 'Yves', 'Pour la boutique'),
                ('Date et heure de la prochaine visio, avec le parrain', 'Yves', 'Pour la campagne C'),
                ('Photo et vidéo d’Yves', 'Yves', 'Facultatif au début'),
            ]),
            donc_ton='mal', donc_mot='Attention',
            donc='sans l’accès Meta Business d’Yves, rien ne part demain. Sans date de visio, on lance A et B seulement et C attend.',
        ),
        # 9
        dict(
            titre='Deux semaines pour savoir quelle campagne remplit l’agenda',
            court='Calendrier',
            schema=X.frise([('26/11', 'Lancement\nA, B, C', 'fort'), ('29/11', 'J+3\non coupe', 'ok'), ('3/12', 'J+7\non déplace', 'ok'),
                            ('4/12', 'Reciblage', 'ok'), ('9/12', 'Point\n2 semaines', 'fort')], aria='Calendrier du 26 novembre au 9 décembre'),
            comparatif=dict(colonnes=['Ce qui se passe'], lignes=[
                ('Jeu. 26/11', 'Mise en ligne au feu vert, test du formulaire, campagnes A, B (et C si la date de visio est fixée) publiées le soir'),
                ('Ven. 27/11', 'Contrôle de la diffusion et des refus éventuels. Black Friday : on ne touche à rien'),
                ('Sam. 28 et dim. 29/11', 'Une story organique par jour sur le compte. J+3 dimanche : on coupe les pubs sans Lead'),
                ('Lun. 30/11', 'Premier point avec Yves : contacts reçus, joints, rappels faits'),
                ('Mar. 1er/12', 'Nouvelles créations pour remplacer celles coupées'),
                ('Mer. 2/12', 'Relances e-mail J0, J2, J5 branchées'),
                ('Jeu. 3/12', 'J+7 : coût par contact et taux de joints, budget déplacé'),
                ('Ven. 4/12', 'Campagne D (reciblage) lancée'),
                ('Du 5 au 8/12', 'Une story par jour ; relance de la visio la veille et le jour même'),
                ('Mer. 9/12', 'Point à deux semaines : budget sur la meilleure campagne, bilan envoyé à Yves'),
                ('Jeu. 10/12', 'Nouvelle série de créations pour la deuxième quinzaine'),
            ]),
        ),
    ],
    decision='On lance demain soir A et B seulement (praticiens et revenu), et C dès qu’Yves donne la date de la visio : oui ou non ?',
    pied='Sources consultées le 25/11/2026 : normes publicitaires de Meta (résultats irréalistes, catégories spéciales), documentation de l’API Marketing, Jon Loomer, Search Engine Land, MediaPost.',
)

sortie = os.path.join(ICI, 'plan-meta.html')
open(sortie, 'w').write(X.document(cfg))
print(sortie)
