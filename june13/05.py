class Knife:
    def __init__(self, material, blade_length, color, handle_type, serrated_edge, steak_knife):
        self.material = material
        self.blade_length = blade_length
        self.color = color
        self.handle_type = handle_type
        self.serrated_edge = serrated_edge
        self.steak_knife = steak_knife

    def cut(self):
        print("Вы можете использовать нож для нарезки пищи")

    def slice_bread(self):
        if self.serrated_edge:
            print("Нож можно использовать для нарезки хлеба")
        else:
            print("Этот нож не подходит для нарезки хлеба")

    def use_as_steak_knife(self):
        if self.steak_knife:
            print("Вы можете использовать нож как нож для стейка")
        else:
            print("Этот нож не предназначен для стейков")

    def change_color(self, new_color):
        self.color = new_color
        print(f"Нож теперь {new_color}")
