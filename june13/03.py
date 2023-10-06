class Spoon:
    def __init__(self, material, length, color, handle_type, soup_scoop, forked_tip):
        self.material = material
        self.length = length
        self.color = color
        self.handle_type = handle_type
        self.soup_scoop = soup_scoop
        self.forked_tip = forked_tip

    def stir(self):
        print("Вы можете использовать ложку для размешивания пищи")

    def scoop_soup(self):
        if self.soup_scoop:
            print("Ложка может поднимать суп.")
        else:
            print("Эта ложка не подходит для поднятия супа")

    def use_as_fork(self):
        if self.forked_tip:
            print("Вы можете использовать ложку как вилку")
        else:
            print("Эта ложка не имеет вилкообразного конца")

    def change_color(self, new_color):
        self.color = new_color
        print(f"Ложка теперь  {new_color}.")
