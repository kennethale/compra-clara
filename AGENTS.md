# Instrucciones para agentes (Codex) — Compra Clara · SIMAN

Este repositorio contiene la presentación académica **«SIMAN – Compra Clara»**, que es a la vez una página web editable y la herramienta para presentar. Está publicada en https://kennethale.github.io/compra-clara/ (GitHub Pages, rama `main`, carpeta raíz). Los datos en vivo se guardan en Firebase Firestore.

Antes de tocar nada, lee en este orden:
1. `docs/01_contexto_y_reglas.md`: el proyecto, la rúbrica y las reglas de evidencia. **Son obligatorias.**
2. `docs/02_sistema_visual.md`: la estética «Atmósfera roja», que debe mantenerse.
3. `docs/03_arquitectura.md`: cómo está hecha la página, cómo se construye y cómo llegan los cambios a la versión compartida.
4. `docs/04_estado_de_las_laminas.md`: qué tiene hoy cada lámina y qué falta completar con datos.
5. `docs/auditoria/SIMAN_auditoria_publica_25nov2026.md`: la revisión pública de siman.com y redes.
6. `datos/`: el focus group y la encuesta que entrega el equipo.

## Reglas que no se negocian
- **No inventes datos.** Cada cifra, cita o porcentaje sale de `datos/` o de la auditoría. Si falta, deja el marcador entre corchetes `[ … ]`.
- Clasifica cada afirmación: **A** dicho por participantes (focus group o encuesta), **B** observado en la web o redes, **C** interpretación del equipo, **D** hipótesis por comprobar.
- Si algo no se verificó, escribe: «No se encontró evidencia pública… al [fecha]».
- **No afirmes que se hizo el piloto de 12 personas.** Fue un protocolo y no se ejecutó.
- Etiqueta visible: «Proyecto académico, no es comunicación oficial de SIMAN». No la quites.
- Máximo **20 láminas sin contar portada y fuentes**.
- No hagas compras, pagos, formularios ni contactos con terceros.
- **No cambies** `fuente/firebase-config.json`, las reglas de Firestore ni la ruta de datos `decks/compra-clara`.
- **No escribas en Firestore directamente.** Los cambios de contenido se entregan como un respaldo `.json` que el equipo restaura desde la página (ver `docs/03_arquitectura.md`).

## Flujo de trabajo
1. Edita solo `fuente/plantilla.html`, normalmente la función `DEFAULT_DECK()`. Si añades imágenes, ponlas en `fuente/capturas/` como `.jpg` (se llaman con `'asset:<nombre-sin-extensión>'`).
2. Construye la página:
   - `python3 fuente/build.py` genera `index.html`, la versión publicada, conectada a Firebase.
   - `python3 fuente/build.py --sin-firebase` genera `index-local.html`, para pruebas.
3. Genera el respaldo para la versión compartida con `node fuente/exportar_respaldo.mjs`. Crea `datos/salida/compra-clara-respaldo.json`.
4. Revisa visualmente cada lámina. Abre `index-local.html`, toca «Probar sin base de datos» y usa «Presentar». Comprueba que ningún texto se desborde y que nada se encime.
5. Haz commit y push a `main`. GitHub Pages publica en 1–2 minutos.
6. Dile al equipo que restaure `datos/salida/compra-clara-respaldo.json` desde «Respaldo → Restaurar un respaldo». Antes, deben descargar un respaldo de la versión en vivo, porque restaurar reemplaza lo que el grupo haya editado.
