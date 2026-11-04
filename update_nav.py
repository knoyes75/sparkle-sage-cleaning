import os, re

nav_html = '''
    <header class="bg-emerald-900 text-white sticky top-0 z-50 shadow-lg">
        <div class="max-w-7xl mx-auto px-4 py-4 flex justify-between items-center">
            <a href="index.html" class="flex items-center space-x-2">
                <i class="fa-solid fa-sparkles text-amber-400 text-2xl"></i>
                <div>
                    <span class="font-bold text-xl tracking-wide block">Sparkle & Sage</span>
                    <span class="text-xs text-emerald-300 uppercase tracking-widest">Tampa Bay Cleaning</span>
                </div>
            </a>
            <nav class="hidden lg:flex items-center space-x-5 text-sm font-medium">
                <a href="index.html" class="hover:text-amber-300 transition">Home</a>
                <a href="residential.html" class="hover:text-amber-300 transition">Residential</a>
                <a href="commercial.html" class="hover:text-amber-300 transition">Commercial</a>
                <a href="airbnb.html" class="hover:text-amber-300 transition">Airbnb</a>
                <!-- Locations Dropdown -->
                <div class="relative group">
                    <button class="hover:text-amber-300 transition inline-flex items-center focus:outline-none py-2">
                        Locations <i class="fa-solid fa-chevron-down ml-1 text-xs"></i>
                    </button>
                    <div class="absolute left-0 mt-0 w-48 bg-emerald-950 rounded-xl shadow-xl py-2 hidden group-hover:block border border-emerald-800">
                        <a href="tampa.html" class="block px-4 py-2 text-sm text-white hover:bg-emerald-900">Tampa, FL</a>
                        <a href="st-petersburg.html" class="block px-4 py-2 text-sm text-white hover:bg-emerald-900">St. Petersburg, FL</a>
                        <a href="clearwater.html" class="block px-4 py-2 text-sm text-white hover:bg-emerald-900">Clearwater, FL</a>
                        <a href="brandon.html" class="block px-4 py-2 text-sm text-white hover:bg-emerald-900">Brandon, FL</a>
                    </div>
                </div>
                <a href="faq.html" class="hover:text-amber-300 transition">FAQ</a>
                <a href="about.html" class="hover:text-amber-300 transition">About</a>
                <a href="contact.html" class="hover:text-amber-300 transition">Contact</a>
                <a href="sms:2078383677" class="bg-amber-400 text-slate-900 px-3 py-2 rounded-xl font-bold hover:bg-amber-300 transition">
                    <i class="fa-solid fa-phone mr-1"></i> (207) 838-3677
                </a>
            </nav>
            <div class="flex lg:hidden items-center space-x-3">
                <a href="sms:2078383677" class="bg-amber-400 text-slate-900 px-3 py-1.5 rounded-lg text-sm font-bold"><i class="fa-solid fa-phone"></i></a>
                <button id="menu-btn" class="text-white text-2xl focus:outline-none"><i class="fa-solid fa-bars"></i></button>
            </div>
        </div>
        <div id="mobile-menu" class="hidden lg:hidden bg-emerald-950 px-4 pt-2 pb-6 space-y-3 border-t border-emerald-800 text-sm">
            <a href="index.html" class="block text-white hover:text-amber-300">Home</a>
            <a href="residential.html" class="block text-white hover:text-amber-300">Residential</a>
            <a href="commercial.html" class="block text-white hover:text-amber-300">Commercial</a>
            <a href="airbnb.html" class="block text-white hover:text-amber-300">Airbnb</a>
            <div class="pl-4 space-y-2 border-l border-emerald-800">
                <span class="text-xs text-amber-300 uppercase tracking-wider block">Locations</span>
                <a href="tampa.html" class="block text-white hover:text-amber-300">Tampa, FL</a>
                <a href="st-petersburg.html" class="block text-white hover:text-amber-300">St. Petersburg, FL</a>
                <a href="clearwater.html" class="block text-white hover:text-amber-300">Clearwater, FL</a>
                <a href="brandon.html" class="block text-white hover:text-amber-300">Brandon, FL</a>
            </div>
            <a href="faq.html" class="block text-white hover:text-amber-300">FAQ</a>
            <a href="about.html" class="block text-white hover:text-amber-300">About</a>
            <a href="contact.html" class="block text-white hover:text-amber-300">Contact</a>
        </div>
    </header>
    <script>
        document.getElementById('menu-btn').addEventListener('click', () => {
            document.getElementById('mobile-menu').classList.toggle('hidden');
        });
    </script>
'''

os.chdir('/home/knoyes75/sparkle-sage-site')

for filename in os.listdir('.'):
    if filename.endswith('.html'):
        with open(filename, 'r') as f:
            content = f.read()
        # replace existing header
        content = re.sub(r'<header.*?</header>\s*<script>.*?</script>', nav_html, content, flags=re.DOTALL)
        with open(filename, 'w') as f:
            f.write(content)
        print(f"Updated nav in {filename}")

