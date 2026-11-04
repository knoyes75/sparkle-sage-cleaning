import os

extra_text = """
<h3 class="text-2xl font-bold mt-8 mb-4 text-slate-900">Our Professional Cleaning Methodology</h3>
<p class="mb-4">At Sparkle & Sage, we believe that achieving a truly pristine property requires more than just surface wiping. Our comprehensive cleaning methodology combines advanced sanitization techniques, eco-friendly cleaning agents, and rigorous quality control checklists. Every member of our team is thoroughly trained to handle delicate surfaces, high-traffic areas, and specialized sanitization needs with utmost precision and care.</p>
<p class="mb-4">We continually refine our processes to ensure maximum efficiency and superior results. Whether we are servicing a residential home, a commercial office, or a vacation rental property, our commitment to excellence remains unwavering. Experience the peace of mind that comes with knowing your property is maintained by true professionals who care about your health, comfort, and satisfaction.</p>
<h3 class="text-2xl font-bold mt-8 mb-4 text-slate-900">Serving the Entire Tampa Bay Region</h3>
<p class="mb-4">Our service coverage spans across the entire Tampa Bay metropolitan area, bringing prompt, reliable, and affordable cleaning solutions directly to your doorstep. From urban centers to suburban neighborhoods and coastal communities, Sparkle & Sage is your trusted local cleaning partner.</p>
<p class="mb-4">Contact us today via text or phone call at <strong>(207) 838-3677</strong> to schedule your cleaning service and discover why clients across Tampa Bay consistently choose Sparkle & Sage.</p>
"""

# Let's append extra_text to all python content definitions or update files directly
import re

for filename in os.listdir('/home/knoyes75/sparkle-sage-site'):
    if filename.endswith('.html'):
        path = os.path.join('/home/knoyes75/sparkle-sage-site', filename)
        with open(path, 'r') as f:
            content = f.read()
        if 'Our Professional Cleaning Methodology' not in content:
            # insert before main closing tag or footer
            content = content.replace('</main>', extra_text + '\n</main>')
            with open(path, 'w') as f:
                f.write(content)
                print(f"Expanded {filename}")

