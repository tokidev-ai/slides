import re, sys, html, os
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from slides import S

P = os.path.join(ROOT, 'index.html')
src = open(os.path.join(HERE, 'base.html'), encoding='utf-8').read()

tokens = {
  '--cs-primary': '#1FD3F5', '--cs-secondary': '#D2F21E', '--cs-accent': '#FF4B3A',
  '--cs-accent-ink': '#FF5A4A', '--cs-on-primary': '#02101F',
  '--cs-cream': '#020D22', '--cs-cream-2': '#071A3A',
  '--cs-black': '#FFFFFF', '--cs-body': '#C9D6EA', '--cs-muted': '#93A4C2', '--cs-white': '#FFFFFF',
  '--cs-surface': '#06183A', '--cs-void': '#00040C',
  '--cs-border': 'rgba(31,211,245,0.22)', '--cs-border-strong': 'rgba(31,211,245,0.40)', '--cs-scrim': 'rgba(31,211,245,0.07)',
  '--cs-grad-radial': 'radial-gradient(112% 150% at 0% 100% in oklch, #06183A 0%, #020D22 100%)',
  '--cs-grad-linear': 'linear-gradient(90deg in oklch, #1FD3F5 0%, #D2F21E 100%)',
  '--cs-grad-text': 'linear-gradient(90deg in oklch, #1FD3F5 0%, #7FE58E 50%, #D2F21E 100%)',
  '--cs-font-sans': "'Archivo', ui-sans-serif, system-ui, sans-serif",
  '--cs-font-heading': "'Anton', 'Archivo', ui-sans-serif, sans-serif",
  '--cs-font-mono': "'Share Tech Mono', ui-monospace, 'SF Mono', Menlo, monospace",
  '--cs-weight-heading': '400',
}
root_m = re.search(r':root \{.*?\n  \}', src, re.S)
root = root_m.group(0)
for k, v in tokens.items():
    root, n = re.subn(rf'({re.escape(k)}:\s*)[^;]+;', lambda m: m.group(1) + v + ';', root, count=1)
    if n == 0:
        root = root.replace('\n  }', f'\n    {k}: {v};\n  }}')
src = src.replace(root_m.group(0), root)

src = re.sub(r'<link href="https://fonts.googleapis.com/css2[^"]*" rel="stylesheet">',
  '<link href="https://fonts.googleapis.com/css2?family=Anton&family=Archivo:wght@400;500;600;700&family=Share+Tech+Mono&display=swap" rel="stylesheet">', src, count=1)

css = open(os.path.join(HERE, 'custom.css'), encoding='utf-8').read()
src = src.replace('</style>\n</head>', css + '\n</style>\n</head>', 1)

src = re.sub(r'<html lang="[^"]*"', '<html lang="es"', src, count=1)
src = re.sub(r'<title>.*?</title>', '<title>De programar con IA a construir con agentes · SCD Cochabamba</title>', src, count=1, flags=re.S)

out = []
for i, (label, cls, steps, body, notes) in enumerate(S, 1):
    nn = f'{i:02d}'
    c = f' class="{cls}"' if cls else ''
    cur = '1' if steps == 1 else '0'
    out.append(f'''
  <section{c} data-label="{nn} {label}" data-steps="{steps}" data-current-step="{cur}">{body}
    <aside class="notes"><p>{html.escape(notes)}</p></aside>
    <div class="footer">
      <div class="left">Student Community Day · Cochabamba</div>
      <div>Rodrigo Torrico · <span class="num">{nn}</span></div>
    </div>
  </section>''')
slides = '\n'.join(out)

start = src.index('<!-- ────────── EXAMPLE 1')
end = src.index('</deck-stage>')
src = src[:start] + slides + '\n\n' + src[end:]
open(P, 'w', encoding='utf-8').write(src)
print('slides:', len(S))
