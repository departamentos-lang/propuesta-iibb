# Arma la copia pública (presentacion.html y el PDF) desde la presentación final de la carpeta del proyecto:
# sin notas del orador, sin comentarios del código y con un aviso para girar el teléfono.
import re, shutil, pathlib
W = pathlib.Path(__file__).parent
P = W.parent.parent  # la carpeta del proyecto, «Presentación Provincia»
I = P / 'Presentacion interactiva'
h = (I / 'Presentación IIBB propuesta.html').read_text(encoding='utf-8')
h = re.sub(r'\s*data-speaker-notes="[^"]*"', '', h)
h = re.sub(r'<!--.*?-->\n?', '', h, flags=re.S)
h = re.sub(r'/\*.*?\*/', '', h, flags=re.S)
h = re.sub(r'const BLOQUES=\[.*?\n\];\n', '', h, count=1, flags=re.S)
assert 'data-speaker-notes' not in h and 'BLOQUES' not in h and 'Gentile' not in h
h = h.replace('</body>', '''<div id="girar"><span>↻</span>Girá el teléfono para ver la presentación más grande. Para pasar, deslizá con el dedo.</div>
<style>#girar{display:none;position:fixed;left:12px;right:12px;bottom:12px;z-index:50;padding:12px 16px;border-radius:14px;background:rgba(2,22,48,.92);border:1px solid rgba(134,208,244,.4);color:#fff;font:15px/1.4 Ubuntu,system-ui,sans-serif;text-align:center}
#girar span{display:inline-block;margin-right:8px;color:#1ED68F;font-size:18px}
@media (orientation:portrait) and (max-width:820px){#girar{display:block}}</style>
</body>''', 1)
(W / 'presentacion.html').write_text(h, encoding='utf-8')
shutil.copy(I / 'Presentación IIBB propuesta.pdf', W / 'propuesta-iibb-uipba.pdf')
shutil.copy(P / 'Informe Ingresos Brutos completo' / 'Informe IIBB modificado.pdf', W / 'documento-tecnico-iibb-uipba.pdf')  # el diagnóstico con el anexo de propuestas
shutil.copy(I / 'QR propuesta IIBB.png', W / 'QR propuesta IIBB.png')
shutil.copy(W.parent / 'QR propuesta IIBB.svg', W / 'QR propuesta IIBB.svg')
print('listo:', len(h), 'bytes')
