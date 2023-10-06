class Table:
    def __init__(self, material, shape, num_legs, height, extendable, color):
        self.material = material
        self.shape = shape
        self.num_legs = num_legs
        self.height = height
        self.extendable = extendable
        self.color = color

    def place_items(self):
        print("Вы можете разместить предметы на столе")

    def adjust_height(self, new_height):
        self.height = new_height
        print(f"Высота стола теперь установлена на {new_height}")

    def extend(self):
        if self.extendable:
            print("Стол теперь разложен")
        else:
            print("Этот стол не раскладывается")

    def paint(self, new_color):
        self.color = new_color
        print(f"Стол теперь покрашен в цвет  {new_color}")
