# -*- coding: utf-8 -*-
"""Guide pour Yves (27/11/2026) : ajouter sa carte bancaire au compte publicitaire « YAC – Eqology Yves » (1115842077938719).
Reprend le dessin d'écran et la mise en page de tuto_meta.py.  python3 -I mission/guide_carte.py  →  ~/Downloads/Guide carte bancaire Meta - Yves.pdf"""
import os, subprocess

ICI = os.path.dirname(os.path.abspath(__file__))
_src = open(os.path.join(ICI, 'tuto_meta.py'), encoding='utf-8').read()
exec(_src.split('ETAPES = [')[0])                                   # ecran(), champ(), MENU, LOGO, TEL
exec('CSS = ' + _src.split('CSS = ', 1)[1].split("'''", 2)[0] + "'''" + _src.split('CSS = ', 1)[1].split("'''", 2)[1] + "'''")

SORTIE = os.path.expanduser('~/Downloads/Guide carte bancaire Meta - Yves.pdf')
LIEN = 'business.facebook.com/billing_hub/payment_settings?asset_id=1115842077938719'
COMPTE = 'YAC – Eqology Yves'

ETAPES = [
    dict(t='Ouvrir la page des paiements',
         p=['Sur votre ordinateur, ouvrez Google Chrome, là où vous êtes connecté à Facebook.',
            f'Tapez cette adresse en haut, puis appuyez sur Entrée :<br><b>{LIEN}</b>',
            f'En haut de la page, vérifiez que le compte affiché est bien <b>« {COMPTE} »</b>.'],
         e=ecran('business.facebook.com/billing_hub', 'Paramètres de paiement', menu=MENU, actif='Facturation',
                 contenu=f'<text x="X0" y="105" font-size="14" fill="#444">Compte publicitaire : {COMPTE}</text>'
                         '<text x="X0" y="130" font-size="14" fill="#444">Aucun moyen de paiement enregistré.</text>',
                 cible=(190, 170, 260, 40, 'Ajouter un moyen de paiement'))),
    dict(t='Cliquer sur « Ajouter un moyen de paiement »',
         p=['Cliquez sur le bouton bleu <b>« Ajouter un moyen de paiement »</b>.',
            'Meta vous propose plusieurs choix : prenez <b>« Carte de crédit ou de débit »</b>, puis <b>« Suivant »</b>.'],
         e=ecran('business.facebook.com/billing_hub', 'Ajouter un moyen de paiement',
                 contenu='<circle cx="32" cy="104" r="8" fill="#1877F2"/><text x="48" y="109" font-size="14" fill="#1A1A1A">Carte de crédit ou de débit</text>'
                         '<circle cx="32" cy="138" r="8" fill="none" stroke="#999"/><text x="48" y="143" font-size="14" fill="#777">PayPal</text>',
                 cible=(20, 190, 130, 40, 'Suivant'))),
    dict(t='Taper les informations de votre carte',
         p=['<b>Nom sur la carte</b> : comme il est écrit sur votre carte.',
            '<b>Numéro de carte</b> : les 16 chiffres.',
            '<b>Date d’expiration</b> (MM/AA) et <b>code de sécurité</b> : les 3 chiffres au dos.',
            'Puis cliquez sur <b>« Enregistrer »</b>.'],
         e=ecran('business.facebook.com/billing_hub', 'Carte de crédit ou de débit',
                 contenu=champ(20, 90, 'Nom sur la carte', 'Yves Coignard', 300) + champ(20, 135, 'Numéro de carte', '•••• •••• •••• ••••', 300)
                         + champ(20, 180, 'MM/AA', '••/••', 120) + champ(160, 180, 'Code de sécurité', '•••', 160),
                 cible=(470, 240, 140, 40, 'Enregistrer'))),
    dict(t='Valider avec votre banque, si elle le demande',
         p=['Votre banque peut vous demander de confirmer : un code reçu par SMS, ou une validation dans son application sur votre téléphone.',
            'Faites-le comme pour un achat en ligne. C’est votre banque qui vérifie que c’est bien vous.'],
         e=ecran('Votre banque', 'Confirmez votre opération',
                 contenu='<text x="X0" y="105" font-size="14" fill="#444">Un code vous a été envoyé par SMS.</text>' + champ(20, 125, 'Code reçu', '••••••', 200),
                 cible=(20, 200, 130, 40, 'Valider'))),
    dict(t='Vérifier que la carte est bien enregistrée',
         p=['Vous revenez sur la page des paiements : votre carte apparaît, avec ses 4 derniers chiffres.',
            'C’est tout. Envoyez-moi un petit SMS : <b>« Carte ajoutée »</b>.'],
         e=ecran('business.facebook.com/billing_hub', 'Paramètres de paiement', menu=MENU, actif='Facturation',
                 contenu='<rect x="190" y="95" width="400" height="56" rx="8" fill="#F6F5F2" stroke="#DDD"/>'
                         '<text x="206" y="118" font-size="14" font-weight="700" fill="#1A1A1A">Visa •••• 1234</text>'
                         '<text x="206" y="139" font-size="12" fill="#1F5A45">Moyen de paiement principal</text>')),
]


def page_etapes(etapes, debut):
    h = '<div class="page">'
    for i, et in enumerate(etapes):
        h += (f'<div class="etape"><div class="num"><b>{debut + i}</b><h2>{et["t"]}</h2></div><ul>'
              + ''.join(f'<li>{x}</li>' for x in et['p']) + '</ul>' + et.get('e', '') + '</div>')
    return h + f'<div class="pied">Un bouton porte un nom un peu différent ? C’est normal, Meta change souvent ses écrans. Cherchez le mot le plus proche, ou appelez-moi au {TEL}.</div></div>'


couv = (f'<div class="page couv"><div class="logo"><img src="{LOGO}" alt="heyfuture"></div>'
        '<h1>Ajouter votre carte bancaire pour lancer les publicités</h1>'
        '<p class="chapo">Votre compte publicitaire est prêt : page Facebook, réglages, publicités. Il ne manque que votre carte. '
        'Cinq étapes, environ 5 minutes, devant votre ordinateur.</p>'
        '<div class="besoin"><h2>Avant de commencer, ayez sous la main</h2><ul>'
        '<li>un <b>ordinateur</b> où vous êtes connecté à Facebook ;</li>'
        '<li>votre <b>carte bancaire</b> ;</li>'
        '<li>votre <b>téléphone</b>, si votre banque demande une validation.</li></ul></div>'
        '<div class="besoin"><h2>Bon à savoir</h2><ul>'
        '<li>Rien n’est prélevé tant que les publicités ne sont pas lancées.</li>'
        '<li>Le budget prévu est de <b>30 € par jour</b>, soit environ 900 € par mois. Meta prélève au fur et à mesure, jamais plus que ce budget.</li>'
        '<li>L’argent va directement à Meta, il ne passe pas par nous. Vous pouvez tout arrêter à tout moment.</li></ul></div>'
        f'<div class="aide">Vous bloquez à une étape ?<span>Appelez-moi au {TEL} : on le fait ensemble au téléphone.</span></div></div>')

html = ('<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>Guide carte bancaire Meta</title>'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700&family=Sora:wght@600;700&display=swap">'
        f'<style>{CSS}</style></head><body>{couv}'
        + page_etapes(ETAPES[0:2], 1) + page_etapes(ETAPES[2:4], 3) + page_etapes(ETAPES[4:5], 5)
        + '</body></html>')
src = os.path.join(ICI, 'guide-carte.html')
open(src, 'w', encoding='utf-8').write(html)
subprocess.run(['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', '--headless=new', '--disable-gpu', '--no-pdf-header-footer',
                '--virtual-time-budget=8000', f'--print-to-pdf={SORTIE}', 'file://' + src], check=True, capture_output=True)
print(SORTIE)
