import os

pages = {
    "index.html": {
        "title": "Sparkle & Sage Cleaning Services | Tampa Bay, FL",
        "desc": "Top-rated residential, commercial, and Airbnb cleaning services across Tampa Bay, FL. Low hourly rates, veteran & senior discounts. Text (207) 838-3677.",
        "heading": "Pristine Cleaning for Homes, Rentals & Businesses in Tampa Bay",
        "img": "https://images.unsplash.com/photo-1581578731548-c64695cc6952?auto=format&fit=crop&w=1200&q=80",
        "content": """
        <p class="mb-4 text-lg">Welcome to Sparkle & Sage Cleaning Services, your premier partner for professional cleaning throughout the Tampa Bay area. Whether you manage a bustling residential household, a commercial office space, or a 5-star short-term rental property, our dedicated team delivers meticulous attention to detail and sparkling results every single time.</p>
        <p class="mb-4">We understand that finding a trustworthy and reliable cleaning service in Tampa Bay can be challenging. That is why we pride ourselves on absolute dependability, transparent low hourly rates, and personalized care tailored to your exact needs. Furthermore, we deeply value those who have served our nation and our senior community, offering special discounted cleaning rates for veterans and senior citizens.</p>
        <h3 class="text-2xl font-bold mt-8 mb-4 text-slate-900">Why Tampa Bay Chooses Sparkle & Sage</h3>
        <ul class="list-disc pl-6 space-y-2 mb-6">
            <li><strong>Uncompromising Quality:</strong> Every clean is performed to the highest standard, ensuring dust-free surfaces, sanitized bathrooms, and spotless floors.</li>
            <li><strong>Affordable Hourly Rates:</strong> Premium cleaning services priced fairly to fit your monthly or weekly budget.</li>
            <li><strong>Veteran & Senior Discounts:</strong> Special appreciation rates for military veterans and senior citizens.</li>
            <li><strong>Flexible Scheduling:</strong> Same-day, weekly, bi-weekly, and monthly cleaning options available across Tampa, St. Petersburg, Clearwater, and Brandon.</li>
        </ul>
        <p class="mb-4">Ready to experience a truly pristine environment without the hassle? Text or call us anytime at <strong>(207) 838-3677</strong> to book your cleaning session today!</p>
        """
    },
    "residential.html": {
        "title": "Residential House Cleaning Services | Sparkle & Sage Tampa Bay",
        "desc": "Professional residential cleaning, deep cleans, and routine housekeeping in Tampa Bay, FL. Veteran & senior discounts. Text (207) 838-3677.",
        "heading": "Expert Residential & House Cleaning in Tampa Bay",
        "img": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1200&q=80",
        "content": """
        <p class="mb-4 text-lg">Your home should be your sanctuary—a clean, peaceful, and rejuvenating space where you can relax with family. At Sparkle & Sage, our professional residential cleaning services take the burden of housework off your shoulders, giving you back your precious weekends across Tampa Bay.</p>
        <p class="mb-4">From routine weekly housekeeping to thorough seasonal deep cleans, our experienced cleaners sanitize every corner of your living spaces. We utilize eco-friendly, family-safe cleaning agents combined with meticulous techniques to ensure your kitchen, bathrooms, bedrooms, and living areas shine.</p>
        <h3 class="text-2xl font-bold mt-8 mb-4 text-slate-900">Our Comprehensive Home Cleaning Checklist</h3>
        <div class="grid md:grid-cols-2 gap-6 my-6">
            <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-200">
                <h4 class="font-bold text-lg mb-2 text-emerald-800"><i class="fa-solid fa-bath mr-2"></i> Bathrooms</h4>
                <p class="text-slate-600 text-sm">Deep sanitization of showers, tubs, sinks, toilets, mirrors, chrome fixtures, and sparkling tile floors.</p>
            </div>
            <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-200">
                <h4 class="font-bold text-lg mb-2 text-emerald-800"><i class="fa-solid fa-utensils mr-2"></i> Kitchens</h4>
                <p class="text-slate-600 text-sm">Countertop detailing, exterior appliance wiping, microwave cleaning, sink disinfection, and floor mopping.</p>
            </div>
            <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-200">
                <h4 class="font-bold text-lg mb-2 text-emerald-800"><i class="fa-solid fa-bed mr-2"></i> Living Areas & Bedrooms</h4>
                <p class="text-slate-600 text-sm">Thorough dusting of all surfaces, furniture polishing, straightening, and meticulous carpet vacuuming.</p>
            </div>
            <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-200">
                <h4 class="font-bold text-lg mb-2 text-emerald-800"><i class="fa-solid fa-plus mr-2"></i> Custom Add-Ons</h4>
                <p class="text-slate-600 text-sm">Interior windows, baseboard detailing, inside cabinets, and custom requests tailored to your home.</p>
            </div>
        </div>
        <p class="mb-4">We proudly offer reduced rates for senior citizens and military veterans throughout Tampa, St. Petersburg, Clearwater, and Brandon. Text us today at <strong>(207) 838-3677</strong> to schedule your residential clean!</p>
        """
    },
    "commercial.html": {
        "title": "Commercial & Office Cleaning Services | Sparkle & Sage Tampa Bay",
        "desc": "Professional commercial office and workspace cleaning in Tampa Bay, FL. Low hourly rates, veteran & senior discounts. Text (207) 838-3677.",
        "heading": "Professional Commercial & Office Cleaning in Tampa Bay",
        "img": "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=1200&q=80",
        "content": """
        <p class="mb-4 text-lg">A clean and sanitary commercial workspace is essential for employee productivity, health, and making an unforgettable impression on visiting clients. Sparkle & Sage provides top-tier commercial cleaning and office maintenance services tailored to businesses across the Tampa Bay area.</p>
        <p class="mb-4">Whether you manage a corporate office suite, retail storefront, medical facility, or coworking hub, our professional cleaning team works around your operational hours to deliver impeccable results with zero disruption to your daily workflow.</p>
        <h3 class="text-2xl font-bold mt-8 mb-4 text-slate-900">Our Commercial Cleaning Solutions</h3>
        <ul class="list-disc pl-6 space-y-2 mb-6">
            <li><strong>Workstation Sanitization:</strong> Desks, keyboards, monitors, and shared office furniture thoroughly dusted and disinfected.</li>
            <li><strong>Conference Rooms & Receptions:</strong> Pristine glass polishing, seating sanitization, and welcoming lobby presentation.</li>
            <li><strong>Restroom Disinfection:</strong> High-traffic restrooms scrubbed, sanitized, deodorized, and fully restocked with essentials.</li>
            <li><strong>Breakrooms & Kitchenettes:</strong> Countertop detailing, sink sanitization, exterior appliance care, and floor cleaning.</li>
            <li><strong>Floor Care & Trash Removal:</strong> Daily vacuuming, hard floor mopping, and secure waste disposal.</li>
        </ul>
        <p class="mb-4">Elevate your business environment with Tampa Bay's most dependable commercial cleaners. Contact us today at <strong>(207) 838-3677</strong> for a customized commercial cleaning plan.</p>
        """
    },
    "airbnb.html": {
        "title": "Airbnb & Vacation Rental Turnover | Sparkle & Sage Tampa Bay",
        "desc": "Reliable Airbnb and vacation rental turnover cleaning in Tampa Bay, FL. Fast turnaround, pristine results. Text (207) 838-3677.",
        "heading": "Airbnb & Vacation Rental Turnover Cleaning in Tampa Bay",
        "img": "https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?auto=format&fit=crop&w=1200&q=80",
        "content": """
        <p class="mb-4 text-lg">In the competitive world of short-term rentals, 5-star cleanliness reviews are everything. Sparkle & Sage specializes in rapid, meticulous Airbnb and vacation rental turnover cleaning across Tampa Bay, ensuring every guest walks into a spotless, welcoming oasis.</p>
        <p class="mb-4">We coordinate seamlessly with your booking calendar to execute fast guest-to-guest turnovers. From deep sanitization and luxurious bed staging to supply restocking and detailed damage inspections, we protect your superhost status and maximize your rental revenue.</p>
        <h3 class="text-2xl font-bold mt-8 mb-4 text-slate-900">What Our Vacation Rental Turnover Includes</h3>
        <ul class="list-disc pl-6 space-y-2 mb-6">
            <li><strong>Rapid Turnaround Scheduling:</strong> Reliable cleaning between back-to-back guest check-outs and check-ins.</li>
            <li><strong>Immaculate Sanitization:</strong> Complete bathroom and kitchen deep cleans for absolute guest satisfaction.</li>
            <li><strong>Linen & Laundry Management:</strong> Professional bed stripping, washing, crisp staging, and towel replenishment.</li>
            <li><strong>Supply Restocking:</strong> Refilling toilet paper, soap, shampoo, coffee, and guest welcome amenities.</li>
            <li><strong>Quality Inspection & Reporting:</strong> Detailed post-clean checks with photo updates and immediate reporting of any property damage.</li>
        </ul>
        <p class="mb-4">Keep your ratings pristine and your guests thrilled. Text us at <strong>(207) 838-3677</strong> to partner with Tampa Bay's top short-term rental cleaning team.</p>
        """
    },
    "about.html": {
        "title": "About Us | Sparkle & Sage Tampa Bay Cleaning",
        "desc": "Learn about Sparkle & Sage Cleaning Services in Tampa Bay, FL. Low hourly rates, veteran & senior discounts. Text (207) 838-3677.",
        "heading": "About Sparkle & Sage Cleaning Services",
        "img": "https://images.unsplash.com/photo-1556911220-e15b29be8c8f?auto=format&fit=crop&w=1200&q=80",
        "content": """
        <p class="mb-4 text-lg">Sparkle & Sage was founded on a simple yet powerful premise: everyone in Tampa Bay deserves a pristine, healthy living and working environment without paying exorbitant prices. We combine meticulous cleaning standards with honest, transparent, low hourly rates.</p>
        <p class="mb-4">Our professional cleaning team is handpicked, thoroughly vetted, and deeply dedicated to excellence. We treat every client's property with the utmost respect and care, building lasting relationships based on trust, consistency, and exceptional results.</p>
        <h3 class="text-2xl font-bold mt-8 mb-4 text-slate-900">Our Core Commitments</h3>
        <div class="grid md:grid-cols-2 gap-6 my-6">
            <div class="bg-emerald-50 p-6 rounded-2xl border border-emerald-100">
                <h4 class="font-bold text-emerald-900 mb-2"><i class="fa-solid fa-medal mr-2"></i> Veteran & Senior Discounts</h4>
                <p class="text-slate-600 text-sm">We proudly honor military veterans and senior citizens with special discounted cleaning rates as a token of our community gratitude.</p>
            </div>
            <div class="bg-emerald-50 p-6 rounded-2xl border border-emerald-100">
                <h4 class="font-bold text-emerald-900 mb-2"><i class="fa-solid fa-heart mr-2"></i> Eco-Friendly Approach</h4>
                <p class="text-slate-600 text-sm">We utilize safe, non-toxic cleaning products that protect your family, pets, and employees while delivering sparkling results.</p>
            </div>
        </div>
        <p class="mb-4">Serving Tampa, St. Petersburg, Clearwater, Brandon, and surrounding communities. Text or call us today at <strong>(207) 838-3677</strong> to discover the Sparkle & Sage difference.</p>
        """
    },
    "contact.html": {
        "title": "Contact Us | Sparkle & Sage Tampa Bay Cleaning",
        "desc": "Contact Sparkle & Sage Cleaning Services in Tampa Bay, FL. Text or call (207) 838-3677 to book your clean today.",
        "heading": "Contact & Booking - Sparkle & Sage",
        "img": "https://images.unsplash.com/photo-1423784346385-c1d4dac9093a?auto=format&fit=crop&w=1200&q=80",
        "content": """
        <p class="mb-4 text-lg">Ready to experience a sparkling clean home, office, or vacation rental in Tampa Bay? We make scheduling simple and straightforward. Please text or call us anytime!</p>
        <div class="bg-white p-8 rounded-3xl shadow-sm border border-slate-200 text-center my-8 max-w-2xl mx-auto">
            <div class="bg-emerald-50 w-16 h-16 rounded-2xl flex items-center justify-center mx-auto text-emerald-700 text-2xl font-bold mb-4">
                <i class="fa-solid fa-phone"></i>
            </div>
            <h3 class="text-3xl font-bold text-slate-900 mb-2">Please Text Anytime</h3>
            <p class="text-slate-600 mb-6">Cleaning slots fill up fast throughout the season. Send us a quick text or call to reserve your preferred date and time!</p>
            <a href="sms:2078383677" class="bg-emerald-700 text-white px-8 py-4 rounded-xl font-bold text-xl hover:bg-emerald-800 transition inline-flex items-center shadow-md">
                <i class="fa-solid fa-comment-sms mr-2"></i> (207) 838-3677
            </a>
            <p class="text-xs text-slate-400 mt-6">Serving Tampa Bay, FL • Low Hourly Rates • Veteran & Senior Discounts</p>
        </div>
        """
    },
    "faq.html": {
        "title": "Frequently Asked Questions | Sparkle & Sage Tampa Bay",
        "desc": "Answers to common cleaning service questions in Tampa Bay, FL. Low hourly rates, veteran & senior discounts. Text (207) 838-3677.",
        "heading": "Frequently Asked Questions",
        "img": "https://images.unsplash.com/photo-1507679799987-c73779587ccf?auto=format&fit=crop&w=1200&q=80",
        "content": """
        <p class="mb-4 text-lg">Have questions about our cleaning services, pricing structure, or scheduling across Tampa Bay? Find clear answers to our most frequently asked questions below.</p>
        <div class="space-y-6 my-8">
            <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-200">
                <h3 class="font-bold text-lg mb-2 text-emerald-900">What areas do you service in Tampa Bay?</h3>
                <p class="text-slate-600 text-sm">We provide residential, commercial, and Airbnb cleaning services across the entire Tampa Bay metropolitan area, including Tampa, St. Petersburg, Clearwater, Brandon, and surrounding neighborhoods.</p>
            </div>
            <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-200">
                <h3 class="font-bold text-lg mb-2 text-emerald-900">Do you offer veteran and senior discounts?</h3>
                <p class="text-slate-600 text-sm">Yes! We proudly offer special reduced rates and discounts for military veterans and senior citizens as our way of giving back to the community.</p>
            </div>
            <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-200">
                <h3 class="font-bold text-lg mb-2 text-emerald-900">How do your hourly rates work?</h3>
                <p class="text-slate-600 text-sm">We believe in transparent, affordable pricing with low hourly rates. There are no hidden fees or surprise charges—you only pay for the expert cleaning time required.</p>
            </div>
            <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-200">
                <h3 class="font-bold text-lg mb-2 text-emerald-900">Do I need to be home during the cleaning?</h3>
                <p class="text-slate-600 text-sm">Not at all! Many of our clients provide keyless entry codes, garage door codes, or lockbox combinations so we can clean while they are at work or running errands.</p>
            </div>
            <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-200">
                <h3 class="font-bold text-lg mb-2 text-emerald-900">How do I book a cleaning appointment?</h3>
                <p class="text-slate-600 text-sm">Booking is fast and easy. Simply text or call us anytime at <strong>(207) 838-3677</strong> to reserve your slot.</p>
            </div>
        </div>
        """
    },
    "tampa.html": {
        "title": "Cleaning Services in Tampa, FL | Sparkle & Sage",
        "desc": "Top-rated residential, commercial, and Airbnb cleaning services in Tampa, FL. Low hourly rates, veteran & senior discounts. Text (207) 838-3677.",
        "heading": "Professional Cleaning Services in Tampa, FL",
        "img": "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?auto=format&fit=crop&w=1200&q=80",
        "content": """
        <p class="mb-4 text-lg">Welcome to Sparkle & Sage Tampa, your trusted local experts for residential housekeeping, commercial office maintenance, and short-term rental turnovers throughout Tampa, Florida.</p>
        <p class="mb-4">Tampa is a vibrant, fast-growing city where homes and businesses deserve immaculate care. Whether you reside in South Tampa, Hyde Park, New Tampa, or downtown, our professional cleaners deliver dependable, high-quality results at low hourly rates.</p>
        <h3 class="text-2xl font-bold mt-8 mb-4 text-slate-900">Why Tampa Residents Choose Us</h3>
        <ul class="list-disc pl-6 space-y-2 mb-6">
            <li><strong>Local Expertise:</strong> Deep understanding of Tampa homes, condos, and commercial properties.</li>
            <li><strong>Veteran & Senior Discounts:</strong> Special appreciation rates for veterans and seniors across Tampa.</li>
            <li><strong>Flexible Scheduling:</strong> Weekly, bi-weekly, monthly, or same-day turnover services.</li>
        </ul>
        <p class="mb-4">Ready to keep your Tampa property looking its absolute best? Text or call us today at <strong>(207) 838-3677</strong>.</p>
        """
    },
    "st-petersburg.html": {
        "title": "Cleaning Services in St. Petersburg, FL | Sparkle & Sage",
        "desc": "Professional residential, commercial, and Airbnb cleaning services in St. Petersburg, FL. Low hourly rates, veteran & senior discounts. Text (207) 838-3677.",
        "heading": "Professional Cleaning Services in St. Petersburg, FL",
        "img": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1200&q=80",
        "content": """
        <p class="mb-4 text-lg">Sparkle & Sage provides top-rated residential, commercial, and vacation rental cleaning services across St. Petersburg, Florida.</p>
        <p class="mb-4">From coastal beach bungalows to downtown St. Pete condos and bustling commercial offices, our experienced cleaning team delivers sparkling results. We pride ourselves on reliability, transparent pricing, and exceptional customer care.</p>
        <h3 class="text-2xl font-bold mt-8 mb-4 text-slate-900">St. Petersburg Cleaning Specialists</h3>
        <ul class="list-disc pl-6 space-y-2 mb-6">
            <li><strong>Vacation Rental Turnovers:</strong> Specialized Airbnb cleaning to maintain stellar guest ratings in St. Pete.</li>
            <li><strong>Housekeeping & Deep Cleans:</strong> Comprehensive cleaning tailored to your family's unique needs.</li>
            <li><strong>Special Discounts:</strong> Honoring veterans and senior citizens with reduced cleaning rates.</li>
        </ul>
        <p class="mb-4">For spotless results in St. Petersburg, text or call us today at <strong>(207) 838-3677</strong>.</p>
        """
    },
    "clearwater.html": {
        "title": "Cleaning Services in Clearwater, FL | Sparkle & Sage",
        "desc": "Professional residential, commercial, and Airbnb cleaning services in Clearwater, FL. Low hourly rates, veteran & senior discounts. Text (207) 838-3677.",
        "heading": "Professional Cleaning Services in Clearwater, FL",
        "img": "https://images.unsplash.com/photo-1519046904884-53103b34b206?auto=format&fit=crop&w=1200&q=80",
        "content": """
        <p class="mb-4 text-lg">Discover premier residential and vacation rental cleaning services in Clearwater, Florida, brought to you by Sparkle & Sage.</p>
        <p class="mb-4">Clearwater properties—from beachside rentals to suburban family homes—require specialized care to combat sand, humidity, and salt air. Our professional cleaners ensure your spaces remain impeccably fresh, sanitized, and inviting year-round.</p>
        <h3 class="text-2xl font-bold mt-8 mb-4 text-slate-900">Clearwater Cleaning Excellence</h3>
        <ul class="list-disc pl-6 space-y-2 mb-6">
            <li><strong>Pristine Beach House Turnovers:</strong> Fast, meticulous Airbnb cleaning for Clearwater Beach hosts.</li>
            <li><strong>Reliable Residential Care:</strong> Routine housekeeping and deep cleans at fair hourly rates.</li>
            <li><strong>Community Discounts:</strong> Proudly offering veteran and senior citizen cleaning discounts.</li>
        </ul>
        <p class="mb-4">Schedule your Clearwater clean today by texting or calling <strong>(207) 838-3677</strong>.</p>
        """
    },
    "brandon.html": {
        "title": "Cleaning Services in Brandon, FL | Sparkle & Sage",
        "desc": "Professional residential, commercial, and Airbnb cleaning services in Brandon, FL. Low hourly rates, veteran & senior discounts. Text (207) 838-3677.",
        "heading": "Professional Cleaning Services in Brandon, FL",
        "img": "https://images.unsplash.com/photo-1513694203232-719a280e022f?auto=format&fit=crop&w=1200&q=80",
        "content": """
        <p class="mb-4 text-lg">Sparkle & Sage delivers expert residential and commercial cleaning services throughout Brandon, Florida and surrounding East Tampa Bay communities.</p>
        <p class="mb-4">We help Brandon homeowners and business operators maintain immaculate environments without the stress. From thorough kitchen and bathroom detailing to office sanitization, our team handles it all with professional precision.</p>
        <h3 class="text-2xl font-bold mt-8 mb-4 text-slate-900">Why Brandon Trusts Sparkle & Sage</h3>
        <ul class="list-disc pl-6 space-y-2 mb-6">
            <li><strong>Dependable Housekeeping:</strong> Consistent, high-quality cleaning on your schedule.</li>
            <li><strong>Transparent Pricing:</strong> Low hourly rates with zero hidden fees.</li>
            <li><strong>Veteran & Senior Discounts:</strong> Special appreciation rates for those who served and seniors.</li>
        </ul>
        <p class="mb-4">Keep your Brandon property spotless. Text or call us today at <strong>(207) 838-3677</strong>.</p>
        """
    }
}

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
                <a href="tampa.html" class="hover:text-amber-300 transition">Tampa</a>
                <a href="st-petersburg.html" class="hover:text-amber-300 transition">St. Pete</a>
                <a href="clearwater.html" class="hover:text-amber-300 transition">Clearwater</a>
                <a href="brandon.html" class="hover:text-amber-300 transition">Brandon</a>
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
            <a href="tampa.html" class="block text-white hover:text-amber-300">Tampa</a>
            <a href="st-petersburg.html" class="block text-white hover:text-amber-300">St. Petersburg</a>
            <a href="clearwater.html" class="block text-white hover:text-amber-300">Clearwater</a>
            <a href="brandon.html" class="block text-white hover:text-amber-300">Brandon</a>
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

footer_html = '''
    <footer class="bg-slate-900 text-slate-400 py-12 px-4 text-center text-sm border-t border-slate-800 mt-16">
        <div class="max-w-7xl mx-auto grid md:grid-cols-4 gap-8 mb-8 text-left">
            <div>
                <h4 class="text-white font-bold mb-3">Sparkle & Sage</h4>
                <p class="text-xs text-slate-400">Professional cleaning services across Tampa Bay, FL. Low hourly rates, veteran & senior discounts.</p>
            </div>
            <div>
                <h4 class="text-white font-bold mb-3">Services</h4>
                <ul class="space-y-1 text-xs">
                    <li><a href="residential.html" class="hover:text-white">Residential Cleaning</a></li>
                    <li><a href="commercial.html" class="hover:text-white">Commercial Cleaning</a></li>
                    <li><a href="airbnb.html" class="hover:text-white">Airbnb & Rentals</a></li>
                </ul>
            </div>
            <div>
                <h4 class="text-white font-bold mb-3">Service Areas</h4>
                <ul class="space-y-1 text-xs">
                    <li><a href="tampa.html" class="hover:text-white">Tampa, FL</a></li>
                    <li><a href="st-petersburg.html" class="hover:text-white">St. Petersburg, FL</a></li>
                    <li><a href="clearwater.html" class="hover:text-white">Clearwater, FL</a></li>
                    <li><a href="brandon.html" class="hover:text-white">Brandon, FL</a></li>
                </ul>
            </div>
            <div>
                <h4 class="text-white font-bold mb-3">Book Now</h4>
                <p class="text-xs text-slate-400 mb-2">Text or call anytime:</p>
                <a href="sms:2078383677" class="text-amber-400 font-bold text-base">(207) 838-3677</a>
            </div>
        </div>
        <p class="border-t border-slate-800 pt-6 text-xs">© Sparkle & Sage Cleaning Services. Serving Tampa Bay, FL.</p>
    </footer>
'''

os.chdir('/home/knoyes75/sparkle-sage-site')

for filename, data in pages.items():
    html = f'''<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{data['title']}</title>
    <meta name="description" content="{data['desc']}">
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body class="bg-slate-50 text-slate-800 font-sans antialiased">
{nav_html}
    <section class="relative bg-slate-900 text-white py-28 px-4 overflow-hidden">
        <div class="absolute inset-0 z-0 opacity-30">
            <img src="{data['img']}" alt="{data['heading']}" class="w-full h-full object-cover">
        </div>
        <div class="max-w-4xl mx-auto text-center relative z-10">
            <span class="bg-emerald-600/30 text-emerald-300 border border-emerald-500/30 px-4 py-1.5 rounded-full text-sm font-semibold inline-block mb-6">
                🌴 Tampa Bay's Trusted Cleaning Professionals
            </span>
            <h1 class="text-4xl sm:text-6xl font-extrabold tracking-tight mb-6">
                {data['heading']}
            </h1>
            <p class="text-xl text-slate-300 max-w-2xl mx-auto mb-8">
                {data['desc']}
            </p>
            <div>
                <a href="sms:2078383677" class="bg-amber-400 text-slate-900 px-8 py-4 rounded-xl font-bold text-lg hover:bg-amber-300 transition shadow-lg inline-flex items-center justify-center">
                    <i class="fa-solid fa-comment-sms mr-2"></i> Text Us Anytime: (207) 838-3677
                </a>
            </div>
        </div>
    </section>

    <main class="py-16 max-w-4xl mx-auto px-4 leading-relaxed text-slate-700">
        <div class="bg-white p-8 sm:p-12 rounded-3xl shadow-sm border border-slate-200">
            {data['content']}
        </div>
    </main>
{footer_html}
</body>
</html>
'''
    with open(filename, 'w') as f:
        f.write(html)
    print(f"Generated {filename}")

