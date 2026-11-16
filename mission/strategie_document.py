# -*- coding: utf-8 -*-
"""Document de stratégie technique pour Yves Coignard (ZENCO SAS), A4 en PDF, DA Heyfuture.
Damien, 16/11/2026 : « un vrai document en mode technique », jamais le gabarit COURS.
Usage : python3 mission/strategie_document.py  →  ~/Downloads/Stratégie Eqology Yves Coignard.pdf"""
import os, base64, subprocess, tempfile

ICI = os.path.dirname(os.path.abspath(__file__))
LOGO = base64.b64encode(open(os.path.expanduser('~/Documents/crm-heyfuture/public/assets/heyfuture-logo.svg'), 'rb').read()).decode()
SORTIE = os.path.expanduser('~/Downloads/Stratégie Eqology Yves Coignard.pdf')


def tableau(entetes, lignes, classe=''):
    h = f'<table class="{classe}"><thead><tr>' + ''.join(f'<th>{e}</th>' for e in entetes) + '</tr></thead><tbody>'
    h += ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in l) + '</tr>' for l in lignes)
    return h + '</tbody></table>'


def section(num, titre, corps, saut=False):
    return f'<section class="{"saut" if saut else ""}"><h2><span>{num:02d}</span>{titre}</h2>{corps}</section>'


CSS = '''
@page{size:A4;margin:18mm 17mm 18mm}
@page :first{margin:0}
:root{--beige:#F4F2EE;--beige2:#E5E2DB;--encre:#1A1A1A;--gris:#5B5A55;--vert:#1F5A45;--vert-nuit:#0F2E24;--vert-pale:#D3E4DA;--fluo:#E4F73B}
*{box-sizing:border-box}
body{margin:0;font:9.6pt/1.55 "Plus Jakarta Sans",Arial,sans-serif;color:var(--encre)}
h1,h2,h3{font-family:Sora,Arial,sans-serif;letter-spacing:-.01em;margin:0}
p{margin:0 0 7px}
.couv{height:297mm;background:var(--vert-nuit);color:#fff;padding:24mm 20mm;display:flex;flex-direction:column;page-break-after:always}
.couv .logo{background:#fff;border-radius:10px;padding:9px 14px;align-self:flex-start}
.couv .logo img{height:22px;display:block}
.couv .type{margin-top:auto;font-size:9pt;letter-spacing:.16em;text-transform:uppercase;color:var(--vert-pale)}
.couv h1{font-size:30pt;line-height:1.1;margin:10px 0 14px;max-width:150mm}
.couv .chapo{font-size:12pt;line-height:1.5;color:#E6EDE9;max-width:145mm}
.couv .trait{width:46px;height:5px;background:var(--fluo);border-radius:3px;margin:22px 0}
.couv dl{display:grid;grid-template-columns:38mm 1fr;gap:5px 10px;font-size:9.5pt;margin:0}
.couv dt{color:var(--vert-pale)}.couv dd{margin:0}
.sommaire{page-break-after:always}
.sommaire h2{font-size:15pt;margin-bottom:10px}
.sommaire ol{list-style:none;padding:0;margin:0;columns:1}
.sommaire li{display:flex;gap:12px;padding:7px 0;border-bottom:1px solid var(--beige2);font-size:10.5pt}
.sommaire li b{font-family:Sora;color:var(--vert);width:22px}
.resume{background:var(--beige);border-radius:10px;padding:14px 16px;margin-top:18px}
.resume h3{font-size:10.5pt;margin-bottom:6px}
.resume ul{margin:0;padding-left:16px}.resume li{margin-bottom:4px}
section{margin-bottom:16px}
.saut{page-break-before:always}
h2{break-after:avoid;font-size:14.5pt;display:flex;align-items:baseline;gap:10px;padding-bottom:6px;border-bottom:2px solid var(--encre);margin-bottom:10px}
h2 span{font-size:10pt;color:var(--vert)}
h3{font-size:10.5pt;margin:12px 0 5px}
table{width:100%;border-collapse:collapse;margin:6px 0 10px;font-size:8.9pt;page-break-inside:avoid}
th{text-align:left;font-size:7.4pt;letter-spacing:.1em;text-transform:uppercase;color:var(--gris);border-bottom:1.5px solid var(--encre);padding:5px 6px}
td{padding:6px;border-bottom:1px solid var(--beige2);vertical-align:top}
td:first-child{font-weight:600}
table.chiffres td:nth-last-child(-n+2),table.chiffres th:nth-last-child(-n+2){text-align:right;white-space:nowrap}
.encart{border-left:4px solid var(--vert);background:var(--beige);padding:9px 12px;border-radius:0 8px 8px 0;margin:8px 0}
.alerte{border-left-color:#B4483A}
.tunnel{display:flex;gap:6px;margin:8px 0 12px;page-break-inside:avoid}
.tunnel div{flex:1;background:var(--beige);border-radius:8px;padding:8px 8px 9px;font-size:8.4pt;line-height:1.35}
.tunnel div b{display:block;font-family:Sora;font-size:9pt;margin-bottom:2px}
.tunnel div.cle{background:var(--vert);color:#fff}
.tunnel i{align-self:center;color:var(--vert);font-style:normal;font-weight:700}
.deux{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.carte{border:1px solid var(--beige2);border-radius:8px;padding:10px 12px}
.carte h3{margin-top:0}
ul.liste{margin:4px 0 8px;padding-left:16px}ul.liste li{margin-bottom:3px}
.pied{margin-top:18px;font-size:7.6pt;color:var(--gris);border-top:1px solid var(--beige2);padding-top:6px}
'''

couverture = f'''<div class="couv">
<div class="logo"><img src="data:image/svg+xml;base64,{LOGO}" alt="heyfuture"></div>
<div class="type">Stratégie et plan d’action</div>
<h1>Recruter des partenaires Eqology avec Instagram et Facebook</h1>
<p class="chapo">Le dispositif complet : les cibles, les campagnes, le site, le parcours d’un futur partenaire, le suivi des résultats, le calendrier et le budget.</p>
<div class="trait"></div>
<dl><dt>Client</dt><dd>ZENCO SAS · Yves Coignard, distributeur indépendant Eqology</dd>
<dt>Préparé par</dt><dd>Damien Tamazout, Heyfuture</dd>
<dt>Date</dt><dd>16 novembre 2026</dd>
<dt>Devis associé</dt><dd>PROP-2026-1116-ZENCO</dd></dl>
</div>'''

sommaire = '''<div class="sommaire"><h2>Sommaire</h2><ol>''' + ''.join(
    f'<li><b>{i:02d}</b>{t}</li>' for i, t in enumerate([
        'L’objectif', 'Ce que font les distributeurs qui réussissent', 'Les cibles et les messages', 'Le parcours d’un futur partenaire',
        'Le dispositif Meta : comptes, campagnes, publicités', 'Le site : page de recrutement et boutique', 'Le suivi des contacts et des résultats',
        'Qui fait quoi', 'Le calendrier', 'Le budget et le règlement', 'Ce dont nous avons besoin'], 1)) + '''</ol>
<div class="resume"><h3>En résumé</h3><ul>
<li>Le chiffre d’affaires d’un distributeur Eqology vient de son équipe. Nous allons donc chercher des partenaires, en priorité des personnes qui ont déjà une clientèle.</li>
<li>Des publicités Instagram et Facebook tournent chaque jour. Elles mènent à une page « Rejoindre l’équipe », où les intéressés laissent leurs coordonnées.</li>
<li>Vous recevez chaque contact sur votre téléphone et vous le rappelez. Les relances, le site et les publicités tournent sans vous.</li>
<li>Le site sera en ligne le lundi 23 novembre, les publicités démarreront le mercredi 25 novembre, et le premier bilan aura lieu fin décembre.</li>
</ul></div></div>'''

s1 = section(1, 'L’objectif', '''
<p><b>Objectif principal :</b> recruter des business partners Eqology qui feront à leur tour la promotion des produits auprès de leur entourage ou de leur clientèle.</p>
<p><b>Objectif secondaire :</b> permettre à toute personne intéressée de commander les produits en ligne, avec chaque commande attribuée à votre compte partenaire.</p>
<div class="encart">Vendre un flacon à la fois rapporte une commission. Recruter une coach qui met trente clients sous oméga-3 rapporte chaque mois, sur toute son activité. Le dispositif est donc construit pour le recrutement. La boutique vient en soutien.</div>''')

s2 = section(2, 'Ce que font les distributeurs qui réussissent', '''
<p>Nous avons étudié les références que vous nous avez transmises, leurs sites et leurs publicités, ainsi que toutes les publicités Meta qui citent Eqology en Europe (320 publicités, dont 80 diffusées en France).</p>''' + tableau(
    ['Référence', 'Leur méthode', 'Ce que nous reprenons'], [
        ['Boost Your Health (Pays-Bas)', 'Un site à deux portes (« ma santé » / « entreprendre »), un appel découverte gratuit de 15 minutes, des témoignages de coachs et de thérapeutes recrutés', 'Les deux portes, l’appel, la cible des professionnels'],
        ['Eqology Business Partners Sicilia', '31 publicités sur 7 mois pour remplir des soirées d’information animées par des responsables Eqology', 'La publicité qui remplit une réunion de présentation'],
        ['Robert Kontriner', 'La page partenaire Eqology à son nom, tous les liens portent son identifiant', 'La boutique à votre nom, sans stock'],
        ['Falko Krismayr', 'Recrutement en face à face, Instagram pour l’image et la crédibilité', 'Le contact humain au bout du parcours'],
        ['Livre « Oméga-3, le verdict de la science »', 'Approche des professionnels de santé par la science, sans parler de produit', 'Parler science aux pros, l’activité ensuite'],
        ['Norway Omega, IM8', 'Marques qui vendent en ligne avec des stories sponsorisées soignées', 'Le format story, la qualité des visuels'],
    ]) + '''
<h3>Les enseignements</h3>
<ul class="liste">
<li><b>Les publicités qui durent</b> (plusieurs mois) mènent toutes à une conversation : message privé, appel ou réunion. Personne ne paie des mois de publicité qui ne rapporte rien.</li>
<li><b>Les publicités « promotion » vers la boutique</b> (exemple : -25 % chez un distributeur bulgare) ont été arrêtées au bout de cinq semaines.</li>
<li><b>En France, aucun distributeur Eqology ne fait de publicité Meta</b> qui cite la marque. La place est libre.</li>
</ul>''')

s3 = section(3, 'Les cibles et les messages', '''
<div class="deux">
<div class="carte"><h3>Cible 1 · Le grand public</h3>
<p>Retraités et actifs de 35 à 70 ans qui cherchent un complément de revenu et s’intéressent à la santé.</p>
<p><b>Message :</b> « Santé et complément de revenu : 45 minutes pour tout comprendre. »</p>
<p><b>Destination :</b> inscription à la visio d’information.</p></div>
<div class="carte"><h3>Cible 2 · Les professionnels</h3>
<p>Coachs sportifs, salles de sport, diététiciennes, kinés, esthéticiennes : des personnes qui ont déjà une clientèle.</p>
<p><b>Message :</b> « Proposez le test oméga-3 à vos clients et ajoutez une source de revenu à votre activité. »</p>
<p><b>Destination :</b> échange découverte avec vous.</p></div>
</div>
<div class="encart"><b>Votre histoire sert de preuve.</b> À 75 ans, en forme et partenaire Eqology, vous parlez directement au public qui cherche un revenu d’appoint. Une courte vidéo de vous sera la première publicité testée.</div>
<p><b>Plus tard :</b> les naturopathes et praticiens de santé, avec une approche par la science et le test, jamais par l’activité au premier contact.</p>''', saut=True)

s4 = section(4, 'Le parcours d’un futur partenaire', '''
<div class="tunnel">
<div><b>1. Publicité</b>Story ou publication sur Instagram et Facebook</div><i>→</i>
<div><b>2. Page</b>« Rejoindre l’équipe » sur votre site</div><i>→</i>
<div><b>3. Formulaire</b>Nom, téléphone, profil, créneau de rappel</div><i>→</i>
<div class="cle"><b>4. Votre appel</b>Sous 48 heures, par téléphone</div><i>→</i>
<div><b>5. Visio</b>Présentation par Eqology ou votre parrain</div><i>→</i>
<div><b>6. Démarrage</b>Business Kit, nouveau partenaire</div>
</div>
<p>Entre l’étape 3 et l’étape 5, une série d’e-mails automatiques présente Eqology, l’activité et la date de la prochaine visio. Quand vous appelez, la personne a déjà reçu l’essentiel.</p>
<p>Les personnes qui veulent seulement acheter sont orientées vers la boutique du site, puis vers la boutique Eqology à votre nom.</p>''')

s5 = section(5, 'Le dispositif Meta : comptes, campagnes, publicités', '''
<h3>Les comptes</h3>
<ul class="liste">
<li>Un portefeuille Meta Business (Business Manager) au nom de ZENCO, avec une page Facebook et un compte Instagram dédiés.</li>
<li>Un compte publicitaire réglé par votre carte bancaire : le budget est payé directement à Meta.</li>
<li>Le compte Instagram reçoit 6 à 9 publications de base (qui vous êtes, l’activité, le test, des témoignages). Il sert de vitrine aux publicités, sans animation de communauté.</li>
</ul>
<h3>Les campagnes</h3>''' + tableau(
    ['Campagne', 'Ciblage', 'Budget de départ', 'Objectif mesuré'], [
        ['Visio d’information', 'France, 35-70 ans, centres d’intérêt santé, bien-être, revenu complémentaire', '20 € par jour', 'Inscriptions au formulaire'],
        ['Professionnels', 'France, métiers et centres d’intérêt : coaching sportif, fitness, nutrition, kinésithérapie, esthétique', '10 € par jour', 'Demandes d’échange'],
    ]) + '''
<p>Après deux semaines, le budget passe sur la campagne qui obtient les inscriptions les moins chères.</p>
<h3>Les publicités</h3>
<ul class="liste">
<li><b>Formats :</b> stories et reels verticaux, publications carrées pour le fil.</li>
<li><b>Trois créations par campagne au départ :</b> une vidéo de vous, un visuel sur le test oméga-3, un message court sur l’activité.</li>
<li><b>Diffusion :</b> tous les jours, avec remplacement des créations qui s’essoufflent.</li>
</ul>
<div class="encart alerte"><b>Règles respectées.</b> Les publicités n’utilisent que les bienfaits des oméga-3 autorisés par l’Union européenne (exemple : « le DHA contribue au fonctionnement normal du cerveau »). Aucune promesse de guérison, aucune promesse de revenu chiffrée, et la mention « distributeur indépendant Eqology » apparaît.</div>''', saut=True)

s6 = section(6, 'Le site : page de recrutement et boutique', tableau(
    ['Partie', 'Contenu', 'Rôle'], [
        ['Rejoindre l’équipe', 'Votre histoire, l’activité expliquée simplement, à qui elle s’adresse, les étapes pour démarrer, le formulaire et la prise de rendez-vous', 'Page d’arrivée des publicités, recrutement'],
        ['Boutique', 'La gamme Eqology présentée en français : oméga-3, packs, vitamines, test', 'Rassurer et permettre la commande'],
        ['Bouton « Commander »', 'Ouvre la fiche du produit sur le site Eqology avec votre identifiant de partenaire', 'Chaque commande vous est attribuée'],
        ['Mentions et confidentialité', 'Mentions légales, politique de confidentialité, consentement au formulaire', 'Conformité'],
    ]) + '''
<p><b>Rien à gérer pour vous :</b> Eqology encaisse, livre et assure le service client. Vous n’avez ni stock ni colis. Les prix restent affichés sur le site Eqology, ce qui évite tout écart quand ils changent.</p>''')

s7 = section(7, 'Le suivi des contacts et des résultats', '''
<h3>Les contacts</h3>
<ul class="liste">
<li>Chaque formulaire envoyé vous parvient immédiatement par SMS ou WhatsApp : nom, téléphone, profil et créneau souhaité.</li>
<li>Une copie arrive chez Heyfuture, pour suivre les relances et vous prévenir si un contact n’a pas été rappelé.</li>
<li>Les e-mails de relance partent automatiquement : confirmation, présentation d’Eqology, témoignage, invitation à la visio.</li>
</ul>
<h3>La mesure</h3>''' + tableau(
    ['Indicateur', 'Ce qu’il dit', 'Source'], [
        ['Coût par inscrit', 'Combien coûte un nouveau contact', 'Meta, événement « inscription » envoyé par le site'],
        ['Taux de rappel', 'Part des inscrits que vous avez joints', 'Suivi des contacts'],
        ['Présents à la visio', 'Intérêt réel des contacts', 'Liste de la visio'],
        ['Nouveaux partenaires', 'Le résultat final', 'Votre compte Eqology'],
        ['Commandes boutique', 'Les ventes attribuées à votre compte', 'Votre compte Eqology'],
    ]) + '<p>Le site envoie à Meta un signal à chaque inscription (pixel Meta et API de conversions). Meta apprend ainsi à montrer les publicités aux personnes qui ressemblent à vos inscrits.</p>', saut=True)

s8 = section(8, 'Qui fait quoi', tableau(
    ['Tâche', 'Yves', 'Heyfuture'], [
        ['Création des comptes Meta et du compte Instagram', 'Ajoute sa carte au compte publicitaire', 'Crée et configure'],
        ['Vidéo de présentation', '10 minutes de tournage au téléphone', 'Script, montage, sous-titres'],
        ['Site et boutique', 'Relit sa présentation', 'Conçoit, développe, met en ligne'],
        ['Publicités', 'Valide les premières créations', 'Crée, diffuse, optimise chaque jour'],
        ['Contacts', 'Rappelle sous 48 heures', 'Alertes, relances e-mail, suivi'],
        ['Visio de présentation', 'Invite ses contacts', 'Organisation avec le parrain si besoin'],
        ['Bilan', 'Partage le nombre de partenaires signés', 'Prépare le bilan chiffré'],
    ]))

s9 = section(9, 'Le calendrier', saut=True, corps=tableau(
    ['Date', 'Étape'], [
        ['Lundi 16 novembre', 'Stratégie, devis et factures'],
        ['Vendredi 20 novembre au plus tard', 'Devis signé, factures 1004 et 1005 réglées (2 700 € TTC)'],
        ['Du 18 au 20 novembre', 'Création des comptes Meta et Instagram, tournage de la vidéo'],
        ['Lundi 23 novembre', 'Site en ligne : page « Rejoindre l’équipe » et boutique'],
        ['Mardi 24 novembre', 'Validation des premières publicités'],
        ['Mercredi 25 novembre', 'Lancement des publicités'],
        ['Mercredi 9 décembre', 'Point à deux semaines : budget réorienté vers la meilleure campagne'],
        ['Fin décembre', 'Bilan du premier mois et décision pour janvier'],
    ]))

s10 = section(10, 'Le budget et le règlement', tableau(
    ['Échéance', 'Document', 'HT', 'TTC'], [
        ['À la signature', 'Facture 1004 : lancement des publicités Meta, payé d’avance', '1 500 €', '1 800 €'],
        ['À la signature', 'Facture 1005 : acompte de 50 % sur le site', '750 €', '900 €'],
        ['Lundi 23 novembre', 'Solde de 50 % sur le site', '750 €', '900 €'],
        ['<b>Total</b>', '<b>Devis PROP-2026-1116-ZENCO</b>', '<b>3 000 €</b>', '<b>3 600 €</b>'],
    ], 'chiffres') + '''
<ul class="liste">
<li><b>Site e-commerce :</b> 3 000 € HT, facturé 1 500 € HT après la remise fidélité (première version déjà réglée).</li>
<li><b>Lancement Meta :</b> 1 500 € HT, comprenant la configuration, la stratégie, les créations et le pilotage du premier mois.</li>
<li><b>Budget publicitaire, en plus :</b> 30 € par jour payés directement à Meta, soit environ 900 € par mois. Un mois minimum avant le bilan, deux mois de préférence.</li>
<li><b>Après le premier mois, en option :</b> pilotage des publicités à 500 € HT par mois, sans engagement.</li>
<li><b>Règlement :</b> par virement à TAM LABS, la société qui porte Heyfuture. Les coordonnées bancaires figurent sur chaque facture.</li>
</ul>''')

s11 = section(11, 'Ce dont nous avons besoin', tableau(
    ['Élément', 'Pourquoi', 'Pour quand'], [
        ['Votre identifiant de partenaire Eqology', 'Coder chaque bouton « Commander » à votre nom', '18 novembre'],
        ['Le nom de votre parrain et ses dates de visio', 'Organiser la présentation des nouveaux contacts', '20 novembre'],
        ['SMS ou WhatsApp', 'Vous prévenir de chaque nouveau contact', '18 novembre'],
        ['Accès à votre compte Facebook', 'Créer la page et le compte publicitaire', '19 novembre'],
        ['10 minutes pour la vidéo', 'Première publicité', '20 novembre'],
        ['Le numéro SIREN de ZENCO', 'Compléter le devis et les factures', '18 novembre'],
    ]) + '<div class="pied">Heyfuture · Damien Tamazout · damien.tamazout@gmail.com · 07 60 55 40 00. Sources : captures transmises par Yves Coignard, sites et publicités des références consultés le 16/11/2026, Bibliothèque publicitaire Meta.</div>')

html = ('<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>Stratégie Eqology · Yves Coignard</title>'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700&family=Sora:wght@600;700&display=swap">'
        f'<style>{CSS}</style></head><body>{couverture}{sommaire}{s1}{s2}{s3}{s4}{s5}{s6}{s7}{s8}{s9}{s10}{s11}</body></html>')
src = os.path.join(ICI, 'strategie-document.html')
open(src, 'w', encoding='utf-8').write(html)
subprocess.run(['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', '--headless=new', '--disable-gpu', '--no-pdf-header-footer',
                '--virtual-time-budget=8000', f'--print-to-pdf={SORTIE}', 'file://' + src], check=True, capture_output=True)
print(SORTIE)
