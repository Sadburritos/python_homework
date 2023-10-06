class Fork:
    def __init__(self, material, tine_count, color, handle_type, salad_forks, dessert_forks):
        self.material = material
        self.tine_count = tine_count
        self.color = color
        self.handle_type = handle_type
        self.salad_forks = salad_forks
        self.dessert_forks = dessert_forks

    def pierce_food(self):
        print("Вы можете использовать вилку для прокалывания пищи")

    def serve_salad(self):
        if self.salad_forks:
            print("Вилку можно использовать для подачи салата")
        else:
            print("Эта вилка не подходит для салата")

    def use_as_dessert_fork(self):
        if self.dessert_forks:
            print("Вы можете использовать вилку как десертную вилку")
        else:
            print("Эта вилка не предназначена для десертов")

    def change_color(self, new_color):
        self.color = new_color
        print(f"Вилка теперь{new_color}")
