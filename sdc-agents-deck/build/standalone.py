"""Genera dist/sdc-agents-deck.html: un solo archivo con imagenes y fuentes embebidas (data: URI)."""
import re, base64, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MIME = {'.woff2': 'font/woff2', '.jpg': 'image/jpeg', '.png': 'image/png'}

def data_uri(rel):
    with open(os.path.join(ROOT, rel), 'rb') as f:
        return f"data:{MIME[os.path.splitext(rel)[1]]};base64," + base64.b64encode(f.read()).decode()

src = open(os.path.join(ROOT, 'index.html'), encoding='utf-8').read()
src = re.sub(r'<link href="https://fonts.googleapis.com/css2[^"]*" rel="stylesheet">\n?', '', src)
src = re.sub(r'(assets/[A-Za-z0-9_\-/]+\.(?:woff2|jpg|png))', lambda m: data_uri(m.group(1)), src)
os.makedirs(os.path.join(ROOT, 'dist'), exist_ok=True)
out = os.path.join(ROOT, 'dist', 'sdc-agents-deck.html')
open(out, 'w', encoding='utf-8').write(src)
print('ok', out, f'{len(src)/1e6:.1f} MB')
