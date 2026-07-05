# 部署手册（Step-by-Step）

> 目标：30-60 分钟内，把 `chuansushang.com` 上线，指向 Cloudflare Pages 上的传溯个人网站。

---

## 0. 准备工作（5 分钟）

需要准备的东西：
- ✅ 一个**邮箱**（用来注册 Cloudflare 和 GitHub）
- ✅ **信用卡 / 支付宝 / PayPal**（Cloudflare Registrar 注册域名需要，约 ¥80/年）
- ✅ 这个项目已经在本地 `C:\Users\shang\Desktop\chuansu-site`，并且 **git 已经初始化并首次提交完成** ✅
- ✅ 一个 **GitHub 账户**（如果还没有，去 https://github.com/signup 注册）

---

## 步骤 1 · 注册 Cloudflare 账户（2 分钟）

1. 打开 https://dash.cloudflare.com/sign-up
2. 填邮箱 + 设置密码
3. 验证邮箱（Cloudflare 会发一封验证邮件，点里面的链接）
4. 登录到 Cloudflare Dashboard

---

## 步骤 2 · 在 Cloudflare Registrar 注册域名（10 分钟）

> Cloudflare Registrar 是**成本价**（不加价），通常比 Namecheap / GoDaddy 便宜 5-20%。

1. 打开 https://dash.cloudflare.com/?to=/:account/registrar
2. 点 **"Register domains"**
3. 在搜索框输入 **`chuansushang.com`**
4. 确认显示 **"Available"** → 选 **1 year** → 点 **"Continue"**
5. 填联系信息（**建议勾选 Privacy** —— Cloudflare 默认开启 Whois 隐私保护）
6. 支付（支持 Visa / Mastercard / Amex / PayPal / 支付宝）
7. **支付完成后等 1-5 分钟**，域名会自动激活

> 备选方案：如果你选 `chuansu.studio` 或 `chuansu.me`，流程完全一样。

---

## 步骤 3 · 在 GitHub 创建仓库（3 分钟）

1. 打开 https://github.com/new
2. 填：
   - **Repository name**: `chuansu-site`
   - **Description**: `Personal site for Jason Shang · 27Fall 美本申请辅材`
   - **Public / Private**: 选 **Public**（Cloudflare Pages 免费版支持私有仓库，但 Public 更方便）
   - **不要**勾选 "Add a README file" / ".gitignore" / "license"（本地已经有了）
3. 点 **"Create repository"**
4. **复制 HTTPS URL**（形如 `https://github.com/你的用户名/chuansu-site.git`）

---

## 步骤 4 · 把本地代码 push 到 GitHub（5 分钟）

打开 PowerShell / 终端：

```powershell
cd "C:\Users\shang\Desktop\chuansu-site"
git remote add origin https://github.com/你的用户名/chuansu-site.git
git branch -M main
git push -u origin main
```

推送时会弹窗要 GitHub 登录，按照提示登录即可。

> 如果你之前没用过 git 推 GitHub，登录方式：
> - 推荐用 **GitHub CLI**（`winget install GitHub.cli`）然后 `gh auth login`
> - 或用 **Personal Access Token**（GitHub Settings → Developer settings → Personal access tokens → Generate new token，勾选 `repo` 权限）

---

## 步骤 5 · 在 Cloudflare Pages 连接 GitHub（10 分钟）

1. 打开 https://dash.cloudflare.com/?to=/:account/pages
2. 点 **"Create a project"** → **"Connect to Git"**
3. 选择 **GitHub**，会跳到 GitHub 授权页
4. 授权 Cloudflare 访问你的 GitHub 账户
5. 选择 **`chuansu-site`** 仓库 → 点 **"Begin setup"**
6. 填项目设置：
   - **Project name**: `chuansu-site`（会成为默认的 `chuansu-site.pages.dev` 子域名）
   - **Production branch**: `main`
   - **Build command**: **留空**（我们是纯静态，不需要 build）
   - **Build output directory**: **留空**（默认就是项目根目录）
   - **Root directory**: **留空**
7. 点 **"Save and Deploy"**

第一次部署需要 1-3 分钟。完成后会显示 **"Success!"**，并给一个临时域名 `chuansu-site.pages.dev`。

**点击临时域名预览网站**，确认一切正常。

---

## 步骤 6 · 绑定自定义域名（5 分钟）

1. 在 Cloudflare Pages 项目页，点 **"Custom domains"** 标签
2. 点 **"Set up a custom domain"**
3. 输入 **`chuansushang.com`** → 点 **"Continue"**
4. Cloudflare 会自动检测你的域名在 Cloudflare Registrar，自动添加 CNAME / 重定向到 `chuansu-site.pages.dev`
5. **DNS 配置通常几秒钟就生效**
6. 重复步骤 2-5，再添加 **`www.chuansushang.com`**（可选，但建议加上，做 301 重定向到主域）

---

## 步骤 7 · 验证 + 上线（5 分钟）

打开浏览器测试：

1. ✅ **访问 `https://chuansushang.com`** —— 应该看到完整的传溯网站
2. ✅ **访问 `https://chuansushang.com/research/`** —— 应该跳到 Research 页
3. ✅ **访问 `https://chuansushang.com/projects/safehome/`** —— SafeHome 深度页
4. ✅ **测试 HTTPS** —— 浏览器地址栏应该有 🔒 锁
5. ✅ **测试 www 重定向** —— 访问 `www.chuansushang.com` 应该跳到 `chuansushang.com`
6. ✅ **手机访问** —— 切到手机模式，看响应式

如果都 OK，**恭喜上线**！

---

## 上线后要做的事（10-15 分钟）

### 8.1 替换邮箱地址
打开 6 个 HTML 文件，搜索 `jason.shang@outlook.com`，替换成你的真实邮箱。

```bash
cd "C:\Users\shang\Desktop\chuansu-site"
# 用 PowerShell 批量替换
Get-ChildItem -Recurse -Filter *.html | ForEach-Object {
  (Get-Content $_.FullName -Raw) -replace 'jason\.shang@outlook\.com', 'your-real-email@gmail.com' | Set-Content $_.FullName -NoNewline
}
git add . && git commit -m "Replace placeholder email" && git push
```

Cloudflare Pages 会自动重新部署（30 秒）。

### 8.2 （可选）替换 OG / Twitter Card
在每个 HTML 的 `<head>` 加 OG 图，招生官转发链接时显示预览图。可以用 Canva / Figma 做一张 1200×630 的卡。

### 8.3 把网站链接加到申请材料
- Common App Activities 描述里加一句："更多项目细节请见 chuansushang.com/projects/safehome/"
- 简历上加一行："Personal site: chuansushang.com"
- 给推荐人发邮件附上链接："FYI, here's some additional context about my work: chuansushang.com"

---

## 9. 故障排查（万一出问题了）

### 网站打不开 / 显示 404
- 检查 `_redirects` 和 `_headers` 是否被 Cloudflare Pages 正确识别
- 在 Cloudflare Pages → Deployments → 点最新一次 → 看 build log

### 静态资源（图片/CSS）加载失败
- 检查 `assets/img/xxx.jpg` 路径是否正确（区分 `../` 层级）
- 看 DevTools → Network → 哪些 404

### HTTPS 没生效
- Cloudflare Pages 默认自动签发证书，等 5-15 分钟
- 在 Cloudflare Pages → Custom domains → 看 status

### 自定义域名显示 "not found"
- 确认 DNS 记录已添加（在 Cloudflare DNS → 应该看到 `chuansushang.com CNAME chuansu-site.pages.dev`）
- 等 DNS 传播（最多 24 小时，通常 5 分钟）

---

## 10. 后续维护

每次改完代码：

```bash
cd "C:\Users\shang\Desktop\chuansu-site"
# 改完文件后
git add .
git commit -m "更新了xxx"
git push
```

Cloudflare Pages 会**自动**拉取新代码并部署。**30 秒到 1 分钟**后线上生效。

---

## 11. 申请季结束后

如果以后想把网站撤掉或换别的：
- 域名不续费即可（不会自动扣款，到期前会邮件提醒）
- Cloudflare Pages 项目可以随时删除，GitHub 仓库也可以设为 Private 或删除

---

## 12. 进阶（可选，看兴趣）

- **加分析**：注册 Plausible.io（隐私友好、无需 cookie 横幅），知道哪个招生官看了哪些页
- **加评论**（比如 Disqus）—— 不推荐，会让页面变重
- **换主题**：网站是纯静态，将来想换样式直接改 CSS 就行
- **加中英双语**：复制 HTML 到 `/en/` 子目录
- **做 PDF 简历下载**：把简历做成 PDF 放在 `assets/JasonShang_Resume.pdf`

---

## 时间表（按时区计划）

| 步骤 | 预计耗时 | 难度 |
|---|---|---|
| 1. 注册 Cloudflare | 2 min | ⭐ |
| 2. 注册域名 | 10 min | ⭐ |
| 3. GitHub 仓库 | 3 min | ⭐ |
| 4. push 代码 | 5 min | ⭐⭐ |
| 5. Cloudflare Pages 链接 | 10 min | ⭐⭐ |
| 6. 绑域名 | 5 min | ⭐ |
| 7. 验证 | 5 min | ⭐ |
| 8. 上线后清理 | 10 min | ⭐ |

**总计：~50 分钟**，可以一口气搞完，也可以分两次（先域名+Cloudflare Pages，第二天清理 + 替换邮箱）。

---

有任何一步卡住，随时叫我。我可以**实时**指导：你在哪个页面看到什么、应该点哪个按钮、应该填什么值。