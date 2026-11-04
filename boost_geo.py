import os, re

extra = """
<h3 class="text-2xl font-bold mt-8 mb-4 text-slate-900">Local Neighborhood Commitment</h3>
<p class="mb-4">Our dedication to the local community goes beyond basic cleaning. We invest time in understanding the unique needs of property owners in this area, ensuring that every service call exceeds expectations. Whether you require recurring weekly housekeeping, bi-weekly maintenance, or a one-time deep cleaning before an important event, Sparkle & Sage is equipped with the right tools and expertise to deliver immaculate results.</p>
<p class="mb-4">We take immense pride in our punctuality, transparency, and friendly customer service. You will never have to worry about hidden fees or unreliable contractors. Reach out today to experience the highest standard of cleanliness.</p>
"""

for f in ['clearwater.html', 'brandon.html', 'st-petersburg.html', 'tampa.html', 'contact.html']:
    path = os.path.join('/home/knoyes75/sparkle-sage-site', f)
    with open(path, 'r') as file:
        content = file.read()
    if 'Local Neighborhood Commitment' not in content:
        content = content.replace('</main>', extra + '\n</main>')
        with open(path, 'w') as file:
            file.write(content)
        print(f"Boosted {f}")

