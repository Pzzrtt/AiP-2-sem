import json

# Чтение файла
with open("products.json", 'r', encoding='utf-8') as file:
    data = json.load(file)



for product in data["products"]:
    print(f"Название: {product['name']}")
    print(f"Цена: {product['price']}")
    print(f"Вес: {product['weight']}")
    print("В наличии" if product['available'] else "Нет в наличии!")
    print()


# Добавление нового продукта
name = input("Название нового продукта, введи название: ")
price = int(input("Цена: "))
weight = int(input("Вес: "))
available = input("В наличии? (да/нет): ").lower() == "да"

data["products"].append({
    "name": name,
    "price": price,
    "available": available,
    "weight": weight
})

# Запись в файл
with open("products.json", 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=2)

# Вывод обновленного списка
print("\nОбновленный список продуктов:\n")
for product in data["products"]:
    print(f"Название: {product['name']}")
    print(f"Цена: {product['price']}")
    print(f"Вес: {product['weight']}")
    print("В наличии" if product['available'] else "Нет в наличии!")
    print()