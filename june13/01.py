class Chair:
    def __init__(self, material, color, num_legs, backrest_height, cushioned, armrests):
        self.material = material
        self.color = color
        self.num_legs = num_legs
        self.backrest_height = backrest_height
        self.cushioned = cushioned
        self.armrests = armrests

    def sit(self):
        print("Вы сидите на стуле")

    def adjust_height(self, new_height):
        self.backrest_height = new_height
        print(f"Высота спинки теперь установлена {new_height}")

    def paint(self, new_color):
        self.color = new_color
        print(f"Стул теперь окрашен в {new_color}")

    def has_armrests(self):
        return self.armrests