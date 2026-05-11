ru_en = {}

with open("en-ru.txt", 'r', encoding='utf-8') as file:
    for line in file:
        if '-' in line:
            eng, rus = line.strip().split('-')
            eng = eng.strip()
            for r in rus.split(','):
                r = r.strip()
                if r not in ru_en:
                    ru_en[r] = [eng]
                else:
                    ru_en[r].append(eng)

# Запись русско-английского словаря
with open("ru-en.txt", 'w', encoding='utf-8') as file:
    for russian in sorted(ru_en.keys()):
        english = ', '.join(sorted(ru_en[russian]))
        file.write(f"{russian} – {english}\n")

print("Словарь успешно создан!")