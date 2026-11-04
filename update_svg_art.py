import os, re

svg_cleaning = '''
<svg viewBox="0 0 800 450" class="w-full h-72 object-cover bg-emerald-950 rounded-2xl shadow-md border border-emerald-800">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#065f46;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#022c22;stop-opacity:1" />
    </linearGradient>
    <linearGradient id="gold" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#fbbf24;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#d97706;stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#grad1)" />
  <!-- Sparkles & Geometric Art -->
  <path d="M 400 80 L 415 120 L 455 135 L 415 150 L 400 190 L 385 150 L 345 135 L 385 120 Z" fill="url(#gold)" />
  <path d="M 200 250 L 208 270 L 228 278 L 208 286 L 200 306 L 192 286 L 172 278 L 192 270 Z" fill="#34d399" opacity="0.8" />
  <path d="M 600 220 L 608 240 L 628 248 L 608 256 L 600 276 L 592 256 L 572 248 L 592 240 Z" fill="#34d399" opacity="0.8" />
  <!-- House / Cleaning Vector Icon Outline -->
  <path d="M 320 320 L 320 230 L 400 170 L 480 230 L 480 320 Z" fill="none" stroke="#fbbf24" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" />
  <path d="M 370 320 L 370 260 L 430 260 L 430 320 Z" fill="none" stroke="#34d399" stroke-width="4" />
  <text x="400" y="380" font-family="sans-serif" font-size="28" font-weight="bold" fill="#ffffff" text-anchor="middle">Sparkle & Sage • Tampa Bay</text>
</svg>
'''

svg_office = '''
<svg viewBox="0 0 800 450" class="w-full h-72 object-cover bg-slate-900 rounded-2xl shadow-md border border-slate-700">
  <defs>
    <linearGradient id="grad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#1e293b;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#0f172a;stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#grad2)" />
  <rect x="150" y="100" width="500" height="250" rx="12" fill="none" stroke="#10b981" stroke-width="3" />
  <line x1="250" y1="180" x2="550" y2="180" stroke="#38bdf8" stroke-width="4" stroke-linecap="round" />
  <line x1="250" y1="240" x2="450" y2="240" stroke="#94a3b8" stroke-width="3" stroke-linecap="round" />
  <circle cx="600" cy="140" r="16" fill="#fbbf24" />
  <text x="400" y="380" font-family="sans-serif" font-size="26" font-weight="bold" fill="#f8fafc" text-anchor="middle">Commercial & Office Maintenance</text>
</svg>
'''

svg_rental = '''
<svg viewBox="0 0 800 450" class="w-full h-72 object-cover bg-emerald-900 rounded-2xl shadow-md border border-emerald-700">
  <defs>
    <linearGradient id="grad3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#047857;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#064e3b;stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect width="800" height="450" fill="url(#grad3)" />
  <path d="M 250 280 C 250 220, 550 220, 550 280 Z" fill="none" stroke="#fbbf24" stroke-width="5" />
  <rect x="300" y="150" width="200" height="120" rx="8" fill="none" stroke="#ffffff" stroke-width="4" />
  <circle cx="400" cy="210" r="30" fill="#fbbf24" />
  <text x="400" y="370" font-family="sans-serif" font-size="26" font-weight="bold" fill="#ffffff" text-anchor="middle">Airbnb & Vacation Rental Turnovers</text>
</svg>
'''

os.chdir('/home/knoyes75/sparkle-sage-site')

for filename in os.listdir('.'):
    if filename.endswith('.html'):
        with open(filename, 'r') as f:
            content = f.read()
        
        # Replace <img> tags with custom inline SVG graphics
        content = re.sub(r'<div class="my-8 rounded-2xl[^>]*>\s*<img[^>]*>\s*<div[^>]*>.*?</div>\s*</div>', svg_cleaning, content)
        
        with open(filename, 'w') as f:
            f.write(content)
        print(f"Updated SVG art in {filename}")

