import { createRequire } from 'module';
const require = createRequire('/Users/damientamazout/Documents/crm-heyfuture/package.json');
const { chromium } = require('playwright');
const [html, out] = process.argv.slice(2);
const b = await chromium.launch();
const p = await b.newPage();
await p.goto('file://' + html, { waitUntil: 'networkidle' });
await p.evaluate(() => document.fonts.ready);
const fonts = await p.evaluate(() => [...document.fonts].map(f => f.family + ':' + f.status));
console.log(fonts.join(', '));
const of = await p.evaluate(() => [...document.querySelectorAll('.page')].map((pg, i) => {
  const r = pg.getBoundingClientRect(); const bad = [];
  pg.querySelectorAll('*').forEach(el => { const e = el.getBoundingClientRect(); if (e.bottom > r.bottom + 0.5 || e.right > r.right + 0.5) bad.push(el.className || el.tagName); });
  return `p${i + 1}: ${bad.length ? 'OVERFLOW ' + bad.join(',') : 'ok'}`;
}));
console.log(of.join(' | '));
await p.pdf({ path: out, format: 'A4', printBackground: true, landscape: false, margin: { top: 0, right: 0, bottom: 0, left: 0 }, preferCSSPageSize: true });
await b.close();
