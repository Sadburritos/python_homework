class XoModel:
    def __init__(self, size):
        self.size = size
        self.table = []
        self.cell = 5

        for r in range(size):
            self.table.append([])
            for c in range(size):
                self.table[r].append("")

    def __repr__(self):
        s = ''
        num = 1
        colum = ord("a")
        for e in self.table:
            print(chr(colum), end="  ")
            colum += 1

        print()

        for r in self.table:
            num = str(num)
            s += str(r) + num + "\n"
            num = int(num)
            num += 1

        return s[:-1]
    def is_empty(self, row, col):
        if self.table[row][col] == "":
             return "empty"

    def set(self, row, col, char):
        self.table[row][col] = char



