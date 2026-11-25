# Remplace l'adresse du site partout (pages, plan du site, robots, liens des pubs, e-mails, kit).
# Usage : python3 mission/changer-domaine.py www.nouveau-domaine.fr
import sys, pathlib
ANCIEN = 'eqology-omega3.vercel.app'
nouveau = sys.argv[1].strip().removeprefix('https://').removeprefix('http://').strip('/')
racine = pathlib.Path(__file__).resolve().parent.parent
total = 0
for f in racine.rglob('*'):
    if f.is_dir() or '.git' in f.parts or f.suffix not in {'.html', '.js', '.xml', '.txt', '.py', '.json', '.md'}:
        continue
    if f.name == 'changer-domaine.py' or (f.name == 'vercel.json'):
        continue  # vercel.json garde les redirections de l'ancien domaine fena-eqology
    s = f.read_text(encoding='utf-8')
    n = s.count(ANCIEN)
    if n:
        f.write_text(s.replace(ANCIEN, nouveau), encoding='utf-8'); total += n
        print(f'{n:3}  {f.relative_to(racine)}')
print(total, 'remplacements vers', nouveau)
