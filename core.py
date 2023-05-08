class Core:
    BLACK = 1
    WHITE = -1

    def __init__(self, board_size):
        self.board_size = board_size
        self.board = [[None for _ in range(board_size)] for _ in range(board_size)]
        self.turn = Core.BLACK
        self.winner = None

    # 重置
    def reset(self):
        self.__init__(self.board_size)

    # 落子
    def drop(self, x, y):
        if self.winner is None and self.board[y][x] is None:
            self.board[y][x] = self.turn
            if self._five_connect(x, y, (1, 0)) or self._five_connect(x, y, (0, 1)) or \
                    self._five_connect(x, y, (1, 1)) or self._five_connect(x, y, (1, -1)):
                self.winner = self.turn  # 有输赢
            else:
                for row in self.board:
                    for chess in row:
                        if chess is None:
                            self.turn = -self.turn  # 继续
                            return
                self.winner = 0  # 平局

    # 是否五子连珠
    def _five_connect(self, x, y, direct):
        return self._same_num(x, y, direct) + self._same_num(x, y, (-direct[0], -direct[1])) >= 4

    # 获取相同棋子数目
    def _same_num(self, x, y, direct):
        chess = self.board[y][x]
        count = 0
        if chess is not None:
            while True:
                x += direct[0]
                y += direct[1]
                if 0 <= x < self.board_size and 0 <= y < self.board_size:
                    if self.board[y][x] == chess:
                        count += 1
                    else:
                        break
        return count
