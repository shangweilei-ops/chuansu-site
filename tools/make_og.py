# -*- coding: utf-8 -*-
"""Generate 1200x630 OG share card for chuansu-site, matching site design tokens."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1200, 630
INK = (15, 27, 45)        # --c-ink
INK2 = (42, 58, 84)       # lighter ink
EMBER = (212, 103, 58)    # --c-ember
PAPER = (250, 247, 241)   # --c-paper
SKY = (59, 110, 165)      # --c-sky
FADE = (168, 178, 192)

F = "C:/Windows/Fonts/"
serif = F + "georgia.ttf"
serif_b = F + "georgiab.ttf"
serif_i = F + "georgiai.ttf"
mono = F + "consolab.ttf"
cn = F + "msyhbd.ttc"

img = Image.new("RGB", (W, H), INK)
d = ImageDraw.Draw(img)

# --- subtle vertical gradient (ink -> slightly lighter at bottom-right) ---
grad = Image.new("L", (1, H))
for y in range(H):
    grad.putpixel((0, y), int(30 * (y / H)))
grad = grad.resize((W, H))
warm = Image.new("RGB", (W, H), (34, 50, 74))
img = Image.composite(warm, img, grad)
d = ImageDraw.Draw(img)

# --- ember glow, bottom-left ---
glow = Image.new("RGB", (W, H), (0, 0, 0))
gd = ImageDraw.Draw(glow)
gd.ellipse((-260, H - 200, 460, H + 260), fill=(60, 30, 16))
gd.ellipse((-160, H - 120, 360, H + 180), fill=(92, 44, 20))
glow = glow.filter(ImageFilter.GaussianBlur(90))
img = Image.blend(img, Image.composite(glow, img, Image.new("L", (W, H), 255)), 0.55)
# simpler: additive blend
img = Image.blend(img, glow, 0.35)
d = ImageDraw.Draw(img)

# --- top rule + eyebrow ---
d.line((80, 96, 240, 96), fill=EMBER, width=3)
f_eyebrow = ImageFont.truetype(mono, 24)
d.text((80, 118), "JASON SHANG  ·  CLASS OF 2027", font=f_eyebrow, fill=FADE)
f_cn_small = ImageFont.truetype(cn, 24)
d.text((560, 114), "商传溯 · 深圳中学国际部", font=f_cn_small, fill=FADE)

# --- main title (serif) ---
f_t1 = ImageFont.truetype(serif, 92)
f_t2i = ImageFont.truetype(serif_i, 92)
f_t2b = ImageFont.truetype(serif_b, 92)
y = 190
d.text((78, y), "Materials for", font=f_t1, fill=PAPER)
y += 118
d.text((78, y), "fragile", font=f_t2i, fill=EMBER)
w_fragile = d.textlength("fragile ", font=f_t2i)
d.text((78 + w_fragile, y), "systems.", font=f_t2b, fill=PAPER)

# --- sub line ---
f_sub = ImageFont.truetype(serif, 30)
d.text((80, 448), "Hydrogel  ·  Fire-safe materials  ·  Skin repair", font=f_sub, fill=(214, 222, 232))
f_sub_i = ImageFont.truetype(serif_i, 28)
d.text((80, 496), "用材料科学，保护那些脆弱的系统。", font=ImageFont.truetype(cn, 27), fill=FADE)

# --- footer url ---
f_url = ImageFont.truetype(mono, 22)
d.text((80, 566), "chuansu-site.shangweilei.workers.dev", font=f_url, fill=(120, 132, 150))

# --- corner marks (frame) ---
m = 36
ln = 26
for (x1, y1, x2, y2) in [(m, m, m + ln, m), (m, m, m, m + ln),
                          (W - m, m, W - m - ln, m), (W - m, m, W - m, m + ln),
                          (m, H - m, m + ln, H - m), (m, H - m, m, H - m - ln),
                          (W - m, H - m, W - m - ln, H - m), (W - m, H - m, W - m, H - m - ln)]:
    d.line((x1, y1, x2, y2), fill=(90, 104, 124), width=2)

img.save("C:/Users/shang/Desktop/chuansu-site/og-image.jpg", quality=92)
print("saved og-image.jpg", img.size)
