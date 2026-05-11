from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

img = Image.open('1.jpg')

img.show()
    
print(f"Размер изображения: {img.size}") # (ширина, высота)
print(f"Формат: {img.format}")
print(f"Цветовая модель: {img.mode}")




img = Image.open('2.jpg')

width, height = img.size
small_img = img.resize((width // 3, height // 3))
small_img.save('3.jpg')

horizontal_flip = img.transpose(Image.FLIP_LEFT_RIGHT)
horizontal_flip.save('4.jpg')

vertical_flip = img.transpose(Image.FLIP_TOP_BOTTOM)
vertical_flip.save('5.jpg')

print("Изображения успешно сохранены.")




output_dir = 'filtered_images'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for i in range(1, 6):
    filename = f"{i}.jpg"
    if os.path.exists(filename):
        with Image.open(filename) as img:
            filtered_img = img.filter(ImageFilter.CONTOUR)
            
            filtered_img.save(f"{output_dir}/filtered_{filename}")
            print(f"Файл {filename} обработан.")



def add_watermark(image_path, text):
    with Image.open(image_path).convert("RGBA") as base:
        txt_layer = Image.new("RGBA", base.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(txt_layer)
        
        width, height = base.size
        draw.text((width - 150, height - 50), text, fill=(255, 255, 255, 128))
        
        out = Image.alpha_composite(base, txt_layer)
        out.convert("RGB").save(f"watermarked_{image_path}")

images_to_process = ['1.jpg', '2.jpg']
for img_p in images_to_process:
    if os.path.exists(img_p):
        add_watermark(img_p, "MY WATERMARK")
        print(f"Водяной знак добавлен на {img_p}")
