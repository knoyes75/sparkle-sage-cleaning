"""Place every hero image, photo and vector graphic on the site.

Rule: every photo appears on exactly one page. Vector graphics come from
graphics/*.svg (built by tools/build_graphics.py) and are inlined so their
text stays readable to search engines.

If a planned photo is not in images/ yet, the hero falls back to the brand
pattern and the photo slot is skipped. Add the file and re-run.

Run: python3 update_media.py
"""
import os
import re
from collections import Counter

SITE_URL = "https://sparkle-sage-site.vercel.app"
ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

P = lambda f, alt, cap: ("photo", f, alt, cap)
G = lambda name, cap: ("svg", name, cap)
O = lambda f, name, role: ("owner", f, name, role)

PAGES = {
    "index.html": dict(hero=("hero-home.jpg", "Bright, freshly cleaned Tampa Bay living room and kitchen"), slots=[
        G("services", "Residential, commercial and Airbnb cleaning across Tampa Bay"),
        G("map-tampa-bay", "Our Tampa Bay service area: Tampa, St. Petersburg, Clearwater and Brandon"),
    ]),
    "residential.html": dict(hero=("hero-residential.jpg", "Clean open-concept dining and living room in a Tampa Bay home"), slots=[
        P("res-1.jpg", "Sanitized master bathroom with glass shower after a residential cleaning in Tampa", "Bathroom Sanitization"),
        P("res-2.jpg", "Detailed kitchen cleaning with spotless stainless appliances in a Tampa Bay home", "Kitchen Detailing"),
    ]),
    "commercial.html": dict(hero=("hero-commercial.jpg", "Modern commercial office lobby cleaned by Sparkle & Sage"), slots=[
        P("com-1.jpg", "Clean office workstations and reception desk after commercial cleaning in Tampa Bay", "Office Workstations"),
        P("com-2.jpg", "Spotless glass-walled conference room cleaned by Sparkle & Sage", "Conference Rooms"),
    ]),
    "airbnb.html": dict(hero=("hero-airbnb.jpg", "Guest-ready vacation rental bedroom with fresh linens"), slots=[
        P("air-1.jpg", "Restocked vacation rental kitchen and coffee bar ready for guest check-in", "Turnover Restocking"),
        P("air-2.jpg", "Clean vacation rental living room with pool lanai in Tampa Bay", "Guest-Ready Living Spaces"),
    ]),
    "about.html": dict(hero=None, slots=[
        O("echo-downs-owner.jpg", "Echo Downs", "Owner, Sparkle &amp; Sage Cleaning Services"),
        G("values", "What we stand for"),
    ]),
    "contact.html": dict(hero=None, slots=[
        G("booking", "Booking takes three quick steps"),
    ]),
    "faq.html": dict(hero=None, slots=[
        G("checklist", "Every standard clean covers these rooms and tasks"),
        G("frequency", "Weekly, bi-weekly and monthly scheduling"),
    ]),
    "tampa.html": dict(hero=("hero-tampa.jpg", "Palm-lined Tampa waterfront boulevard on Tampa Bay"), slots=[
        G("map-tampa", "Tampa neighborhoods we serve"),
        P("loc-1.jpg", "Tampa Florida home exterior served by Sparkle & Sage Cleaning", "Tampa Properties"),
    ]),
    "st-petersburg.html": dict(hero=("hero-st-petersburg.jpg", "St. Petersburg, FL waterfront and marina"), slots=[
        G("map-st-petersburg", "St. Petersburg areas we serve"),
        P("st-pete-1.jpg", "Freshly cleaned St. Petersburg home interior", "St. Pete Homes"),
    ]),
    "clearwater.html": dict(hero=("hero-clearwater.jpg", "Clearwater Beach, FL shoreline"), slots=[
        G("map-clearwater", "Clearwater areas we serve"),
        P("clearwater-1.jpg", "Guest-ready Clearwater beach rental living room", "Clearwater Rentals"),
    ]),
    "brandon.html": dict(hero=("hero-brandon.jpg", "Brandon, FL suburban neighborhood"), slots=[
        G("map-brandon", "Brandon and East Tampa Bay communities we serve"),
        P("brandon-1.jpg", "Clean family kitchen in a Brandon, FL home", "Brandon Residences"),
    ]),
}

PHOTO_FIG = '''
        <figure class="sage-photo my-8 rounded-2xl overflow-hidden shadow-md border border-slate-200">
            <img src="images/{f}" alt="{alt}" width="1200" height="670" loading="lazy" decoding="async" class="w-full h-72 object-cover">
            <figcaption class="p-3 bg-white text-center text-sm font-semibold text-emerald-800">{cap}</figcaption>
        </figure>'''
OWNER_FIG = '''
        <figure class="sage-photo my-8 flex flex-col sm:flex-row items-center gap-6 bg-emerald-50 rounded-2xl p-6 border border-emerald-100">
            <img src="images/{f}" alt="{name}, owner of Sparkle &amp; Sage Cleaning Services in Tampa Bay" width="600" height="803" loading="lazy" decoding="async" class="w-40 h-52 sm:w-48 sm:h-60 object-cover object-top rounded-2xl shadow-md border-4 border-white shrink-0">
            <figcaption class="text-center sm:text-left">
                <span class="block text-xs font-bold uppercase tracking-wider text-emerald-700">Meet the Owner</span>
                <span class="block mt-1 text-2xl font-extrabold text-slate-900">{name}</span>
                <span class="block mt-1 text-sm font-semibold text-slate-600">{role}</span>
            </figcaption>
        </figure>'''
SVG_FIG = '''
        <figure class="sage-graphic my-8">
            {svg}
            <figcaption class="pt-3 text-center text-sm font-semibold text-emerald-800">{cap}</figcaption>
        </figure>'''

HERO_RE = re.compile(r'<div class="absolute inset-0 z-0[^"]*">\s*(?:<img[^>]*>|<svg.*?</svg>)\s*</div>', re.S)
FIG_RE = re.compile(r'\s*<figure class="sage-(?:photo|graphic).*?</figure>', re.S)
OG_RE = re.compile(r'\s*<meta (?:property="og:image(?::alt)?"|name="twitter:(?:image|card)")[^>]*>', re.I)


def svg(name):
    for ext in (".html", ".svg"):
        path = os.path.join("graphics", name + ext)
        if os.path.exists(path):
            return open(path, encoding="utf-8").read()
    raise FileNotFoundError(name)


def has(f):
    return os.path.exists(os.path.join("images", f))


used, missing = Counter(), []
for page, cfg in PAGES.items():
    html = open(page, encoding="utf-8").read()

    hero = cfg["hero"]
    if hero and has(hero[0]):
        used[hero[0]] += 1
        hero_html = (f'<div class="absolute inset-0 z-0 opacity-40">\n            <img src="images/{hero[0]}" alt="{hero[1]}" '
                     f'width="1376" height="768" fetchpriority="high" class="w-full h-full object-cover">\n        </div>')
        og = hero[0]
    else:
        if hero:
            missing.append(hero[0])
        hero_html = f'<div class="absolute inset-0 z-0">\n            {svg("hero-pattern")}\n        </div>'
        og = "og-default.png"
    html, n = HERO_RE.subn(hero_html, html, count=1)
    assert n == 1, f"hero not found in {page}"

    html = FIG_RE.sub("", html)
    head, sep, main = html.partition("<main")
    paras = main.split("</p>")
    for idx, slot in zip((1, 4), cfg["slots"]):
        if slot[0] == "owner":
            used[slot[1]] += 1
            block = OWNER_FIG.format(f=slot[1], name=slot[2], role=slot[3])
        elif slot[0] == "photo":
            if not has(slot[1]):
                missing.append(slot[1])
                continue
            used[slot[1]] += 1
            block = PHOTO_FIG.format(f=slot[1], alt=slot[2], cap=slot[3])
        else:
            block = SVG_FIG.format(svg=svg(slot[1]), cap=slot[2])
        if len(paras) > idx + 1:
            paras[idx + 1] = block + paras[idx + 1]
    html = head + sep + "</p>".join(paras)

    html = OG_RE.sub("", html)
    html = html.replace("</head>", f'\n    <meta property="og:image" content="{SITE_URL}/images/{og}">'
                        f'\n    <meta name="twitter:card" content="summary_large_image">'
                        f'\n    <meta name="twitter:image" content="{SITE_URL}/images/{og}">\n</head>', 1)
    open(page, "w", encoding="utf-8").write(html)
    print("updated", page)

dupes = [f for f, c in used.items() if c > 1]
assert not dupes, f"photos used more than once: {dupes}"
unused = sorted(f for f in os.listdir("images") if f.endswith(".jpg") and f not in used)
print("\nphotos placed:", len(used), "| duplicates: none")
if missing:
    print("waiting on photos:", ", ".join(missing))
if unused:
    print("in images/ but not placed:", ", ".join(unused))
