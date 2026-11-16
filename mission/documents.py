# -*- coding: utf-8 -*-
"""Devis et facture d'acompte TAM LABS pour ZENCO SAS (Yves Coignard), mission V2 du 16/11/2026.
Mise en page reprise des documents TAM LABS déjà émis (devis Gray Laser PROP-2026-014-V2, facture 1001).
Usage : python3 mission/documents.py  →  PDF dans ~/Downloads (Chrome headless)."""
import os, subprocess, tempfile

DATE = '16/11/2026'
VALIDITE = '16/12/2026'
DEVIS = 'PROP-2026-1116-ZENCO'
FACTURE_META = '1004'     # suite de la numérotation TAM LABS (1001, 1002, 1003 en base le 16/11)
FACTURE_ACOMPTE = '1005'  # les ads se paient d'avance, l'acompte ne porte que sur le site (Damien, 16/11)
ACOMPTE_PCT = 50

EMETTEUR = ['<b>TAM LABS</b>', 'SASU au capital de 1 000 €', '138 avenue Victor Hugo, 75116 Paris',
            'RCS Paris 131 975 054', 'SIRET 131 975 054 00019 · NAF 6201Z', 'TVA FR80131975054', 'Président : Damien Tamazout']
CLIENT = ['<b>ZENCO SAS</b>', '29-31 boulevard de la Muette', '95140 Garges-lès-Gonesse',
          '<span class="manque">SIREN à compléter</span>', 'À l’attention de M. Yves Coignard, co-président']
RIB = ['Titulaire : TAM LABS', 'Banque : Qonto', 'IBAN : FR76 1695 8000 0152 9635 4169 030', 'BIC : QNTOFRP1XXX']
PIED = ('TAM LABS · SASU au capital de 1 000 € · 138 avenue Victor Hugo, 75116 Paris · RCS Paris 131 975 054 · TVA FR80131975054<br>'
        'Catégorie d’opération : prestation de services. Pas d’escompte pour paiement anticipé. En cas de retard de paiement, une pénalité de 3 fois '
        'le taux d’intérêt légal s’applique, à laquelle s’ajoute une indemnité forfaitaire de 40 € pour frais de recouvrement.')

LIGNES = [
    ('1. Lancement des publicités Instagram et Facebook (Meta)',
     'Configuration du compte publicitaire, de la page et du compte Instagram. Stratégie de recrutement de partenaires '
     '(visio d’information, niches de professionnels). Création des stories et publications sponsorisées. Pilotage et optimisation des campagnes pendant le premier mois.',
     1500),
    ('2. Site e-commerce simplifié Eqology',
     'Catalogue des produits en français, chaque bouton « Commander » mène à la boutique Eqology avec le lien partenaire d’Yves. '
     'Page « Rejoindre l’équipe » avec formulaire et prise de rendez-vous. Alerte à chaque nouveau contact, relances automatiques par e-mail. '
     'Hébergement 12 mois et certificat SSL inclus.',
     3000),
]
REMISE = ('Remise fidélité', 'La première version du site a déjà été réglée : le site e-commerce est facturé 1 500 € HT au lieu de 3 000 € HT.', -1500)

CSS = '''
@page{size:A4;margin:12mm 14mm 12mm}
*{box-sizing:border-box}body{font:10pt/1.45 "Helvetica Neue",Arial,sans-serif;color:#1d2433;margin:0}
.tete{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:18px}
.marque{font-weight:700;font-size:15pt;letter-spacing:-.01em}.marque small{display:block;font-weight:400;font-size:9pt;color:#5d6577}
h1{font-size:20pt;margin:0;font-weight:700}
.meta{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;border-top:2px solid #1d2433;border-bottom:1px solid #d9dde5;padding:8px 0;margin-bottom:12px}
.meta div{white-space:nowrap}.meta div span{display:block;font-size:7.5pt;letter-spacing:.12em;text-transform:uppercase;color:#5d6577}
.parties{display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-bottom:12px}
.parties h3{font-size:7.5pt;letter-spacing:.12em;text-transform:uppercase;color:#5d6577;margin:0 0 4px}
.parties p{margin:0;font-size:9.5pt;line-height:1.45}
table{width:100%;border-collapse:collapse;margin-bottom:12px}
th{font-size:7.5pt;letter-spacing:.12em;text-transform:uppercase;color:#5d6577;text-align:left;border-bottom:1px solid #1d2433;padding:6px 4px}
td{vertical-align:top;padding:5px 4px;border-bottom:1px solid #e6e9ef}
td.n,th.n{text-align:right;white-space:nowrap}
td .d{display:block;font-size:8.8pt;color:#5d6577;margin-top:2px}
.totaux{display:grid;grid-template-columns:1fr 260px;gap:24px;align-items:start;margin-bottom:14px}
.totaux table td{border:none;padding:3px 4px}.totaux .ttc td{font-weight:700;font-size:12pt;border-top:2px solid #1d2433;padding-top:6px}
.bloc h3{font-size:7.5pt;letter-spacing:.12em;text-transform:uppercase;color:#5d6577;margin:0 0 4px}.bloc p{margin:0;font-size:9.5pt}
.note{background:#f3f5f9;border-radius:6px;padding:9px 12px;font-size:9.2pt;margin-bottom:10px}
.signature{display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-top:16px}
.signature div{border:1px solid #d9dde5;border-radius:6px;height:52px;padding:8px 10px;font-size:8.5pt;color:#5d6577}
.pied{margin-top:14px;border-top:1px solid #d9dde5;padding-top:6px;font-size:7.3pt;color:#5d6577;line-height:1.4}
.manque{color:#c2410c;font-weight:700}
'''


def euros(x, dec=False):
    s = f'{abs(x):,.2f}' if dec else f'{abs(x):,.0f}'
    s = s.replace(',', ' ').replace('.', ',')
    return ('-' if x < 0 else '') + s + ' €'


def entete(titre, meta):
    m = ''.join(f'<div><span>{k}</span>{v}</div>' for k, v in meta)
    return (f'<div class="tete"><div class="marque">heyfuture<small>heyfuture.fr · 07 60 55 40 00 · damien.tamazout@gmail.com</small></div><h1>{titre}</h1></div>'
            f'<div class="meta">{m}</div>')


def parties(gauche, droite, titre_d):
    return (f'<div class="parties"><div><h3>Émis par</h3><p>{"<br>".join(gauche)}</p></div>'
            f'<div><h3>{titre_d}</h3><p>{"<br>".join(droite)}</p></div></div>')


def devis():
    ht = sum(l[2] for l in LIGNES) + REMISE[2]
    tva = round(ht * 0.2, 2); ttc = ht + tva
    ac_ht = ht * ACOMPTE_PCT / 100
    lignes = ''.join(f'<tr><td><b>{t}</b><span class="d">{d}</span></td><td class="n">1</td><td class="n">{euros(p)}</td><td class="n">{euros(p)}</td></tr>'
                     for t, d, p in LIGNES + [REMISE])
    h = f'<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>Devis {DEVIS}</title><style>{CSS}</style></head><body>'
    h += entete('Devis', [('N° de devis', DEVIS), ('Date', DATE), ('Valable jusqu’au', VALIDITE), ('Objet', 'Recrutement de partenaires Eqology')])
    h += parties(EMETTEUR[:-1], CLIENT, 'Adressé à')
    h += f'<table><thead><tr><th>Désignation</th><th class="n">Qté</th><th class="n">P.U. HT</th><th class="n">Total HT</th></tr></thead><tbody>{lignes}</tbody></table>'
    h += ('<div class="totaux"><div class="bloc"><h3>Règlement par virement</h3><p>' + '<br>'.join(RIB) + '</p></div>'
          f'<table><tr><td>Total HT</td><td class="n">{euros(ht)}</td></tr><tr><td>TVA 20 %</td><td class="n">{euros(tva)}</td></tr>'
          f'<tr class="ttc"><td>Total TTC</td><td class="n">{euros(ttc)}</td></tr></table></div>')
    meta = LIGNES[0][2]; site = LIGNES[1][2] + REMISE[2]; ac_site = site * ACOMPTE_PCT / 100
    h += ('<table><thead><tr><th>Échéancier</th><th>Quoi</th><th class="n">HT</th><th class="n">TTC</th></tr></thead><tbody>'
          f'<tr><td>À la signature</td><td>Lancement Meta, payé d’avance en totalité</td><td class="n">{euros(meta)}</td><td class="n">{euros(meta*1.2)}</td></tr>'
          f'<tr><td>À la signature</td><td>Acompte de {ACOMPTE_PCT} % sur le site</td><td class="n">{euros(ac_site)}</td><td class="n">{euros(ac_site*1.2)}</td></tr>'
          f'<tr><td>À la mise en ligne du site</td><td>Solde de {100-ACOMPTE_PCT} % sur le site</td><td class="n">{euros(site-ac_site)}</td><td class="n">{euros((site-ac_site)*1.2)}</td></tr></tbody></table>')
    h += ('<div class="note"><b>Budget publicitaire, non compris dans ce devis :</b> 30 € par jour, payé directement à Meta par carte bancaire, '
          'soit environ 900 € par mois. Un mois minimum avant le premier bilan, deux mois de préférence.<br><b>Après le premier mois, en option :</b> pilotage et optimisation des campagnes, 500 € HT par mois, sans engagement de durée.</div>')
    h += ('<div class="signature"><div>Pour TAM LABS<br>Damien Tamazout, président</div>'
          '<div>Pour ZENCO SAS<br>Date, signature et mention « Bon pour accord »</div></div>')
    h += f'<div class="pied">{PIED}</div></body></html>'
    return h


def facture(numero, titre, ligne, detail, ht, apres=''):
    tva = round(ht * 0.2, 2); ttc = ht + tva
    h = f'<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>Facture {numero}</title><style>{CSS}</style></head><body>'
    h += entete(titre, [('N° de facture', numero), ('Émise le', DATE), ('Échéance', 'À réception'), ('Devis', DEVIS)])
    h += parties(EMETTEUR, CLIENT, 'Facturée à')
    h += ('<table><thead><tr><th>Désignation</th><th class="n">Qté</th><th class="n">P.U. HT</th><th class="n">TVA</th><th class="n">Total HT</th></tr></thead><tbody>'
          f'<tr><td><b>{ligne}</b><span class="d">{detail}</span></td>'
          f'<td class="n">1</td><td class="n">{euros(ht, True)}</td><td class="n">20 %</td><td class="n">{euros(ht, True)}</td></tr></tbody></table>')
    h += ('<div class="totaux"><div class="bloc"><h3>Règlement par virement</h3><p>' + '<br>'.join(RIB) + '</p></div>'
          f'<table><tr><td>Total HT</td><td class="n">{euros(ht, True)}</td></tr><tr><td>TVA 20 %</td><td class="n">{euros(tva, True)}</td></tr>'
          f'<tr class="ttc"><td>Total TTC</td><td class="n">{euros(ttc, True)}</td></tr></table></div>')
    if apres:
        h += f'<p style="font-size:9.5pt">{apres}</p>'
    h += f'<div class="pied">{PIED}</div></body></html>'
    return h


META_HT = LIGNES[0][2]
SITE_HT = LIGNES[1][2] + REMISE[2]
ACOMPTE_SITE_HT = SITE_HT * ACOMPTE_PCT / 100
DOCUMENTS = [
    (f'Devis {DEVIS} TAM LABS ZENCO.pdf', devis()),
    (f'Facture {FACTURE_META} TAM LABS ZENCO (lancement Meta).pdf',
     facture(FACTURE_META, 'Facture', 'Lancement des publicités Instagram et Facebook (Meta), payé d’avance',
             'Configuration du compte publicitaire, de la page et du compte Instagram, stratégie de recrutement, créations des stories et publications sponsorisées, '
             f'pilotage du premier mois. Devis n° {DEVIS}. Le budget publicitaire se paie directement à Meta.', META_HT)),
    (f'Facture {FACTURE_ACOMPTE} TAM LABS ZENCO (acompte site).pdf',
     facture(FACTURE_ACOMPTE, 'Facture d’acompte', f'Acompte de {ACOMPTE_PCT} % sur le site e-commerce simplifié Eqology',
             f'Site e-commerce simplifié : 3 000 € HT, remise fidélité de 1 500 € HT, soit {euros(SITE_HT)} HT. Devis n° {DEVIS}.', ACOMPTE_SITE_HT,
             f'Solde de {euros(SITE_HT - ACOMPTE_SITE_HT)} HT à la mise en ligne du site.')),
]

CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
for nom, html in DOCUMENTS:
    with tempfile.NamedTemporaryFile('w', suffix='.html', delete=False, encoding='utf-8') as f:
        f.write(html); src = f.name
    sortie = os.path.expanduser(f'~/Downloads/{nom}')
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--no-pdf-header-footer', f'--print-to-pdf={sortie}', 'file://' + src],
                   check=True, capture_output=True)
    print(sortie)
