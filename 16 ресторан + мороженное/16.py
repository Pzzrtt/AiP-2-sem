class Restaurant:

    def __init__(self, restaurant_name, cuisine_type, rating=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating
        self.cleaner = None

    def describe_restaurant(self):
        print(f"Ресторан '{self.restaurant_name}' предлагает {self.cuisine_type} кухню. Рейтинг: {self.rating}")

    def open_restaurant(self):
        print(f"Ресторан '{self.restaurant_name}' сейчас открыт!")

    def update_rating(self, new_rating):
        self.rating = new_rating
        print(f"Рейтинг ресторана '{self.restaurant_name}' обновлён до {self.rating}")

    def hire_cleaner(self, cleaner):
        self.cleaner = cleaner
        print(f"В ресторан '{self.restaurant_name}' нанят уборщик {cleaner.name}")

    def request_cleaning(self):
        if self.cleaner:
            self.cleaner.clean(self.restaurant_name)
        else:
            print(f"В ресторане '{self.restaurant_name}' нет уборщика!")


class Cleaner:
    def __init__(self, name):
        self.name = name

    def clean(self, restaurant_name):
        print(f"Уборщик {self.name} делает уборку в ресторане '{restaurant_name}'.")


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, location="", hours=""):
        super().__init__(restaurant_name, "мороженое")
        self.flavors = []
        self.location = location
        self.hours = hours
        # Инициализация типов мороженого
        self.ice_cream_types = {
            "на палочке": [],
            "мягкое": [],
            "в стаканчике": [],
            "весовое": []
        }

    #Базовый метод вывода сортов
    def show_flavors(self):
        if self.flavors:
            print(f"Сорта мороженого в '{self.restaurant_name}':")
            for flavor in self.flavors:
                print(f"  - {flavor}")
        else:
            print(f"В '{self.restaurant_name}' пока нет мороженого.")

    #11.2.б: Добавление и удаление сортов
    def add_flavor(self, *flavors):
        for flavor in flavors:
            if flavor not in self.flavors:
                self.flavors.append(flavor)
                print(f"Сорт '{flavor}' добавлен в меню.")
            else:
                print(f"Сорт '{flavor}' уже есть в меню.")

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            # Удаляем из всех типов
            for type_list in self.ice_cream_types.values():
                if flavor in type_list:
                    type_list.remove(flavor)
            print(f"Сорт '{flavor}' удалён из меню.")
        else:
            print(f"Сорта '{flavor}' нет в меню.")

    #11.2.в: Проверка наличия сорта
    def check_flavor(self, flavor):
        """Проверяет, есть ли указанный сорт в меню."""
        if flavor in self.flavors:
            print(f"Сорт '{flavor}' есть в меню!")
            return True
        else:
            print(f"Сорта '{flavor}' нет в меню.")
            return False

    #11.2.г: Методы для работы с типами мороженого
    def show_ice_cream_types(self):
        print(f"Типы мороженого в '{self.restaurant_name}':")
        for ice_type in self.ice_cream_types:
            print(f"  - {ice_type}")

    def add_flavor_to_type(self, ice_type, flavor):
        if ice_type not in self.ice_cream_types:
            print(f"Тип '{ice_type}' не существует.")
            return
        if flavor not in self.flavors:
            print(f"Сначала добавьте сорт '{flavor}' в общее меню.")
            return
        if flavor not in self.ice_cream_types[ice_type]:
            self.ice_cream_types[ice_type].append(flavor)
            print(f"Сорт '{flavor}' добавлен в тип '{ice_type}'.")
        else:
            print(f"Сорт '{flavor}' уже есть в типе '{ice_type}'.")

    def show_type_flavors(self, ice_type):
        if ice_type in self.ice_cream_types:
            if self.ice_cream_types[ice_type]:
                print(f"Мороженое '{ice_type}' — сорта:")
                for flavor in self.ice_cream_types[ice_type]:
                    print(f"  - {flavor}")
            else:
                print(f"Нет сортов для типа '{ice_type}'.")
        else:
            print(f"Тип '{ice_type}' не найден.")

    def show_all_types_with_flavors(self):
        print(f"\n Полное меню '{self.restaurant_name}' ")
        for ice_type, flavors_list in self.ice_cream_types.items():
            if flavors_list:
                print(f"  {ice_type}: {', '.join(flavors_list)}")
            else:
                print(f"  {ice_type}: пока нет сортов")

    #11.2.а: Информация о локации и времени работы
    def set_location(self, location):
        self.location = location
        print(f"Локация '{self.restaurant_name}' установлена: {location}")

    def set_hours(self, hours):
        self.hours = hours
        print(f"Часы работы '{self.restaurant_name}': {hours}")

    def show_info(self):
        print(f"\nИнформация о '{self.restaurant_name}':")
        print(f"  Локация: {self.location if self.location else 'не указана'}")
        print(f"  Часы работы: {self.hours if self.hours else 'не указаны'}")
        print(f"  Количество сортов: {len(self.flavors)}")

    # Переопределение метода для полного описания
    def describe_restaurant(self):
        super().describe_restaurant()
        self.show_info()
        self.show_all_types_with_flavors()




print("11.1 — Базовое кафе-мороженое")


my_ice_stand = IceCreamStand("Сладкий пломбир")
my_ice_stand.flavors = ["ванильное", "шоколадное", "клубничное", "фисташковое"]
my_ice_stand.show_flavors()


print("11.2.а — Локация и время работы")


my_ice_stand.set_location("ул. Морозная, д. 5")
my_ice_stand.set_hours("10:00 – 22:00")
my_ice_stand.show_info()


print("11.2.б — Добавление и удаление сортов")


my_ice_stand.add_flavor("манговое", "карамельное")
my_ice_stand.add_flavor("ванильное")  # Уже есть
my_ice_stand.remove_flavor("фисташковое")
my_ice_stand.show_flavors()


print("11.2.в — Проверка наличия сорта")


my_ice_stand.check_flavor("шоколадное")
my_ice_stand.check_flavor("арбузное")


print("11.2.г — Типы мороженого")


# Добавляем сорта в разные типы
my_ice_stand.add_flavor_to_type("мягкое", "ванильное")
my_ice_stand.add_flavor_to_type("мягкое", "шоколадное")
my_ice_stand.add_flavor_to_type("на палочке", "клубничное")
my_ice_stand.add_flavor_to_type("на палочке", "манговое")
my_ice_stand.add_flavor_to_type("в стаканчике", "карамельное")
my_ice_stand.add_flavor_to_type("весовое", "шоколадное")
my_ice_stand.add_flavor_to_type("весовое", "манговое")

# Просмотр типов
my_ice_stand.show_type_flavors("мягкое")
my_ice_stand.show_type_flavors("на палочке")

print("ПОЛНОЕ ОПИСАНИЕ КАФЕ")

my_ice_stand.describe_restaurant()