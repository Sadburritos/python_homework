class Plate:
    def __init__(self, material, shape, color, diameter, microwave_safe, dishwasher_safe):
        self.material = material
        self.shape = shape
        self.color = color
        self.diameter = diameter
        self.microwave_safe = microwave_safe
        self.dishwasher_safe = dishwasher_safe

    def serve_food(self):
        print("Вы можете использовать тарелку для подачи пищи.")

    def heat_in_microwave(self):
        if self.microwave_safe:
            print("Тарелку можно использовать в микроволновой печи")
        else:
            print("Эта тарелка не подходит для использования в микроволновой печи")

    def clean_in_dishwasher(self):
        if self.dishwasher_safe:
            print("Тарелку можно мыть в посудомоечной машине")
        else:
            print("Эту тарелку следует мыть вручную")

    def change_color(self, new_color):
        self.color = new_color
        print(f"Тарелка теперь {new_color}")
