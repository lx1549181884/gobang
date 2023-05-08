import sys

import pygame

from config import BOARD_SIZE, WINDOW_SIZE, BLOCK_SIZE, LINE_END, LINE_START, BG_COLOR, LINE_COLOR, BLACK_COLOR, \
    WHITE_COLOR
from core import Core


def _get_tip_text(core):
    if core.winner == 0:
        return '平局，点击重新开始'
    elif core.winner == Core.BLACK:
        return '黑棋胜，点击重新开始'
    elif core.winner == Core.WHITE:
        return '白棋胜，点击重新开始'
    elif core.turn == Core.BLACK:
        return '黑棋落子'
    else:
        return '白棋落子'


if __name__ == '__main__':
    core = Core(BOARD_SIZE)
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption('gobang')
    font = pygame.font.SysFont("microsoftyahei", 16)
    while True:
        # 棋盘
        screen.fill(BG_COLOR)
        for i in range(BOARD_SIZE + 1):
            offset = LINE_START + i * BLOCK_SIZE
            pygame.draw.line(screen, LINE_COLOR, (LINE_START, offset), (LINE_END, offset))
            pygame.draw.line(screen, LINE_COLOR, (offset, LINE_START), (offset, LINE_END))
        # 棋子
        for y, row in enumerate(core.board):
            for x, chess in enumerate(row):
                if chess is not None:
                    center = (LINE_START + x * BLOCK_SIZE, LINE_START + y * BLOCK_SIZE)
                    color = BLACK_COLOR if chess == Core.BLACK else WHITE_COLOR
                    pygame.draw.circle(screen, color, center, BLOCK_SIZE / 3)
        # 提示文字
        tip_render = font.render(_get_tip_text(core), True, WHITE_COLOR)
        tip_w, tip_h = tip_render.get_size()
        tip_x = (WINDOW_SIZE - tip_w) / 2
        tip_y = (LINE_START - tip_h) / 2
        screen.blit(tip_render, (tip_x, tip_y))
        # 更新UI
        pygame.display.update()

        # 循环监听事件
        for event in pygame.event.get():
            # 关闭按钮
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # 鼠标点击
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x = event.pos[0]
                y = event.pos[1]
                if core.winner is not None and tip_x < x < tip_x + tip_w and tip_y < y < tip_y + tip_h:
                    core.reset()  # 重新开始
                else:
                    x = int((x - LINE_START / 2) / BLOCK_SIZE)
                    y = int((y - LINE_START / 2) / BLOCK_SIZE)
                    core.drop(x, y)  # 落子
