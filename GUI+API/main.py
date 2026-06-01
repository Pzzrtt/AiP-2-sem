import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
from io import BytesIO
import webbrowser


profile_url = ""


def open_profile():
    if profile_url:
        webbrowser.open(profile_url)


def find_user():
    global profile_url

    username = entry_username.get().strip()

    if not username:
        messagebox.showerror("Ошибка", "Введите логин GitHub")
        return

    try:
        # Запрос профиля
        user_url = f"https://api.github.com/users/{username}"
        response = requests.get(user_url)

        if response.status_code == 404:
            messagebox.showerror("Ошибка", "Пользователь не найден")
            return

        user_data = response.json()

        profile_url = user_data["html_url"]

        # Основная информация
        name_value.config(text=user_data.get("name") or "Не указано")
        login_value.config(text=user_data.get("login"))
        repos_value.config(text=user_data.get("public_repos"))
        followers_value.config(text=user_data.get("followers"))
        following_value.config(text=user_data.get("following"))
        company_value.config(text=user_data.get("company") or "Не указано")
        location_value.config(text=user_data.get("location") or "Не указано")

        # Аватар
        avatar_url = user_data["avatar_url"]
        avatar_response = requests.get(avatar_url)

        image = Image.open(BytesIO(avatar_response.content))
        image = image.resize((120, 120))

        photo = ImageTk.PhotoImage(image)

        avatar_label.config(image=photo)
        avatar_label.image = photo

        # Репозитории
        repos_list.delete(0, tk.END)

        repos_url = f"https://api.github.com/users/{username}/repos"
        repos_response = requests.get(repos_url)

        repos_data = repos_response.json()

        if len(repos_data) == 0:
            repos_list.insert(tk.END, "Нет публичных репозиториев")

        else:
            for repo in repos_data:
                repos_list.insert(
                    tk.END,
                    f"{repo['name']} ⭐ {repo['stargazers_count']}"
                )

    except Exception as e:
        messagebox.showerror("Ошибка", str(e))


# Главное окно
root = tk.Tk()
root.title("GitHub Profile Explorer")
root.geometry("800x650")
root.resizable(False, False)

# Заголовок
title = tk.Label(
    root,
    text="GitHub Profile Explorer",
    font=("Arial", 18, "bold")
)
title.pack(pady=10)

# Поиск
search_frame = tk.Frame(root)
search_frame.pack(pady=10)

tk.Label(
    search_frame,
    text="GitHub логин:"
).pack(side=tk.LEFT)

entry_username = tk.Entry(
    search_frame,
    width=30
)
entry_username.pack(side=tk.LEFT, padx=5)

search_button = tk.Button(
    search_frame,
    text="Найти",
    command=find_user
)
search_button.pack(side=tk.LEFT)

# Верхняя часть
top_frame = tk.Frame(root)
top_frame.pack(pady=10)

# Аватар
avatar_label = tk.Label(top_frame)
avatar_label.grid(row=0, column=0, rowspan=8, padx=20)

# Информация
tk.Label(top_frame, text="Имя:", font=("Arial", 10, "bold")).grid(row=0, column=1, sticky="w")
name_value = tk.Label(top_frame, text="-")
name_value.grid(row=0, column=2, sticky="w")

tk.Label(top_frame, text="Логин:", font=("Arial", 10, "bold")).grid(row=1, column=1, sticky="w")
login_value = tk.Label(top_frame, text="-")
login_value.grid(row=1, column=2, sticky="w")

tk.Label(top_frame, text="Репозитории:", font=("Arial", 10, "bold")).grid(row=2, column=1, sticky="w")
repos_value = tk.Label(top_frame, text="-")
repos_value.grid(row=2, column=2, sticky="w")

tk.Label(top_frame, text="Подписчики:", font=("Arial", 10, "bold")).grid(row=3, column=1, sticky="w")
followers_value = tk.Label(top_frame, text="-")
followers_value.grid(row=3, column=2, sticky="w")

tk.Label(top_frame, text="Подписки:", font=("Arial", 10, "bold")).grid(row=4, column=1, sticky="w")
following_value = tk.Label(top_frame, text="-")
following_value.grid(row=4, column=2, sticky="w")

tk.Label(top_frame, text="Компания:", font=("Arial", 10, "bold")).grid(row=5, column=1, sticky="w")
company_value = tk.Label(top_frame, text="-")
company_value.grid(row=5, column=2, sticky="w")

tk.Label(top_frame, text="Локация:", font=("Arial", 10, "bold")).grid(row=6, column=1, sticky="w")
location_value = tk.Label(top_frame, text="-")
location_value.grid(row=6, column=2, sticky="w")

profile_button = tk.Button(
    top_frame,
    text="Открыть профиль",
    command=open_profile
)
profile_button.grid(row=7, column=1, pady=10)

# Список репозиториев
repos_title = tk.Label(
    root,
    text="Публичные репозитории",
    font=("Arial", 14, "bold")
)
repos_title.pack()

repos_frame = tk.Frame(root)
repos_frame.pack(pady=10)

scrollbar = tk.Scrollbar(repos_frame)

repos_list = tk.Listbox(
    repos_frame,
    width=80,
    height=18
)

scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
repos_list.pack(side=tk.LEFT)

repos_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=repos_list.yview)

root.mainloop()