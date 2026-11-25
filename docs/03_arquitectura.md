# 03 · Arquitectura de la página

## Archivos
| Ruta | Qué es |
|---|---|
| `fuente/plantilla.html` | **Fuente única.** Editor, modo presentación, sincronización con Firebase y `DEFAULT_DECK()` (contenido base) |
| `fuente/build.py` | Inserta fuente, logos, íconos, capturas y configuración de Firebase; genera `index.html` |
| `fuente/assets.json` | Fuente Roboto (base64), logos y capturas en base64 |
| `fuente/icons2.json` | 72 íconos Lucide en SVG |
| `fuente/capturas/*.jpg` | Capturas disponibles como `asset:<nombre>` |
| `fuente/firebase-config.json` | Configuración web de Firebase (es pública por diseño; lo que protege la base son las reglas) |
| `fuente/exportar_respaldo.mjs` | Exporta `DEFAULT_DECK()` a `datos/salida/compra-clara-respaldo.json` |
| `index.html` | Lo que sirve GitHub Pages. **Es generado: no lo edites a mano** |

## Modelo de datos
```js
deck = { v:1, docId:'compra-clara-v1', assets:{…}, slides:[ slide… ] }
slide = { id, title, bg:{ color, fog, img, grain }, notes, els:[ el… ] }
el = { id, type, x, y, w, h, rot, op, anim, lock, p:{…} }   // coordenadas en el lienzo de 1920×1080
```

Los constructores están en la plantilla:
- `E.text(html, x, y, w, h, {size, weight, lh, ls, color, align, …})`: admite `<b>`, `<br>` y `PH('…')` para marcadores grises.
- `E.img(src, x, y, w, h, {fit, radius, glow, tilt, anim})`: `src` es `'asset:clave'`, una URL o un dataURL.
- `E.shape(kind, …)`: rombo, rombo-borde, rect, circle, line o glass.
- `E.icon(nombre, x, y, s, {color, bg})`.
- `E.search(texto, …)`, `E.flip(t1, t2, cita, fuente, …)`, `E.counter(valor, …, {dec, pre, suf, size})`.
- Ayudantes:
  - `S(title, fog, els, notes, {color})` crea una lámina;
  - `chrome(etiqueta)` pone logotipo y etiqueta de sección;
  - `glassCard(x, y, w, h)` crea una tarjeta de cristal;
  - `PH(texto)` crea un marcador `[texto]` en gris.

## Persistencia compartida (Firebase)
- **Proyecto:** `compra-clara-46746`, Firestore en edición Standard, cuenta de Google de Kenneth.
- **Rutas:**
  - `decks/compra-clara` es un documento con `{ j: JSON del orden de láminas }`;
  - `decks/compra-clara/slides/<id>` guarda un documento por lámina con `{ j: JSON de la lámina, t }`.
- **Reglas publicadas:** lectura y escritura abiertas solo bajo `decks/compra-clara/**`, para que el grupo edite sin iniciar sesión. Cualquiera con el link puede editar; por eso existe el menú **Respaldo**.
- **Imágenes:** las que suban los usuarios se guardan comprimidas dentro de la lámina (máximo unos 950 KB por lámina), porque Storage requiere un plan de pago.
- **Conflictos:** gana el último que guarda. Los cambios remotos se aplican cuando nadie está arrastrando ni escribiendo.
- **`DEFAULT_DECK()` solo se usa cuando la base está vacía.** Hoy la base ya tiene las 21 láminas. Por eso, **cambiar `DEFAULT_DECK()` no cambia lo que ve el grupo**. Hay que restaurar el respaldo exportado.

## Cómo entregar contenido nuevo al grupo
1. Edita `DEFAULT_DECK()` en `fuente/plantilla.html` y otras partes si hace falta.
2. Ejecuta `python3 fuente/build.py && python3 fuente/build.py --sin-firebase`.
3. Ejecuta `node fuente/exportar_respaldo.mjs`, que crea `datos/salida/compra-clara-respaldo.json`.
4. Verifica visualmente en `index-local.html`: «Probar sin base de datos» y luego «Presentar».
5. Haz commit y push.
6. El equipo, en https://kennethale.github.io/compra-clara/:
   - «Respaldo → Descargar respaldo», para guardar lo que tienen;
   - luego «Respaldo → Restaurar un respaldo», con el archivo nuevo.

Si el grupo ya editó láminas en vivo, pide primero su respaldo descargado. Compáralo con el nuevo e incorpora sus cambios antes de entregar.

## Cambios en el código de la página
- Funciones que también puedes mejorar: el editor, la presentación y los nuevos tipos de elementos.
- Mantén lo siguiente:
  - un solo archivo HTML autocontenido;
  - la etiqueta `<script id="fbcfg" type="application/json">null</script>` en la plantilla (`build.py` la reemplaza);
  - el formato `{j: string}` en Firestore;
  - que no haya `alert()`, `confirm()` ni `prompt()`.
- **Prueba antes de hacer push:** que cargue sin errores de consola, el modo presentación (flechas, N notas, O índice, F pantalla completa, Esc) y que el respaldo descargue y restaure.
