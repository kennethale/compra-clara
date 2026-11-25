# 02 · Sistema visual: «Atmósfera roja»

La presentación debe sentirse como una extensión de siman.com con una dirección de arte editorial. El equipo eligió la opción **B · Atmósfera roja** entre tres propuestas (ver `referencias/Opcion_B.jpg`). Prefiere las referencias de Pinterest: fondos oscuros con niebla roja difusa, tipografía enorme y capturas reales que flotan con sombra. **No cambies de estilo.**

## Lienzo
- Láminas de **1920 × 1080 px** (W, H en la plantilla).
- Margen lateral de 100 px. El cromado superior va a 80 px del borde: logotipo a la izquierda y etiqueta de sección a la derecha, en tamaño 22.

## Color
| Token | Hex | Uso |
|---|---|---|
| Fondo base | `#120405` (variantes `#0C0203`, `#1A0607`) | Fondo de todas las láminas |
| Rojo SIMAN | `#D02D37` | Acento principal, botones, formas |
| Burdeos (S del logo) | `#A83338` / `#A93439` | Fondos de íconos, reverso de tarjetas |
| Vino | `#881D11` | Profundidad |
| Rosa | `#E74C7B` / `#FF7A8A` | Niebla «rosa», destellos |
| Tinta | `#1F1F1F` | Texto sobre claro (poco uso) |
| Texto | `#FFFFFF`, secundario `#CFCFCF` | Sobre fondo oscuro |
| Verde cuotas | `#316C0C` | Solo para citar la UI de SIMAN |
| Azul Credisiman | `#03499A` | Solo si se habla de Credisiman |

El rojo domina en la niebla y en los acentos; no se usan otros colores de marca como decoración.

**Nieblas (`bg.fog`):** portada, derecha, izquierda, centro, abajo, arriba, rosa y ninguna. Son degradados radiales definidos en `FOGS`. Llevan **textura de grano** (`bg.grain: true`) encima.

## Tipografía
- **Roboto únicamente.** Es la fuente que siman.com carga de verdad: ClanOT, Postea y Maven Pro están declaradas, pero no se cargan.
- Va embebida como fuente variable (`marca/roboto.woff`, pesos 100–900, ancho 75–100 %).
- **Contraste de pesos:**
  - títulos en 300 (Light) con la frase clave en **800** (`<b>`);
  - tamaños de título de 90–140;
  - interlineado de 1,0–1,05 e interletrado de −2 en títulos;
  - cuerpo en 22–34, peso 300, interlineado de 1,35–1,5.
- Cifras grandes con el elemento `counter`, en tamaños de 150–260 y peso 800.

## Formas y componentes
- **Radios:** 16 / 8 / 100 px (los de la web); tarjetas de cristal de 28.
- **Tarjeta de cristal (`glassCard`):** fondo translúcido con desenfoque y borde fino. Sirve para agrupar texto.
- **Rombo:** el isotipo de SIMAN es un rombo con S. Se usa como viñeta o detalle, nunca deformado.
- **Capturas:** van en `image` con `radius` 20–28, `glow: true` y una inclinación (`tilt`) leve de −14 a 14. Animan desde abajo o desde un lado.
- **Elementos interactivos:**
  - `search`: el buscador que escribe solo, para mostrar lo que busca un comprador;
  - `flip`: tarjeta que gira, para las citas del focus group;
  - `counter`: cifra animada.
- **Íconos:** set Lucide (72 en `fuente/icons2.json`), blancos sobre círculo burdeos `#A83338`.

## Logotipos (en `marca/`)
- `siman-com-logotipo-blanco.svg`: oficial, tomado del encabezado de la web. Se usa en el cromado de cada lámina.
- `siman-com-logotipo-tinta.svg`: derivado, para fondos claros.
- `siman-isotipo-*.svg`: rombo con S.
- No alteres proporciones ni colores del logotipo.

## Ritmo narrativo (storytelling)
- Alterna láminas de **frase grande** con láminas de **evidencia**: captura, cifra o cita.
- Cada lámina tiene un solo mensaje.
- Animaciones: aparecer, subir o acercar, escalonadas como máximo 0,08 s × 10. No abuses de ellas.

## Referencias visuales
- `referencias/Opcion_A.jpg`, `Opcion_B.jpg` (la elegida) y `Opcion_C.jpg`.
- `marca/referencias/`: capturas de siman.com y redes.
- `marca/SIMAN_ADN_de_marca_Compra_Clara.html` y `marca/SIMAN_web_sistema_visual_Compra_Clara.html`: guías completas de marca y de la UI web.
