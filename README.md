# Jason Shang · Personal Site

> Materials for fragile systems — 传溯（Jason Shang）的个人网站，美本申请辅材。

## 项目结构

```
chuansu-site/
├── index.html                # 主页（单页叙事）
├── assets/
│   ├── css/main.css          # 主样式（设计令牌 + 全部组件）
│   └── js/main.js            # 轻量交互（移动端菜单 + 滚动入场）
├── research/
│   └── index.html            # Hydrogel & Skin Repair 深度页
├── projects/
│   ├── safehome/index.html   # SafeHome 产品页
│   └── chemisfun/index.html  # Chemisfun 科普页
├── writing/
│   └── index.html            # 4 篇 essay
├── about/
│   └── index.html            # 申请画像
└── screenshots/              # 预览截图
```

## 本地预览

```bash
cd chuansu-site
python -m http.server 8765
# 浏览器打开 http://localhost:8765/
```

或者用任意静态服务器（VSCode Live Server / `npx serve` 都可）。

## 技术栈

- **零依赖**：纯 HTML + CSS + 原生 JS，无构建步骤
- **字体**：Google Fonts (Crimson Pro + Inter + JetBrains Mono)
- **响应式**：mobile-first，< 768px 自动切换汉堡菜单
- **可访问性**：`prefers-reduced-motion` 已支持，无 JS 也能完整浏览

## 视觉设计令牌

| Token | 值 | 用途 |
|---|---|---|
| `--c-ink` | `#0F1B2D` | 主文字、深蓝 |
| `--c-ember` | `#D4673A` | 强调色、暖橙 |
| `--c-paper` | `#FAF7F1` | 页面底色（米白） |
| `--c-sky` | `#3B6EA5` | 次要强调、蓝色 |
| `--f-serif` | Crimson Pro | 标题、引文 |
| `--f-sans` | Inter | 正文、UI |
| `--f-mono` | JetBrains Mono | 标签、meta |

## 修改建议

1. **真实邮箱 / 联系方式**：搜索 `jason.shang@outlook.com` 替换为真实地址
2. **真实照片 / 产品图**：在 `assets/img/` 建子目录，把图占位换掉
3. **项目时间 / 数据**：所有"2025 / 2026 / 3 years"等根据真实情况调整
4. **学术成果**：一旦论文 / 海报产出，把 PDF 放进 `assets/` 并在 Research 页加链接
5. **OG / Twitter Card 图**：建议做一张 1200×630 的社交分享图

## 部署

详见 `DEPLOY.md`。