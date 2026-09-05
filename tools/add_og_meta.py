# -*- coding: utf-8 -*-
"""Insert OG + Twitter card meta into all pages of chuansu-site. Idempotent."""
import io, re, os

BASE = "https://chuansu-site.shangweilei.workers.dev"
IMG = BASE + "/og-image.jpg"

PAGES = [
    ("index.html", "/", "Jason Shang · Materials for Fragile Systems",
     "用材料科学保护脆弱系统——从灭火到水凝胶，从产品到人性认知。"),
    ("about/index.html", "/about/", "About · Jason Shang",
     "商传溯（Jason Shang）——深中国际部 27Fall 申请者。GPA 4.52 / SAT 1570 / TOEFL 117。"),
    ("projects/safehome/index.html", "/projects/safehome/", "SafeHome · Jason Shang",
     "SafeHome——把灭火材料从实验室搬进真实家庭、学校、宿舍、社区。"),
    ("projects/chemisfun/index.html", "/projects/chemisfun/", "Chemisfun · Jason Shang",
     "Chemisfun——把复杂化学讲给普通人听的科普平台。"),
    ("research/index.html", "/research/", "Research · Jason Shang",
     "水凝胶与皮肤修复研究——从灭火材料到组织修复的材料科学。"),
    ("writing/index.html", "/writing/", "Writing · Jason Shang",
     "Notes, reflections, science — Jason Shang 的写作。"),
]

TPL = """  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{img}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:site_name" content="Jason Shang">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="{img}">
"""

root = "C:/Users/shang/Desktop/chuansu-site"
for rel, path, title, desc in PAGES:
    fp = os.path.join(root, rel)
    with io.open(fp, "r", encoding="utf-8") as f:
        src = f.read()
    if "og:image" in src:
        print("skip (already has og:image):", rel)
        continue
    block = TPL.format(title=title, desc=desc, url=BASE + path, img=IMG)
    # insert right after the meta description line
    m = re.search(r'[ \t]*<meta name="description"[^>]*>\s*\n', src)
    if not m:
        m = re.search(r'[ \t]*<title>[^<]*</title>\s*\n', src)
    if m:
        src = src[:m.end()] + block + src[m.end():]
    else:
        raise SystemExit("no anchor found in " + rel)
    with io.open(fp, "w", encoding="utf-8", newline="") as f:
        f.write(src)
    print("updated:", rel)

# update Last updated footer
for rel, *_ in PAGES:
    fp = os.path.join(root, rel)
    with io.open(fp, "r", encoding="utf-8") as f:
        src = f.read()
    new = src.replace("Last updated 2026.07", "Last updated 2026.09")
    if new != src:
        with io.open(fp, "w", encoding="utf-8", newline="") as f:
            f.write(new)
        print("footer updated:", rel)
