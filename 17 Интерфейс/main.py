import tkinter as tk

#главное окно
root = tk.Tk()
root.title("Калькулятор среднего балла")
root.geometry("400x400")

# Надпись для вывода результатов
label_result = tk.Label(root, text="Введите оценки", font=("Arial", 16))
label_result.pack(pady=20)

# Поле ввода: Математика
label_math = tk.Label(root, text="Математика", font=("Arial", 12))
label_math.pack()
entry_math = tk.Entry(root, font=("Arial", 14))
entry_math.pack(pady=5)

# Поле ввода: Физика
label_phys = tk.Label(root, text="Физика", font=("Arial", 12))
label_phys.pack()
entry_phys = tk.Entry(root, font=("Arial", 14))
entry_phys.pack(pady=5)

# Поле ввода: Программирование
label_prog = tk.Label(root, text="Программирование", font=("Arial", 12))
label_prog.pack()
entry_prog = tk.Entry(root, font=("Arial", 14))
entry_prog.pack(pady=5)

# Функция для расчёта среднего балла
def calculate_average():
    try:
        math = float(entry_math.get())
        phys = float(entry_phys.get())
        prog = float(entry_prog.get())
        average = round((math + phys + prog) / 3, 1)
        label_result.config(text=f"Средний балл: {average}")
    except ValueError:
        label_result.config(text="Ошибка: введите числа")

# Функция для очистки полей
def clear_fields():
    entry_math.delete(0, tk.END)
    entry_phys.delete(0, tk.END)
    entry_prog.delete(0, tk.END)
    label_result.config(text="Введите оценки")

# Кнопка расчёта
button_calc = tk.Button(root, text="Посчитать средний балл", command=calculate_average)
button_calc.pack(pady=10)

# Кнопка очистки
button_clear = tk.Button(root, text="Очистить", command=clear_fields)
button_clear.pack(pady=5)

# Запуск главного цикла
root.mainloop()