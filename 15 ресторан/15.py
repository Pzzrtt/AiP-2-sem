class Restaurant:

    def __init__(self, restaurant_name, cuisine_type, rating=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating
        self.cleaner = None  # Пока уборщика нет

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


print("ЗАДАНИЕ 10.1")

newRestaurant = Restaurant("Вкусные истории", "европейскую")

print(f"Название ресторана: {newRestaurant.restaurant_name}")
print(f"Тип кухни: {newRestaurant.cuisine_type}")

newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()

print("ЗАДАНИЕ 10.2")

restaurant_1 = Restaurant("Вкусные истории", "европейскую")
restaurant_2 = Restaurant("Сакура", "японскую")
restaurant_3 = Restaurant("Пекин", "китайскую")

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

print("ЗАДАНИЕ 10.3")

print(f"Начальный рейтинг '{restaurant_1.restaurant_name}': {restaurant_1.rating}")
restaurant_1.update_rating(5)
restaurant_1.describe_restaurant()


print("ЗАДАНИЕ 10.4")

cleaner_ivan = Cleaner("Иван")
restaurant_1.hire_cleaner(cleaner_ivan)
restaurant_1.request_cleaning()