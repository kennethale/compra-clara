"""Construye ../index.html a partir de plantilla.html.
Uso: python3 fuente/build.py   (requiere Pillow: pip install pillow)
Opción --sin-firebase: genera index-local.html sin configuración (modo local / pantalla de conexión)."""
import json, base64, io, re, sys, pathlib
from PIL import Image
D = pathlib.Path(__file__).resolve().parent
ROOT = D.parent
A = json.load(open(D/'assets.json')); I = json.load(open(D/'icons2.json'))
# Recursos fijos que la plantilla llama con 'asset:<clave>'
assets = {'logoW': A['siman-com-logotipo-blanco'], 'logoT': A['siman-com-logotipo-tinta'], 'iso': A['siman-isotipo-rojo']}
for f in sorted((D/'capturas').glob('*.jpg')):
    im = Image.open(f).convert('RGB'); im.thumbnail((1400, 1000)); b = io.BytesIO(); im.save(b, 'JPEG', quality=80)
    assets[f.stem] = 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()
t = (D/'plantilla.html').read_text(encoding='utf-8')
t = t.replace('{{font}}', A['font']).replace('{{logoW}}', A['siman-com-logotipo-blanco'])
t = re.sub(r'\{\{ic:([^}]+)\}\}', lambda m: I[m.group(1)], t)
t = t.replace('{{icons}}', json.dumps(I)).replace('{{assets}}', json.dumps(assets)).replace('{{seed}}', 'null')
local = '--sin-firebase' in sys.argv
if not local:
    cfg = json.load(open(D/'firebase-config.json'))
    tag = '<script id="fbcfg" type="application/json">null</script>'
    assert t.count(tag) == 1, 'No se encontró la etiqueta fbcfg en la plantilla'
    t = t.replace(tag, '<script id="fbcfg" type="application/json">' + json.dumps(cfg).replace('<', '\\u003c') + '</script>')
out = ROOT/('index-local.html' if local else 'index.html')
out.write_text(t, encoding='utf-8'); print(out.name, len(t)//1024, 'KB')
