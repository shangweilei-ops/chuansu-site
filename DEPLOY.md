# 部署指南 · 域名 + 服务器

> 给传溯个人网站的部署 / 上线建议。三个层次，按预算和需求挑。

---

## 一、域名（Domain Name）

### 推荐域名（按优先级）

| 域名 | 优点 | 缺点 | 价格（首年） | 推荐度 |
|---|---|---|---|---|
| `chuansu.com` | 简短、好记、英文圈通用 | 可能已被注册 | ~¥80 | ⭐⭐⭐⭐⭐ |
| `chuansushang.com` | 拼写完整、避免歧义 | 略长 | ~¥80 | ⭐⭐⭐⭐ |
| `jasonshang.com` | 国际化、招生官友好 | 可能已被注册 | ~¥80 | ⭐⭐⭐⭐⭐ |
| `jason-shang.com` | 同上 | 连字符略输 | ~¥80 | ⭐⭐⭐ |
| `chuansu.studio` | 适合个人项目气质 | `.studio` 略小众 | ~¥200 | ⭐⭐⭐ |
| `jasonshang.me` | 个人品牌 | `.me` 偏博客感 | ~¥80 | ⭐⭐ |

**我的建议**：
- **首选**：`chuansu.com` 或 `jasonshang.com`（短、好记、和名字直接对应）
- **次选**：`chuansushang.com`（避免歧义）
- **如果主域名被抢**：可考虑 `chuansu.studio` 或 `jasonshang.io`

### 在哪买

| 注册商 | 价格 | 备注 |
|---|---|---|
| **Cloudflare Registrar** | 成本价（无加价） | ⭐ 推荐，DNS 解析全球最快 |
| Namecheap | 便宜，首年常有折扣 | 续费略贵 |
| GoDaddy | 略贵，UI 友好 | 中规中矩 |
| 阿里云 / 腾讯云 | 国内访问快 | 需要实名备案才能绑国内服务器 |

**海外招生官看 → 选 Cloudflare 或 Namecheap**（不用备案、全球 CDN、隐私保护）。

---

## 二、托管平台（Hosting）

这是零依赖的静态网站，**不需要买服务器**。三个推荐方案，按推荐度排序：

### 方案 A：Cloudflare Pages ⭐⭐⭐⭐⭐（首推）

- **价格**：**免费**（个人项目永久免费，无限流量）
- **速度**：全球 CDN，比大多数付费 VPS 还快
- **HTTPS**：自动签发 + 自动续期
- **部署**：连 GitHub 仓库 → push 即部署
- **域名**：直接绑你自己的域名即可
- **适合**：美本申请主战场，招生官从全球任何地方访问都飞快

**步骤**：
1. 把代码 push 到 GitHub（私有仓也行）
2. Cloudflare 注册 → Pages → Connect Git → 选仓库
3. Build settings 全部留空（纯静态无构建）
4. Custom domain → 改 Cloudflare 自己的 DNS → 完成

### 方案 B：Vercel ⭐⭐⭐⭐⭐

- **价格**：**免费**（个人项目无限流量）
- **速度**：与 Cloudflare 同档，开发者体验更好
- **HTTPS**：自动
- **特点**：如果以后想加 React/Next.js，无缝迁移
- **缺点**：国内访问偶尔慢

### 方案 C：Netlify ⭐⭐⭐⭐

- **价格**：**免费**（100GB 流量/月，个人项目绝对够）
- **特点**：表单收集、identity 都很方便
- **缺点**：比 Cloudflare / Vercel 略慢一点

### 方案 D：GitHub Pages ⭐⭐⭐

- **价格**：**免费**
- **特点**：最简单，但**国内访问不稳定**
- **建议**：作为备份，主战场用 Cloudflare

### ❌ 不推荐：自购 VPS

- 阿里云 / 腾讯云轻量服务器（~¥60/月起）
- 优点：自由度高
- 缺点：要备案、要运维、自己配 HTTPS、要防攻击
- **对个人 Portfolio 来说严重过重**

---

## 三、我的推荐组合

**最低成本 + 最高效果**：

```
域名：chuansu.com（或 jasonshang.com）
      Cloudflare Registrar 注册，约 ¥80/年

托管：Cloudflare Pages
      免费，无限流量，全球 CDN

DNS：Cloudflare 自带
      自动解析，自动 HTTPS

总成本：约 ¥80/年（约 $11）
```

---

## 四、上线 Checklist

域名 / 服务器搞完之后，按这个顺序收尾：

1. ✅ 替换真实邮箱（`jason.shang@outlook.com` → 真实地址）
2. ✅ 替换占位的项目时间 / 数据（按真实情况）
3. ✅ 加上 OG 图（1200×630 的社交分享卡，招生官转发时显示）
4. ✅ 加上 Favicon（多尺寸，建议用一个简化的 "JS" 或水凝胶图标）
5. ✅ 用 [PageSpeed Insights](https://pagespeed.web.dev/) 跑一遍性能（目标 90+）
6. ✅ 用 [WAVE](https://wave.webaim.org/) 跑一遍可访问性
7. ✅ 跨设备检查（手机 / 平板 / 桌面）
8. ✅ 把链接加到简历 / Common App Activities / 推荐信材料里

---

## 五、域名备案问题

如果只用海外服务（Cloudflare / Vercel / GitHub Pages），**不需要备案**。

只有当你买国内服务器、或把域名解析到国内 IP 时才需要 ICP 备案（7-20 天）。

**对美本申请 → 强烈不建议备案**，因为：
- 海外访问备案后可能反而慢
- 流程繁琐
- 没必要

---

## 六、扩展建议（如果以后想升级）

| 升级方向 | 推荐做法 |
|---|---|
| 加博客系统 | 迁移到 Vercel + MDX / Notion API |
| 加作品集 PDF 下载 | 加 `assets/JasonShang_Portfolio.pdf` |
| 加中英双语 | 复制页面做 `/en/` 路由 |
| 加访客分析 | Plausible.io（隐私友好，不需 cookie 提示） |
| 加 OG 图自动生成 | Vercel OG Image 或 @vercel/og |

---

## 七、时间线建议

美本申请季时间敏感：

- **7 月内**：注册域名 + 部署到 Cloudflare Pages（30 分钟搞定）
- **8 月**：把占位内容全部替换为真实（产品图、研究海报、Chemisfun 链接）
- **9 月**：把网站 URL 加进简历、Common App Additional Info、推荐信附注
- **10-11 月**：招生官打开时能看到一个完整的、可信的人设空间

---

有问题随时找我，整个部署过程我可以一步步带。