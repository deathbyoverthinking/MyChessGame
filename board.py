import inspect


class Figure():
    def __init__(self, type: str, position: list, color: str):
        self.type = type
        self.position = position
        self.color = color

    def isMoveValid(self, move_position):
        move_x, move_y = move_position
        all_symbols = "**ABCDEFGH**"
        all_numbers = "**12345678**"
        self_symbol_ind = all_symbols.index(self.position[0])
        self_number_ind = all_numbers.index(str(self.position[1]))
        if self.type == "knight":
            allowed_moves = [[all_symbols[self_symbol_ind - 1], all_numbers[self_number_ind + 2]],
                             [all_symbols[self_symbol_ind + 1], all_numbers[self_number_ind + 2]],
                             [all_symbols[self_symbol_ind + 2], all_numbers[self_number_ind + 1]],
                             [all_symbols[self_symbol_ind + 2], all_numbers[self_number_ind - 1]],
                             [all_symbols[self_symbol_ind + 1], all_numbers[self_number_ind - 2]],
                             [all_symbols[self_symbol_ind - 1], all_numbers[self_number_ind - 2]],
                             [all_symbols[self_symbol_ind - 2], all_numbers[self_number_ind - 1]],
                             [all_symbols[self_symbol_ind - 2], all_numbers[self_number_ind + 1]]]
            allowed_moves = [move for move in allowed_moves if '*' not in move]
            if [move_x, move_y] in allowed_moves:
                for figure in figures:
                    if figure.position == [move_x, move_y] and figure.color == self.color:
                        break
                    elif figure.position == [move_x, move_y] and figure.color != self.color:
                        return True
                else:
                    return True
            else:
                return False

        elif self.type == "pawn":
            if self.color == "black" and self.position[1] == 7:
                allowed_moves = [[self.position[0], self.position[1]-1], [self.position[0], self.position[1]-2]]
            elif self.color == "white" and self.position[1] == 2:
                allowed_moves = [[self.position[0], self.position[1] + 1], [self.position[0], self.position[1] + 2]]
            elif self.color == "black":
                allowed_moves = [[self.position[0], self.position[1] - 1]]
            elif self.color == "white":
                allowed_moves = [[self.position[0], self.position[1] + 1]]
            allowed_moves = [move for move in allowed_moves if '*' not in move]
            for figure in figures:
                if figure.position == [move_x, int(move_y)]:
                    return False
                if move_y == self.position[1] - 2 and figure.position[1] == self.position[1] - 1:
                    return False
                if move_y == self.position[1] + 2 and figure.position[1] == self.position[1] + 1:
                    return False

            else:
                if [move_x, int(move_y)] in allowed_moves:
                    return True
                else:
                    return False


        elif self.type == "rook":
            ...

        elif self.type == "king":
            ...

        elif self.type == "bishop":
            ...

        elif self.type == "queen":
            ...


    def move(self, move_position):
        move_x, move_y = move_position
        self.position = [move_x, int(move_y)]


    def getVarName(self):
        for i in inspect.currentframe().f_back.f_locals.items():
            if id(self) == id(i[1]):
                return i[0]

    def getName(self):
        return self.type[0] + self.color[0]


rb1 = Figure("rook", ["A", 8], "black")
rb2 = Figure("rook", ["H", 8], "black")
kb1 = Figure("knight", ["B", 8], "black")
kb2 = Figure("knight", ["G", 8], "black")
bb1 = Figure("bishop", ["C", 8], "black")
bb2 = Figure("bishop", ["F", 8], "black")
kb = Figure("king", ["E", 8], "black")
qb = Figure("queen", ["D", 8], "black")
pb1 = Figure("pawn", ["A", 7], "black")
pb2 = Figure("pawn", ["B", 7], "black")
pb3 = Figure("pawn", ["C", 7], "black")
pb4 = Figure("pawn", ["D", 7], "black")
pb5 = Figure("pawn", ["E", 7], "black")
pb6 = Figure("pawn", ["F", 7], "black")
pb7 = Figure("pawn", ["G", 7], "black")
pb8 = Figure("pawn", ["H", 7], "black")
rw1 = Figure("rook", ["A", 1], "white")
rw2 = Figure("rook", ["H", 1], "white")
kw1 = Figure("knight", ["B", 1], "white")
kw2 = Figure("knight", ["G", 1], "white")
bw1 = Figure("bishop", ["C", 1], "white")
bw2 = Figure("bishop", ["F", 1], "white")
kw = Figure("king", ["E", 1], "white")
qw = Figure("queen", ["D", 1], "white")
pw1 = Figure("pawn", ["A", 2], "white")
pw2 = Figure("pawn", ["B", 2], "white")
pw3 = Figure("pawn", ["C", 2], "white")
pw4 = Figure("pawn", ["D", 2], "white")
pw5 = Figure("pawn", ["E", 2], "white")
pw6 = Figure("pawn", ["F", 2], "white")
pw7 = Figure("pawn", ["G", 2], "white")
pw8 = Figure("pawn", ["H", 2], "white")

figures = [rb1, rb2, kb1, kb2, bb1, bb2, kb, qb, rw1, rw2, kw1, kw2, bw1, bw2, kw, qw, pb1, pb2, pb3, pb4, pb5, pb6,
           pb7, pb8, pw1, pw2, pw3, pw4, pw5, pw6, pw7, pw8]
