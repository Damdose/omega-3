// Rend toutes les pubs en PNG : node mission/pubs/rendre.mjs  (serveur local sur le port 8140)
import { createRequire } from 'module';
import fs from 'fs'; import path from 'path'; import { fileURLToPath } from 'url';
const require = createRequire('/Users/damientamazout/Documents/crm-heyfuture/package.json');
const { chromium } = require('playwright');
const ici = path.dirname(fileURLToPath(import.meta.url));
const src = fs.readFileSync(path.join(ici, 'pubs.js'), 'utf8');
const ctx0 = {}; new Function('window', src)(ctx0);
const sortie = path.join(ici, 'png'); fs.mkdirSync(sortie, { recursive: true });
const b = await chromium.launch();
for (const [format, h] of [['story', 1920], ['feed', 1350]]) {
  const p = await b.newPage({ viewport: { width: 1080, height: h } });
  for (const pub of ctx0.PUBS) {
    if (pub.visio && !ctx0.DATE_VISIO.jour) { console.log('en attente de la date :', pub.id); continue; }
    await p.goto(`http://127.0.0.1:8140/mission/pubs/pub.html?id=${pub.id}&format=${format}&v=${Date.now()}`, { waitUntil: 'networkidle' });
    await p.evaluate(() => document.fonts.ready);
    await p.locator('#pub').screenshot({ path: path.join(sortie, `${pub.id}-${format}.png`) });
  }
  await p.close();
}
await b.close();
console.log('ok', fs.readdirSync(sortie).length, 'fichiers');
