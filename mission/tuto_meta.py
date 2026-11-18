# -*- coding: utf-8 -*-
"""Guide pas à pas pour Yves (75 ans, novice) : créer son compte Meta Business, relier sa page Facebook,
créer le compte publicitaire, ajouter sa carte et inviter Damien (damien.growth@gmail.com).
Chaque étape a un dessin simplifié de l'écran, le bouton à cliquer entouré.
Usage : python3 mission/tuto_meta.py  →  ~/Downloads/Guide compte publicitaire Facebook - Yves.pdf"""
import os, base64, subprocess, tempfile

ICI = os.path.dirname(os.path.abspath(__file__))
LOGO = 'data:image/svg+xml;base64,' + base64.b64encode(open(os.path.expanduser('~/Documents/crm-heyfuture/public/assets/heyfuture-logo.svg'), 'rb').read()).decode()
SORTIE = os.path.expanduser('~/Downloads/Guide compte publicitaire Facebook - Yves.pdf')
EMAIL_DAMIEN = 'damien.growth@gmail.com'
TEL = '07 60 55 40 00'


def ecran(url, titre, menu=None, actif=None, contenu='', cible=None):
    """Un écran d'ordinateur dessiné : barre d'adresse, menu à gauche, contenu, bouton cible entouré en jaune."""
    W, H = 640, 300
    s = f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" font-family="Arial, sans-serif">'
    s += f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="12" fill="#fff" stroke="#CFCBC2" stroke-width="2"/>'
    s += '<rect x="1" y="1" width="638" height="36" rx="12" fill="#ECE9E3"/><rect x="1" y="26" width="638" height="11" fill="#ECE9E3"/>'
    s += ''.join(f'<circle cx="{20+i*16}" cy="19" r="5" fill="{c}"/>' for i, c in enumerate(['#E5786D', '#E8C05A', '#7DBF73']))
    s += f'<rect x="80" y="9" width="420" height="20" rx="10" fill="#fff"/><text x="96" y="23" font-size="12" fill="#555">🔒 {url}</text>'
    x0 = 20
    if menu:
        s += '<rect x="1" y="37" width="170" height="262" fill="#F6F5F2"/>'
        for i, m in enumerate(menu):
            y = 66 + i * 30
            if m == actif:
                s += f'<rect x="10" y="{y-17}" width="150" height="26" rx="6" fill="#DCE9E2"/>'
            s += f'<text x="22" y="{y}" font-size="13" fill="#1A1A1A" font-weight="{700 if m == actif else 400}">{m}</text>'
        x0 = 190
    s += f'<text x="{x0}" y="70" font-size="18" font-weight="700" fill="#1A1A1A">{titre}</text>'
    s += contenu.replace('X0', str(x0))
    if cible:
        cx, cy, cw, ch, lib = cible
        s += f'<rect x="{cx}" y="{cy}" width="{cw}" height="{ch}" rx="8" fill="#1877F2"/>'
        s += f'<text x="{cx + cw/2}" y="{cy + ch/2 + 5}" font-size="14" font-weight="700" fill="#fff" text-anchor="middle">{lib}</text>'
        s += f'<rect x="{cx-7}" y="{cy-7}" width="{cw+14}" height="{ch+14}" rx="12" fill="none" stroke="#E4C21B" stroke-width="5"/>'
        if cx + cw + 170 <= W:   # flèche à droite du bouton
            s += f'<path d="M{cx+cw+70},{cy-28} L{cx+cw+14},{cy+4}" stroke="#E4C21B" stroke-width="5" stroke-linecap="round"/>'
            s += f'<path d="M{cx+cw+14},{cy+4} l18,-2 M{cx+cw+14},{cy+4} l4,-17" stroke="#E4C21B" stroke-width="5" stroke-linecap="round"/>'
            s += f'<text x="{cx+cw+74}" y="{cy-30}" font-size="15" font-weight="700" fill="#B8860B">Cliquez ici</text>'
        else:                     # pas la place : flèche à gauche du bouton
            s += f'<path d="M{cx-70},{cy-28} L{cx-14},{cy+4}" stroke="#E4C21B" stroke-width="5" stroke-linecap="round"/>'
            s += f'<path d="M{cx-14},{cy+4} l-18,-2 M{cx-14},{cy+4} l-4,-17" stroke="#E4C21B" stroke-width="5" stroke-linecap="round"/>'
            s += f'<text x="{cx-74}" y="{cy-30}" font-size="15" font-weight="700" fill="#B8860B" text-anchor="end">Cliquez ici</text>'
    return s + '</svg>'


def champ(x, y, lib, val, w=330):
    return (f'<text x="{x}" y="{y}" font-size="12" fill="#666">{lib}</text>'
            f'<rect x="{x}" y="{y+6}" width="{w}" height="28" rx="6" fill="#fff" stroke="#BDB8AE"/>'
            f'<text x="{x+10}" y="{y+25}" font-size="14" fill="#1A1A1A">{val}</text>')


MENU = ['Accueil', 'Paramètres', 'Comptes', 'Utilisateurs', 'Facturation']

ETAPES = [
    dict(t='Ouvrir le site de Meta Business',
         p=['Sur votre ordinateur, ouvrez Google Chrome (ou Safari).',
            'Tapez cette adresse en haut, puis appuyez sur Entrée : <b>business.facebook.com</b>',
            'Si on vous le demande, connectez-vous avec votre compte Facebook habituel (votre e-mail et votre mot de passe Facebook).'],
         e=ecran('business.facebook.com', 'Meta Business Suite',
                 contenu='<text x="X0" y="110" font-size="14" fill="#444">Gérez votre entreprise sur Facebook et Instagram</text>',
                 cible=(20, 150, 230, 44, 'Se connecter avec Facebook'))),
    dict(t='Créer le compte de votre entreprise',
         p=['Cliquez sur le bouton <b>« Créer un compte »</b>. Il peut aussi s’appeler <b>« Créer un portefeuille business »</b>.',
            'S’il n’apparaît pas tout de suite, cliquez sur le petit menu en haut à gauche (votre nom ou une flèche) : il s’y trouve.'],
         e=ecran('business.facebook.com', 'Bienvenue', contenu='<text x="X0" y="110" font-size="14" fill="#444">Vous n’avez pas encore de compte d’entreprise.</text>',
                 cible=(20, 150, 200, 44, 'Créer un compte'))),
    dict(t='Remplir les trois cases',
         p=['<b>Nom de l’entreprise</b> : ZENCO',
            '<b>Votre nom</b> : Yves Coignard',
            '<b>E-mail professionnel</b> : zenco.coignard@gmail.com',
            'Puis cliquez sur <b>« Envoyer »</b> (ou « Créer »).'],
         e=ecran('business.facebook.com', 'Créer un portefeuille business',
                 contenu=champ(20, 95, 'Nom de l’entreprise', 'ZENCO') + champ(20, 140, 'Votre nom', 'Yves Coignard') + champ(20, 185, 'E-mail professionnel', 'zenco.coignard@gmail.com'),
                 cible=(390, 230, 130, 40, 'Envoyer'))),
    dict(t='Confirmer votre e-mail',
         p=['Meta vous envoie un e-mail sur zenco.coignard@gmail.com.',
            'Ouvrez votre messagerie, trouvez l’e-mail de Meta (« Confirmez votre adresse e-mail ») et cliquez sur le bouton bleu <b>« Confirmer »</b>.',
            'Pas d’e-mail au bout de 5 minutes ? Regardez dans le dossier « Spam » ou « Courrier indésirable ».'],
         e=ecran('mail.google.com', 'Meta · Confirmez votre adresse e-mail',
                 contenu='<text x="X0" y="110" font-size="14" fill="#444">Bonjour Yves, confirmez votre adresse pour finir la création.</text>',
                 cible=(20, 150, 160, 44, 'Confirmer'))),
    dict(t='Relier votre page Facebook',
         p=['Vous avez déjà créé votre page Facebook : il faut maintenant la relier à votre compte d’entreprise.',
            'Dans le menu à gauche, cliquez sur la <b>roue dentée « Paramètres »</b>, puis sur <b>« Comptes »</b>, puis sur <b>« Pages »</b>.',
            'Cliquez sur <b>« Ajouter »</b>, puis sur <b>« Ajouter une Page existante »</b>, et choisissez votre page.'],
         e=ecran('business.facebook.com/settings', 'Pages', menu=MENU, actif='Comptes',
                 contenu='<text x="X0" y="110" font-size="14" fill="#444">Aucune page pour l’instant.</text>',
                 cible=(190, 150, 120, 40, 'Ajouter'))),
    dict(t='Créer le compte publicitaire',
         p=['Toujours dans <b>« Paramètres »</b> puis <b>« Comptes »</b>, cliquez cette fois sur <b>« Comptes publicitaires »</b>.',
            'Cliquez sur <b>« Ajouter »</b>, puis sur <b>« Créer un compte publicitaire »</b>.',
            'Remplissez : nom <b>ZENCO Eqology</b> · fuseau horaire <b>Europe/Paris</b> · devise <b>Euro (EUR)</b>.',
            'Quand Meta demande pour qui est ce compte, choisissez <b>« Mon entreprise »</b>, puis <b>« Créer »</b>.'],
         e=ecran('business.facebook.com/settings', 'Créer un compte publicitaire', menu=MENU, actif='Comptes',
                 contenu=champ(190, 95, 'Nom du compte', 'ZENCO Eqology', 260) + champ(190, 140, 'Fuseau horaire', 'Europe/Paris', 260) + champ(190, 185, 'Devise', 'Euro (EUR)', 260),
                 cible=(480, 235, 110, 40, 'Créer'))),
    dict(t='Ajouter votre carte bancaire',
         p=['Le budget des publicités (30 € par jour) sera prélevé sur votre carte, directement par Meta.',
            'Dans le menu, cliquez sur <b>« Facturation »</b> (ou « Facturation et paiements »), puis sur <b>« Ajouter un moyen de paiement »</b>.',
            'Entrez les numéros de votre carte, sa date d’expiration et le code à 3 chiffres au dos, puis <b>« Enregistrer »</b>.'],
         e=ecran('business.facebook.com/billing', 'Moyens de paiement', menu=MENU, actif='Facturation',
                 contenu='<text x="X0" y="110" font-size="14" fill="#444">Aucun moyen de paiement enregistré.</text>',
                 cible=(190, 150, 260, 40, 'Ajouter un moyen de paiement'))),
    dict(t='M’inviter pour que je m’occupe du reste',
         p=['Dans le menu, cliquez sur <b>« Utilisateurs »</b>, puis sur <b>« Personnes »</b>, puis sur <b>« Ajouter »</b> (ou « Inviter des personnes »).',
            f'Tapez mon adresse : <b>{EMAIL_DAMIEN}</b>',
            'Choisissez <b>« Contrôle total »</b> (parfois appelé « Administrateur »).',
            'Si Meta vous propose de choisir des éléments, cochez <b>votre page Facebook</b> et <b>votre compte publicitaire</b>, avec l’accès complet.',
            'Cliquez sur <b>« Envoyer l’invitation »</b>.'],
         e=ecran('business.facebook.com/settings', 'Inviter des personnes', menu=MENU, actif='Utilisateurs',
                 contenu=champ(190, 95, 'Adresse e-mail', EMAIL_DAMIEN, 300)
                         + '<rect x="190" y="150" width="18" height="18" rx="4" fill="#1877F2"/><text x="194" y="164" font-size="14" fill="#fff">✓</text>'
                         + '<text x="216" y="164" font-size="14" fill="#1A1A1A">Contrôle total</text>',
                 cible=(190, 210, 200, 40, 'Envoyer l’invitation'))),
]

CSS = '''
@page{size:A4;margin:0}*{box-sizing:border-box}
html,body{margin:0;background:#F4F2EE}
body{font:12.5pt/1.5 "Plus Jakarta Sans",Arial,sans-serif;color:#1A1A1A;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{width:210mm;height:296mm;overflow:hidden;padding:14mm 15mm;display:flex;flex-direction:column;gap:6mm;page-break-after:always}
.page:last-child{page-break-after:auto}
h1,h2{font-family:Sora,Arial,sans-serif;margin:0;letter-spacing:-.01em}
.couv{background:#0F2E24;color:#F4F2EE}
.couv .logo{background:#fff;border-radius:10px;padding:8px 12px;align-self:flex-start}.couv .logo img{height:18px;display:block}
.couv h1{font-size:30pt;line-height:1.15;margin-top:18mm}
.couv .chapo{font-size:15pt;color:#D3E4DA;line-height:1.5}
.besoin{background:#F4F2EE;color:#1A1A1A;border-radius:14px;padding:16px 20px}
.besoin h2{font-size:15pt;margin-bottom:8px}
.besoin ul{margin:0;padding-left:22px}.besoin li{margin:6px 0}
.aide{background:#E4F73B;color:#1A1A1A;border-radius:14px;padding:14px 20px;font-size:14pt;font-weight:700;margin-top:auto}
.aide span{display:block;font-weight:400;font-size:12pt}
.etape{background:#fff;border:1px solid #E5E2DB;border-radius:16px;padding:14px 18px;display:flex;flex-direction:column;gap:8px}
.num{display:flex;align-items:center;gap:12px}
.num b{font-family:Sora,Arial,sans-serif;width:40px;height:40px;border-radius:50%;background:#1F5A45;color:#fff;display:grid;place-items:center;font-size:17pt;flex:none}
.num h2{font-size:16pt}
.etape ul{margin:0;padding-left:22px}.etape li{margin:4px 0}
.etape svg{width:100%;height:auto;display:block}
.fin{background:#1F5A45;color:#fff;border-radius:16px;padding:18px 22px}
.fin h2{font-size:18pt;margin-bottom:6px}
.pied{font-size:9pt;color:#6E6B65;margin-top:auto}
'''


def page_etapes(etapes, debut):
    h = '<div class="page">'
    for i, et in enumerate(etapes):
        h += (f'<div class="etape"><div class="num"><b>{debut + i}</b><h2>{et["t"]}</h2></div><ul>'
              + ''.join(f'<li>{x}</li>' for x in et['p']) + f'</ul>{et["e"]}</div>')
    return h + f'<div class="pied">Un bouton porte un nom un peu différent ? C’est normal, Meta change souvent ses écrans. Cherchez le mot le plus proche, ou appelez-moi au {TEL}.</div></div>'


couv = (f'<div class="page couv"><div class="logo"><img src="{LOGO}" alt="heyfuture"></div>'
        '<h1>Créer votre compte publicitaire Facebook, pas à pas</h1>'
        '<p class="chapo">Un guide en 8 étapes, à suivre tranquillement devant votre ordinateur. Comptez environ 15 minutes. '
        'À la fin, vos publicités pourront être mises en route.</p>'
        '<div class="besoin"><h2>Avant de commencer, ayez sous la main</h2><ul>'
        '<li>un <b>ordinateur</b> (c’est plus simple que le téléphone) ;</li>'
        '<li>votre <b>compte Facebook</b> : votre e-mail et votre mot de passe ;</li>'
        '<li>votre <b>carte bancaire</b> ;</li>'
        '<li>l’accès à votre <b>messagerie</b> zenco.coignard@gmail.com.</li></ul></div>'
        f'<div class="aide">Vous bloquez à une étape ?<span>Appelez-moi au {TEL} : on le fait ensemble au téléphone, en dix minutes.</span></div></div>')

fin = ('<div class="page"><div class="fin"><h2>C’est terminé, bravo !</h2>'
       '<p>Envoyez-moi juste un petit SMS : « C’est fait ». Je reçois votre invitation, je l’accepte, et je m’occupe de tout le reste : '
       'la mise en service de votre agent Ads et le lien avec votre site.</p></div>'
       '<div class="besoin" style="background:#fff;border:1px solid #E5E2DB"><h2>Récapitulatif</h2><ul>'
       '<li>Compte d’entreprise : <b>ZENCO</b></li>'
       '<li>Page Facebook : <b>reliée</b></li>'
       '<li>Compte publicitaire : <b>ZENCO Eqology</b>, Europe/Paris, Euro</li>'
       '<li>Carte bancaire : <b>ajoutée</b></li>'
       f'<li>Invitation envoyée à : <b>{EMAIL_DAMIEN}</b>, contrôle total</li></ul></div>'
       '<div class="besoin" style="background:#fff;border:1px solid #E5E2DB"><h2>Bon à savoir</h2><ul>'
       '<li>Rien n’est dépensé tant que les publicités ne sont pas lancées.</li>'
       '<li>Le budget est prélevé par Meta, sur votre carte : il ne passe pas par nous.</li>'
       '<li>Vous gardez la main : le compte est à votre nom, vous pouvez tout voir et tout arrêter à tout moment.</li></ul></div>'
       f'<div class="aide">Une question ?<span>{TEL} · damien.growth@gmail.com</span></div></div>')

html = ('<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>Guide compte publicitaire Facebook</title>'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700&family=Sora:wght@600;700&display=swap">'
        f'<style>{CSS}</style></head><body>{couv}'
        + page_etapes(ETAPES[0:2], 1) + page_etapes(ETAPES[2:4], 3) + ''.join(page_etapes(ETAPES[i:i+1], i + 1) for i in range(4, 8))
        + fin + '</body></html>')
src = os.path.join(ICI, 'tuto-meta.html')
open(src, 'w', encoding='utf-8').write(html)
subprocess.run(['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', '--headless=new', '--disable-gpu', '--no-pdf-header-footer',
                '--virtual-time-budget=8000', f'--print-to-pdf={SORTIE}', 'file://' + src], check=True, capture_output=True)
print(SORTIE)
