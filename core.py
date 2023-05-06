class Core:
    class Result:
        DRAW = 0
        BLACK_WIN = 1
        WHITE_WIN = 2

    def __init__(self, board_size):
        self.board_size = board_size
        self.board = [[None for _ in range(board_size)] for _ in range(board_size)]
        self.is_black_turn = True
        self.result = None

    def reset(self):
        self.__init__(self.board_size)

    def drop(self, x, y):
        if self.result is not None:
            raise Exception(fr'game is over, result is {self.result}')
        elif self.board[x][y] is not None:
            raise Exception(fr'board[{x}][{y}] already has chess')
        else:
            self.board[x][y] = self.is_black_turn
            if self.is_five_connect(x, y, (1, 0)) or self.is_five_connect(x, y, (0, 1)) or \
                    self.is_five_connect(x, y, (1, 1)) or self.is_five_connect(x, y, (1, -1)):
                self.result = Core.Result.BLACK_WIN if self.is_black_turn else Core.Result.WHITE_WIN
            else:
                full_board = all([c is not None for row in self.board for c in row])
                if full_board: self.result = Core.Result.DRAW
            if self.result is None: self.is_black_turn = not self.is_black_turn
            print(self.__dict__)

    def is_five_connect(self, x, y, direct):
        chess = self.board[x][y]
        if chess is None: raise Exception(fr'board[{x}][{y}] has no chess')
        count = 1
        temp_x = x
        temp_y = y
        try:
            while True:
                temp_x, temp_y, temp_chess = self.next(temp_x, temp_y, direct)
                if temp_chess == chess:
                    count += 1
                else:
                    break
        except:
            pass

        temp_x = x
        temp_y = y
        try:
            while True:
                temp_x, temp_y, temp_chess = self.next(temp_x, temp_y, (-direct[0], -direct[1]))
                if temp_chess == chess:
                    count += 1
                else:
                    break
        except:
            pass

        return count >= 5

    def next(self, x, y, direct):
        x = x + direct[0]
        y = y + direct[1]
        return x, y, self.board[x][y]
