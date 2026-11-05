"""Build an ASCII portrait that is progressively revealed by a scanning line.
Pillow is used to sample the source avatar; output is a self-contained animated SVG.
"""
from pathlib import Path
from html import escape
from PIL import Image, ImageOps
root=Path(__file__).resolve().parents[1]
im=ImageOps.autocontrast(Image.open(root/'assets/avatar.png').convert('RGB')).resize((100,67))
chars=' .:;+=xX$&#@'
head='''<svg xmlns="http://www.w3.org/2000/svg" width="480" height="536" viewBox="0 0 480 536" role="img" aria-labelledby="title desc">
<title id="title">Lin Yuchao — animated ASCII portrait</title>
<desc id="desc">The avatar and cat appear gradually from top to bottom over six seconds, hold, then repeat.</desc>
<defs>
<linearGradient id="border"><stop stop-color="#a897ed"/><stop offset="1" stop-color="#62cbdc"/></linearGradient>
<linearGradient id="beam" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#38bdf8" stop-opacity="0"/><stop offset="1" stop-color="#38bdf8" stop-opacity=".3"/></linearGradient>
<clipPath id="frame"><rect x="20" y="65" width="440" height="440" rx="10"/></clipPath>
<clipPath id="reveal"><rect x="20" y="65" width="440" height="440"><animate attributeName="height" values="0;440;440;440;0" keyTimes="0;.6;.88;.999;1" dur="10s" repeatCount="indefinite"/></rect></clipPath>
</defs>
<style>.glyph{font-family:Menlo,Consolas,monospace;font-size:7px}.label{font-family:Menlo,Consolas,monospace;fill:#64748b;font-size:11px}.shell{fill:#fff}.line{stroke:#e2e8f0}@media(prefers-color-scheme:dark){.shell{fill:#151e2d}.label{fill:#a1b0c7}.line{stroke:#303c55}}@media(prefers-reduced-motion:reduce){.moving{display:none}.portrait{clip-path:none!important;opacity:1!important}}</style>
<rect class="shell" x="1" y="1" width="478" height="534" rx="20" stroke="url(#border)"/>
<circle cx="23" cy="26" r="4" fill="#ff6c70"/><circle cx="37" cy="26" r="4" fill="#ffca57"/><circle cx="51" cy="26" r="4" fill="#51ce7b"/>
<text x="170" y="30" class="label">portrait.ascii</text><path class="line" d="M20 47H460"/>
<g clip-path="url(#frame)"><rect x="20" y="65" width="440" height="440" fill="#101b2d"/>
<g class="portrait" clip-path="url(#reveal)" opacity="1"><animate attributeName="opacity" values="1;1;1;0;0" keyTimes="0;.6;.88;.99;1" dur="10s" repeatCount="indefinite"/>
'''
parts=[head]
for y in range(67):
 for x in range(100):
  r,g,b=im.getpixel((x,y)); lum=(.299*r+.587*g+.114*b)/255
  # Gamma lifts midtones so the face remains legible at README display sizes.
  lum=lum**.65; char=chars[min(11,int(lum*12))]
  if char==' ':char='·'
  c=f'rgb({int(40+lum*175)},{int(65+lum*185)},{int(90+lum*165)})'
  parts.append(f'<text x="{20+x*4.4:.1f}" y="{71+y*6.53:.2f}" class="glyph" fill="{c}">{escape(char)}</text>')
parts.append('''</g><g class="moving" opacity="1"><animate attributeName="opacity" values="1;1;0;0" keyTimes="0;.6;.601;1" dur="10s" repeatCount="indefinite"/>
<g><animateTransform attributeName="transform" type="translate" values="0 0;0 440;0 440" keyTimes="0;.6;1" dur="10s" repeatCount="indefinite"/>
<rect x="20" y="37" width="440" height="28" fill="url(#beam)"/><path d="M20 65H460" stroke="#6ce5ff" stroke-width="2"/></g></g></g>
<text x="20" y="523" class="label">LIN YUCHAO / SCANNING PORTRAIT</text></svg>''')
full=''.join(parts)
(root/'assets/portrait-scan.svg').write_text(full)
# Borderless square for the equal-sized README cards; animation uses the same coordinates.
square=full.replace('width="480" height="536" viewBox="0 0 480 536"', 'width="440" height="440" viewBox="20 65 440 440"')
(root/'assets/portrait-square.svg').write_text(square)
print('Built portrait-scan.svg: 6s reveal + hold + fade, repeating every 10s.')
