# De programar con IA a construir con agentes

Slides de la charla de Rodrigo Torrico ([@tokidev.ai](https://instagram.com/tokidev.ai)) para **Student Community Day Cochabamba**, 10 de octubre de 2026.

30 slides sobre harness engineering, skills, loop engineering y orquestación con Orca. Cada slide trae sus notas de presentador. El diseño sigue el template oficial del SCD Cochabamba, con su fondo de grilla, sus corchetes neón y la mascota Kori.

Las slides se hicieron con [slizdeck](https://github.com/pedroanze/slizdeck).

## Cómo presentar

| Archivo | Para qué |
|---|---|
| `index.html` | Versión principal. Necesita la carpeta `assets/` al lado. Sirve para GitHub Pages. |
| `dist/sdc-agents-deck.html` | Un solo archivo con imágenes y fuentes embebidas. Funciona sin internet. |

Atajos de teclado:

- Flechas o espacio: avanzar y retroceder.
- `P`: modo presentador, con las notas.
- Botón de la esquina superior derecha: pantalla completa.

## Cómo editar

El contenido vive en `build/`:

- `slides.py`: el texto, el layout y las notas de cada slide.
- `custom.css`: la piel del SCD (paneles HUD, anillos numerados, cita, terminal).
- `base.html`: el template de slizdeck con el pack `terminal` ya aplicado.
- `assemble.py`: aplica los tokens de color y fuentes y genera `index.html`.
- `standalone.py`: genera `dist/sdc-agents-deck.html`.

Para regenerar los dos archivos:

```bash
python3 build/assemble.py
python3 build/standalone.py
```

Para validar con slizdeck (necesita Chrome):

```bash
node <slizdeck>/scripts/audit.mjs index.html
node <slizdeck>/scripts/check-overflow.mjs index.html
node <slizdeck>/scripts/shoot.mjs index.html
```

## Créditos

- Fondo, Cristo y mascota Kori: template oficial de Student Community Day Cochabamba.
- Fuentes: Anton, Archivo y Share Tech Mono (SIL Open Font License), incluidas en `assets/fonts/`.
