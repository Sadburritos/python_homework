class XoViev:
    def show(self, text):
        print(text)

    def show_win(self):
        print("Better player wins ")

    def show_lose(self):
        print("Skill issue")

    def input(self, char):
        while True:
            user_input = input(f"Ваш ход {char}: ")
            if self.validate_input(user_input):
                return user_input
            else:
                print("Некорректный ввод. Введите в формате буква+цифра")

    def validate_input(self, user_input):
        if len(user_input) != 2:
            return False
        row, col = user_input[0], user_input[1]
        if not row.isalpha() or not col.isdigit():
            return False
        if 'a' <= row <= 'c' and '1' <= col <= '3':
            return True
        return False
