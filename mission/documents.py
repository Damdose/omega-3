# -*- coding: utf-8 -*-
"""Devis et facture d'acompte TAM LABS pour ZENCO SAS (Yves Coignard), mission V2 du 16/11/2026.
Mise en page calquée sur les premiers documents TAM LABS (devis PROP-2026-014-V2, facture 1001 de Gray Laser) :
fond beige, logo heyfuture, Sora + Plus Jakarta Sans, cartes blanches, total TTC sur pavé vert.
Damien, 16/11 : une seule facture d'acompte de 50 % sur le total, solde de 50 % à la mise en ligne.
Usage : python3 mission/documents.py  →  PDF dans ~/Downloads (Chrome headless)."""
import os, subprocess, tempfile, base64

DATE = '16/11/2026'
VALIDITE = '16/12/2026'
DEVIS = 'PROP-2026-1116-ZENCO'
FACTURE = '1004'          # suite de la numérotation TAM LABS (1001, 1002, 1003 en base le 16/11)
ACOMPTE_PCT = 50

ASSETS = os.path.expanduser('~/Documents/crm-heyfuture/public/assets')
LOGO = 'data:image/svg+xml;base64,' + base64.b64encode(open(f'{ASSETS}/heyfuture-logo.svg', 'rb').read()).decode()
LOGO_CLAIR = 'data:image/svg+xml;base64,' + base64.b64encode(open(f'{ASSETS}/heyfuture-logo-clair.svg', 'rb').read()).decode()

EMETTEUR = ['SASU au capital de 1 000 €', '138 avenue Victor Hugo, 75116 Paris', 'RCS Paris 131 975 054',
            'SIRET 131 975 054 00019 · NAF 6201Z', 'TVA FR80131975054']
CLIENT = ['29 boulevard de la Muette', '95140 Garges-lès-Gonesse', '<span class="manque">SIREN à compléter</span>',
          'À l’attention de M. Yves Coignard, co-président']

LIGNES = [
    ('1. Solution agent Ads Meta : développement, paramétrage et mise en service',
     'Développement et paramétrage de l’agent logiciel pour ZENCO, connexion technique au compte publicitaire Meta, '
     'au site et au suivi des conversions (pixel et API de conversions), mise en service.', 1500),
    ('2. Conception et développement du site e-commerce',
     'Page « Rejoindre l’équipe » avec formulaire et prise de rendez-vous en ligne, catalogue produits avec liens partenaire, '
     'alertes automatiques des contacts, relances e-mail automatiques, hébergement 12 mois.', 3000),
    ('3. Remise commerciale', 'Remise accordée sur la conception du site.', -1500),
]
PERIODE = 'du 16/11/2026 au 25/11/2026 (mise en service)'
TOTAL_HT = sum(l[2] for l in LIGNES)
ACOMPTE_HT = TOTAL_HT * ACOMPTE_PCT / 100

CSS = '''
@page{size:A4;margin:0}
*{box-sizing:border-box}
html,body{margin:0;background:#F4F2EE}
body{font:9.4pt/1.45 "Plus Jakarta Sans",Arial,sans-serif;color:#1A1A1A;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{width:210mm;height:296mm;overflow:hidden;padding:13mm 13mm 0;position:relative;display:flex;flex-direction:column;gap:3.4mm}
.page--devis{padding-top:0;gap:2.2mm}
b,strong{font-weight:700}
.logo{height:17px;display:block}
.contact{font-size:8pt;color:#5E5B55;margin-top:9px;line-height:1.55}
.tete{display:flex;justify-content:space-between;align-items:flex-end;padding-bottom:9mm;border-bottom:1px solid #DDD9D1;margin-bottom:2mm}
.tete h1{font-family:Sora,Arial,sans-serif;font-weight:700;font-size:21pt;letter-spacing:-.02em;margin:0}
.bandeau{background:#0F2E24;color:#F4F2EE;margin:0 -13mm 3mm;padding:8mm 13mm 6mm;display:flex;justify-content:space-between;align-items:center}
.bandeau .contact{color:#C9D6CF}
.pastille{background:#E4F73B;color:#1A1A1A;font-family:Sora,Arial,sans-serif;font-weight:700;font-size:20pt;padding:4px 16px;border-radius:9px;transform:rotate(-4deg);box-shadow:3px 3px 0 #1A1A1A}
.carte{background:#fff;border:1px solid #E5E2DB;border-radius:10px;padding:10px 12px}
.carte--pale{background:#D3E4DA;border-color:#C2D8CB}
.k{font-family:Sora,Arial,sans-serif;font-weight:700;font-size:6.6pt;letter-spacing:.14em;text-transform:uppercase;color:#5E5B55;margin-bottom:5px}
.meta{display:grid;gap:8px}.meta--4{grid-template-columns:repeat(4,1fr)}.meta--3{grid-template-columns:repeat(3,1fr)}
.meta .v{font-family:Sora,Arial,sans-serif;font-weight:600;font-size:9.4pt}
.deux{display:grid;grid-template-columns:1fr 1fr;gap:3mm}
.deux p{margin:0;font-size:8.6pt;line-height:1.55}
.deux p b{font-family:Sora,Arial,sans-serif;font-size:9.6pt;display:block;margin-bottom:1px}
table{width:100%;border-collapse:collapse}
.carte--tab{padding:0;overflow:hidden}
th{font-family:Sora,Arial,sans-serif;font-weight:700;font-size:6.6pt;letter-spacing:.14em;text-transform:uppercase;color:#5E5B55;text-align:left;padding:7px 12px;border-bottom:1px solid #E5E2DB}
td{padding:6px 12px;vertical-align:top;border-bottom:1px solid #EFECE6;font-size:8.8pt}
tr:last-child td{border-bottom:0}
.n{text-align:right;white-space:nowrap}
td .t{font-family:Sora,Arial,sans-serif;font-weight:700;font-size:9pt;display:block}
td .d{display:block;font-size:7.8pt;color:#5E5B55;margin-top:2px;line-height:1.45}
.bas{display:grid;grid-template-columns:1fr 1fr;gap:3mm;align-items:stretch}
.bas--droite{grid-template-columns:1fr 66mm}
.rib p{margin:0;font-size:8.6pt;line-height:1.6}
.total{background:#1F5A45;color:#fff;border-radius:10px;padding:12px 14px;display:flex;flex-direction:column;gap:3px;font-size:8.6pt}
.total div{display:flex;justify-content:space-between}
.total .ttc{border-top:1px solid rgba(255,255,255,.3);margin-top:6px;padding-top:9px;font-family:Sora,Arial,sans-serif;font-weight:700;font-size:15pt}
.note{font-size:8pt;color:#3D3B37;margin:1mm 0 0}
.pied{margin-top:auto;padding:4mm 0 6mm;font-size:6.9pt;color:#6E6B65;line-height:1.55}
.manque{color:#C2410C;font-weight:700}
.signature{display:grid;grid-template-columns:1fr 1fr;gap:3mm}
.signature .carte{height:14mm;font-size:7.8pt;color:#5E5B55}
'''

FONTS = ('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&family=Sora:wght@600;700&display=swap">')
PIED_TXT = ('TAM LABS · SASU au capital de 1 000 € · 138 avenue Victor Hugo, 75116 Paris · RCS Paris 131 975 054 · TVA FR80131975054<br>'
            'Catégorie d’opération : prestation de services. Pas d’escompte pour paiement anticipé. En cas de retard de paiement, une pénalité de 3 fois le taux '
            'd’intérêt légal s’applique, à laquelle s’ajoute une indemnité forfaitaire de 40 € pour frais de recouvrement.')


def euros(x, dec=False):
    s = f'{abs(x):,.2f}' if dec else f'{abs(x):,.0f}'
    s = s.replace(',', ' ').replace('.', ',')
    return ('-' if x < 0 else '') + s + ' €'


def doc(titre, corps):
    return (f'<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>{titre}</title>{FONTS}<style>{CSS}</style></head>'
            f'<body>{corps}</body></html>')


def parties(titre_client, president=False):
    em = EMETTEUR + (['Président : Damien Tamazout'] if president else [])
    return (f'<div class="deux"><div class="carte"><div class="k">Émis par</div><p><b>TAM LABS</b>{"<br>".join(em)}</p></div>'
            f'<div class="carte"><div class="k">{titre_client}</div><p><b>ZENCO SAS</b>{"<br>".join(CLIENT)}</p></div></div>')


def devis():
    tva = TOTAL_HT * 0.2
    lignes = ''.join(f'<tr><td><span class="t">{t}</span><span class="d">{d}</span></td><td class="n">1</td>'
                     f'<td class="n">{euros(p)}</td><td class="n">{euros(p)}</td></tr>' for t, d, p in LIGNES)
    c = '<div class="page page--devis">'
    c += (f'<div class="bandeau"><div><img class="logo" src="{LOGO_CLAIR}" alt="heyfuture">'
          '<div class="contact">heyfuture.fr · 07 60 55 40 00 · damien.tamazout@gmail.com</div></div><div class="pastille">Devis</div></div>')
    c += (f'<div class="carte carte--pale meta meta--3"><div><div class="k">N° de devis</div><div class="v">{DEVIS}</div></div>'
          f'<div><div class="k">Date</div><div class="v">{DATE}</div></div><div><div class="k">Valable jusqu’au</div><div class="v">{VALIDITE}</div></div></div>')
    c += parties('Adressé à')
    c += (f'<div class="carte carte--tab"><table><thead><tr><th>Désignation</th><th class="n">Qté</th><th class="n">P.U. HT</th><th class="n">Total HT</th></tr></thead>'
          f'<tbody>{lignes}</tbody></table></div>')
    c += (f'<div class="bas bas--droite"><div></div><div class="total"><div><span>Total HT</span><span>{euros(TOTAL_HT)}</span></div>'
          f'<div><span>TVA 20 %</span><span>{euros(tva)}</span></div><div class="ttc"><span>Total TTC</span><span>{euros(TOTAL_HT + tva)}</span></div></div></div>')
    c += ('<div class="carte carte--tab"><table><thead><tr><th>Échéancier</th><th>Quoi</th><th class="n">HT</th><th class="n">TTC</th></tr></thead><tbody>'
          f'<tr><td>À la signature</td><td>Acompte de {ACOMPTE_PCT} % (facture {FACTURE})</td><td class="n">{euros(ACOMPTE_HT)}</td><td class="n">{euros(ACOMPTE_HT * 1.2)}</td></tr>'
          f'<tr><td>À la mise en service du site et de l’agent Ads</td><td>Solde de {100 - ACOMPTE_PCT} %</td><td class="n">{euros(TOTAL_HT - ACOMPTE_HT)}</td><td class="n">{euros((TOTAL_HT - ACOMPTE_HT) * 1.2)}</td></tr>'
          '</tbody></table></div>')
    c += ('<div class="carte rib"><div class="k">RIB, règlement par virement</div><p>Titulaire : TAM LABS · Banque : Qonto<br>'
          'IBAN : <b>FR76 1695 8000 0152 9635 4169 030</b> · BIC : <b>QNTOFRP1XXX</b></p></div>')
    c += (f'<p class="note">Période de la prestation : {PERIODE} · Catégorie de l’opération : prestation de services.<br>'
          'Le budget publicitaire se paie directement à Meta par le client : il n’est pas facturé par Tam Labs. '
          'À partir du deuxième mois, en option : abonnement solution agent Ads (licence, hébergement, maintenance), 500 € HT par mois, sans engagement.</p>')
    c += ('<div class="signature"><div class="carte">Pour TAM LABS<br>Damien Tamazout, président</div>'
          '<div class="carte">Pour ZENCO SAS<br>Date, signature et mention « Bon pour accord »</div></div>')
    c += f'<div class="pied">{PIED_TXT}</div></div>'
    return doc(f'Devis {DEVIS}', c)


def facture():
    ht = ACOMPTE_HT; tva = round(ht * 0.2, 2); ttc = ht + tva
    c = '<div class="page">'
    c += (f'<div class="tete"><div><img class="logo" src="{LOGO}" alt="heyfuture"><div class="contact">heyfuture.fr · 07 60 55 40 00<br>damien.tamazout@gmail.com</div></div>'
          '<h1>Facture d’acompte</h1></div>')
    c += (f'<div class="carte meta meta--4"><div><div class="k">N° de facture</div><div class="v">{FACTURE}</div></div>'
          f'<div><div class="k">Émise le</div><div class="v">{DATE}</div></div><div><div class="k">Échéance</div><div class="v">À réception</div></div>'
          f'<div><div class="k">Devis</div><div class="v">{DEVIS}</div></div></div>')
    c += parties('Facturée à', president=True)
    c += ('<div class="carte carte--tab"><table><thead><tr><th>Désignation</th><th class="n">Qté</th><th class="n">P.U. HT</th><th class="n">TVA</th><th class="n">Total HT</th></tr></thead><tbody>'
          f'<tr><td><span class="t">Acompte de {ACOMPTE_PCT} % : solution agent Ads Meta et site e-commerce</span>'
          f'<span class="d">Solution agent Ads Meta, développement, paramétrage et mise en service (1 500 € HT), et conception du site e-commerce (1 500 € HT après remise commerciale), '
          f'devis n° {DEVIS}.</span></td><td class="n">1</td><td class="n">{euros(ht, True)}</td><td class="n">20 %</td><td class="n">{euros(ht, True)}</td></tr>'
          '</tbody></table></div>')
    c += ('<div class="bas"><div class="carte rib"><div class="k">Règlement par virement</div><p>Titulaire : TAM LABS<br>Banque : Qonto<br>'
          'IBAN : <b>FR76 1695 8000 0152 9635 4169 030</b><br>BIC : <b>QNTOFRP1XXX</b></p></div>'
          f'<div class="total"><div><span>Total HT</span><span>{euros(ht, True)}</span></div><div><span>TVA 20 %</span><span>{euros(tva, True)}</span></div>'
          f'<div class="ttc"><span>Total TTC</span><span>{euros(ttc, True)}</span></div></div></div>')
    c += f'<p class="note">Période de la prestation : {PERIODE} · Catégorie de l’opération : prestation de services.<br>Solde de {euros(TOTAL_HT - ht)} HT à la mise en service du site et de l’agent Ads.</p>'
    c += f'<div class="pied">{PIED_TXT}</div></div>'
    return doc(f'Facture {FACTURE}', c)


DOCUMENTS = [
    (f'Devis {DEVIS} TAM LABS ZENCO.pdf', devis()),
    (f'Facture {FACTURE} TAM LABS ZENCO (acompte).pdf', facture()),
]

CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
for nom, html in DOCUMENTS:
    with tempfile.NamedTemporaryFile('w', suffix='.html', delete=False, encoding='utf-8') as f:
        f.write(html); src = f.name
    sortie = os.path.expanduser(f'~/Downloads/{nom}')
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--no-pdf-header-footer', '--virtual-time-budget=8000',
                    f'--print-to-pdf={sortie}', 'file://' + src], check=True, capture_output=True)
    print(sortie)
