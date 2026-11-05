# 主页设计与维护

- 保留原有 capsule-render 紫色横幅，横幅下为左右双栏：左侧本地扫描头像 SVG，右侧使用原版蓝色打字 SVG 服务与统计徽章。
- SVG 只含矢量与声明式动画，无脚本、外部字体或图片依赖。头像逐步显现：0–6 秒从上到下扫描，6–8.8 秒停留，随后淡出；每 10 秒循环。减少动态效果时显示完整头像。
- GitHub README 不支持自定义 CSS / JavaScript 悬浮弹层。微信入口使用原生 details 点击展开，兼容触屏。
- 二维码为用户提供的原文件，不重绘；公众号名称由用户确认。实际扫码指向仍建议由账号本人检查。
- 迹中局介绍依据其公开仓库 README；北京线下三天开发来自用户提供的信息。未增加获奖或量化成绩。
- 旧统计图替换为本地开发方向卡片，不伪造贡献统计。顶部访问量、关注数和星标仍是第三方动态徽章。
- 品牌图标来自 @lobehub/icons-static-svg 1.102.0（MIT），项目 https://github.com/lobehub/lobe-icons 。VS Code 使用其标志形状。Muse 按个人智能体 App 收录，采用该图标库的 Muse 图标，待本人确认品牌是否一致。
- 参考 https://github.com/arielshakaramiro/arielshakaramiro 的终端双栏与扫描概念；本仓库重新生成布局及头像，未复制参考 SVG 源码。

重新生成扫描头像：`python3 scripts/build_portrait.py`（需要 Pillow）。重新生成徽章：`python3 scripts/build_badges.py <解包后的图标包/icons目录>`。

发布目标为本仓库 main 分支；历史静态截图仅供对照，最新交互预览入口为 previews/index.html。

本次修订按用户反馈恢复原版蓝色逐字动画，删除替代文字信息卡；顶部横幅 HTML 与仓库原始提交逐字一致。

## 右侧卡片修订

- 保留原版蓝色三行逐字介绍与原服务 URL；不再添加紫色姓名标题。
- 右侧加入 15 个技术标签及 7 个圆形品牌入口：GitHub、X、网站、微信、公众号、QQ 邮箱和 Gmail。
- README 的微信 / 公众号圆形按钮直接打开原始二维码图片；下方仍有点击展开二维码的入口。
- `previews/index.html` 为独立本地预览，微信与公众号支持鼠标悬浮或键盘聚焦弹出二维码。这段 CSS 不放入 README，因为 GitHub 会过滤。
- 圆形品牌图标采用 Simple Icons 16.36.0（CC0，https://simpleicons.org/），网站使用通用地球符号。
- 重新生成圆形按钮与标签：`python3 scripts/build_connect.py <Simple Icons 解包目录/package>`。

## 卡片尺寸对齐

左右列统一为 50% / 50%，顶部对齐。头像使用无外框的正方形 SVG，由同规格卡片容器承载；两侧终端标题栏共用 650 × 42 尺寸，预览中的内边距、圆角、边框也完全相同。

## 边框细化

两侧终端栏采用同规格细渐变描边与淡色底，章节间使用透明渐变分隔线；圆形入口边框降低饱和度。以上 SVG 装饰可直接在 GitHub 显示。本地 HTML 额外提供圆角容器与轻阴影；GitHub 外层表格边框由平台样式控制。

生成装饰素材：`python3 scripts/build_frames.py`。
