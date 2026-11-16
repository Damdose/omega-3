# -*- coding: utf-8 -*-
"""Dossier de stratégie pour Yves Coignard, au format des dossiers Heyfuture (moteur fabriquer.py des « Fondations »).
Damien, 16/11/2026 : « format horizontal, en mode comme un audit ».
Usage : python3 mission/dossier_yves.py  →  mission/dossier-yves.html"""
import os, sys, json
sys.path.insert(0, os.path.expanduser('~/Documents/audits-heyfuture/clients/heyfuture-strategie'))
import fabriquer as F

ICI = os.path.dirname(os.path.abspath(__file__))
F.TITRE = 'Recruter des partenaires Eqology'
F.DATE = '16 novembre 2026 · Yves Coignard'

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
        'Deux cibles : le grand public qui cherche un complément de revenu, et les professionnels qui ont déjà des clients (coachs, salles de sport, diététiciennes).',
        'Votre seul rôle : rappeler les personnes intéressées. Le site, les publicités, les relances et le suivi sont pris en charge.',
        'Calendrier : signature et règlement de 2 700 € TTC d’ici vendredi 20/11, site lundi 23/11, publicités mercredi 25/11, bilan fin décembre.'],
       [dict(type='cartes', titre='Le dispositif en quatre repères', colonnes=4, cartes=[
           dict(etiquette='Cible', titre='Des partenaires', texte='Des personnes qui feront à leur tour la promotion des produits, en priorité des professionnels qui ont déjà une clientèle.'),
           dict(etiquette='Canal', titre='Instagram et Facebook', texte='Des stories et publications sponsorisées, chaque jour, avec un budget de 30 € par jour payé à Meta.'),
           dict(etiquette='Conversion', titre='Votre appel', texte='Chaque inscrit vous arrive par SMS ou WhatsApp. Vous le rappelez sous 48 heures, puis il assiste à une visio.'),
           dict(etiquette='Mesure', titre='Un bilan chiffré', texte='Coût par inscrit, taux de rappel, présents à la visio, nouveaux partenaires : premier bilan fin décembre.')]),
        dict(type='texte', titre='Pourquoi recruter plutôt que vendre', paragraphes=[
            'Vendre un flacon à la fois rapporte une commission. Recruter une coach qui met trente clients sous oméga-3 rapporte chaque mois, sur toute son activité.',
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
        'Les professionnels : coachs sportifs, salles de sport, diététiciennes, kinés, esthéticiennes. Une recrue peut amener des dizaines de clients.',
        'Votre histoire sert de preuve : à 75 ans, en forme et partenaire Eqology. Une courte vidéo de vous sera la première publicité testée.',
        'Les naturopathes viendront plus tard, avec une approche par la science et le test.'],
       [dict(type='cartes', titre='Les deux cibles', colonnes=2, cartes=[
           dict(etiquette='Cible 1', titre='Le grand public', sousTitre='Retraités et actifs, 35 à 70 ans', texte='Ils ont du temps, un entourage et l’envie d’un revenu d’appoint.',
                puces=['Message : « Santé et complément de revenu : 45 minutes pour tout comprendre. »', 'Destination : inscription à la visio d’information']),
           dict(etiquette='Cible 2', titre='Les professionnels', sousTitre='Ils ont déjà une clientèle', texte='Coachs sportifs, salles de sport, diététiciennes, kinés, esthéticiennes.',
                puces=['Message : « Proposez le test oméga-3 à vos clients et ajoutez une source de revenu à votre activité. »', 'Destination : échange découverte avec vous'])]),
        dict(type='cartes', titre='Trois premières publicités', colonnes=3, cartes=[
            dict(etiquette='Vidéo', titre='Votre histoire', texte='« J’ai 75 ans, je prends mes oméga-3 chaque matin et j’accompagne des partenaires. » Vous face caméra, 30 secondes, sous-titrée.'),
            dict(etiquette='Visuel', titre='Le test oméga-3', texte='Le test à faire chez soi, le résultat, puis l’invitation à la visio. Pour le grand public.'),
            dict(etiquette='Message', titre='Pour les pros', texte='« Coach ou thérapeute ? Proposez le test à vos clients. » Pour les professionnels.')])])

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
           dict(titre='Formulaire', texte='Nom, téléphone, profil (particulier ou professionnel), créneau de rappel.'),
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
        'Campagne « visio » à 20 € par jour, campagne « professionnels » à 10 € par jour, puis réallocation après deux semaines.',
        'Seuls les bienfaits des oméga-3 autorisés par l’Union européenne sont utilisés, sans promesse de revenu chiffrée.'],
       [dict(type='cartes', titre='Les comptes', colonnes=3, cartes=[
           dict(titre='Meta Business', texte='Le portefeuille qui regroupe la page, le compte Instagram et le compte publicitaire, au nom de ZENCO.'),
           dict(titre='Compte publicitaire', texte='Réglé par votre carte bancaire : vous payez Meta directement, sans intermédiaire.'),
           dict(titre='Compte Instagram', texte='6 à 9 publications de base (qui vous êtes, l’activité, le test, des témoignages). Il sert de vitrine, sans animation de communauté.')]),
        dict(type='tableau', titre='Les campagnes', colonnes=['Campagne', 'Ciblage', 'Budget de départ', 'Objectif mesuré'], lignes=[
            ['Visio d’information', 'France, 35-70 ans, intérêts santé, bien-être, revenu complémentaire', '20 € par jour', 'Inscriptions au formulaire'],
            ['Professionnels', 'France, métiers et intérêts : coaching sportif, fitness, nutrition, kinésithérapie, esthétique', '10 € par jour', 'Demandes d’échange']],
            lire='Après deux semaines, le budget passe sur la campagne qui obtient les inscriptions les moins chères.'),
        dict(type='cartes', titre='Les règles', colonnes=3, cartes=[
            dict(titre='Allégations autorisées', texte='Uniquement les bienfaits validés par l’Europe, par exemple : « le DHA contribue au fonctionnement normal du cerveau ».'),
            dict(titre='Pas de promesse de revenu', texte='On parle d’activité et de complément de revenu, jamais d’un montant gagné.'),
            dict(titre='Transparence', texte='La mention « distributeur indépendant Eqology » apparaît sur le site et dans les publicités.')])])

onglet('Le site', 'layers',
       'À quoi sert le nouveau site ?',
       'Il a deux portes : « Rejoindre l’équipe », où mènent les publicités, et une boutique qui présente toute la gamme Eqology à votre nom.',
       ['La page « Rejoindre l’équipe » est la page d’arrivée des publicités.',
        'La boutique rassure et permet de commander : chaque bouton « Commander » ouvre Eqology avec votre identifiant de partenaire.',
        'Eqology encaisse, livre et assure le service client : vous n’avez ni stock ni colis.',
        'En ligne le lundi 23 novembre.'],
       [dict(type='tableau', titre='Ce que contient le site', colonnes=['Partie', 'Contenu', 'Rôle'], lignes=[
           ['Rejoindre l’équipe', 'Votre histoire, l’activité, à qui elle s’adresse, les étapes, le formulaire et la prise de rendez-vous', 'Recrutement, page d’arrivée des publicités'],
           ['Boutique', 'La gamme Eqology présentée en français : oméga-3, packs, vitamines, test', 'Rassurer et permettre la commande'],
           ['Bouton « Commander »', 'Ouvre la fiche du produit sur le site Eqology avec votre identifiant', 'Chaque commande vous est attribuée'],
           ['Mentions et confidentialité', 'Mentions légales, politique de confidentialité, consentement au formulaire', 'Conformité']]),
        dict(type='texte', titre='Pourquoi les prix restent chez Eqology', paragraphes=[
            'Les prix sont affichés sur le site Eqology au moment de la commande. Le site n’a donc jamais de prix faux quand Eqology les change.'])])

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
       ['Ces dates supposent le devis signé et les deux premières factures réglées d’ici vendredi 20 novembre.',
        'Point à deux semaines le mercredi 9 décembre.',
        'Bilan du premier mois fin décembre, décision pour janvier.'],
       [dict(type='tableau', titre='Les dates', colonnes=['Date', 'Étape'], lignes=[
           ['Lundi 16 novembre', 'Stratégie, devis et factures'],
           ['Vendredi 20 novembre au plus tard', 'Devis signé, factures 1004 et 1005 réglées (2 700 € TTC)'],
           ['Du 18 au 20 novembre', 'Création des comptes Meta et Instagram, tournage de la vidéo'],
           ['Lundi 23 novembre', 'Site en ligne : page « Rejoindre l’équipe » et boutique'],
           ['Mardi 24 novembre', 'Validation des premières publicités'],
           ['Mercredi 25 novembre', 'Lancement des publicités'],
           ['Mercredi 9 décembre', 'Point à deux semaines : budget réorienté vers la meilleure campagne'],
           ['Fin décembre', 'Bilan du premier mois et décision pour janvier']])])

onglet('Budget et règlement', 'payment',
       'Combien, et comment se passe le règlement ?',
       '3 000 € HT (3 600 € TTC) au total : 2 700 € TTC à la signature, 900 € TTC à la mise en ligne du site. Le budget publicitaire se paie à part, directement à Meta.',
       ['Le lancement des publicités est payé d’avance (facture 1004, 1 800 € TTC).',
        'Le site fait l’objet d’un acompte de 50 % (facture 1005, 900 € TTC) et d’un solde à la mise en ligne (900 € TTC).',
        'Le site e-commerce vaut 3 000 € HT ; la première version ayant été réglée, il est facturé 1 500 € HT.',
        'Budget publicitaire : 30 € par jour payés à Meta, environ 900 € par mois. Pilotage à partir du deuxième mois : 500 € HT par mois, en option.'],
       [dict(type='tableau', titre='L’échéancier', colonnes=['Échéance', 'Document', 'HT', 'TTC'], lignes=[
           ['À la signature', 'Facture 1004 : lancement des publicités Meta, payé d’avance', '1 500 €', '1 800 €'],
           ['À la signature', 'Facture 1005 : acompte de 50 % sur le site', '750 €', '900 €'],
           ['Lundi 23 novembre', 'Solde de 50 % sur le site', '750 €', '900 €'],
           ['Total', 'Devis PROP-2026-1116-ZENCO', '3 000 €', '3 600 €']],
            lire='Règlement par virement à TAM LABS, la société qui porte Heyfuture. Les coordonnées bancaires figurent sur chaque facture.'),
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
ajoute('Cibles et messages', 1, dict(type='captures', titre='Ce que font déjà d’autres distributeurs', colonnes=2,
    images=[
        dict(src='pubs/marloes.jpg', titre='Pour les professionnels', texte='Une distributrice néerlandaise vise directement les coachs et thérapeutes.', source='Bibliothèque Meta'),
        dict(src='pubs/soiree-pologne.jpg', titre='Pour le grand public', texte='Un distributeur polonais invite à une soirée « Business Opportunity » : « Je n’invite pas tout le monde ».', source='Bibliothèque Meta, juin 2026')]))
ajoute('Le parcours', 1, dict(type='captures', titre='Deux exemples de parcours observés', colonnes=2,
    images=[
        dict(src=W + '13 at 15.18.01.jpeg', titre='L’appel découverte', texte='Chez Boost Your Health, tout mène à 15 minutes en visio. Pour vous, ce sera un appel téléphonique.', source='Calendly de Boost Your Health'),
        dict(src='pubs/lang-gesund.jpg', titre='Le formulaire au bout de la publicité', texte='La publicité mène à une candidature : nom, coordonnées, motivation. C’est le principe de notre page « Rejoindre l’équipe ».', source='Bibliothèque Meta')]))
ajoute('Le site', 1, dict(type='captures', titre='Les modèles du nouveau site', colonnes=3,
    images=[
        dict(src='boost/2-deux-portes.jpg', titre='Les deux portes', texte='Le principe repris pour votre page d’accueil.', source='boostyourhealth.eu'),
        dict(src='boost/6-linktree.jpg', titre='Le catalogue codé', texte='Chaque produit mène à Eqology avec le code du partenaire.', source='linktr.ee/boostyourhealth.eu'),
        dict(src=W + '14 at 13.18.22 (3).jpeg', titre='La page partenaire', texte='La boutique Eqology au nom du partenaire, vers laquelle mènent les boutons « Commander ».', source='partner.eqology.com/omegarob')]))

for i, o in enumerate(O):
    o['numero'] = f'{i:02d}'
    o['_fichier'] = o['id']
    o['blocs'] = [b for b in o['blocs'] if b.get('type') in F.RENDUS]

police = None
try:
    police = json.load(open(F.CHARTE, encoding='utf-8'))['polices']['embarque'][0]
except Exception as ex:  # noqa: BLE001
    print(f'! police non embarquée ({ex})', file=sys.stderr)
html = F.page(O, police).replace('</style>', CSS_CAPTURES + '</style>', 1)
sortie = os.path.join(ICI, 'dossier-yves.html')
open(sortie, 'w', encoding='utf-8').write(html)
print(sortie, len(html) // 1024, 'Ko')
