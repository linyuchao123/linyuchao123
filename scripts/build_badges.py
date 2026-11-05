"""Build local badges using Lobe Icons SVGs from an extracted npm package.
Usage: python3 scripts/build_badges.py /path/to/package/icons
"""
from pathlib import Path
import sys, re, html
src=Path(sys.argv[1]); out=Path(__file__).resolve().parents[1]/'assets/badges'
items=[('Codex','codex','codex','181818'),('Claude Code','claude','claudecode','D97757'),('Muse','m','muse','8B5CF6'),('WorkBuddy','w','workbuddy','4976EF'),('VS Code','visualstudiocode',None,'007ACC'),('Qoder','qoder','qoder','6C5CE7'),('Cursor','cursor','cursor','222222'),('Trae','trae','trae','149E8E'),('ChatGPT','openai','openai','10A37F'),('Gemini','googlegemini','gemini','4285F4'),('DeepSeek','deepseek','deepseek','4D6BFE'),('Kimi','kimi','kimi','222222'),('Qwen 千问','qwen','qwen','615CED'),('GLM 智谱','zhipu','zhipu','3855CB'),('Doubao 豆包','doubao','doubao','17B89B')]
for name,slug,icon,c in items:
 if icon:
  raw=(src/f'{icon}.svg').read_text(); inner=raw[raw.index('>')+1:raw.rindex('</svg>')]; inner=re.sub(r'<title>.*?</title>','',inner)
 else:
  inner='<path d="M17 1 7 10 2 6 0 7v10l2 1 5-4 10 9 7-3V4zm0 5v12l-7-6z"/>'
 width=44+sum(13 if ord(x)>127 else 7 for x in name)
 svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="30" viewBox="0 0 {width} 30"><rect width="{width}" height="30" rx="7" fill="#{c}"/><svg x="8" y="6" width="18" height="18" viewBox="0 0 24 24" fill="white" color="white" fill-rule="evenodd">{inner}</svg><text x="34" y="20" fill="white" font-size="12" font-family="Arial,PingFang SC,sans-serif">{html.escape(name)}</text></svg>'
 (out/f'{slug}.svg').write_text(svg)
# Claude model uses Claude icon; Claude Code badge uses its dedicated icon.
p=out/'claude-model.svg'; raw=(src/'claude.svg').read_text(); inner=raw[raw.index('>')+1:raw.rindex('</svg>')]
s=(out/'claude.svg').read_text().replace('Claude Code','Claude')
s=re.sub(r'(<svg x=.*?>).*?(</svg>)',lambda m:m[1]+inner+m[2],s,flags=re.S)
p.write_text(s)
