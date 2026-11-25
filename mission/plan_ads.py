# -*- coding: utf-8 -*-
"""Plan Meta Ads d'Yves (recrutement de partenaires Eqology), format EXPLICATION.  python3 -I mission/plan_ads.py
Reprend le dispositif du dossier client (onglets 08 et 09) : deux campagnes, 30 € par jour, trois créations chacune."""
import os, sys
ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser('~/Documents/crm-heyfuture/docs/chantier-skills/formats'))
import explication as X

cfg = dict(
    onglet='Plan Meta Ads · Yves',
    oeil='Yves Coignard · plan Meta Ads · 25 novembre 2026',
    titre='Une campagne à 30 € par jour, partagée entre deux publics, dès que six prérequis sont réglés',
    chapo='Le dossier d’Yves annonçait les pubs pour aujourd’hui. Le dispositif est prêt, mais le portefeuille YAC est vide : ni compte pub, ni Page, ni Instagram. Voici la campagne, les six premières pubs, les deux premières semaines et ce qui bloque.',
    logo=os.path.join(ICI, '..', 'assets', 'images', 'eqology-eq.png'),
    polices=dict(titre='Space Grotesk', texte='DM Sans',
                 lien='https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,600;9..40,700&family=Space+Grotesk:wght@500;600;700&display=swap'),
    couleurs=dict(rouge='#335075', vert='#3d8691', jaune='#A88C5C'),
    variables={'fond': '#FAFAF8', 'trait': '#ECEAE4', 'vert-pale': '#EEF8F9'},
    parties=[
        dict(
            titre='Une pub ne sert qu’à obtenir un numéro de téléphone',
            court='Objectif',
            schema=X.flux([('Pub Meta', 'story ou fil', 'neutre'), ('Page équipe', 'page d’arrivée', 'fort'),
                           ('Formulaire', 'signal « Lead »', 'fort'), ('Appel d’Yves', 'sous 48 h', 'ok'), ('Visio', 'puis kit', 'ok')],
                          legende='Toutes les pubs mènent au même endroit'),
            intro=['Meta apprend à qui montrer les pubs grâce au signal « Lead » envoyé à chaque formulaire rempli. Sans ce signal, il diffuse à l’aveugle.'],
            donc='on juge les pubs sur le coût par inscrit, puis sur le taux de rappel et les présents à la visio, jamais sur les clics.',
        ),
        dict(
            titre='Une campagne « Prospects » à 30 € par jour, Meta répartit entre deux publics',
            court='Campagne',
            deux=[dict(titre='Ensemble 1 · Praticiens de santé · au moins 10 € par jour',
                       texte='France, 25 à 65 ans, intérêts naturopathie, micronutrition, diététique, ostéopathie et kinésithérapie (selon ce que Meta propose encore). Message : la science et le test, l’activité vient pendant l’appel.'),
                  dict(titre='Ensemble 2 · Visio d’information · le reste du budget',
                       texte='France, 35 à 70 ans, audience Advantage+ avec la santé et le bien-être comme suggestions. Message : découvrir en 45 minutes l’activité de distributeur indépendant Eqology.')],
            points=[dict(titre='Les réglages communs',
                         texte='Budget de 30 € par jour au niveau de la campagne (budget Advantage+), avec un minimum de 10 € par jour pour les praticiens, sinon Meta pousse tout vers le public le moins cher · objectif Prospects, conversion sur le site, événement Lead · placements automatiques (stories, Reels, fil) · une pub au format 9:16 et 4:5 · carte d’Yves au nom de ZENCO.'),
                    dict(titre='Le suivi par pub',
                         texte='Chaque lien porte <code>utm_source=meta&amp;utm_campaign={{adset.name}}&amp;utm_content={{ad.name}}</code>, pour que l’e-mail d’Yves dise de quelle pub vient le contact.')],
            donc='le total reste celui du dossier envoyé à Yves le 16/11 (30 € par jour) ; seule l’organisation change, et il faut le lui dire.',
        ),
        dict(
            titre='Six pubs au départ : la science pour les pros, l’histoire d’Yves pour les autres',
            court='Pubs',
            points=[
                dict(titre='Pros 1 · Le test', texte='« Mesurez l’équilibre oméga-6 / oméga-3 de vos patients : un test sanguin à domicile, analysé par un laboratoire indépendant. » Visuel du kit.'),
                dict(titre='Pros 2 · Ce que dit l’Europe', texte='Carrousel de 3 cartes, avec seulement les allégations autorisées : l’EPA et le DHA contribuent au fonctionnement normal du cœur, le DHA à celui du cerveau et de la vision.'),
                dict(titre='Pros 3 · L’échange', texte='« 15 minutes avec Yves pour voir comment proposer le test à vos patients. » Ton confraternel, celui de son livre.'),
                dict(titre='Visio 1 · Yves face caméra', texte='30 secondes : « J’ai 75 ans, voici pourquoi je fais ça. » <b>Attend sa vidéo.</b> En attendant, on lance avec 5 pubs.'),
                dict(titre='Visio 2 · 45 minutes pour comprendre', texte='Les dates de visio, ce qu’on y voit et l’absence d’engagement. Aucun montant, aucun « revenu rapide ».'),
                dict(titre='Visio 3 · Le test d’abord', texte='« Avant de prendre des oméga-3, je mesure. » L’angle qui marche chez les distributeurs relevés dans la veille.'),
            ],
            exemple='Chaque pub porte la mention « Distributeur indépendant Eqology ». Elles sont dessinées à partir de la charte du site, sans visage inventé ni témoignage fabriqué.',
        ),
        dict(
            titre='Sept jours sans toucher, puis on coupe et on ajuste',
            court='Calendrier',
            schema=X.frise([('Veille', 'faux contact\nde test', 'ok'), ('J0', 'lancement\n6 pubs', 'fort'),
                            ('J1 → J7', 'apprentissage,\non ne touche à rien', 'ok'), ('J7', 'coupe les pubs\nsans inscrit', 'ok'),
                            ('J14', 'on revoit le\nminimum des pros', 'fort'), ('Fin déc.', 'bilan\nà Yves', 'ok')]),
            intro=['Une pub qui a dépensé 30 € sans un seul inscrit s’arrête à J7. Le coût cible par inscrit se fixe à J14, sur les vrais chiffres, pas avant.'],
            donc='la dépense est d’environ 420 € sur les deux premières semaines et 900 € par mois, réglés par Yves directement à Meta.',
        ),
        dict(
            titre='Six prérequis, dont quatre dépendent d’Yves',
            court='Prérequis',
            points=[
                dict(titre='1. Le compte publicitaire dans YAC (Yves)', texte='Avec sa carte, et toi en contrôle total. S’il existe hors de YAC, on le retrouve d’abord dans le Gestionnaire de publicités.'),
                dict(titre='2. La Page Facebook dans YAC (Yves)', texte='Les pubs paraissent en son nom : sans Page, aucune diffusion possible.'),
                dict(titre='3. Le compte Instagram relié (Yves)', texte='Plus 6 à 9 publications de base, que je prépare.'),
                dict(titre='4. Le lien partenaire Eqology (Yves)', texte='Il conditionne la mise en ligne de la V2 : sans lui, les commandes de la boutique ne lui sont pas attribuées.'),
                dict(titre='5. Le pixel et le signal Lead (toi, puis moi)', texte='Claude in Chrome le crée, je le pose dans site-config.js et j’ajoute l’envoi des UTM par le formulaire, qui manque aujourd’hui.'),
                dict(titre='6. La page d’arrivée en ligne (toi)', texte='« Rejoindre l’équipe » n’existe que sur la V2. Elle part en ligne à ton feu vert sur eqology-france.vercel.app (en ligne depuis le 25/11), en attendant un vrai domaine.'),
            ],
            donc_ton='mal', donc_mot='Attention',
            donc='la date du 25/11 annoncée à Yves ne tient plus. Il faut lui envoyer une nouvelle date dès que les points 1 à 3 sont réglés.',
        ),
        dict(
            titre='Trois risques, chacun avec sa parade',
            court='Risques',
            deux=[dict(titre='Meta refuse les pubs « opportunité »', ton='mal',
                       texte='Les promesses de revenu facile et la vente multiniveau sont surveillées. Parade : l’angle test et science, aucun montant. En cas de refus, on reformule ou on déclare la catégorie « Emploi ».'),
                  dict(titre='Un contact qui n’est pas rappelé', ton='mal',
                       texte='Un inscrit qu’on ne rappelle pas, c’est de l’argent perdu. Parade : j’en reçois une copie, et l’alerte SMS ou WhatsApp d’Yves passe avant le lancement.')],
            points=[dict(titre='Les allégations santé', texte='Seuls les bienfaits autorisés par l’Union européenne. Jamais « vous êtes fatigué ? » : Meta refuse qu’une pub suppose l’état de santé de la personne.')],
        ),
    ],
    decision='Domaine tranché le 25/11 : on lance sur eqology-france.vercel.app, puis on bascule sur un vrai domaine au nom d’Yves (redirection, le pixel garde son historique). Reste à trancher : <b>A · un minimum de 10 € par jour pour les praticiens</b> (recommandée : ils restent la cible prioritaire), ou <b>B · Meta répartit librement</b> les 30 €. Réponds d’un mot : A ou B.',
    pied='Sources : dossier de stratégie d’Yves du 16/11 (onglets 08 et 09), veille Meta Ads du 16/11 (veille/yves-2026-11/META-ADS.md), rapport Claude in Chrome sur le portefeuille YAC du 25/11.',
)

sortie = os.path.join(ICI, 'plan-ads.html')
open(sortie, 'w').write(X.document(cfg))
print(sortie)
