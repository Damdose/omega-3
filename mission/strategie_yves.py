# -*- coding: utf-8 -*-
"""Document de stratégie pour Yves Coignard (format COURS, vouvoiement), mission V2 du 16/11/2026.
Usage : python3 mission/strategie_yves.py  →  mission/strategie-yves.html"""
import os, sys, json, tempfile
sys.path.insert(0, os.path.expanduser('~/.claude-2/plugins/cache/heyfuture/heyfuture/b77a5afd4fee/skills/livrable-clair/scripts'))
import cours

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(ICI)

# Charte Heyfuture (crm-heyfuture/src/styles/tokens.css) : beige, encre, verts ; Sora + Plus Jakarta Sans (Damien, 16/11 : « dans la DA de Heyfuture »)
CHARTE = dict(palette=dict(nuit='#0F2E24', principale='#1F5A45', pale='#D3E4DA', fond='#F4F2EE', encre='#1A1A1A',
                           accent='#1F5A45', trait='#E5E2DB', sur_accent='#ffffff'),
              polices=dict(titre='Sora', texte='Plus Jakarta Sans'))
LOGO = os.path.expanduser('~/Documents/crm-heyfuture/public/assets/heyfuture-logo.svg')
charte = os.path.join(tempfile.gettempdir(), 'charte-yves.json')
json.dump(CHARTE, open(charte, 'w'))


def svg(w, h, corps, titre):
    return (f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="{titre}" xmlns="http://www.w3.org/2000/svg" '
            f'style="width:100%;height:auto;font-family:var(--texte)">{corps}</svg>')


def boite(x, y, w, h, t, s='', fond='var(--carte)', bord='var(--trait)', ct='var(--encre)'):
    out = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{fond}" stroke="{bord}" stroke-width="2"/>'
    cy = y + h / 2 + (-6 if s else 5)
    out += f'<text x="{x + w / 2}" y="{cy}" text-anchor="middle" font-size="16" font-weight="700" fill="{ct}">{t}</text>'
    if s:
        cs = '#D3E4DA' if ct == '#fff' else 'var(--encre-2)'
        out += f'<text x="{x + w / 2}" y="{cy + 22}" text-anchor="middle" font-size="13" fill="{cs}">{s}</text>'
    return out


def fleche(x1, y1, x2, y2):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2 - 8}" y2="{y2}" stroke="var(--accent)" stroke-width="3"/>'
            f'<polygon points="{x2},{y2} {x2 - 10},{y2 - 6} {x2 - 10},{y2 + 6}" fill="var(--accent)"/>')


# 1. Une vente contre une équipe
s_ref = svg(720, 250, (
    '<text x="170" y="28" text-anchor="middle" font-size="15" font-weight="700" fill="var(--encre-2)">Vendre soi-même</text>'
    + boite(95, 50, 150, 60, 'Vous', 'un flacon') + fleche(170, 112, 170, 168) + boite(95, 170, 150, 60, '1 client', 'une commission')
    + '<text x="530" y="28" text-anchor="middle" font-size="15" font-weight="700" fill="var(--accent)">Recruter une professionnelle</text>'
    + boite(455, 50, 150, 60, 'Vous', 'un partenaire', 'var(--pale)', 'var(--accent)')
    + ''.join(fleche(530, 112, 400 + i * 65, 168) for i in range(5))
    + ''.join(f'<circle cx="{400 + i * 65}" cy="195" r="24" fill="var(--carte)" stroke="var(--accent)" stroke-width="2"/>'
              f'<text x="{400 + i * 65}" y="200" text-anchor="middle" font-size="12" fill="var(--encre)">client</text>' for i in range(5))
    + '<text x="530" y="243" text-anchor="middle" font-size="13" fill="var(--encre-2)">ses clients commandent chaque mois</text>'), 'Une vente contre une équipe')

# 2. Deux publics
s_publics = svg(720, 260, (
    boite(20, 20, 320, 70, 'Le grand public', 'retraités, actifs, complément de revenu', 'var(--pale)', 'var(--accent)')
    + boite(380, 20, 320, 70, 'Les professionnels', 'ils ont déjà des clients', 'var(--pale)', 'var(--principale)')
    + boite(20, 120, 320, 56, 'Visio d’information', '45 minutes pour tout comprendre')
    + boite(380, 120, 320, 56, 'Une offre pour leurs clients', 'proposer le test oméga-3')
    + fleche(180, 92, 180, 118) + fleche(540, 92, 540, 118)
    + fleche(180, 178, 340, 222) + fleche(540, 178, 380, 222)
    + boite(250, 200, 220, 52, 'Vous les rappelez', '', 'var(--principale)', 'var(--principale)', '#fff')), 'Deux publics, un même rendez-vous')

# 3. Le parcours
etapes = [('Publicité', 'Instagram, Facebook'), ('Page', '« Rejoindre l’équipe »'), ('Inscription', 'nom et téléphone'),
          ('Votre appel', 'sous 48 heures'), ('Visio', 'présentation'), ('Démarrage', 'nouveau partenaire')]
c = ''
for i, (t, s) in enumerate(etapes):
    x = 10 + (i % 3) * 240
    y = 20 if i < 3 else 150
    accent = i == 3
    c += boite(x, y, 200, 76, t, s, 'var(--principale)' if accent else 'var(--carte)', 'var(--principale)' if accent else 'var(--trait)', '#fff' if accent else 'var(--encre)')
    if i in (0, 1, 3, 4):
        c += fleche(x + 202, y + 38, x + 238, y + 38)
c += '<path d="M 590 98 C 590 125, 110 120, 110 148" fill="none" stroke="var(--accent)" stroke-width="3"/><polygon points="110,150 104,139 116,139" fill="var(--accent)"/>'
s_parcours = svg(720, 240, c, 'Le parcours d’un futur partenaire')

# 4. Les pubs
s_pubs = svg(720, 250, (
    ''.join(f'<rect x="{30 + i * 230}" y="10" width="200" height="230" rx="22" fill="var(--carte)" stroke="var(--trait)" stroke-width="2"/>'
            f'<rect x="{42 + i * 230}" y="24" width="176" height="150" rx="12" fill="var(--pale)"/>'
            f'<text x="{130 + i * 230}" y="92" text-anchor="middle" font-size="15" font-weight="700" fill="var(--principale)">{t1}</text>'
            f'<text x="{130 + i * 230}" y="114" text-anchor="middle" font-size="15" font-weight="700" fill="var(--principale)">{t2}</text>'
            f'<rect x="{62 + i * 230}" y="190" width="136" height="34" rx="17" fill="var(--accent)"/>'
            f'<text x="{130 + i * 230}" y="212" text-anchor="middle" font-size="13" font-weight="700" fill="#fff">{b}</text>'
            for i, (t1, t2, b) in enumerate([('Santé et revenu :', '45 min pour comprendre', 'Je m’inscris'),
                                             ('Coach ou thérapeute ?', 'Le test pour vos clients', 'En savoir plus'),
                                             ('75 ans, en forme,', 'et partenaire Eqology', 'Rejoindre l’équipe')]))), 'Trois exemples de stories sponsorisées')

# 5. Le site
s_site = svg(720, 240, (
    boite(250, 10, 220, 56, 'Votre site', 'eqology-omega3', 'var(--pale)', 'var(--principale)')
    + fleche(330, 68, 190, 108) + fleche(390, 68, 530, 108)
    + boite(40, 110, 300, 80, 'Rejoindre l’équipe', 'là où mènent les publicités', 'var(--principale)', 'var(--principale)', '#fff')
    + boite(380, 110, 300, 80, 'La boutique', 'toute la gamme Eqology')
    + '<text x="190" y="222" text-anchor="middle" font-size="13" fill="var(--encre-2)">formulaire, puis votre appel</text>'
    + '<text x="530" y="222" text-anchor="middle" font-size="13" fill="var(--encre-2)">« Commander » ouvre Eqology à votre nom</text>'), 'Deux portes sur le site')

# 6. Vous et nous
s_roles = svg(720, 250, (
    boite(20, 10, 320, 50, 'Ce que vous faites', '', 'var(--principale)', 'var(--principale)', '#fff')
    + boite(380, 10, 320, 50, 'Ce qui tourne sans vous', '', 'var(--pale)', 'var(--accent)')
    + ''.join(boite(20, 72 + i * 58, 320, 48, t) for i, t in enumerate(['Rappeler les inscrits', 'Inviter à la visio', 'Valider les publicités, une fois']))
    + ''.join(boite(380, 72 + i * 58, 320, 48, t) for i, t in enumerate(['Le site et la boutique', 'Les publicités, chaque jour', 'Les e-mails de relance et le bilan']))), 'Qui fait quoi')

# 7. Calendrier
jalons = [('Ven. 20/11', 'devis signé, 2 700 € réglés'), ('Lun. 23/11', 'site en ligne'), ('Mer. 25/11', 'publicités lancées'),
          ('Fin décembre', 'premier bilan'), ('Janvier', 'on garde ce qui marche')]
c = '<line x1="40" y1="70" x2="690" y2="70" stroke="var(--trait)" stroke-width="4"/>'
for i, (t, s) in enumerate(jalons):
    x = 60 + i * 150
    c += f'<circle cx="{x}" cy="70" r="13" fill="{"var(--principale)" if i == 3 else "var(--accent)"}"/>'
    c += f'<text x="{x}" y="38" text-anchor="middle" font-size="15" font-weight="700" fill="var(--encre)">{t}</text>'
    for k, ligne in enumerate(s.split(', ')):
        c += f'<text x="{x}" y="{106 + k * 19}" text-anchor="middle" font-size="13" fill="var(--encre-2)">{ligne}</text>'
s_cal = svg(740, 160, c, 'Le calendrier des deux premiers mois')

TABLE_REF = cours.table(['Référence', 'Ce qu’elle fait', 'Ce que nous en gardons'], [
    ['Boost Your Health (Pays-Bas)', 'Un site à deux portes, un appel gratuit de 15 minutes, des professionnels recrutés', 'Les deux portes, le rendez-vous, la cible des pros'],
    ['L’équipe Eqology de Sicile', '31 publicités en 7 mois pour remplir des soirées d’information', 'La publicité qui remplit une réunion'],
    ['Robert Kontriner', 'La page partenaire Eqology à son nom', 'La boutique à votre nom, sans stock'],
    ['Falko Krismayr', 'Le recrutement en face à face, Instagram pour l’image', 'Le contact humain au bout du parcours'],
    ['Le livre « Oméga-3, le verdict de la science »', 'Il aborde les professionnels par la science', 'Parler science aux pros, jamais business d’entrée'],
    ['Norway Omega, IM8', 'Des marques qui vendent en ligne avec des stories sponsorisées', 'Le format story, des visuels soignés'],
])

cfg = dict(
    onglet='Votre stratégie Eqology',
    menu_titre='Votre stratégie Eqology',
    oeil='Stratégie · Yves Coignard · 16 novembre 2026',
    titre='Trouver des partenaires Eqology grâce à Instagram et Facebook',
    sous=('Nous avons étudié les distributeurs que vous nous avez envoyés, leurs sites et leurs publicités. '
          'Voici ce qui marche chez eux, et comment nous allons l’appliquer pour vous, étape par étape.'),
    minutes=9, logo=LOGO, marque='Heyfuture', charte=charte, cle='yves-strategie',
    essentiel=[
        'Le chiffre se fait en recrutant des partenaires qui ont déjà des clients. Des publicités Instagram et Facebook, chaque jour, les invitent à une visio et à un appel avec vous.',
        'Vous n’avez qu’une chose à faire : rappeler les personnes intéressées. Le site, les publicités et les relances tournent sans vous.',
        'Le site sera en ligne lundi 23 novembre, les publicités démarreront mercredi 25 novembre, et le premier bilan arrivera fin décembre.',
    ],
    decision='Pouvez-vous signer le devis et régler les deux premières factures (2 700 € TTC) d’ici vendredi 20 novembre, pour tenir ces dates ?',
    chapitres=[
        dict(id='references', menu='Vos références', q='Qu’avons-nous appris de vos références ?',
             reponse='Ceux qui réussissent recrutent des gens qui ont déjà des clients. Ils ne vendent presque jamais l’huile un flacon à la fois.',
             schema=s_ref, legende='À gauche, une vente. À droite, une professionnelle recrutée, dont les clients commandent chaque mois.',
             analogie='C’est comme un verger. On ne compte pas les pommes une à une : on plante des arbres qui en donnent chaque année.',
             points=[
                 ('Boost Your Health, aux Pays-Bas', 'Leur site demande « Où voulez-vous commencer ? » : la santé ou l’activité. Tout mène à un appel gratuit de 15 minutes. Leurs témoignages viennent de coachs et de thérapeutes qu’ils ont recrutés.'),
                 ('L’équipe Eqology de Sicile', 'Elle a diffusé 31 publicités pendant 7 mois pour remplir ses soirées d’information. Personne ne paie aussi longtemps une publicité qui ne rapporte rien.'),
                 ('Ce qui ne marche pas', 'Les publicités « -25 % » qui renvoient directement vers la boutique ont été arrêtées au bout de cinq semaines.'),
             ],
             retenir='La publicité sert à faire venir des gens à une rencontre, pas à vendre un flacon.',
             fond_titre='Le détail de vos références', fond=TABLE_REF),
        dict(id='publics', menu='Qui chercher', q='Qui allons-nous chercher ?',
             reponse='Deux publics : des personnes qui cherchent un complément de revenu, et des professionnels qui ont déjà une clientèle.',
             schema=s_publics, legende='Deux messages différents, qui mènent au même endroit : votre appel.',
             analogie='C’est comme pêcher avec deux lignes : l’une ramène beaucoup de petits poissons, l’autre moins de prises, mais bien plus grosses.',
             points=[
                 ('Le grand public', 'Des retraités et des actifs qui veulent un revenu d’appoint. Ils ont du temps et un entourage à qui en parler.'),
                 ('Les professionnels', 'Des coachs sportifs, des salles de sport, des diététiciennes, des kinés, des esthéticiennes. Une seule recrue peut amener des dizaines de clients.'),
                 ('Votre histoire', 'À 75 ans, en forme, vous êtes la meilleure preuve. Une courte vidéo de vous parlera à beaucoup de monde.'),
             ],
             retenir='On commence par les coachs, les salles de sport et les diététiciennes, et par le grand public.',
             glossaire=[('un complément de revenu', 'Un revenu en plus de la retraite ou du salaire, en quelques heures par semaine.')]),
        dict(id='parcours', menu='Le parcours', q='Comment une personne devient-elle partenaire ?',
             reponse='Elle voit une publicité, s’inscrit en laissant son téléphone, vous l’appelez, puis elle assiste à une présentation.',
             schema=s_parcours, legende='Six étapes, de la publicité au démarrage. Votre appel est au centre.',
             analogie='C’est comme une journée portes ouvertes : l’affiche fait venir les visiteurs, et c’est la discussion sur place qui les décide.',
             points=[
                 ('La page « Rejoindre l’équipe »', 'Elle explique l’activité simplement : qui vous êtes, pour qui c’est fait, comment on démarre.'),
                 ('Votre appel', 'Vous recevez chaque contact par SMS ou WhatsApp, avec son nom et son numéro. Il suffit de rappeler sous 48 heures.'),
                 ('La visio de présentation', 'Elle est assurée par Eqology ou par votre parrain. Vous n’avez rien à préparer.'),
             ],
             retenir='Votre seul rôle dans ce parcours : rappeler les personnes intéressées.',
             glossaire=[('une visio', 'Une réunion par vidéo sur ordinateur ou téléphone, comme un appel avec l’image.'),
                        ('votre parrain', 'La personne qui vous a fait entrer chez Eqology et qui organise souvent des présentations pour son équipe.')]),
        dict(id='pubs', menu='Les publicités', q='À quoi ressembleront les publicités ?',
             reponse='Des stories et des publications sponsorisées, qui tournent chaque jour sur Instagram et Facebook.',
             schema=s_pubs, legende='Trois exemples de messages. Nous en testerons plusieurs et garderons les meilleurs.',
             analogie='C’est comme une affiche dans la rue, sauf qu’elle ne s’affiche que devant les personnes susceptibles d’être intéressées.',
             points=[
                 ('Le budget', '30 € par jour, payés directement à Meta par carte, soit environ 900 € par mois.'),
                 ('La durée', 'Un mois minimum avant le premier bilan, deux mois de préférence pour bien régler les publicités.'),
                 ('Les règles', 'Les publicités n’utilisent que les bienfaits des oméga-3 autorisés par l’Europe. Pas de promesse de guérison, pas de promesse de revenu chiffrée.'),
             ],
             retenir='On teste plusieurs messages, on mesure les inscriptions, et on garde ce qui marche.',
             glossaire=[('une story sponsorisée', 'Une image ou une courte vidéo plein écran, payée pour apparaître chez des personnes choisies.'),
                        ('Meta', 'L’entreprise qui possède Instagram et Facebook.')]),
        dict(id='site', menu='Le site', q='À quoi servira le nouveau site ?',
             reponse='Il a deux portes : « Rejoindre l’équipe », où mènent les publicités, et une boutique avec toute la gamme Eqology.',
             schema=s_site, legende='Les publicités mènent à la page « Rejoindre l’équipe ». La boutique rassure et permet de commander.',
             analogie='C’est comme une vitrine de magasin avec une porte « recrutement » : la vitrine montre le sérieux, la porte fait entrer les futurs partenaires.',
             points=[
                 ('Rejoindre l’équipe', 'La page principale : votre histoire, l’activité, les étapes et le formulaire.'),
                 ('La boutique', 'Les produits présentés en français. Le bouton « Commander » ouvre le site Eqology à votre nom : chaque commande vous revient.'),
                 ('Rien à gérer', 'Eqology s’occupe du paiement, de la livraison et du service client. Vous n’avez ni stock ni colis.'),
             ],
             retenir='La page équipe recrute, la boutique rassure et encaisse les commandes à votre nom.'),
        dict(id='roles', menu='Votre rôle', q='Qu’aurez-vous à faire, concrètement ?',
             reponse='Rappeler les personnes intéressées et les inviter à la visio. Tout le reste est pris en charge.',
             schema=s_roles, legende='À gauche, votre part. À droite, ce qui tourne sans vous.',
             analogie='C’est comme un restaurant : nous faisons venir les clients en salle, vous les accueillez à table.',
             points=[
                 ('Ce que nous préparons', 'Le site, les comptes Instagram et Facebook, les publicités, les e-mails de relance et le suivi des chiffres.'),
                 ('Ce que vous faites', 'Rappeler chaque contact reçu, inviter à la visio, valider les publicités une première fois.'),
                 ('Ce dont nous avons besoin', 'Votre identifiant de partenaire Eqology, le nom de votre parrain et ses dates de visio, votre préférence entre SMS et WhatsApp, et dix minutes pour filmer une courte vidéo de vous.'),
             ],
             retenir='Vous n’avez aucun outil à manipuler : les contacts arrivent tout prêts sur votre téléphone.'),
        dict(id='lancement', menu='Dates et règlement', q='Quand lance-t-on, et comment se passe le règlement ?',
             reponse='Le site sera en ligne lundi 23 novembre et les publicités démarreront mercredi 25 novembre.',
             schema=s_cal, legende='De la signature au premier bilan.',
             analogie='C’est comme régler la radio : on tourne le bouton quelques jours, puis le son devient clair.',
             points=[
                 ('Pour tenir ces dates', 'Le devis signé et les deux premières factures réglées d’ici vendredi 20 novembre, soit 2 700 € TTC.'),
                 ('Ce que l’on mesure', 'Le nombre d’inscrits, le coût d’un inscrit, le nombre d’appels et de partenaires qui démarrent.'),
                 ('Le premier bilan', 'Fin décembre, après un mois de publicités, nous vous montrons ces chiffres et ce que nous changeons.'),
             ],
             retenir='Signature cette semaine, site lundi 23/11, publicités mercredi 25/11, premier bilan fin décembre.',
             fond_titre='Le devis, les factures et l’échéancier',
             fond=(cours.table(['Quand', 'Quoi', 'HT', 'TTC'], [
                 ['À la signature', 'Facture 1004 : lancement des publicités Meta, payé d’avance', '1 500 €', '1 800 €'],
                 ['À la signature', 'Facture 1005 : acompte de 50 % sur le site', '750 €', '900 €'],
                 ['Lundi 23/11, mise en ligne du site', 'Solde de 50 % sur le site', '750 €', '900 €'],
                 ['<b>Total du devis</b>', '<b>Devis PROP-2026-1116-ZENCO</b>', '<b>3 000 €</b>', '<b>3 600 €</b>'],
             ])
                   + '<p>Le site e-commerce vaut 3 000 € HT. Comme vous avez déjà réglé la première version, il vous est facturé 1 500 € HT.</p>'
                   + '<p><b>Le budget publicitaire</b> se paie à part, directement à Meta par carte : 30 € par jour, soit environ 900 € par mois.</p>'
                   + '<p><b>Après le premier mois</b>, le pilotage des publicités est proposé à 500 € HT par mois, sans engagement.</p>'
                   + '<p>Règlement par virement à TAM LABS, la société qui porte Heyfuture. Les coordonnées bancaires figurent sur chaque facture.</p>'
                   + '<p class="docs"><a href="devis.pdf">Le devis</a> · <a href="facture-1004.pdf">La facture 1004</a> · <a href="facture-1005.pdf">La facture 1005</a></p>')),
    ],
    pied='Heyfuture · Préparé par Damien Tamazout pour Yves Coignard, le 16 novembre 2026. Sources : vos captures, les sites et les publicités de vos références, consultés le 16/11/2026.',
)

html = cours.page(cfg)
# Vouvoiement : le gabarit tutoie dans ses textes fixes
html = html.replace('Ce qu\'on te demande', 'Ce que nous vous demandons').replace('Fais glisser le schéma', 'Faites glisser le schéma')
# Les polices Heyfuture
html = html.replace('<style>', '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" '
                    'href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700&family=Sora:wght@600;700&display=swap"><style>.docs a{font-weight:700;color:var(--principale)}.tab td:nth-last-child(-n+2),.tab th:nth-last-child(-n+2){white-space:nowrap}', 1)
open(os.path.join(ICI, 'strategie-yves.html'), 'w').write(html)
print('ok')
