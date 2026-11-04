import os, re

# We will update each file to include 2 dispersed custom graphics inside the main content area alongside the text.

dispersed_snippets = {
    "index.html": ('images/res-1.jpg', 'images/com-1.jpg', 'Professional Housekeeping', 'Commercial Office Care'),
    "residential.html": ('images/res-1.jpg', 'images/res-2.jpg', 'Bathroom Deep Clean', 'Kitchen Sanitization'),
    "commercial.html": ('images/com-1.jpg', 'images/com-2.jpg', 'Workstation Care', 'Conference Room Maintenance'),
    "airbnb.html": ('images/air-1.jpg', 'images/air-2.jpg', 'Bed Staging & Linens', 'Turnover Restocking'),
    "about.html": ('images/loc-1.jpg', 'images/loc-2.jpg', 'Tampa Bay Team', 'Community Commitment'),
    "contact.html": ('images/loc-1.jpg', 'images/loc-2.jpg', 'Booking & Scheduling', 'Tampa Bay Service'),
    "faq.html": ('images/res-1.jpg', 'images/com-1.jpg', 'Cleaning Standards', 'Scheduling Flexibility'),
    "tampa.html": ('images/loc-1.jpg', 'images/loc-2.jpg', 'Tampa Properties', 'Local Cleaning Experts'),
    "st-petersburg.html": ('images/loc-1.jpg', 'images/loc-2.jpg', 'St. Pete Beach & Homes', 'Coastal Cleaning'),
    "clearwater.html": ('images/loc-1.jpg', 'images/loc-2.jpg', 'Clearwater Rentals', 'Beach House Turnover'),
    "brandon.html": ('images/loc-1.jpg', 'images/loc-2.jpg', 'Brandon Residences', 'East Tampa Bay Care')
}

os.chdir('/home/knoyes75/sparkle-sage-site')

for filename, (img1, img2, cap1, cap2) in dispersed_snippets.items():
    if not os.path.exists(filename): continue
    with open(filename, 'r') as f:
        content = f.read()
    
    # insert img1 after first paragraph or section
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
    
    # Remove old inserted images if any
    content = re.sub(r'<div class="my-8 rounded-2xl.*?</div>\s*</div>', '', content, flags=re.DOTALL)
    
    # Find main div
    parts = content.split('<main')
    if len(parts) == 2:
        main_content = parts[1]
        # split by paragraphs or headings
        paragraphs = main_content.split('</p>')
        if len(paragraphs) >= 3:
            paragraphs[1] += media_block_1
            if len(paragraphs) >= 6:
                paragraphs[4] += media_block_2
            main_content = '</p>'.join(paragraphs)
            content = parts[0] + '<main' + main_content
            with open(filename, 'w') as f:
                f.write(content)
            print(f"Dispersed images in {filename}")

