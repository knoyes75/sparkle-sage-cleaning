from PIL import Image, ImageDraw
import os

os.makedirs('/home/knoyes75/sparkle-sage-site/images', exist_ok=True)

def create_graphic(filename, title, subtitle, bg_color=(15, 23, 42), accent=(16, 185, 129)):
    img = Image.new('RGB', (800, 500), color=bg_color)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 800, 30], fill=accent)
    d.rectangle([0, 470, 800, 500], fill=accent)
    d.rectangle([50, 50, 750, 450], outline=accent, width=3)
    img.save(f'/home/knoyes75/sparkle-sage-site/images/{filename}.jpg')

create_graphic('res-1', 'Bathroom Sanitization', 'Sparkle & Sage')
create_graphic('res-2', 'Kitchen Detailing', 'Sparkle & Sage')
create_graphic('com-1', 'Office Workstations', 'Sparkle & Sage')
create_graphic('com-2', 'Conference Rooms', 'Sparkle & Sage')
create_graphic('air-1', 'Bed Staging & Linens', 'Sparkle & Sage')
create_graphic('air-2', 'Turnover Restocking', 'Sparkle & Sage')
create_graphic('loc-1', 'Tampa Bay Region', 'Sparkle & Sage')
create_graphic('loc-2', 'Local Cleaners', 'Sparkle & Sage')
print('Additional custom graphics created.')
