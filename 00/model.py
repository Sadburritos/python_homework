class XoModel:
    def __init__(self, size):
        self.size = size
        self.table = []
        self.cell = 5

        for r in range(size):
            self.table.append([])
            for c in range(size):
                self.table[r].append("__")

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

    def row(self, row):
        return tuple(self.table[row])

    def col(self, col):
        return tuple(self.table[i][col] for i in range(self.size))

    def diag(self, main=True):
        if main:
            return tuple(self.table[i][i] for i in range(self.size))
        else:
            return tuple(self.table[i][self.size - i - 1] for i in range(self.size))

    def __str__(self):
        s = ''
        num = 1
        colum = ord("a")

        for e in self.table:
            print(chr(colum), end="  ")
            colum += 1
        print()

        for r in self.table:
            num = str(num)
            s += " ".join(r) + num + "\n"
            num = int(num)
            num += 1

        return s



# xo_board = XoModel(10)
#
#
# print(xo_board)
#
# xo_board.set(1, 1, 'O')
# xo_board.set(2, 2, 'X')
#
# print(xo_board)
#
#
# main_diag = xo_board.diag(main=True)
# side_diag = xo_board.diag(main=False)
#
# print(main_diag)
# print(side_diag)