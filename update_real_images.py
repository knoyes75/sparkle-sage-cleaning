"""Swap the inline SVG placeholders for the local photos in images/.

Safe to re-run: it strips any SVG placeholders and any previously inserted
photo blocks, then inserts two fresh photo blocks per page after the 2nd and
5th paragraphs inside <main>. Also adds og:image / twitter:image tags.
"""
import os
import re

SITE_URL = "https://sparkle-sage-site.vercel.app"

# page: [(image, alt text, caption), (image, alt text, caption)], og image
PAGES = {
    "index.html": ([
        ("res-2.jpg", "Spotless white kitchen with polished counters cleaned by Sparkle & Sage in Tampa Bay", "Professional Housekeeping"),
        ("com-1.jpg", "Clean modern office reception area serviced by Sparkle & Sage Tampa Bay", "Commercial Office Care"),
    ], "hero-home.jpg"),
    "residential.html": ([
        ("res-1.jpg", "Sanitized master bathroom with glass shower after a residential cleaning in Tampa", "Bathroom Sanitization"),
        ("res-2.jpg", "Detailed kitchen cleaning with spotless stainless appliances in a Tampa Bay home", "Kitchen Detailing"),
    ], "hero-residential.jpg"),
    "commercial.html": ([
        ("com-1.jpg", "Clean office workstations and reception desk after commercial cleaning in Tampa Bay", "Office Workstations"),
        ("com-2.jpg", "Spotless glass-walled conference room cleaned by Sparkle & Sage", "Conference Rooms"),
    ], "hero-commercial.jpg"),
    "airbnb.html": ([
        ("air-1.jpg", "Restocked vacation rental kitchen and coffee bar ready for guest check-in", "Turnover Restocking"),
        ("air-2.jpg", "Clean vacation rental living room with pool lanai in Tampa Bay", "Guest-Ready Living Spaces"),
    ], "hero-airbnb.jpg"),
    "about.html": ([
        ("loc-2.jpg", "Sparkle & Sage Cleaning Services team members in Tampa Bay", "Tampa Bay Team"),
        ("loc-1.jpg", "Tampa Bay Florida home served by Sparkle & Sage Cleaning Services", "Community Commitment"),
    ], "hero-home.jpg"),
    "contact.html": ([
        ("loc-2.jpg", "Sparkle & Sage cleaning professionals ready to book your Tampa Bay cleaning", "Booking & Scheduling"),
        ("res-1.jpg", "Freshly cleaned bathroom from a Sparkle & Sage residential service", "Tampa Bay Service"),
    ], "hero-home.jpg"),
    "faq.html": ([
        ("res-2.jpg", "Kitchen cleaned to Sparkle & Sage standards in a Tampa Bay home", "Cleaning Standards"),
        ("air-1.jpg", "Vacation rental kitchen turnover with flexible scheduling", "Scheduling Flexibility"),
    ], "hero-home.jpg"),
    "tampa.html": ([
        ("loc-1.jpg", "Tampa Florida home exterior served by Sparkle & Sage Cleaning", "Tampa Properties"),
        ("loc-2.jpg", "Local Sparkle & Sage cleaning experts serving Tampa", "Local Cleaning Experts"),
    ], "hero-tampa.jpg"),
    "st-petersburg.html": ([
        ("air-2.jpg", "Clean St. Petersburg vacation home living area with pool lanai", "St. Pete Beach & Homes"),
        ("loc-1.jpg", "Coastal St. Petersburg Florida home cleaned by Sparkle & Sage", "Coastal Cleaning"),
    ], "hero-tampa.jpg"),
    "clearwater.html": ([
        ("air-2.jpg", "Guest-ready Clearwater vacation rental after turnover cleaning", "Clearwater Rentals"),
        ("loc-2.jpg", "Sparkle & Sage team handling Clearwater beach house turnovers", "Beach House Turnover"),
    ], "hero-tampa.jpg"),
    "brandon.html": ([
        ("res-2.jpg", "Spotless kitchen in a Brandon Florida residence cleaned by Sparkle & Sage", "Brandon Residences"),
        ("loc-2.jpg", "Sparkle & Sage cleaning team serving Brandon and East Tampa Bay", "East Tampa Bay Care"),
    ], "hero-tampa.jpg"),
}

BLOCK = '''
        <figure class="sage-photo my-8 rounded-2xl overflow-hidden shadow-md border border-slate-200">
            <img src="images/{img}" alt="{alt}" width="1200" height="670" loading="lazy" decoding="async" class="w-full h-72 object-cover">
            <figcaption class="p-3 bg-white text-center text-sm font-semibold text-emerald-800">{cap}</figcaption>
        </figure>
'''

SVG_RE = re.compile(r'\s*<svg viewBox="0 0 800 450".*?</svg>\s*', re.DOTALL)
OLD_BLOCK_RE = re.compile(r'\s*<figure class="sage-photo.*?</figure>\s*', re.DOTALL)
OG_RE = re.compile(r'\s*<meta (?:property="og:image"|name="twitter:(?:image|card)")[^>]*>', re.I)

os.chdir(os.path.dirname(os.path.abspath(__file__)))

for filename, (photos, og_img) in PAGES.items():
    if not os.path.exists(filename):
        continue
    with open(filename, encoding="utf-8") as f:
        content = f.read()

    content = SVG_RE.sub("\n", content)
    content = OLD_BLOCK_RE.sub("\n", content)

    head, sep, main = content.partition("<main")
    if not sep:
        print(f"Skipped {filename}: no <main>")
        continue
    paras = main.split("</p>")
    # paras[i] + "</p>" is paragraph i; insert a photo right after paragraphs 1 and 4
    for idx, (img, alt, cap) in zip((1, 4), photos):
        if len(paras) > idx + 1:
            paras[idx + 1] = BLOCK.format(img=img, alt=alt, cap=cap).rstrip("\n") + paras[idx + 1]
    content = head + sep + "</p>".join(paras)

    og = (f'\n    <meta property="og:image" content="{SITE_URL}/images/{og_img}">'
          f'\n    <meta name="twitter:card" content="summary_large_image">'
          f'\n    <meta name="twitter:image" content="{SITE_URL}/images/{og_img}">')
    content = OG_RE.sub("", content)
    content = content.replace("</head>", og + "\n</head>", 1)

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {filename}")
