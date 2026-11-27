# -*- coding: utf-8 -*-
"""Kit des pubs LinkedIn (praticiens) pour YAC, en PDF A4 : visuels 1200×1200 + textes prêts à coller.  python3 -I pubs/linkedin.py
Consigne d'Yves (27/11) : pas de « commission » ni de « rémunération », on parle de rétribution de suivi et du parrain (tutoriels, supports) ; YAC à la place de ZENCO."""
import os, html, subprocess, tempfile, base64
ICI = os.path.dirname(os.path.abspath(__file__))
FONT = os.path.join(ICI, '..', 'assets', 'fonts', 'albertsans.woff2')
MONO = os.path.join(ICI, '..', 'assets', 'fonts', 'ibmplexmono-400.woff2')
B = lambda p: base64.b64encode(open(p, 'rb').read()).decode()
LIEN = 'https://eqology-france.vercel.app/partenaire.html?cible=pro&utm_source=linkedin&utm_medium=paid&utm_campaign=praticiens&utm_content='
PUBS = [
    ('cures', 'Pub 1 · Les cures',
     "Vous construisez des cures pour vos patients ? Avec Eqology, vous y ajoutez un test sanguin à domicile qui mesure leur équilibre oméga‑6 / oméga‑3 avant de commencer. Un second test, quelques mois plus tard, montre où ils en sont.\n\nVos patients commandent seuls avec votre lien. Eqology encaisse et livre, et vous percevez une rétribution de suivi sur leurs commandes. Un parrain vous accompagne tout au long du parcours, avec tutoriels et supports.\n\nLaissez vos coordonnées : un distributeur indépendant Eqology vous rappelle sous 48 h.",
     'Ajoutez le test oméga‑3 à vos cures'),
    ('test', 'Pub 2 · Mesurez avant de conseiller',
     "Avant de conseiller des oméga‑3, vous pouvez mesurer. Le test Eqology se fait à domicile, au bout du doigt, et il est analysé par un laboratoire indépendant. Votre patient connaît son équilibre oméga‑6 / oméga‑3 avant sa cure, puis le refait pour voir où il en est.\n\nVotre kit de bienvenue de 99 € vous est remboursé, et un parrain vous accompagne avec tutoriels et supports.\n\nLaissez vos coordonnées : un distributeur indépendant Eqology vous rappelle sous 48 h.",
     'Mesurez avant de conseiller'),
    ('cabinet', 'Pub 3 · Vous conseillez, Eqology encaisse',
     "Vous ne voulez rien vendre au cabinet ? Vous n’aurez pas à le faire. Vous recommandez le test et l’huile Eqology, vos patients commandent en ligne avec votre lien, et Eqology encaisse, expédie et gère le service client.\n\nVous percevez une rétribution de suivi sur leurs commandes. Un parrain vous accompagne tout au long du parcours, avec tutoriels et supports.\n\nLaissez vos coordonnées : un distributeur indépendant Eqology vous rappelle sous 48 h.",
     'Vous conseillez, Eqology encaisse et livre'),
]
for _, _, t, titre in PUBS:
    assert len(t) <= 600, (titre, len(t))   # limite LinkedIn du texte d'introduction
    assert 'commission' not in t.lower() and 'rémunération' not in t.lower()

e = html.escape
pages = ['''<section class="page"><div class="oeil">YAC · pubs LinkedIn · praticiens de santé au naturel</div>
<h1>Trois pubs LinkedIn pour recruter des praticiens</h1>
<p class="chapo">Chaque pub mène à la page praticiens du site, où le praticien laisse ses coordonnées. Un distributeur indépendant Eqology le rappelle sous 48 h.</p>
<div class="bloc"><h2>Réglages de la campagne</h2><ul>
<li><b>Annonceur</b> : page entreprise <b>YAC</b>.</li>
<li><b>Objectif</b> : visites du site web (ou génération de prospects si vous utilisez le formulaire LinkedIn).</li>
<li><b>Format</b> : publicité à image unique, visuels carrés 1200 × 1200.</li>
<li><b>Ciblage</b> : France. Intitulés de poste : naturopathe, micronutritionniste, diététicien, nutritionniste, ostéopathe, kinésithérapeute, praticien en médecine douce.</li>
<li><b>Bouton</b> : En savoir plus.</li>
<li><b>Vocabulaire</b> : on parle de <b>rétribution de suivi</b> et du <b>parrain</b> qui accompagne (tutoriels, supports), jamais de commission ni de rémunération. Aucun montant de gain.</li>
</ul></div>
<div class="planche">''' + ''.join(f'<img src="data:image/png;base64,{B(os.path.join(ICI, f"linkedin-{c}-1x1.png"))}" alt="">' for c, *_ in PUBS) + '</div></section>']
for c, nom, texte, titre in PUBS:
    pages.append(f'''<section class="page"><div class="oeil">{e(nom)}</div>
<img class="visuel" src="data:image/png;base64,{B(os.path.join(ICI, f"linkedin-{c}-1x1.png"))}" alt="">
<div class="bloc"><div class="k">Texte d’introduction</div><p>{e(texte).replace(chr(10)*2, "</p><p>")}</p>
<div class="k">Titre</div><p><b>{e(titre)}</b></p>
<div class="k">Lien</div><p class="mono">{e(LIEN + c)}</p></div></section>''')

doc = f'''<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>Pubs LinkedIn YAC</title><style>
@font-face{{font-family:'Albert Sans';src:url(data:font/woff2;base64,{B(FONT)}) format('woff2');font-weight:100 900}}
@font-face{{font-family:'Plex';src:url(data:font/woff2;base64,{B(MONO)}) format('woff2')}}
@page{{size:A4;margin:0}}*{{box-sizing:border-box}}body{{margin:0;font:11pt/1.5 'Albert Sans',sans-serif;color:#0B1D2E;background:#F5F4F0}}
.page{{width:210mm;height:297mm;padding:16mm 16mm;page-break-after:always;display:flex;flex-direction:column;gap:5mm;overflow:hidden}}
.oeil{{font:8pt 'Plex',monospace;text-transform:uppercase;letter-spacing:.06em;color:#3D8691}}
h1{{font-weight:300;font-size:26pt;line-height:1.1;margin:0;letter-spacing:-.02em}}h2{{font-size:12pt;margin:0 0 2mm}}
.chapo{{font-size:12pt;margin:0;color:#33475a}}
.bloc{{background:#fff;border-radius:4mm;padding:6mm 7mm}}.bloc ul{{margin:0;padding-left:5mm}}.bloc li{{margin:1.2mm 0}}.bloc p{{margin:0 0 2.5mm}}
.k{{font:7.5pt 'Plex',monospace;text-transform:uppercase;letter-spacing:.06em;color:#3D8691;margin:3mm 0 1mm}}
.mono{{font:8pt 'Plex',monospace;word-break:break-all;color:#33475a}}
.planche{{display:grid;grid-template-columns:repeat(3,1fr);gap:3mm}}.planche img{{width:100%;border-radius:2mm}}
.visuel{{width:118mm;align-self:center;border-radius:3mm;box-shadow:0 6px 20px -10px rgba(11,29,46,.4)}}
</style></head><body>{"".join(pages)}</body></html>'''

sortie = os.path.expanduser('~/Downloads/Pubs LinkedIn praticiens - YAC.pdf')
with tempfile.NamedTemporaryFile('w', suffix='.html', delete=False, encoding='utf-8') as f:
    f.write(doc); src = f.name
subprocess.run(['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', '--headless=new', '--disable-gpu', '--no-pdf-header-footer',
                '--virtual-time-budget=8000', f'--print-to-pdf={sortie}', 'file://' + src], check=True, capture_output=True)
print(sortie, [len(t) for _, _, t, _ in PUBS])
