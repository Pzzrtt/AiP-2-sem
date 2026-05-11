from PIL import Image, ImageDraw, ImageFont
import os


def crop_card(input_path, output_name):
    with Image.open(input_path) as img:
        width, height = img.size 
        area = (width * 0.1, height * 0.1, width * 0.9, height * 0.9)
        cropped_img = img.crop(area)
        cropped_img.save(output_name)
        return output_name


def process_holiday_card():
    cards_dict = {
        "Новый год": "ny.jpg",
        "День рождения": "bday.jpg",
        "8 марта": "march8.jpg"
    }

    holiday = input("К какому празднику нужна открытка? (Новый год/День рождения/8 марта): ")
    
    if holiday in cards_dict:
        filename = cards_dict[holiday]
        
        #заглушка для теста
        if not os.path.exists(filename):
            Image.new('RGB', (500, 300), color='pink').save(filename)

        name = input("Кого вы хотите поздравить? ")
        
        with Image.open(filename) as img:
            draw = ImageDraw.Draw(img)
            
            # Чтобы сделать текст ЖИРНЫМ, нужно загрузить файл шрифта с начертанием Bold. По умолчанию жирный шрифт
            font_path = "ofont.ru_Chicoree.ttf"
            try:
                font = ImageFont.truetype(font_path, size=30)
            except:
                font = ImageFont.load_default()

            message = f"{name}, поздравляю!"
            
            width, height = img.size
            bbox = draw.textbbox((0, 0), message, font=font)
            text_width = bbox[2] - bbox[0]
            x = (width - text_width) / 2
            y = height - 50

            draw.text((x, y), message, fill="red", font=font)
            
            result_name = f"congrats_{holiday}.png"
            img.save(result_name)
            img.show()
            print(f"Готово! Открытка сохранена как {result_name}")
    else:
        print("Такого праздника не бывает.")


if __name__ == "__main__":
    process_holiday_card()
