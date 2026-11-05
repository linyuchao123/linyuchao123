"""Generate skill cards and circular connection buttons. Pass Simple Icons package directory."""
from pathlib import Path
import re,sys
from html import escape
root=Path(__file__).resolve().parents[1]; out=root/'assets/connect';out.mkdir(exist_ok=True)
icons=Path(sys.argv[1])/'icons'
items=[('github','GitHub','github'),('x','Twitter / X','x'),('website','个人网站',None),('wechat','个人微信','wechat'),('official','微信公众号','wechat'),('qq','QQ 邮箱','qq'),('gmail','Gmail','gmail')]
for slug,label,icon in items:
 if icon:
  raw=(icons/f'{icon}.svg').read_text(); body=raw[raw.index('>')+1:raw.rindex('</svg>')];body=re.sub(r'<title>.*?</title>','',body)
 else:body='<circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="1.6"/><ellipse cx="12" cy="12" rx="4" ry="9" fill="none" stroke="currentColor" stroke-width="1.4"/><path d="M3 12h18M5 7h14M5 17h14" fill="none" stroke="currentColor" stroke-width="1.4"/>'
 color={'wechat':'#16a065','official':'#16a065','gmail':'#d94b40','qq':'#1686d9'}.get(slug,'#17243b')
 svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="90" height="92" viewBox="0 0 90 92" role="img" aria-label="{label}"><defs><linearGradient id="edge"><stop stop-color="#b0a0d4"/><stop offset="1" stop-color="#7ebcbd"/></linearGradient></defs><circle cx="45" cy="33" r="25" fill="#fff" stroke="url(#edge)" stroke-width="1.2"/><svg x="33" y="21" width="24" height="24" viewBox="0 0 24 24" fill="{color}" color="{color}">{body}</svg><text x="45" y="80" text-anchor="middle" font-size="11.5" font-family="Arial,PingFang SC,sans-serif" fill="#59677e">{escape(label)}</text></svg>'''
 (out/f'{slug}.svg').write_text(svg)
# A transparent local info/skills panel lets the surrounding GitHub theme show through.
body='<style>text{font-family:Arial,PingFang SC,sans-serif;fill:#28364c}.label{font-family:Menlo,Consolas,monospace;fill:#7f8da5}@media(prefers-color-scheme:dark){text{fill:#dce7f5}.label{fill:#a3b1c8}}</style>'
for y,k,v in [(23,'focus','AI 应用开发 · AI 智能体 · RAG'),(56,'building','From ideas to working products'),(89,'writing','老林的AI探秘日常')]:
 body+=f'<text x="18" y="{y}" class="label" font-size="13">{k}</text><text x="128" y="{y}" font-size="16">{v}</text>'
body+='<text x="18" y="126" class="label" font-size="12" letter-spacing="2">SKILLS / TOOLKIT</text>'
rows=[['Python','TypeScript','JavaScript','React','Vue'],['FastAPI','LangChain','LangGraph','RAG','AI Agents'],['ASR / TTS','Multimodal AI','Redis','Docker','Git']]
for row,tags in enumerate(rows):
 x=18;y=142+row*41
 for tag in tags:
  w=26+len(tag)*7.4
  body+=f'<rect x="{x}" y="{y}" width="{w}" height="29" rx="14.5" fill="#9a8ce5" fill-opacity=".07" stroke="#a7b7de" stroke-opacity=".7"/><text x="{x+w/2}" y="{y+19}" text-anchor="middle" font-size="12.5">{escape(tag)}</text>'
  x+=w+10
(root/'assets/info-skills.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="650" height="270" viewBox="0 0 650 270" role="img" aria-label="专注 AI 应用与智能体；15 个技术标签">{body}</svg>')
print('Built 7 brand buttons and 15 skill tags.')
