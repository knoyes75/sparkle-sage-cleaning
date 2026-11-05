"""Build the site's vector graphics into graphics/*.svg.

Maps use OpenStreetMap-derived land polygons (geo-maps earth-lands-250m, ODbL,
(c) OpenStreetMap contributors), clipped to Tampa Bay in
tools/data/tampa-bay-land.geojson and smoothed for an illustrated look.

Run: python3 tools/build_graphics.py
"""
import json
import math
import os
from html import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "graphics")
os.makedirs(OUT, exist_ok=True)

# Brand palette
EM900, EM700, EM600, EM500 = "#064e3b", "#047857", "#059669", "#10b981"
EM100, EM50 = "#d1fae5", "#ecfdf5"
AMBER, AMBER_D = "#fbbf24", "#b45309"
SL900, SL600, SL400, SL200 = "#0f172a", "#475569", "#94a3b8", "#e2e8f0"
WATER, WATER_D, WATER_T = "#dbeef5", "#b9dbe8", "#3b7d95"
LAND, LAND_EDGE = "#f3f7f1", "#9cc9ae"
FONT = "style=\"font-family:inherit\""


def svg_open(w, h, title, desc, ident):
    return (f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{escape(title)}" '
            f'aria-labelledby="{ident}-t {ident}-d" class="w-full h-auto block" {FONT}>'
            f'<title id="{ident}-t">{escape(title)}</title><desc id="{ident}-d">{escape(desc)}</desc>')


def save(name, svg):
    with open(os.path.join(OUT, name + ".svg"), "w", encoding="utf-8") as f:
        f.write(svg)
    print("wrote graphics/%s.svg (%d bytes)" % (name, len(svg)))


# ---------------------------------------------------------------- maps
LAND_GEO = json.load(open(os.path.join(ROOT, "tools", "data", "tampa-bay-land.geojson")))


def rings():
    polys = LAND_GEO["coordinates"] if LAND_GEO["type"] == "MultiPolygon" else [LAND_GEO["coordinates"]]
    for poly in polys:
        for ring in poly:
            yield ring


def chaikin(pts, n=3):
    for _ in range(n):
        out = []
        for i in range(len(pts) - 1):
            (x0, y0), (x1, y1) = pts[i], pts[i + 1]
            out += [(0.75 * x0 + 0.25 * x1, 0.75 * y0 + 0.25 * y1), (0.25 * x0 + 0.75 * x1, 0.25 * y0 + 0.75 * y1)]
        out.append(out[0])
        pts = out
    return pts


class Proj:
    def __init__(self, bbox, w):
        self.lon0, self.lat0, self.lon1, self.lat1 = bbox
        self.k = math.cos(math.radians((self.lat0 + self.lat1) / 2))
        self.w = w
        self.s = w / ((self.lon1 - self.lon0) * self.k)
        self.h = round((self.lat1 - self.lat0) * self.s)

    def __call__(self, lat, lon):
        return ((lon - self.lon0) * self.k * self.s, (self.lat1 - lat) * self.s)


def land_path(p):
    """Project, clip and simplify land polygons for one map view."""
    from shapely.geometry import shape, box
    from shapely import affinity
    from shapely.geometry import Polygon
    geom = shape(LAND_GEO).buffer(0)
    view = box(p.lon0 - 0.02, p.lat0 - 0.02, p.lon1 + 0.02, p.lat1 + 0.02)
    geom = geom.intersection(view)
    # to pixel space: x = (lon-lon0)*k*s, y = (lat1-lat)*s
    geom = affinity.affine_transform(geom, [p.k * p.s, 0, 0, -p.s, -p.lon0 * p.k * p.s, p.lat1 * p.s])
    geom = geom.simplify(1.3)
    d = []
    for poly in getattr(geom, "geoms", [geom]):
        if poly.geom_type != "Polygon" or poly.area < 80:
            continue
        holes = [r for r in poly.interiors if Polygon(r).area > 2500]
        for ring in [poly.exterior, *holes]:
            pts = chaikin(list(ring.coords), 2)
            d.append("M" + " L".join("%.1f %.1f" % xy for xy in pts) + " Z")
    return " ".join(d)


def label(x, y, text, size=15, weight=600, fill=SL900, anchor="start", halo=True, italic=False, cls=""):
    style = (' font-style="italic"' if italic else "") + (f' class="{cls}"' if cls else "")
    h = (f'<text x="{x:.0f}" y="{y:.0f}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}"'
         f'{style} fill="none" stroke="#fff" stroke-width="4" stroke-linejoin="round" opacity="0.9">{escape(text)}</text>') if halo else ""
    return h + (f'<text x="{x:.0f}" y="{y:.0f}" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}"'
                f'{style} fill="{fill}">{escape(text)}</text>')


def pin(x, y, color=EM600, r=1.0):
    return (f'<g transform="translate({x:.1f} {y:.1f}) scale({r})">'
            f'<ellipse cx="0" cy="2" rx="7" ry="2.5" fill="{SL900}" opacity="0.18"/>'
            f'<path d="M0 0 C-4 -9 -13 -14 -13 -23 A13 13 0 0 1 13 -23 C13 -14 4 -9 0 0 Z" fill="{color}" stroke="#fff" stroke-width="2"/>'
            f'<circle cx="0" cy="-23" r="5" fill="#fff"/></g>')


def dot(x, y, color=EM700, r=5):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{color}" stroke="#fff" stroke-width="2"/>'


def compass(x, y):
    return (f'<g transform="translate({x} {y})" opacity="0.8"><circle r="18" fill="#fff" stroke="{SL200}"/>'
            f'<path d="M0 -13 L5 2 L0 -1 L-5 2 Z" fill="{EM700}"/><text y="14" font-size="9" font-weight="700" '
            f'text-anchor="middle" fill="{SL600}">N</text></g>')


def build_map(name, bbox, title, desc, city=None, places=(), cities=(), waters=(), radius_mi=None, w=800, banner=None, chip_label="Areas served"):
    p = Proj(bbox, w)
    h = p.h
    s = [svg_open(w, h, title, desc, name).replace("<svg ", f'<svg id="{name}" ', 1),
         f'<style>@media (max-width:640px){{#{name} .nb,#{name} .wl,#{name} .lg{{display:none}}#{name} .c1{{font-size:44px}}#{name} .c2{{font-size:32px}}}}</style>',
         f'<defs><clipPath id="{name}-c"><rect width="{w}" height="{h}" rx="18"/></clipPath>'
         f'<pattern id="{name}-wv" width="22" height="10" patternUnits="userSpaceOnUse">'
         f'<path d="M0 6 Q5.5 2 11 6 T22 6" fill="none" stroke="{WATER_D}" stroke-width="1"/></pattern></defs>',
         f'<g clip-path="url(#{name}-c)">',
         f'<rect width="{w}" height="{h}" fill="{WATER}"/><rect width="{w}" height="{h}" fill="url(#{name}-wv)" opacity="0.6"/>',
         f'<path d="{land_path(p)}" fill="{LAND}" fill-rule="evenodd" stroke="{LAND_EDGE}" stroke-width="2" stroke-linejoin="round"/>']
    for wt in waters:
        x, y = p(wt["lat"], wt["lon"])
        s.append(label(x, y, wt["name"], size=wt.get("size", 15), weight=500, fill=WATER_T, anchor="middle", halo=False, italic=True, cls="wl"))
    if city and radius_mi:
        cx, cy = p(city["lat"], city["lon"])
        r = radius_mi / 69.0 * p.s
        s.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{EM500}" fill-opacity="0.10" '
                 f'stroke="{EM600}" stroke-width="2" stroke-dasharray="7 6"/>')
    for c in cities:  # other service cities (secondary)
        x, y = p(c["lat"], c["lon"])
        s.append(dot(x, y, SL400, 5) + label(x + c.get("dx", 10), y + c.get("dy", 5), c["name"], 14, 600, SL600, c.get("anchor", "start"), cls="c2"))
    for pl in places:  # neighborhoods
        x, y = p(pl["lat"], pl["lon"])
        s.append(dot(x, y, EM700, 4.5) + label(x + pl.get("dx", 9), y + pl.get("dy", 5), pl["name"], 14, 600, SL900, pl.get("anchor", "start"), cls="nb"))
    if city:
        x, y = p(city["lat"], city["lon"])
        s.append(pin(x, y, EM600, 1.25) + label(x + city.get("dx", 0), y + city.get("dy", -40), city["name"], 22, 800, EM900, city.get("anchor", "middle"), cls="c1"))
    for m in (banner or []):
        x, y = p(m["lat"], m["lon"])
        s.append(pin(x, y, m.get("color", EM600), 1.05) + label(x + m.get("dx", 0), y + m.get("dy", -34), m["name"], 18, 800, EM900, m.get("anchor", "middle"), cls="c1"))
    s.append(compass(w - 34, 34))
    # legend
    lg = f'<g class="lg" transform="translate(16 {h - 40})"><rect width="{220 if radius_mi else 190}" height="28" rx="8" fill="#fff" opacity="0.92"/>'
    if radius_mi:
        lg += (f'<circle cx="16" cy="14" r="7" fill="{EM500}" fill-opacity="0.15" stroke="{EM600}" stroke-dasharray="3 2"/>'
               f'<text x="30" y="19" font-size="12" font-weight="600" fill="{SL600}">~{radius_mi}-mile core service area</text>')
    else:
        lg += (f'<path d="M16 21 C14 17 10 15 10 11 A6 6 0 0 1 22 11 C22 15 18 17 16 21Z" fill="{EM600}"/>'
               f'<text x="30" y="19" font-size="12" font-weight="600" fill="{SL600}">Sparkle &amp; Sage service city</text>')
    s.append(lg + "</g>")
    s.append(f'<text x="{w - 10}" y="{h - 8}" font-size="10" text-anchor="end" fill="{SL400}">Map data \u00a9 OpenStreetMap contributors</text>')
    s.append(f'<rect width="{w}" height="{h}" rx="18" fill="none" stroke="{SL200}" stroke-width="2"/></g></svg>')
    svg = "".join(s)
    save(name, svg)
    names = [pl["name"] for pl in places] or [m["name"] for m in (banner or [])]
    chips = "".join(f'<li class="px-3 py-1 rounded-full bg-emerald-50 border border-emerald-200 text-emerald-900 text-xs font-semibold">{escape(n)}</li>' for n in names)
    save_html(name, f'<div class="rounded-2xl overflow-hidden">{svg}</div><ul class="flex flex-wrap justify-center gap-2 mt-3" aria-label="{escape(chip_label)}">{chips}</ul>')


TAMPA = dict(name="Tampa", lat=27.950, lon=-82.457)
STPETE = dict(name="St. Petersburg", lat=27.771, lon=-82.640)
CLEAR = dict(name="Clearwater", lat=27.966, lon=-82.800)
BRANDON = dict(name="Brandon", lat=27.938, lon=-82.286)


def maps():
    build_map(
        "map-tampa-bay", (-82.98, 27.62, -82.16, 28.12),
        "Sparkle & Sage service area map of Tampa Bay",
        "Map of the Tampa Bay area showing the four cities Sparkle & Sage Cleaning Services serves: Tampa, St. Petersburg, Clearwater and Brandon.",
        banner=[dict(TAMPA, dy=-36), dict(STPETE, dx=0, dy=-36), dict(CLEAR, dx=0, dy=-36), dict(BRANDON, dy=-36)],
        waters=[dict(name="Gulf of Mexico", lat=27.80, lon=-82.89, size=17), dict(name="Tampa Bay", lat=27.72, lon=-82.57, size=17),
                dict(name="Old Tampa Bay", lat=27.90, lon=-82.62, size=13)])
    build_map(
        "map-tampa", (-82.64, 27.84, -82.28, 28.16),
        "Tampa cleaning service area map",
        "Map of Tampa, FL neighborhoods served by Sparkle & Sage, including Downtown, Ybor City, Channelside, Hyde Park, South Tampa, Westshore, Seminole Heights, Carrollwood and New Tampa.",
        city=dict(TAMPA, name="Tampa", dx=-34, dy=-40), radius_mi=8,
        places=[dict(name="Ybor City", lat=27.960, lon=-82.437, dx=9, dy=-6), dict(name="Channelside", lat=27.943, lon=-82.447, dx=9, dy=14),
                dict(name="Hyde Park", lat=27.937, lon=-82.474, dx=-9, dy=5, anchor="end"), dict(name="South Tampa", lat=27.900, lon=-82.497, dx=9, dy=5),
                dict(name="Westshore", lat=27.950, lon=-82.525, dx=-9, dy=5, anchor="end"), dict(name="Seminole Heights", lat=27.995, lon=-82.460, dx=9, dy=5),
                dict(name="Carrollwood", lat=28.050, lon=-82.505, dx=9, dy=5), dict(name="New Tampa", lat=28.130, lon=-82.360, dx=9, dy=5)],
        cities=[dict(BRANDON, dx=-10, dy=-12, anchor="end")],
        waters=[dict(name="Old Tampa Bay", lat=27.905, lon=-82.590), dict(name="Hillsborough Bay", lat=27.875, lon=-82.425)])
    build_map(
        "map-st-petersburg", (-82.82, 27.64, -82.54, 27.88),
        "St. Petersburg cleaning service area map",
        "Map of St. Petersburg, FL areas served by Sparkle & Sage, including Downtown, Old Northeast, Snell Isle, Kenwood, Gulfport and St. Pete Beach.",
        city=dict(STPETE, name="St. Petersburg", dx=-16, dy=26, anchor="end"), radius_mi=7,
        places=[dict(name="Old Northeast", lat=27.785, lon=-82.632, dx=9, dy=0), dict(name="Snell Isle", lat=27.797, lon=-82.618, dx=9, dy=-4),
                dict(name="Kenwood", lat=27.774, lon=-82.676, dx=-9, dy=5, anchor="end"), dict(name="Gulfport", lat=27.748, lon=-82.703, dx=-9, dy=5, anchor="end"),
                dict(name="St. Pete Beach", lat=27.725, lon=-82.738, dx=-9, dy=16, anchor="end"), dict(name="Pinellas Park", lat=27.842, lon=-82.699, dx=9, dy=5)],
        waters=[dict(name="Gulf of Mexico", lat=27.80, lon=-82.785), dict(name="Tampa Bay", lat=27.69, lon=-82.60)])
    build_map(
        "map-clearwater", (-82.90, 27.88, -82.66, 28.08),
        "Clearwater cleaning service area map",
        "Map of Clearwater, FL areas served by Sparkle & Sage, including Downtown Clearwater, Clearwater Beach, Sand Key, Countryside and nearby Dunedin and Largo.",
        city=dict(CLEAR, name="Clearwater", dx=24, dy=-40), radius_mi=6,
        places=[dict(name="Clearwater Beach", lat=27.977, lon=-82.827, dx=-9, dy=-8, anchor="end"), dict(name="Sand Key", lat=27.930, lon=-82.833, dx=-9, dy=5, anchor="end"),
                dict(name="Countryside", lat=28.035, lon=-82.737, dx=9, dy=5), dict(name="Dunedin", lat=28.020, lon=-82.772, dx=9, dy=5),
                dict(name="Largo", lat=27.910, lon=-82.787, dx=9, dy=5), dict(name="Safety Harbor", lat=27.991, lon=-82.693, dx=-9, dy=-8, anchor="end")],
        waters=[dict(name="Gulf of Mexico", lat=28.03, lon=-82.865), dict(name="Clearwater Harbor", lat=27.945, lon=-82.808, size=12)])
    build_map(
        "map-brandon", (-82.47, 27.80, -82.17, 28.06),
        "Brandon cleaning service area map",
        "Map of Brandon, FL and East Tampa Bay communities served by Sparkle & Sage, including Valrico, Seffner, Riverview and Bloomingdale.",
        city=dict(BRANDON, name="Brandon", dx=0, dy=-40), radius_mi=6,
        places=[dict(name="Valrico", lat=27.938, lon=-82.236, dx=9, dy=5), dict(name="Seffner", lat=27.984, lon=-82.276, dx=9, dy=5),
                dict(name="Riverview", lat=27.866, lon=-82.326, dx=9, dy=5), dict(name="Bloomingdale", lat=27.893, lon=-82.250, dx=9, dy=5)],
        cities=[dict(TAMPA, dx=10, dy=5)],
        waters=[dict(name="Hillsborough Bay", lat=27.86, lon=-82.435, size=13)])


# ---------------------------------------------------------------- icons
def icon_house(x, y, s=1, c=EM700):
    return (f'<g transform="translate({x} {y}) scale({s})" fill="none" stroke="{c}" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round">'
            f'<path d="M-26 2 L0 -22 L26 2"/><path d="M-19 -4 V24 H19 V-4"/><rect x="-6" y="8" width="12" height="16"/>'
            f'<path d="M14 -14 V-24 H20 V-9"/></g>')


def icon_building(x, y, s=1, c=EM700):
    return (f'<g transform="translate({x} {y}) scale({s})" fill="none" stroke="{c}" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round">'
            f'<rect x="-20" y="-24" width="40" height="48" rx="3"/><path d="M-10 -14h6M4 -14h6M-10 -3h6M4 -3h6M-10 8h6M4 8h6"/>'
            f'<path d="M-5 24 V16 H5 V24"/></g>')


def icon_bed(x, y, s=1, c=EM700):
    return (f'<g transform="translate({x} {y}) scale({s})" fill="none" stroke="{c}" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round">'
            f'<path d="M-26 20 V-14 M-26 6 H26 V20 M26 6 V-2 Q26 -8 20 -8 H-2 V6"/><circle cx="-14" cy="-2" r="6"/>'
            f'<path d="M14 -22 l2 -5 l2 5 l5 2 l-5 2 l-2 5 l-2 -5 l-5 -2 z" fill="{AMBER}" stroke="{AMBER}" stroke-width="1.5"/></g>')


def sparkle(x, y, s=1, c=AMBER):
    return (f'<path transform="translate({x} {y}) scale({s})" d="M0 -10 Q1.5 -1.5 10 0 Q1.5 1.5 0 10 Q-1.5 1.5 -10 0 Q-1.5 -1.5 0 -10Z" fill="{c}"/>')


def card(x, y, w, h, fill="#fff", stroke=SL200):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="{fill}" stroke="{stroke}" stroke-width="2"/>'


def g_phone(x, y):
    return (f'<g transform="translate({x} {y})" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">'
            f'<rect x="-11" y="-18" width="22" height="36" rx="4"/><path d="M-4 12h8"/><path d="M-5 -7h10M-5 -1h7" stroke="{AMBER}"/></g>')


def g_quote(x, y):
    return (f'<g transform="translate({x} {y})" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">'
            f'<rect x="-14" y="-17" width="28" height="34" rx="3"/><path d="M-7 -7h14M-7 0h14M-7 7h8"/>'
            f'<text x="9" y="20" font-size="15" font-weight="800" fill="{AMBER}" stroke="none">$</text></g>')


def g_sparkles(x, y):
    return (f'<g transform="translate({x} {y})">' + sparkle(-6, 2, 1.5, "#fff") + sparkle(12, -11, 0.8, AMBER) + sparkle(11, 12, 0.6, "#fff") + "</g>")


def g_leaf(x, y):
    return (f'<g transform="translate({x} {y})" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">'
            f'<path d="M-14 14 C-14 -6 -2 -16 16 -16 C16 4 4 14 -14 14Z"/><path d="M-14 14 L6 -6"/></g>')


def g_shield(x, y):
    return (f'<g transform="translate({x} {y})" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">'
            f'<path d="M0 -18 L15 -12 V0 C15 10 7 16 0 19 C-7 16 -15 10 -15 0 V-12 Z"/><path d="M-6 0 l4 5 l8 -9" stroke="{AMBER}"/></g>')


def g_star(x, y):
    return (f'<path transform="translate({x} {y})" d="M0 -17 L5 -6 L17 -5 L8 3 L11 15 L0 9 L-11 15 L-8 3 L-17 -5 L-5 -6 Z" '
            f'fill="none" stroke="#fff" stroke-width="3" stroke-linejoin="round"/>')


def save_html(name, html):
    with open(os.path.join(OUT, name + ".html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote graphics/%s.html (%d bytes)" % (name, len(html)))


def ico(body, size=56, view=64, stroke=EM700, bg=EM100):
    """Small inline SVG icon in a soft circle (decorative)."""
    return (f'<span class="inline-flex items-center justify-center rounded-full shrink-0" style="width:{size}px;height:{size}px;background:{bg}">'
            f'<svg viewBox="{-view/2} {-view/2} {view} {view}" width="{int(size*0.62)}" height="{int(size*0.62)}" aria-hidden="true">{body}</svg></span>')


I_HOUSE = icon_house(0, 0, 0.95)
I_BUILD = icon_building(0, 0, 0.95)
I_BED = icon_bed(0, 0, 0.95)
W = lambda g: g(0, 0)  # white glyphs from the step icons


def services():
    items = [("Residential Cleaning", "Homes, condos and deep cleans for busy Tampa Bay households.", I_HOUSE, "residential.html"),
             ("Commercial Cleaning", "Offices, medical suites and retail spaces, cleaned around your hours.", I_BUILD, "commercial.html"),
             ("Airbnb Turnovers", "Linens, restocking and guest-ready resets between every stay.", I_BED, "airbnb.html")]
    cards = "".join(
        f'<a href="{href}" class="group block bg-white rounded-2xl border border-slate-200 p-5 text-center hover:border-emerald-500 hover:shadow-md transition">'
        f'{ico(b, 64)}<span class="block mt-3 text-lg font-extrabold text-slate-900">{t}</span>'
        f'<span class="block mt-1 text-sm text-slate-600 leading-snug">{d}</span>'
        f'<span class="block mt-3 text-sm font-bold text-emerald-700 group-hover:text-emerald-900">Learn more &rarr;</span></a>'
        for t, d, b, href in items)
    save_html("services", f'<div class="grid gap-4 sm:grid-cols-3 bg-emerald-50 rounded-2xl p-4 sm:p-5">{cards}</div>')


def step_cards(name, items, numbered=True):
    cards = []
    for i, (t, d, glyph) in enumerate(items):
        num = (f'<span class="absolute top-3 left-3 w-7 h-7 rounded-full bg-amber-400 text-slate-900 text-sm font-extrabold '
               f'inline-flex items-center justify-center">{i + 1}</span>') if numbered else ""
        cards.append(f'<div class="relative bg-white rounded-2xl border border-slate-200 p-5 text-center">{num}'
                     f'{ico(W(glyph), 64, 64, "#fff", EM700)}<span class="block mt-3 text-lg font-extrabold text-slate-900">{t}</span>'
                     f'<span class="block mt-1 text-sm text-slate-600 leading-snug">{d}</span></div>')
    save_html(name, f'<div class="grid gap-4 sm:grid-cols-3 bg-emerald-50 rounded-2xl p-4 sm:p-5">{"".join(cards)}</div>')


def checklist():
    rooms = [("Kitchen", ["Counters and backsplash", "Stovetop and microwave", "Sink and faucet polished", "Floors swept and mopped"]),
             ("Bathrooms", ["Toilet, tub and shower", "Mirrors and glass", "Vanity and fixtures", "Floors sanitized"]),
             ("Living &amp; Bedrooms", ["Dusting all surfaces", "Carpets and rugs vacuumed", "Beds made", "Trash emptied"])]
    tick = ('<svg viewBox="0 0 24 24" width="22" height="22" class="shrink-0 mt-px" aria-hidden="true"><rect x="1" y="1" width="22" height="22" rx="6" '
            f'fill="{EM100}" stroke="{EM600}" stroke-width="2"/><path d="M7 12l3.5 3.5L17 9" fill="none" stroke="{EM700}" stroke-width="2.6" '
            'stroke-linecap="round" stroke-linejoin="round"/></svg>')
    cols = "".join(
        f'<div class="bg-white rounded-2xl border border-slate-200 overflow-hidden"><h4 class="bg-emerald-700 text-white font-extrabold text-center py-3">{r}</h4>'
        f'<ul class="p-4 space-y-3">' + "".join(f'<li class="flex gap-2 text-sm text-slate-800">{tick}<span>{t}</span></li>' for t in tasks) + "</ul></div>"
        for r, tasks in rooms)
    save_html("checklist", '<div class="bg-emerald-50 rounded-2xl p-4 sm:p-5"><p class="text-center text-xl font-extrabold text-emerald-900 mb-4">'
              f'What&rsquo;s Included in a Standard Clean</p><div class="grid gap-4 sm:grid-cols-3">{cols}</div></div>')


def frequency():
    plans = [("Weekly", (1, 2, 3, 4), "Busy households, pets and kids"),
             ("Bi-Weekly", (1, 3), "A steady balance of fresh and tidy"),
             ("Monthly", (1,), "Light upkeep and a monthly reset")]
    cards = []
    for t, on, d in plans:
        weeks = "".join(
            f'<span class="w-9 h-10 rounded-lg border-2 inline-flex flex-col items-center justify-center leading-none '
            f'{"bg-emerald-700 border-emerald-700 text-white" if k in on else "bg-white border-slate-200 text-slate-400"}">'
            f'<span class="text-[9px] font-bold">WK</span><span class="text-sm font-extrabold">{k}</span></span>' for k in (1, 2, 3, 4))
        n = len(on)
        cards.append(f'<div class="bg-white rounded-2xl border border-slate-200 p-5 text-center"><span class="block text-xl font-extrabold text-slate-900">{t}</span>'
                     f'<span class="flex justify-center gap-2 my-3">{weeks}</span>'
                     f'<span class="block text-sm font-bold text-emerald-700">{n} visit{"s" if n > 1 else ""} a month</span>'
                     f'<span class="block mt-1 text-sm text-slate-600">{d}</span></div>')
    save_html("frequency", '<div class="bg-emerald-50 rounded-2xl p-4 sm:p-5"><p class="text-center text-xl font-extrabold text-emerald-900 mb-4">Pick a Schedule That Fits</p>'
              f'<div class="grid gap-4 sm:grid-cols-3">{"".join(cards)}</div>'
              '<p class="text-center text-xs text-slate-600 mt-4">One-time deep cleans and same-day service also available.</p></div>')


def hero_pattern():
    """Line-art pattern used behind text on heroes without a photo."""
    w, h = 1600, 640
    s = [f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" aria-hidden="true" class="w-full h-full">',
         f'<defs><linearGradient id="hp-g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{EM900}"/>'
         f'<stop offset="0.55" stop-color="#065f46"/><stop offset="1" stop-color="{SL900}"/></linearGradient>'
         f'<radialGradient id="hp-r" cx="0.5" cy="0.45" r="0.6"><stop offset="0" stop-color="{EM500}" stop-opacity="0.25"/>'
         f'<stop offset="1" stop-color="{EM500}" stop-opacity="0"/></radialGradient></defs>',
         f'<rect width="{w}" height="{h}" fill="url(#hp-g)"/><rect width="{w}" height="{h}" fill="url(#hp-r)"/>']
    import random
    rnd = random.Random(7)
    for _ in range(46):
        x, y, k = rnd.uniform(0, w), rnd.uniform(0, h), rnd.uniform(0.5, 1.6)
        if 420 < x < 1180 and 140 < y < 520:
            continue  # keep the text area calm
        t = rnd.choice(["s", "s", "l", "h"])
        if t == "s":
            s.append(f'<g opacity="{rnd.uniform(0.25, 0.6):.2f}">' + sparkle(x, y, k, AMBER if rnd.random() < 0.4 else EM100) + "</g>")
        elif t == "l":
            s.append(f'<g transform="translate({x:.0f} {y:.0f}) scale({k * 1.6:.2f}) rotate({rnd.uniform(0, 360):.0f})" opacity="0.22" fill="none" stroke="{EM100}" stroke-width="1.6" stroke-linecap="round">'
                     f'<path d="M-14 14 C-14 -6 -2 -16 16 -16 C16 4 4 14 -14 14Z"/><path d="M-14 14 L6 -6"/></g>')
        else:
            s.append(f'<g opacity="0.18">' + icon_house(round(x), round(y), k * 1.3, EM100).replace('stroke-width="3.5"', 'stroke-width="2"') + "</g>")
    save("hero-pattern", "".join(s) + "</svg>")


if __name__ == "__main__":
    maps()
    services()
    step_cards("booking", [("Text or Call", "(207) 838-3677, any time of day", g_phone),
                           ("Get a Quote", "Fast, transparent hourly pricing", g_quote),
                           ("We Clean", "Our team arrives fully equipped", g_sparkles)])
    step_cards("values", [("Vetted Team", "Trained and trusted local professionals", g_shield),
                          ("Eco-Friendly", "Safer products for kids and pets", g_leaf),
                          ("Veteran &amp; Senior Rates", "Discounted pricing as a thank-you", g_star)], numbered=False)
    checklist()
    frequency()
    hero_pattern()
