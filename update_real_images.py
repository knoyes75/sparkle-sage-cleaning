import os, re

dispersed_photos = {
    "index.html": ('https://images.unsplash.com/photo-1584622650111-993a426fbf0a?auto=format&fit=crop&w=1200&q=80', 'https://images.unsplash.com/photo-1497366811353-6870744d04b2?auto=format&fit=crop&w=1200&q=80', 'Professional Housekeeping', 'Commercial Office Care'),
    "residential.html": ('https://images.unsplash.com/photo-1584622650111-993a426fbf0a?auto=format&fit=crop&w=1200&q=80', 'https://images.unsplash.com/photo-1556911220-e15b29be8c8f?auto=format&fit=crop&w=1200&q=80', 'Bathroom Sanitization', 'Kitchen Detailing'),
    "commercial.html": ('https://images.unsplash.com/photo-1497366811353-6870744d04b2?auto=format&fit=crop&w=1200&q=80', 'https://images.unsplash.com/photo-1497215728101-856f4ea42174?auto=format&fit=crop&w=1200&q=80', 'Office Workstations', 'Conference Rooms'),
    "airbnb.html": ('https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?auto=format&fit=crop&w=1200&q=80', 'https://images.unsplash.com/photo-1590490360182-c33d57733427?auto=format&fit=crop&w=1200&q=80', 'Bed Staging & Linens', 'Turnover Restocking'),
    "about.html": ('https://images.unsplash.com/photo-1581578731548-c64695cc6952?auto=format&fit=crop&w=1200&q=80', 'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1200&q=80', 'Tampa Bay Team', 'Community Commitment'),
    "contact.html": ('https://images.unsplash.com/photo-1581578731548-c64695cc6952?auto=format&fit=crop&w=1200&q=80', 'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1200&q=80', 'Booking & Scheduling', 'Tampa Bay Service'),
    "faq.html": ('https://images.unsplash.com/photo-1584622650111-993a426fbf0a?auto=format&fit=crop&w=1200&q=80', 'https://images.unsplash.com/photo-1497366811353-6870744d04b2?auto=format&fit=crop&w=1200&q=80', 'Cleaning Standards', 'Scheduling Flexibility'),
    "tampa.html": ('https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?auto=format&fit=crop&w=1200&q=80', 'https://images.unsplash.com/photo-1581578731548-c64695cc6952?auto=format&fit=crop&w=1200&q=80', 'Tampa Properties', 'Local Cleaning Experts'),
    "st-petersburg.html": ('https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1200&q=80', 'https://images.unsplash.com/photo-1581578731548-c64695cc6952?auto=format&fit=crop&w=1200&q=80', 'St. Pete Beach & Homes', 'Coastal Cleaning'),
    "clearwater.html": ('https://images.unsplash.com/photo-1519046904884-53103b34b206?auto=format&fit=crop&w=1200&q=80', 'https://images.unsplash.com/photo-1581578731548-c64695cc6952?auto=format&fit=crop&w=1200&q=80', 'Clearwater Rentals', 'Beach House Turnover'),
    "brandon.html": ('https://images.unsplash.com/photo-1513694203232-719a280e022f?auto=format&fit=crop&w=1200&q=80', 'https://images.unsplash.com/photo-1581578731548-c64695cc6952?auto=format&fit=crop&w=1200&q=80', 'Brandon Residences', 'East Tampa Bay Care')
}

# os.chdir('/home/knoyes75/sparkle-sage-site')

for filename, (img1, img2, cap1, cap2) in dispersed_photos.items():
    if not os.path.exists(filename): continue
    with open(filename, 'r') as f:
        content = f.read()
    
    media_block_1 = f'''
    <div class="my-8 rounded-2xl overflow-hidden shadow-md border border-slate-200">
        <img src="{img1}" alt="{cap1}" class="w-full h-72 object-cover">
        <div class="p-3 bg-white text-center text-sm font-semibold text-emerald-800">{cap1}</div>
    </div>
    '''
    media_block_2 = f'''
    <div class="my-8 rounded-2xl overflow-hidden shadow-md border border-slate-200">
        <img src="{img2}" alt="{cap2}" class="w-full h-72 object-cover">
        <div class="p-3 bg-white text-center text-sm font-semibold text-emerald-800">{cap2}</div>
    </div>
    '''
    
        content = re.sub(r'<svg viewBox="0 0 800 450".*?</svg>', '', content, flags=re.DOTALL)
content = re.sub(r'<div class="my-8 rounded-2xl.*?</div>\s*</div>', '', content, flags=re.DOTALL)
    
    parts = content.split('<main')
    if len(parts) == 2:
        main_content = parts[1]
        paragraphs = main_content.split('</p>')
        if len(paragraphs) >= 3:
            paragraphs[1] += media_block_1
            if len(paragraphs) >= 6:
                paragraphs[4] += media_block_2
            main_content = '</p>'.join(paragraphs)
            content = parts[0] + '<main' + main_content
            with open(filename, 'w') as f:
                f.write(content)
            print(f"Updated real photos in {filename}")

