# -*- coding: utf-8 -*-
"""Stratégie Meta Ads recentrée sur les praticiens (26/11/2026), format EXPLICATION.  python3 -I mission/plan_ads_pros.py
Remplace le dispositif à deux publics de plan_ads.py : 30 € par jour, un seul ensemble « praticiens », trois créations statiques."""
import os, sys
ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.expanduser('~/Documents/crm-heyfuture/docs/chantier-skills/formats'))
import explication as X


def crea(nom, titre, role):
    return (f'<figure style="margin:0;display:grid;gap:8px"><div style="display:grid;grid-template-columns:4fr 2.25fr;gap:8px;align-items:start">'
            f'<img src="../pubs/pro-{nom}-4x5.png" alt="{titre}, format 4:5" style="width:100%;border-radius:10px;border:1px solid var(--trait)">'
            f'<img src="../pubs/pro-{nom}-9x16.png" alt="{titre}, format 9:16" style="width:100%;border-radius:10px;border:1px solid var(--trait)"></div>'
            f'<figcaption style="font-size:14px;color:var(--encre-2)"><b style="color:var(--encre)">{titre}</b> · {role}</figcaption></figure>')


PLANCHE = ('<div style="display:grid;gap:26px">'
           + crea('cures', 'A1 · Les cures', 'lancement : le mécanisme que le praticien connaît déjà')
           + crea('test', 'A2 · Mesurez avant de conseiller', 'lancement : la science d’abord')
           + crea('cabinet', 'A3 · Vous conseillez, Eqology encaisse', 'réserve : remplace la moins bonne à J7')
           + '</div>')

cfg = dict(
    onglet='Meta Ads praticiens · Yves',
    oeil='Yves Coignard · stratégie Meta Ads · 26 novembre 2026',
    titre='30 € par jour, uniquement sur les praticiens, avec deux pubs qui parlent leur langue : les cures et le test',
    chapo='Un particulier n’a personne à qui recommander un abonnement à 100 € par mois. Un naturopathe, si : il met déjà ses patients en cure. Toute la campagne vise donc les praticiens de santé au naturel, et on la juge au coût par praticien rappelé, pas au nombre de clics.',
    logo=os.path.join(ICI, '..', 'assets', 'images', 'eqology-eq.png'),
    polices=dict(titre='Space Grotesk', texte='DM Sans',
                 lien='https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,600;9..40,700&family=Space+Grotesk:wght@500;600;700&display=swap'),
    couleurs=dict(rouge='#335075', vert='#3d8691', jaune='#A88C5C'),
    variables={'fond': '#FAFAF8', 'trait': '#ECEAE4', 'vert-pale': '#EEF8F9'},
    css='code{word-break:break-all}.page>*{min-width:0}',
    parties=[
        dict(
            titre='Ce qui rapporte, c’est un praticien qui met ses patients en cure',
            court='Pourquoi les pros',
            schema=X.flux([('Praticien', 'recruté par Yves', 'fort'), ('Test', 'avant la cure', 'neutre'),
                           ('Cure', '3 mois, puis renouvelée', 'fort'), ('Second test', 'il voit où il en est', 'neutre'),
                           ('Commission', 'à chaque commande', 'ok')],
                          legende='Un praticien, c’est des dizaines de patients qui commandent et renouvellent'),
            intro=['Un particulier recruté vend, au mieux, à deux ou trois proches. Un praticien conseille des cures toute la semaine : il ajoute le test et l’huile à ce qu’il fait déjà, et ses patients renouvellent.'],
            donc='la campagne entière vise les praticiens. L’ensemble « complément de revenus » est supprimé.',
        ),
        dict(
            titre='Meta ne connaît pas les métiers : c’est la pub qui fait le tri',
            court='Ciblage',
            intro=['Meta ne cible plus par profession. Il cible des centres d’intérêt, et l’intérêt « naturopathie » regroupe les naturopathes, leurs patients et tous les curieux. Trois choses resserrent quand même la cible.'],
            points=[
                dict(titre='1. Un message que seul un praticien comprend', texte='« Ajoutez le test à vos cures », « Mesurez avant de conseiller » : un particulier ne se sent pas concerné et ne clique pas. On paie moins de curieux.'),
                dict(titre='2. Des intérêts de métier, sans élargissement automatique', texte='France, 25 à 65 ans. Naturopathie, micronutrition, diététique, phytothérapie, ostéopathie, kinésithérapie, nutrition. On choisit « options d’audience d’origine » pour que Meta ne sorte pas de ces intérêts.'),
                dict(titre='3. Le formulaire qui dit qui est pro', texte='La question « Vous êtes… » sépare praticiens, coachs et particuliers. Aujourd’hui la version pros la saute et range tout le monde en praticien : à corriger avant le lancement.'),
            ],
            donc='on juge les pubs au coût par praticien rappelé. Une demande de particulier ne compte pas.',
        ),
        dict(
            titre='Une campagne, un ensemble, deux pubs : 30 € par jour ne se divisent pas',
            court='Campagne',
            points=[
                dict(titre='Campagne', texte='Objectif Prospects · conversion sur le site · événement « Prospect » (Lead) du pixel 1114935464677335 · budget réglé sur l’ensemble, pas sur la campagne.'),
                dict(titre='Ensemble « Praticiens » · 30 € par jour', texte='Ciblage ci-dessus · placements automatiques (fil, stories, Reels) · Page « Yves Coignard · Distributeur indépendant Eqology » · annonceur et payeur ZENCO SAS.'),
                dict(titre='Deux pubs au lancement, une en réserve', texte='A1 Les cures et A2 Le test, chacune en 4:5 pour le fil et 9:16 pour les stories. A3 Le cabinet attend J7. Avec 30 € par jour, une troisième pub au départ diluerait l’apprentissage.'),
                dict(titre='Le suivi', texte='Chaque lien porte <code>?cible=pro&amp;utm_source=meta&amp;utm_campaign=praticiens&amp;utm_content=cures</code> (ou test, cabinet) : l’e-mail d’Yves dit de quelle pub vient le contact.'),
            ],
            donc='Meta affichera « apprentissage limité » : à ce budget il ne verra pas 50 demandes par semaine. C’est normal, il apprend plus lentement.',
        ),
        dict(
            titre='Trois pubs statiques, une idée chacune',
            court='Les pubs',
            intro=['Dessinées dans la charte du site (bleu nuit, sable, Albert Sans), avec les vraies photos produits. Aucun visage présenté comme un client, aucun montant, la mention « Distributeur indépendant Eqology » partout.'],
            html=PLANCHE,
            points=[
                dict(titre='A1 · Texte de la pub « Les cures »',
                     texte='Vous construisez des cures pour vos patients ? Avec Eqology, vous y ajoutez un test sanguin à domicile : il mesure leur équilibre oméga‑6 / oméga‑3 avant de commencer. Un second test, quelques mois plus tard, montre où ils en sont.<br><br>Entre les deux, ils suivent leur cure avec une huile de Norvège issue d’une pêche certifiée MSC. Ils commandent seuls avec votre lien, Eqology encaisse et livre, et vous touchez une commission sur chaque commande, renouvellements compris.<br><br>Votre kit de bienvenue de 99 € vous est remboursé, histoire de tester vous‑même les produits. Laissez votre numéro : un distributeur indépendant Eqology vous rappelle sous 48 h.<br><br><b>Titre</b> : Ajoutez le test oméga‑3 à vos cures · <b>Description</b> : Rappel sous 48 h, sans engagement'),
                dict(titre='A2 · Texte de la pub « Mesurez avant de conseiller »',
                     texte='Avant de conseiller des oméga‑3, vous pouvez mesurer. Le test Eqology se fait à domicile, au bout du doigt, et il est analysé par un laboratoire indépendant. Votre patient connaît son équilibre oméga‑6 / oméga‑3 avant sa cure, puis le refait pour voir où il en est.<br><br>Il commande seul avec votre lien. Eqology encaisse et livre, et vous touchez une commission sur ses commandes.<br><br>Votre kit de bienvenue de 99 € vous est remboursé. Laissez votre numéro : un distributeur indépendant Eqology vous rappelle sous 48 h.<br><br><b>Titre</b> : Mesurez avant de conseiller · <b>Description</b> : Rappel sous 48 h, sans engagement'),
                dict(titre='A3 · Texte de la pub « Le cabinet » (réserve)',
                     texte='Vous ne voulez rien vendre au cabinet ? Vous n’aurez pas à le faire. Vous recommandez le test et l’huile Eqology, vos patients commandent en ligne avec votre lien, et Eqology encaisse, expédie et gère le service client.<br><br>Vous touchez une commission sur chaque commande, renouvellements compris. Aucun stock, aucun paiement à gérer. Votre kit de bienvenue de 99 € vous est remboursé.<br><br>Laissez votre numéro : un distributeur indépendant Eqology vous rappelle sous 48 h.<br><br><b>Titre</b> : Vous conseillez, Eqology encaisse et livre · <b>Description</b> : Rappel sous 48 h, sans engagement'),
            ],
        ),
        dict(
            titre='Quatorze jours pour savoir si Meta trouve des praticiens à bon prix',
            court='Calendrier',
            schema=X.frise([('Veille', 'une demande\nde test', 'ok'), ('J0', 'lancement\nA1 + A2', 'fort'),
                            ('J1 → J7', 'on ne touche\nà rien', 'ok'), ('J7', 'A3 remplace\nla moins bonne', 'ok'),
                            ('J14', 'bilan : coût par\npraticien rappelé', 'fort')]),
            intro=['Une pub qui a dépensé 60 € sans une seule demande s’arrête à J7 et A3 prend sa place. À J14, on regarde combien de praticiens Yves a vraiment eus au téléphone, et ce que chacun a coûté.'],
            donc='le test coûte environ 420 €, réglés par Yves directement à Meta. À J14, soit on continue, soit on coupe et on mise tout sur la prospection directe.',
        ),
        dict(
            titre='Honnêtement : quelques bons contacts par semaine, pas un raz-de-marée',
            court='Mon avis',
            deux=[dict(titre='Ce qui joue pour nous', ton='ok',
                       texte='Le terrain est libre : aucun distributeur Eqology francophone ne fait de pub en France (veille du 16/11). L’angle des cures parle aux naturopathes. Le site, le pixel, la conversion et la Page sont prêts. Et Yves est bon au téléphone.'),
                  dict(titre='Ce qui joue contre nous', ton='mal',
                       texte='Meta touchera surtout des curieux, pas des praticiens. Beaucoup de naturopathes se méfient de la vente en réseau, et le mot « commission » en fera fuir une partie. Avec 30 € par jour, Meta apprend lentement. Tout dépend enfin des rappels d’Yves, à 75 ans.')],
            points=[dict(titre='Ce que j’attends, en estimation à vérifier',
                         texte='20 à 45 demandes par mois, dont peut-être un tiers de vrais praticiens, soit 5 à 15. Si Yves en convainc un ou deux par mois, chacun avec des patients en cure, l’opération est rentable sur l’année. Elle ne le sera pas sur le premier mois.')],
            donc='Meta seul ne fera pas une machine à recruter. Il apportera quelques conversations qualifiées par semaine. Le levier le plus sûr reste la liste des naturopathes appelés en direct, à lancer en parallèle.',
            donc_mot='Mon avis',
        ),
        dict(
            titre='Avant d’appuyer sur « Publier », quatre choses',
            court='Avant le lancement',
            points=[
                dict(titre='1. La carte bancaire d’Yves (Yves)', texte='Seul blocage côté Meta. Tout le reste du compte est prêt : Page, pixel relié, conversion « Demande de rappel », annonceur et payeur.'),
                dict(titre='2. La question « Vous êtes… » dans le formulaire pros (moi, à ton feu vert)', texte='Sans elle, Yves ne sait pas qui est vraiment praticien avant d’appeler.'),
                dict(titre='3. Le titre de la page pros aligné sur la pub (moi, à ton feu vert)', texte='La pub parle de cures, la page d’arrivée dit encore « touchez une commission à chaque vente ». Je propose « Ajoutez le test oméga‑3 à vos cures. »'),
                dict(titre='4. Qui reçoit les demandes (toi)', texte='Yves doit les recevoir directement pour rappeler sous 48 h. L’adresse d’envoi n’a pas changé tant que tu ne l’as pas validé.'),
            ],
        ),
    ],
    decision='Je corrige le formulaire et le titre de la page pros, puis je monte la campagne en brouillon via Claude pour Chrome : <b>oui</b> ou <b>non</b> ?',
    pied='Sources : veille Meta Ads du 16/11 (veille/yves-2026-11/META-ADS.md), état du compte YAC relevé par Claude pour Chrome le 26/11, échanges avec Damien du 26/11. Les chiffres attendus sont des estimations à vérifier sur 14 jours.',
)

sortie = os.path.join(ICI, 'plan-ads-pros.html')
open(sortie, 'w').write(X.document(cfg))
print(sortie)
