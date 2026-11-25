// Genera datos/salida/compra-clara-respaldo.json con las láminas de DEFAULT_DECK() de la plantilla.
// Ese archivo se carga en la página publicada con «Respaldo → Restaurar un respaldo (.json)».
// Uso: python3 fuente/build.py --sin-firebase && node fuente/exportar_respaldo.mjs
// Requiere Playwright (npm i -D playwright && npx playwright install chromium).
import { chromium } from 'playwright';
import { writeFileSync, mkdirSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const b = await chromium.launch(); const p = await b.newPage();
const errs = []; p.on('pageerror', e => errs.push(e.message));
await p.goto(pathToFileURL(resolve(root, 'index-local.html')).href);
await p.waitForTimeout(800);
const json = await p.evaluate(() => JSON.stringify({ v: 1, slides: DEFAULT_DECK().slides }));
mkdirSync(resolve(root, 'datos/salida'), { recursive: true });
writeFileSync(resolve(root, 'datos/salida/compra-clara-respaldo.json'), json);
console.log('Láminas:', JSON.parse(json).slides.length, '· errores de página:', errs.length ? errs : 'ninguno');
await b.close();
