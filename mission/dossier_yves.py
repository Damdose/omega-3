# -*- coding: utf-8 -*-
"""Dossier de stratégie pour Yves Coignard, au format des dossiers Heyfuture (moteur fabriquer.py des « Fondations »).
Damien, 16/11/2026 : « format horizontal, en mode comme un audit ».
Usage : python3 mission/dossier_yves.py  →  mission/dossier-yves.html"""
import os, sys, json
sys.path.insert(0, os.path.expanduser('~/Documents/audits-heyfuture/clients/heyfuture-strategie'))
import fabriquer as F

ICI = os.path.dirname(os.path.abspath(__file__))
F.TITRE = 'Recruter des partenaires Eqology'
F.DATE = 'Yves Coignard · 16 novembre 2026 · préparé par Heyfuture'

# ——— Bloc « captures » ajouté ici (le moteur partagé fabriquer.py n'est pas modifié)
import base64, io
from PIL import Image
VEILLE = os.path.join(os.path.dirname(ICI), 'veille', 'yves-2026-11')


def img_uri(chemin, largeur=900):
    im = Image.open(os.path.join(VEILLE, chemin)).convert('RGB')
    if im.width > largeur:
        im = im.resize((largeur, round(im.height * largeur / im.width)))
    buf = io.BytesIO(); im.save(buf, 'JPEG', quality=78)
    return 'data:image/jpeg;base64,' + base64.b64encode(buf.getvalue()).decode()


def b_captures(b, ctx):
    figs = ''
    for c in b.get('images', []):
        cls = 'cap cap--large' if c.get('large') else 'cap'
        figs += (f'<figure class="{cls}"><div class="cap__img"><img src="{img_uri(c["src"])}" alt="{F.e(c.get("titre"))}" loading="eager"></div>'
                 f'<figcaption><b>{F.e(c.get("titre"))}</b>{F.e(c.get("texte"))}'
                 + (f'<span class="cap__src">{F.e(c["source"])}</span>' if c.get('source') else '') + '</figcaption></figure>')
    return (f'<h2 class="bloc__titre">{F.e(b.get("titre"))}</h2>' * bool(b.get('titre'))
            + (f'<p class="cap__intro">{F.e(b["intro"])}</p>' if b.get('intro') else '')
            + f'<div class="caps caps--{b.get("colonnes", 3)}">{figs}</div>')


F.RENDUS['captures'] = b_captures
F.TYPES['captures'] = 'Captures'
CSS_CAPTURES = '''
.cap__intro{font-size:15.5px;line-height:1.6;color:var(--encre-2);max-width:76ch;margin:0 0 18px}
.caps{display:grid;gap:18px;align-items:start}
.caps--2{grid-template-columns:repeat(2,minmax(0,1fr))}.caps--3{grid-template-columns:repeat(3,minmax(0,1fr))}.caps--4{grid-template-columns:repeat(4,minmax(0,1fr))}
.cap{margin:0;display:flex;flex-direction:column;gap:10px;background:var(--carte);border:1px solid var(--trait);border-radius:var(--r);padding:12px;box-shadow:var(--ombre)}
.cap--large{grid-column:1/-1}
.cap__img{background:var(--relief);border-radius:10px;overflow:hidden;display:flex;justify-content:center;max-height:560px}
.cap__img img{display:block;max-width:100%;height:auto;object-fit:contain;object-position:top}
.cap--large .cap__img{max-height:none}
.cap figcaption{font-size:14px;line-height:1.5;color:var(--encre-2)}
.cap figcaption b{display:block;color:var(--encre);font-size:15px;margin-bottom:2px}
.cap__src{display:block;margin-top:6px;font-size:12px;color:var(--encre-3)}
@media (max-width:900px){.caps--3,.caps--4{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:560px){.caps--2,.caps--3,.caps--4{grid-template-columns:1fr}}
@media print{.cap{break-inside:avoid}}
'''
W = 'medias/WhatsApp Image 2026-11-'

O = []


def onglet(titre, icone, question, reponse, en_bref, blocs):
    O.append(dict(id=F.slug(titre), titre=titre, icone=icone, question=question, reponse=reponse, enBref=en_bref, blocs=blocs))


onglet('Synthèse', 'compass',
       'Comment trouver des partenaires Eqology avec Instagram et Facebook ?',
       'En recrutant d’abord des personnes qui ont déjà une clientèle. Des publicités quotidiennes les invitent à une visio et à un appel avec vous. '
       'Le site est en ligne lundi 23 novembre, les publicités démarrent mercredi 25 novembre.',
       ['Le chiffre d’un distributeur Eqology vient de son équipe : l’objectif principal est de recruter des business partners, la boutique vient en soutien.',
        'Vos références qui réussissent mènent toutes à une conversation (appel, visio, soirée). Les publicités « promotion » vers une boutique s’arrêtent vite.',
        'Deux cibles : le grand public qui cherche un complément de revenu, et les praticiens de santé qui ont déjà une patientèle, en commençant par les naturopathes.',
        'Votre seul rôle : rappeler les personnes intéressées. Le site, les publicités, les relances et le suivi sont pris en charge.',
        'Calendrier : signature et acompte de 1 800 € TTC d’ici vendredi 20/11, site lundi 23/11, publicités mercredi 25/11, bilan fin décembre.'],
       [dict(type='cartes', titre='Le dispositif en quatre repères', colonnes=4, cartes=[
           dict(etiquette='Cible', titre='Des partenaires', texte='Des personnes qui feront à leur tour la promotion des produits, en priorité des professionnels qui ont déjà une clientèle.'),
           dict(etiquette='Canal', titre='Instagram et Facebook', texte='Des stories et publications sponsorisées, chaque jour, avec un budget de 30 € par jour payé à Meta.'),
           dict(etiquette='Conversion', titre='Votre appel', texte='Chaque inscrit vous arrive par SMS ou WhatsApp. Vous le rappelez sous 48 heures, puis il assiste à une visio.'),
           dict(etiquette='Mesure', titre='Un bilan chiffré', texte='Coût par inscrit, taux de rappel, présents à la visio, nouveaux partenaires : premier bilan fin décembre.')]),
        dict(type='texte', titre='Pourquoi recruter plutôt que vendre', paragraphes=[
            'Vendre un flacon à la fois rapporte une commission. Recruter une naturopathe qui met trente patients sous oméga-3 rapporte chaque mois, sur toute son activité.',
            'C’est ce que font les distributeurs que vous nous avez envoyés : leurs comptes Instagram comptent entre 50 et 5 000 abonnés seulement. Leur chiffre ne vient pas de leur audience, il vient de leur équipe.'])])

onglet('Vos références', 'search',
       'Que font les distributeurs que vous nous avez envoyés ?',
       'Ils recrutent des gens qui ont déjà des clients, et tout leur parcours mène à une conversation. Aucun ne vend l’huile flacon par flacon avec de la publicité.',
       ['Boost Your Health (Pays-Bas) : un site à deux portes, un appel gratuit de 15 minutes, des coachs et thérapeutes recrutés.',
        'L’équipe Eqology de Sicile : 31 publicités sur 7 mois pour remplir des soirées d’information.',
        'Sur 320 publicités Meta qui citent Eqology en Europe, celles qui durent mènent à un échange ; celles qui promettent -25 % s’arrêtent en cinq semaines.',
        'En France, aucun distributeur Eqology ne fait de publicité Meta qui cite la marque : la place est libre.'],
       [dict(type='tableau', titre='Vos références, une par une', colonnes=['Référence', 'Leur méthode', 'Ce que nous reprenons'], lignes=[
           ['Boost Your Health (Pays-Bas)', 'Site à deux portes (« ma santé » / « entreprendre »), appel découverte de 15 minutes, témoignages de professionnels recrutés, Instagram centré sur leur vie de famille', 'Les deux portes, l’appel, la cible des professionnels'],
           ['Eqology Business Partners Sicilia', 'Soirées de présentation avec des responsables Eqology, remplies par des publicités régulières', 'La publicité qui remplit une réunion'],
           ['Robert Kontriner', 'Page partenaire Eqology à son nom, chaque lien porte son identifiant', 'La boutique à votre nom, sans stock'],
           ['Falko Krismayr', 'Recrutement en face à face, Instagram et presse pour la crédibilité', 'Le contact humain au bout du parcours'],
           ['Livre « Oméga-3, le verdict de la science »', 'Approche des professionnels de santé par la science, sans parler de produit', 'Parler science aux pros, l’activité ensuite'],
           ['Norway Omega, IM8', 'Marques en ligne, stories sponsorisées soignées, offre de bienvenue', 'Le format story et la qualité des visuels']]),
        dict(type='tableau', titre='Ce que montrent les publicités Meta', colonnes=['Annonceur', 'Durée de diffusion', 'Où mène la publicité', 'Lecture'], lignes=[
            ['Eqology Business Partners Sicilia', '7 mois, 31 publicités', 'Soirées d’information', 'Ça marche'],
            ['Pure Omega3 (Roumanie)', '7 mois, 31 publicités', 'Message privé', 'Ça marche'],
            ['Diététicienne (Pologne)', '10 mois, 17 publicités', 'Instagram puis échange', 'Ça marche'],
            ['Kiné-diététicienne (Bulgarie)', '6 mois, 11 publicités', 'Page partenaire', 'Ça marche'],
            ['Gradina Health (Bulgarie)', '5 semaines, 38 publicités', 'Boutique avec -25 %', 'Arrêté'],
            ['Recrutement frontal (Pays-Bas)', 'Une seule diffusion', '« Rejoins mon équipe »', 'Pas de preuve']],
            lire='Personne ne paie des mois de publicité qui ne rapporte rien : la durée de diffusion est le meilleur indice disponible. Source : Bibliothèque publicitaire Meta, 16/11/2026.')])

onglet('Cibles et messages', 'target',
       'Qui allons-nous chercher, et avec quel message ?',
       'Deux publics, deux messages, une même destination : votre appel.',
       ['Le grand public : 35 à 70 ans, intéressé par la santé, qui cherche un complément de revenu.',
        'Les praticiens de santé en premier : naturopathes, micronutritionnistes, diététiciens-nutritionnistes, puis kinés et ostéopathes. Une recrue peut amener des dizaines de patients.',
        'Votre histoire sert de preuve : à 75 ans, en forme et partenaire Eqology. Une courte vidéo de vous sera la première publicité testée.',
        'Avec eux, on parle d’abord science et test ; l’activité vient ensuite. C’est l’approche de votre livre « Oméga-3, le verdict de la science ».'],
       [dict(type='cartes', titre='Les deux cibles', colonnes=2, cartes=[
           dict(etiquette='Cible 1', titre='Le grand public', sousTitre='Retraités et actifs, 35 à 70 ans', texte='Ils ont du temps, un entourage et l’envie d’un revenu d’appoint.',
                puces=['Message : « Santé et complément de revenu : 45 minutes pour tout comprendre. »', 'Destination : inscription à la visio d’information']),
           dict(etiquette='Cible 2, en premier', titre='Les praticiens de santé', sousTitre='Naturopathes et voie médicale', texte='Naturopathes, micronutritionnistes, diététiciens-nutritionnistes, puis kinés, ostéopathes et autres praticiens. Ils ont une patientèle qui leur fait confiance.',
                puces=['Message : « Mesurez l’équilibre oméga-6 / oméga-3 de vos patients avec un test sanguin à domicile, analysé par un laboratoire indépendant. »', 'Destination : un échange avec vous, puis le test pour le praticien lui-même'])]),
        dict(type='cartes', titre='Trois premières publicités', colonnes=3, cartes=[
            dict(etiquette='Vidéo', titre='Votre histoire', texte='« J’ai 75 ans, je prends mes oméga-3 chaque matin et j’accompagne des partenaires. » Vous face caméra, 30 secondes, sous-titrée.'),
            dict(etiquette='Visuel', titre='Le test oméga-3', texte='Le test à faire chez soi, le résultat, puis l’invitation à la visio. Pour le grand public.'),
            dict(etiquette='Science', titre='Pour les praticiens de santé', texte='« Naturopathe ou praticien de santé ? Le test oméga-3 pour vos patients, et les études qui l’accompagnent. »')])])

onglet('Le parcours', 'funnel',
       'Comment une personne devient-elle partenaire ?',
       'Elle voit une publicité, s’inscrit en laissant son téléphone, vous l’appelez, puis elle assiste à une présentation.',
       ['Six étapes, de la publicité au démarrage.',
        'Entre l’inscription et la visio, des e-mails automatiques présentent Eqology et l’activité.',
        'Quand vous appelez, la personne a déjà reçu l’essentiel.',
        'Ceux qui veulent seulement acheter passent par la boutique.'],
       [dict(type='etapes', titre='Les six étapes', etapes=[
           dict(titre='Publicité', texte='Une story ou une publication sur Instagram et Facebook.'),
           dict(titre='Page « Rejoindre l’équipe »', texte='Votre histoire, l’activité, à qui elle s’adresse, comment on démarre.'),
           dict(titre='Formulaire ou rendez-vous', texte='Le visiteur laisse ses coordonnées, ou réserve directement un créneau dans votre agenda, comme chez Boost Your Health.'),
           dict(titre='Votre appel', texte='Sous 48 heures, par téléphone. Vous recevez le contact par SMS ou WhatsApp.'),
           dict(titre='Visio de présentation', texte='Assurée par Eqology ou par votre parrain. Vous n’avez rien à préparer.'),
           dict(titre='Démarrage', texte='Le nouveau partenaire choisit son Business Kit et rejoint votre équipe.')]),
        dict(type='tableau', titre='Les e-mails automatiques', colonnes=['Quand', 'Contenu'], lignes=[
            ['Juste après l’inscription', 'Confirmation, qui vous êtes, la date de la prochaine visio'],
            ['Deux jours après', 'Pourquoi Eqology : le test, les produits, la Norvège'],
            ['Cinq jours après', 'Un témoignage de partenaire'],
            ['La veille de la visio', 'Le rappel et le lien de connexion']])])

onglet('Dispositif Meta', 'megaphone',
       'Comment les publicités sont-elles organisées ?',
       'Deux campagnes, 30 € par jour au total, trois créations chacune, optimisées en continu.',
       ['Un portefeuille Meta Business au nom de ZENCO, une page Facebook et un compte Instagram dédiés.',
        'Le budget est payé directement à Meta par votre carte bancaire.',
        'Campagne « visio » à 20 € par jour, campagne « praticiens de santé » à 10 € par jour, puis réallocation après deux semaines.',
        'Seuls les bienfaits des oméga-3 autorisés par l’Union européenne sont utilisés, sans promesse de revenu chiffrée.'],
       [dict(type='cartes', titre='Les comptes', colonnes=3, cartes=[
           dict(titre='Meta Business', texte='Le portefeuille qui regroupe la page, le compte Instagram et le compte publicitaire, au nom de ZENCO.'),
           dict(titre='Compte publicitaire', texte='Réglé par votre carte bancaire : vous payez Meta directement, sans intermédiaire.'),
           dict(titre='Compte Instagram', texte='6 à 9 publications de base (qui vous êtes, l’activité, le test, des témoignages). Il sert de vitrine, sans animation de communauté.')]),
        dict(type='tableau', titre='Les campagnes', colonnes=['Campagne', 'Ciblage', 'Budget de départ', 'Objectif mesuré'], lignes=[
            ['Visio d’information', 'France, 35-70 ans, intérêts santé, bien-être, revenu complémentaire', '20 € par jour', 'Inscriptions au formulaire'],
            ['Praticiens de santé', 'France, métiers et intérêts : naturopathie, micronutrition, diététique, ostéopathie, kinésithérapie', '10 € par jour', 'Demandes d’échange']],
            lire='Après deux semaines, le budget passe sur la campagne qui obtient les inscriptions les moins chères.'),
        dict(type='cartes', titre='Les règles', colonnes=3, cartes=[
            dict(titre='Allégations autorisées', texte='Uniquement les bienfaits validés par l’Europe, par exemple : « le DHA contribue au fonctionnement normal du cerveau ».'),
            dict(titre='Pas de promesse de revenu', texte='On parle d’activité et de complément de revenu, jamais d’un montant gagné.'),
            dict(titre='Transparence', texte='La mention « distributeur indépendant Eqology » apparaît sur le site et dans les publicités.')])])

onglet('La page de recrutement', 'star',
       'Que trouve un futur partenaire sur la page « Rejoindre l’équipe », et que lui dites-vous au téléphone ?',
       'Une page qui raconte votre histoire, explique l’activité sans jargon et se termine par un formulaire. Ensuite, votre appel suit une trame simple en cinq temps.',
       ['C’est la page d’arrivée de toutes les publicités de recrutement.',
        'Elle répond aux questions avant qu’on les pose : stock, coût de départ, temps nécessaire, façon d’être payé.',
        'Aucun montant de revenu n’est promis : on explique le fonctionnement, pas un chiffre.',
        'Votre appel dure 10 à 15 minutes et se termine par une invitation à la visio.'],
       [dict(type='etapes', titre='Les sections de la page', etapes=[
           dict(titre='L’accroche et votre vidéo', texte='« Santé et complément de revenu : je vous explique comment je fais, à 75 ans. » Votre vidéo de 30 secondes juste en dessous.'),
           dict(titre='Votre histoire', texte='Qui vous êtes, pourquoi vous avez choisi Eqology, ce que l’activité vous apporte.'),
           dict(titre='L’activité, en clair', texte='Recommander des produits que l’on utilise soi-même, avec un test qui montre le résultat. Quelques heures par semaine, depuis chez soi.'),
           dict(titre='Comment on est payé', texte='Une commission sur ses propres ventes, puis une part sur les ventes de l’équipe que l’on accompagne. Sans montant promis.'),
           dict(titre='Pour qui', texte='Les praticiens de santé qui veulent proposer le test à leurs patients, et les personnes qui cherchent un revenu d’appoint.'),
           dict(titre='Comment on démarre', texte='Formulaire, puis votre appel, puis la visio de présentation, puis le Business Kit.'),
           dict(titre='Les questions fréquentes', texte='Stock, coût de départ, temps nécessaire, accompagnement : les réponses avant le formulaire.'),
           dict(titre='Le formulaire', texte='En bas de page et rappelé en haut : cinq champs, moins d’une minute.')]),
        dict(type='tableau', titre='Le formulaire', colonnes=['Champ', 'Pourquoi'], lignes=[
            ['Prénom et nom', 'Savoir qui vous rappelez'],
            ['Téléphone', 'Vous rappelez par téléphone, pas par e-mail'],
            ['Profil', 'Particulier ou professionnel, et le métier : vous adaptez votre discours'],
            ['Créneau de rappel', 'Matin, après-midi ou soir : vous appelez au bon moment'],
            ['Consentement', 'Accord pour être rappelé et recevoir les e-mails, obligatoire']]),
        dict(type='etapes', titre='Votre appel, en cinq temps', etapes=[
            dict(titre='Vous présenter', texte='« Bonjour, Yves Coignard, vous avez demandé des informations sur l’activité Eqology. Vous avez quelques minutes ? »'),
            dict(titre='Écouter', texte='« Qu’est-ce qui vous a donné envie de cliquer ? » Revenu, santé, ses propres clients : la réponse oriente la suite.'),
            dict(titre='Expliquer simplement', texte='Les produits, le test, la façon d’être payé, le temps nécessaire. Votre propre expérience vaut mieux qu’un argumentaire.'),
            dict(titre='Inviter', texte='À la prochaine visio, avec la date. Pour un praticien de santé : lui proposer d’abord de faire le test lui-même et de lire les études.'),
            dict(titre='Confirmer', texte='Un SMS avec la date et le lien de la visio. La personne reçoit aussi les e-mails automatiques.')]),
        dict(type='cartes', titre='Les questions qu’on vous posera', colonnes=2, cartes=[
            dict(titre='« Faut-il acheter du stock ? »', texte='Non. Les clients commandent directement chez Eqology, qui livre. Il n’y a ni stock ni colis.'),
            dict(titre='« Combien coûte le démarrage ? »', texte='Le Business Kit, dont le montant dépend du kit choisi. Votre parrain et vous présentez les options pendant la visio.'),
            dict(titre='« Combien peut-on gagner ? »', texte='Cela dépend du temps consacré et de l’équipe accompagnée. On ne promet pas de chiffre : on explique comment la rémunération fonctionne.'),
            dict(titre='« Je ne sais pas vendre. »', texte='On commence par un produit que l’on utilise soi-même, avec un test qui montre le résultat. On est accompagné par son parrain et par la formation Eqology.')])])

onglet('La boutique en ligne', 'payment',
       'Comment fonctionne la boutique en ligne ?',
       'Une vitrine en français de toute la gamme Eqology. Le client choisit, clique sur « Commander » et finalise sa commande sur le site Eqology, à votre nom. Vous touchez votre commission, sans stock ni colis.',
       ['La boutique présente les produits en français : bienfaits autorisés, mode d’emploi, test.',
        'Chaque bouton « Commander » ouvre la fiche Eqology avec votre identifiant : la commande vous est attribuée.',
        'Eqology encaisse, livre, gère les retours et le service client. Les prix restent toujours à jour.',
        'Elle travaille pour vous jour et nuit : vos clients commandent seuls, reviennent chaque mois, et chaque commande vous revient.'],
       [dict(type='etapes', titre='Le parcours d’achat d’un client', etapes=[
           dict(titre='Il arrive sur la boutique', texte='Depuis votre site, un lien envoyé après votre appel, ou le lien en bio de votre compte Instagram.'),
           dict(titre='Il choisit', texte='Un produit, un pack ou le test, grâce à une fiche claire en français.'),
           dict(titre='Il clique sur « Commander »', texte='La fiche du produit s’ouvre sur eqology.com, avec votre identifiant de partenaire.'),
           dict(titre='Il paie chez Eqology', texte='Paiement sécurisé par carte sur le site Eqology, qui prépare et expédie le colis.'),
           dict(titre='La vente vous revient', texte='La commande apparaît dans votre compte Eqology, avec votre commission.')]),
        dict(type='tableau', titre='Ce que contient la boutique', colonnes=['Rubrique', 'Produits présentés'], lignes=[
            ['Oméga-3', 'Pure Arctic Oil, Gold, Heart & Energy, Vegan Oil, Kids'],
            ['Packs', 'Les packs avantage qui associent l’huile, les vitamines et le test'],
            ['Le test oméga-3', 'Comment il se fait à la maison, ce qu’il mesure, pourquoi le refaire après quelques mois'],
            ['Vitamines et minéraux', 'Vitamine K2 + D3, D3 en gouttes, Nordic Energy Booster, Essential'],
            ['Beauté et forme', 'Collagène marin, Collagen Booster, soins Ocean Miracle, shakes protéinés']],
            lire='La liste exacte suit le catalogue Eqology France au moment de la mise en ligne.'),
        dict(type='cartes', titre='Une fiche produit', colonnes=3, cartes=[
            dict(titre='Ce que c’est', texte='Le produit, sa composition et son origine (poissons sauvages de l’Arctique, huile d’olive, vitamine D3).'),
            dict(titre='Ce qu’il apporte', texte='Uniquement les bienfaits autorisés par l’Union européenne, par exemple : « l’EPA et le DHA contribuent à une fonction cardiaque normale ».'),
            dict(titre='Comment le prendre', texte='La dose, le moment, la durée conseillée, et le test à faire avant puis après.')]),
        dict(type='cartes', titre='Qui fait quoi dans la vente', colonnes=2, cartes=[
            dict(titre='Eqology', puces=['Le paiement et la facture au client', 'La préparation et la livraison', 'Les retours et le service client', 'Les prix, toujours à jour']),
            dict(titre='Votre boutique', puces=['La présentation en français, simple et claire', 'Votre nom et votre histoire, qui rassurent', 'Le lien que vous envoyez après chaque appel', 'La preuve de sérieux pour un futur partenaire'])]),
        dict(type='cartes', titre='Ce que la boutique vous apporte', colonnes=3, cartes=[
            dict(etiquette='Ventes', titre='Une boutique ouverte jour et nuit', texte='Vos clients commandent seuls, à toute heure, sans vous appeler. Chaque commande est enregistrée à votre nom.'),
            dict(etiquette='Fidélité', titre='Des clients qui reviennent', texte='Les oméga-3 se prennent tous les jours : un client satisfait recommande chaque mois par votre lien, et votre commission tombe à chaque fois.'),
            dict(etiquette='Différence', titre='Votre vitrine, à votre image', texte='Les autres partenaires n’ont que la page Eqology standard. Vous avez une vraie boutique en français, avec votre histoire et vos conseils.'),
            dict(etiquette='Recrutement', titre='La preuve de votre sérieux', texte='Un futur partenaire voit une gamme claire, un site professionnel et un distributeur installé : il vous fait confiance plus vite.'),
            dict(etiquette='Appels', titre='Le lien de fin d’appel', texte='Après chaque conversation, vous envoyez le lien de la boutique par SMS. La personne commande quand elle est prête.'),
            dict(etiquette='Avenir', titre='Prête pour la suite', texte='Quand les ventes suivront, la boutique pourra recevoir ses propres publicités, sans rien reconstruire.')]),
        dict(type='tableau', titre='D’où viennent les visiteurs de la boutique', colonnes=['Source', 'Comment'], lignes=[
            ['Votre site', 'La porte « Ma santé » de la page d’accueil'],
            ['Votre compte Instagram', 'Le lien en bio, comme le Linktree de Boost Your Health'],
            ['Vos appels', 'Le lien envoyé par SMS après chaque conversation'],
            ['La visio de présentation', 'Le lien partagé à la fin de chaque séance'],
            ['Vos documents', 'Le QR code de vos présentations et de vos cartes']])])

onglet('Suivi et mesure', 'chart',
       'Comment suit-on les contacts et les résultats ?',
       'Chaque inscription vous arrive sur le téléphone, part en relance automatique et remonte dans les chiffres de la campagne.',
       ['Chaque formulaire vous parvient immédiatement par SMS ou WhatsApp.',
        'Une copie arrive chez Heyfuture pour suivre les relances et vous prévenir si un contact n’a pas été rappelé.',
        'Le site envoie un signal à Meta à chaque inscription : Meta apprend à montrer les publicités aux bonnes personnes.',
        'Cinq indicateurs, suivis chaque semaine.'],
       [dict(type='tableau', titre='Les indicateurs', colonnes=['Indicateur', 'Ce qu’il dit', 'Source'], lignes=[
           ['Coût par inscrit', 'Combien coûte un nouveau contact', 'Meta, événement « inscription » envoyé par le site'],
           ['Taux de rappel', 'Part des inscrits que vous avez joints', 'Suivi des contacts'],
           ['Présents à la visio', 'Intérêt réel des contacts', 'Liste de la visio'],
           ['Nouveaux partenaires', 'Le résultat final', 'Votre compte Eqology'],
           ['Commandes boutique', 'Les ventes attribuées à votre compte', 'Votre compte Eqology']]),
        dict(type='texte', titre='Le suivi technique', paragraphes=[
            'Le site est équipé du pixel Meta et de l’API de conversions : à chaque inscription, Meta reçoit l’information, même si le visiteur bloque les cookies du navigateur.',
            'Chaque campagne porte ses propres paramètres de suivi, pour savoir quelle publicité a amené quel contact.'])])

onglet('Qui fait quoi', 'users',
       'Qu’aurez-vous à faire, concrètement ?',
       'Rappeler les personnes intéressées et les inviter à la visio. Tout le reste est pris en charge.',
       ['Vous n’avez aucun outil à manipuler : les contacts arrivent tout prêts sur votre téléphone.',
        'Vous validez les premières publicités une fois.',
        'Dix minutes de tournage au téléphone suffisent pour la vidéo.'],
       [dict(type='tableau', titre='La répartition des tâches', colonnes=['Tâche', 'Yves', 'Heyfuture'], lignes=[
           ['Comptes Meta et Instagram', 'Ajoute sa carte au compte publicitaire', 'Crée et configure'],
           ['Vidéo de présentation', '10 minutes de tournage au téléphone', 'Script, montage, sous-titres'],
           ['Site et boutique', 'Relit sa présentation', 'Conçoit, développe, met en ligne'],
           ['Publicités', 'Valide les premières créations', 'Crée, diffuse, optimise chaque jour'],
           ['Contacts', 'Rappelle sous 48 heures', 'Alertes, relances e-mail, suivi'],
           ['Visio de présentation', 'Invite ses contacts', 'Organisation avec le parrain si besoin'],
           ['Bilan', 'Partage le nombre de partenaires signés', 'Prépare le bilan chiffré']])])

onglet('Calendrier', 'rocket',
       'Quand lance-t-on ?',
       'Site en ligne le lundi 23 novembre, publicités le mercredi 25 novembre, premier bilan fin décembre.',
       ['Ces dates supposent le devis signé et l’acompte réglé d’ici vendredi 20 novembre.',
        'Point à deux semaines le mercredi 9 décembre.',
        'Bilan du premier mois fin décembre, décision pour janvier.'],
       [dict(type='tableau', titre='Les dates', colonnes=['Date', 'Étape'], lignes=[
           ['Lundi 16 novembre', 'Stratégie, devis et factures'],
           ['Vendredi 20 novembre au plus tard', 'Devis signé, facture d’acompte 1004 réglée (1 800 € TTC)'],
           ['Du 18 au 20 novembre', 'Création des comptes Meta et Instagram, tournage de la vidéo'],
           ['Lundi 23 novembre', 'Site en ligne : page « Rejoindre l’équipe » et boutique'],
           ['Mardi 24 novembre', 'Validation des premières publicités'],
           ['Mercredi 25 novembre', 'Lancement des publicités'],
           ['Mercredi 9 décembre', 'Point à deux semaines : budget réorienté vers la meilleure campagne'],
           ['Fin décembre', 'Bilan du premier mois et décision pour janvier']])])

onglet('Budget et règlement', 'payment',
       'Combien, et comment se passe le règlement ?',
       '3 000 € HT (3 600 € TTC) au total, réglés en deux fois : 50 % à la signature, 50 % à la mise en ligne du site et des publicités. Le budget publicitaire se paie à part, directement à Meta.',
       ['Acompte de 50 % à la signature : facture 1004, 1 800 € TTC.',
        'Solde de 50 % à la mise en ligne du site et des publicités : 1 800 € TTC.',
        'Le site e-commerce vaut 3 000 € HT ; la première version ayant été réglée, il est facturé 1 500 € HT.',
        'Budget publicitaire : 30 € par jour payés à Meta, environ 900 € par mois. Pilotage à partir du deuxième mois : 500 € HT par mois, en option.'],
       [dict(type='tableau', titre='Le devis', colonnes=['Prestation', 'Contenu', 'HT'], lignes=[
           ['Lancement des publicités Meta', 'Comptes, stratégie, stories et publications, vidéo, suivi, pilotage du premier mois', '1 500 €'],
           ['Site e-commerce simplifié', 'Page « Rejoindre l’équipe », prise de rendez-vous, boutique, alertes, relances, hébergement 12 mois', '3 000 €'],
           ['Remise fidélité', 'Première version du site déjà réglée', '-1 500 €'],
           ['Total', 'Devis PROP-2026-1116-ZENCO', '3 000 € HT, soit 3 600 € TTC']]),
        dict(type='tableau', titre='L’échéancier', colonnes=['Échéance', 'Document', 'HT', 'TTC'], lignes=[
           ['À la signature', 'Facture d’acompte 1004 : 50 %', '1 500 €', '1 800 €'],
           ['Mise en ligne du site et des publicités', 'Facture de solde : 50 %', '1 500 €', '1 800 €']],
            lire='Règlement par virement à TAM LABS, la société qui porte Heyfuture. Les coordonnées bancaires figurent sur la facture.'),
        dict(type='cartes', titre='Ce qui n’est pas dans le devis', colonnes=2, cartes=[
            dict(titre='Le budget publicitaire', texte='30 € par jour, payés directement à Meta par carte. Un mois minimum avant le bilan, deux mois de préférence.'),
            dict(titre='Le pilotage après le premier mois', texte='En option : 500 € HT par mois, sans engagement, pour continuer à créer et optimiser les publicités.')])])

onglet('Ce qu’il nous faut', 'check',
       'De quoi avons-nous besoin pour démarrer ?',
       'Six éléments, à transmettre entre le 18 et le 20 novembre.',
       ['Votre identifiant de partenaire Eqology, pour coder les boutons « Commander ».',
        'Le nom de votre parrain et ses dates de visio.',
        'Votre choix entre SMS et WhatsApp pour recevoir les contacts.',
        'Dix minutes pour la vidéo, et le SIREN de ZENCO pour les documents.'],
       [dict(type='tableau', titre='La liste', colonnes=['Élément', 'Pourquoi', 'Pour quand'], lignes=[
           ['Votre identifiant de partenaire Eqology', 'Coder chaque bouton « Commander » à votre nom', '18 novembre'],
           ['Le nom de votre parrain et ses dates de visio', 'Organiser la présentation des nouveaux contacts', '20 novembre'],
           ['SMS ou WhatsApp', 'Vous prévenir de chaque nouveau contact', '18 novembre'],
           ['Accès à votre compte Facebook', 'Créer la page et le compte publicitaire', '19 novembre'],
           ['10 minutes pour la vidéo', 'Première publicité', '20 novembre'],
           ['Le numéro SIREN de ZENCO', 'Compléter le devis et les factures', '18 novembre']])])

onglet('Vos demandes', 'mail',
       'Qu’avez-vous demandé, et où y répondons-nous ?',
       'Chacune de vos demandes est reprise dans ce dossier : la prise de rendez-vous, la boutique, les stories chaque jour, les distributeurs qui marchent, le calendrier.',
       ['Votre modèle, Boost Your Health, est repris : « Rejoindre l’équipe » avec prise de rendez-vous en ligne.',
        'La boutique permet d’acheter directement, comme dans la publicité IM8 que vous avez repérée.',
        'Les stories sponsorisées tournent tous les jours, avec un budget de 30 € par jour.',
        'Le site est en ligne le lundi 23 novembre.'],
       [dict(type='tableau', titre='Vos messages, un par un', colonnes=['Votre demande', 'Date', 'Notre réponse', 'Où dans le dossier'], lignes=[
           ['« Il faudrait retirer la mention FENA du QR code »', '08/11', 'Fait : le QR mène à la page d’accueil, sans FENA', 'Déjà livré'],
           ['« Le hollandais il a un calendrier pour prendre rendez-vous »', '13/11', 'Prise de rendez-vous en ligne sur votre page « Rejoindre l’équipe », reliée à votre agenda', 'Le site : rejoindre l’équipe'],
           ['« Direct tu achètes » (la publicité IM8)', '13/11', 'Une boutique où l’on commande directement, à votre nom', 'Le site : la boutique'],
           ['« Il met Join the team avec un calendrier où les gens peuvent prendre rendez-vous »', '14/11', 'Votre page « Rejoindre l’équipe », sur le modèle de Boost Your Health', 'Le site : rejoindre l’équipe'],
           ['« Maintenant faut les mettre sur Instagram »', '14/11', 'Stories et publications sponsorisées chaque jour sur Instagram et Facebook', 'Dispositif Meta'],
           ['« … et LinkedIn »', '14/11', 'Prévu dans un second temps pour aborder les professionnels, hors de ce devis', 'Cibles et messages'],
           ['« Des Eqology qui marchent fort »', '14/11', 'Chaque compte analysé : site, Instagram, publicités, et ce que nous reprenons', 'Vos références'],
           ['« En quoi consistent les 30 € par jour ? Avec des stories ? »', '13/11', 'Le budget payé à Meta pour diffuser vos stories chaque jour', 'Budget et règlement'],
           ['« Quelle fréquence pour les stories ? »', '13/11', 'Tous les jours, avec des créations renouvelées', 'Dispositif Meta'],
           ['« Quel est ton timing pour le site ? »', '15/11', 'Site en ligne le lundi 23/11, publicités le mercredi 25/11', 'Calendrier']])])

onglet('Le site : plan général', 'layers',
       'Comment est organisé votre nouveau site ?',
       'Un site neuf, pensé pour le téléphone, avec deux portes dès l’accueil : « Rejoindre l’équipe » et « Ma santé », qui mène à la boutique.',
       ['L’accueil demande « Par où voulez-vous commencer ? », comme chez Boost Your Health.',
        'La partie recrutement et la boutique partagent le même site, la même adresse et votre image.',
        'Chaque page est pensée pour le téléphone, là où arrivent les visiteurs d’Instagram.',
        'Formulaire, prise de rendez-vous, alertes et suivi sont reliés dès la mise en ligne.'],
       [dict(type='tableau', titre='Les pages du site', colonnes=['Page', 'Ce qu’on y trouve', 'À quoi elle sert'], lignes=[
           ['Accueil', 'Votre photo, une phrase d’accroche, les deux portes « Rejoindre l’équipe » et « Ma santé »', 'Orienter chaque visiteur en une seconde'],
           ['Rejoindre l’équipe', 'Votre histoire, l’activité, comment on démarre, le formulaire et la prise de rendez-vous', 'Recruter des partenaires'],
           ['Boutique', 'Les familles de produits, les packs, le test', 'Vendre à votre nom'],
           ['Fiches produits', 'Composition, bienfaits autorisés, mode d’emploi, bouton « Commander »', 'Convaincre et faire commander'],
           ['Le test oméga-3', 'Comment il se fait, ce qu’il mesure, pourquoi le refaire', 'La porte d’entrée santé, comme chez vos références'],
           ['Qui suis-je', 'Votre parcours, pourquoi Eqology, vos engagements', 'Créer la confiance'],
           ['Contact et mentions', 'Téléphone, formulaire, mentions légales, confidentialité', 'Rassurer et rester en règle']]),
        dict(type='cartes', titre='Ce qui est compris', colonnes=3, cartes=[
            dict(titre='Pensé pour le téléphone', texte='Lisible et rapide sur mobile, là où arrivent les visiteurs des publicités.'),
            dict(titre='Votre image', texte='Votre logo, vos couleurs, vos photos et votre vidéo, sur toutes les pages.'),
            dict(titre='La prise de rendez-vous', texte='Un calendrier en ligne relié à votre agenda : les rendez-vous apparaissent sur votre téléphone.'),
            dict(titre='Les alertes', texte='Chaque contact vous arrive par SMS ou WhatsApp, avec une copie chez Heyfuture.'),
            dict(titre='Le suivi', texte='Le pixel Meta et l’API de conversions, pour que les publicités apprennent qui s’inscrit.'),
            dict(titre='Hébergement et sécurité', texte='Hébergement de 12 mois, certificat de sécurité (cadenas), sauvegardes.')])])

# ——— Les captures de l'analyse
def ajoute(titre_onglet, position, bloc):
    o = next(x for x in O if x['titre'] == titre_onglet)
    o['blocs'].insert(position, bloc)


ajoute('Vos références', 1, dict(type='captures', titre='Ce que vous nous avez envoyé : les distributeurs', colonnes=3,
    intro='Les captures transmises le 13 et le 14 novembre. Chacune a été ouverte et analysée : site, compte Instagram, liens, publicités.',
    images=[
        dict(src=W + '14 at 13.18.22.jpeg', titre='Boost Your Health', texte='1 876 abonnés. Leur vie de famille, et « Travailler où tu veux ? Rejoins l’équipe » dans la bio.', source='Instagram @boostyourhealth.eu'),
        dict(src=W + '13 at 15.18.01.jpeg', titre='Leur prise de rendez-vous', texte='« Échange découverte sans engagement », 15 minutes en visio : c’est la seule vraie conversion de leur site.', source='Calendly de Boost Your Health'),
        dict(src=W + '13 at 15.18.44.jpeg', titre='Eqology Business Partners Sicilia', texte='Soirée de présentation à Catane avec des responsables Eqology : « Transforme ta passion pour le bien-être en une nouvelle profession ».', source='Instagram @ecologybusinesspartnersicilia'),
        dict(src=W + '14 at 13.18.22 (3).jpeg', titre='La page partenaire de Robert Kontriner', texte='Le site Eqology à son nom : tous les liens portent son identifiant, chaque commande lui revient.', source='partner.eqology.com/omegarob'),
        dict(src=W + '14 at 13.18.22 (5).jpeg', titre='Falko Krismayr', texte='Ancien coach olympique devenu mentor. Il recrute en face à face ; Instagram et la presse servent sa crédibilité.', source='Instagram @falko_krismayr'),
        dict(src=W + '14 at 13.18.22 (6).jpeg', titre='eqologywithaga', texte='Un compte qui démarre : 4 abonnés, aucune publication. Le minimum fourni par Eqology ne suffit pas à recruter.', source='Instagram @eqologywithaga')]))
ajoute('Vos références', 2, dict(type='captures', titre='Le compte officiel et les marques', colonnes=4,
    images=[
        dict(src=W + '14 at 13.18.22 (1).jpeg', titre='Eqology Business', texte='Le compte officiel : stories Products, Kick Off, Opportunity, Convention, que les partenaires reprennent.', source='Instagram @eqologybusiness'),
        dict(src=W + '14 at 13.18.22 (2).jpeg', titre='Une cliente qui déballe', texte='Eqology reposte les déballages de ses clientes : la preuve vient des utilisateurs.', source='Story @eqology'),
        dict(src=W + '13 at 15.17.24.jpeg', titre='Norway Omega', texte='Story sponsorisée : produit dans la glace, 20 € offerts avec le code OCEANDEEP.', source='Publicité Instagram'),
        dict(src=W + '13 at 15.17.32.jpeg', titre='IM8 Health', texte='Story sponsorisée diffusée au nom d’un média, qui mène à une page dédiée à un médecin.', source='Publicité Instagram')]))
ajoute('Vos références', 3, dict(type='captures', titre='Boost Your Health, étape par étape', colonnes=2,
    intro='La référence la plus complète. Leur site ne vend presque rien directement : il remplit l’agenda de Dennis.',
    images=[
        dict(src='boost/1-accueil.jpg', titre='L’accueil', texte='« Boost health, Grow wealth » : l’argent est annoncé dès la première seconde.', source='boostyourhealth.eu', large=True),
        dict(src='boost/2-deux-portes.jpg', titre='Les deux portes', texte='« Où veux-tu commencer ? » : améliorer sa santé, ou entreprendre dans la santé. Puis les chiffres d’Eqology.', source='boostyourhealth.eu'),
        dict(src='boost/3-famille.jpg', titre='Leur offre', texte='Ils vendent leur accompagnement et leur liberté : « Je travaille quand et où je veux ».', source='boostyourhealth.eu'),
        dict(src='boost/4-temoignages.jpg', titre='Des professionnels recrutés', texte='Coach en nutrition, thérapeute, salle de sport : chacun a d’abord proposé Eqology à ses clients, puis monté son équipe.', source='boostyourhealth.eu'),
        dict(src='boost/6-linktree.jpg', titre='Le lien en bio, une boutique', texte='22 produits, chacun avec leur code partenaire : le client paie chez Eqology, la vente leur revient.', source='linktr.ee/boostyourhealth.eu')]))
ajoute('Vos références', 5, dict(type='captures', titre='Les publicités relevées', colonnes=3,
    intro='Captures de la Bibliothèque publicitaire Meta, le registre public de toutes les publicités Facebook et Instagram.',
    images=[
        dict(src='pubs/sicilia.jpg', titre='Sicile : remplir les soirées', texte='31 publicités sur 7 mois, sur la santé, pour faire venir du monde aux présentations. Ça marche.', source='Bibliothèque Meta, 12/04 au 06/05/2026'),
        dict(src='pubs/pure-omega3.jpg', titre='Roumanie : la conversation privée', texte='Pas de prix affiché, tout se conclut en message privé. 31 publicités sur 7 mois.', source='Bibliothèque Meta, juin 2026'),
        dict(src='pubs/lang-gesund.jpg', titre='Allemagne : « 3 participants recherchés »', texte='8 semaines d’huile et 2 tests offerts, candidature par formulaire : une prise de contacts déguisée en projet.', source='Bibliothèque Meta, active depuis le 13/11/2026'),
        dict(src='pubs/gesundezelle.jpg', titre='Allemagne : les coffrets de Noël', texte='Coffrets à 109 € et 189 € avec test sanguin. On commente « SMALL » ou « LARGE », la vente se fait en privé.', source='Bibliothèque Meta, active depuis le 12/11/2026'),
        dict(src='pubs/gradina.jpg', titre='Bulgarie : la promotion vers la boutique', texte='-25 % et renvoi direct vers la boutique. 38 publicités en cinq semaines, puis arrêt : ça n’a pas marché.', source='Bibliothèque Meta, 02 au 09/03/2026'),
        dict(src='pubs/marloes.jpg', titre='Pays-Bas : recruter les coachs', texte='« Tu es coach ou thérapeute ? Rejoins mon équipe Eqology. » Diffusée une seule fois : pas encore de preuve.', source='Bibliothèque Meta, 04 au 10/02/2026')]))
ajoute('Cibles et messages', 1, dict(type='cartes', titre='Avec les praticiens de santé : la science d’abord', colonnes=3, cartes=[
    dict(titre='Le test et les études avant l’activité', texte='Une approche trop commerciale fait fuir les praticiens. On leur présente d’abord le test, les résultats de leurs patients et les études ; l’activité vient dans un second temps.'),
    dict(titre='Les médecins à part', texte='Un médecin ne vend pas de compléments à ses patients. Avec eux, on parle uniquement du test et de la science, sans proposer l’activité.'),
    dict(titre='Des allégations irréprochables', texte='Uniquement les bienfaits autorisés par l’Union européenne, avec les sources citées. C’est ce qui crédibilise un distributeur face à un professionnel de santé.')]))
ajoute('Cibles et messages', 2, dict(type='captures', titre='La voie santé, déjà ouverte par d’autres distributeurs', colonnes=3,
    images=[
        dict(src='pubs/dieteticienne-pologne.jpg', titre='Une diététicienne (Pologne)', texte='Des publicités sur la santé, relancées pendant 10 mois : la plus longue diffusion relevée.', source='Bibliothèque Meta, 2025-2026'),
        dict(src='pubs/kine-bulgarie.jpg', titre='Une kiné-diététicienne (Bulgarie)', texte='Une tournée santé nationale, et sa page partenaire Eqology en lien. 11 publicités sur 6 mois.', source='Bibliothèque Meta, 2026'),
        dict(src='pubs/livre-linkedin.jpg', titre='Votre livre, sur LinkedIn', texte='« Mes chers confrères » : l’approche par la science, sans produit, puis la porte vers l’activité. Le bon ton pour les praticiens.', source='Votre document « Réseau LinkedIn »')]))
ajoute('Cibles et messages', 3, dict(type='captures', titre='Ce que font déjà d’autres distributeurs', colonnes=2,
    images=[
        dict(src='pubs/marloes.jpg', titre='Pour les professionnels', texte='Une distributrice néerlandaise vise directement les coachs et thérapeutes.', source='Bibliothèque Meta'),
        dict(src='pubs/soiree-pologne.jpg', titre='Pour le grand public', texte='Un distributeur polonais invite à une soirée « Business Opportunity » : « Je n’invite pas tout le monde ».', source='Bibliothèque Meta, juin 2026')]))
ajoute('Le parcours', 1, dict(type='captures', titre='Deux exemples de parcours observés', colonnes=2,
    images=[
        dict(src=W + '13 at 15.18.01.jpeg', titre='L’appel découverte', texte='Chez Boost Your Health, tout mène à 15 minutes en visio. Pour vous, ce sera un appel téléphonique.', source='Calendly de Boost Your Health'),
        dict(src='pubs/lang-gesund.jpg', titre='Le formulaire au bout de la publicité', texte='La publicité mène à une candidature : nom, coordonnées, motivation. C’est le principe de notre page « Rejoindre l’équipe ».', source='Bibliothèque Meta')]))
ajoute('La page de recrutement', 1, dict(type='captures', titre='Les modèles observés', colonnes=2,
    images=[
        dict(src='boost/3-famille.jpg', titre='Raconter son histoire', texte='Boost Your Health vend d’abord leur parcours et leur accompagnement.', source='boostyourhealth.eu'),
        dict(src='boost/4-temoignages.jpg', titre='Montrer des partenaires', texte='Des professionnels qui racontent comment ils ont démarré.', source='boostyourhealth.eu')]))
ajoute('La boutique en ligne', 1, dict(type='captures', titre='Les modèles de la boutique', colonnes=3,
    images=[
        dict(src='boost/2-deux-portes.jpg', titre='Les deux portes', texte='« Ma santé » mène à la boutique, « entreprendre » à la page de recrutement.', source='boostyourhealth.eu'),
        dict(src='boost/6-linktree.jpg', titre='Le catalogue codé', texte='Chaque produit mène à Eqology avec le code du partenaire.', source='linktr.ee/boostyourhealth.eu'),
        dict(src=W + '14 at 13.18.22 (3).jpeg', titre='La page partenaire', texte='La boutique Eqology au nom du partenaire, vers laquelle mènent les boutons « Commander ».', source='partner.eqology.com/omegarob')]))

NOMS = {'La page de recrutement': 'Le site : rejoindre l’équipe', 'La boutique en ligne': 'Le site : la boutique'}
for o in O:
    if o['titre'] in NOMS:
        o['titre'] = NOMS[o['titre']]; o['id'] = F.slug(o['titre'])
ORDRE = ['Synthèse', 'Vos demandes', 'Vos références', 'Cibles et messages', 'Le parcours', 'Le site : plan général',
         'Le site : rejoindre l’équipe', 'Le site : la boutique', 'Dispositif Meta', 'Suivi et mesure', 'Qui fait quoi',
         'Calendrier', 'Budget et règlement', 'Ce qu’il nous faut']
O.sort(key=lambda o: ORDRE.index(o['titre']))
bq = next(o for o in O if o['titre'] == 'Le site : la boutique')
bq['blocs'].sort(key=lambda b: 0 if b.get('titre') == 'Ce que la boutique vous apporte' else 1)

for i, o in enumerate(O):
    o['numero'] = f'{i:02d}'
    o['_fichier'] = o['id']
    o['blocs'] = [b for b in o['blocs'] if b.get('type') in F.RENDUS]

police = None
try:
    police = json.load(open(F.CHARTE, encoding='utf-8'))['polices']['embarque'][0]
except Exception as ex:  # noqa: BLE001
    print(f'! police non embarquée ({ex})', file=sys.stderr)
CHARTE_YVES = (':root{--fond:#FAFAF8;--relief:#F5F4F0;--pale:#E8F4F4;--nuit:#0B1D2E;--nuit-2:#172847;'
               '--accent:#4DA8B5;--accent-fonce:#2E656D;--accent-fond:#EEF8F9;--n1:#EEF8F9;--n2:#D5EFF2;--n3:#ABDFE5;--n4:#81CFD8;--n5:#4DA8B5}'
               '.marque-logo{display:inline-flex;background:#fff;border-radius:10px;padding:7px 12px}.marque-logo img{height:20px;width:auto;display:block}'
               '.lat__tete .marque-logo img{height:24px}.couverture .marque-logo img{height:34px}')
LOGO_YVES = 'data:image/webp;base64,' + base64.b64encode(open(os.path.join(os.path.dirname(ICI), 'assets/images/eqology-logo.png'), 'rb').read()).decode()
html = F.page(O, police).replace('</style>', CSS_CAPTURES + CHARTE_YVES + '</style>', 1)
html = html.replace('<span class="marque">heyfuture</span>', f'<span class="marque-logo"><img src="{LOGO_YVES}" alt="Eqology"></span>')
sortie = os.path.join(ICI, 'dossier-yves.html')
open(sortie, 'w', encoding='utf-8').write(html)
print(sortie, len(html) // 1024, 'Ko')
