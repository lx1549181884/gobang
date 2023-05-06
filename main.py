import sys

import pygame

from config import BOARD_SIZE, WINDOW_SIZE, BLOCK_SIZE, LINE_END, LINE_START
from core import Core

if __name__ == '__main__':
    print(pygame.font.get_fonts())
    core = Core(BOARD_SIZE)
    line_color = '#555555'
    black_color = '#111111'
    white_color = '#dddddd'
    # 使用pygame之前必须初始化
    pygame.init()
    # 设置主屏窗口
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    # screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE), pygame.NOFRAME)
    # 设置窗口的标题
    pygame.display.set_caption('gobang')
    # 字体
    myfont = pygame.font.SysFont("microsoftyahei", 16)
    while True:

        # 背景
        screen.fill('#333333')
        # 划线
        for i in range(BOARD_SIZE + 1):
            offset = LINE_START + i * BLOCK_SIZE
            pygame.draw.line(screen, line_color, (LINE_START, offset), (LINE_END, offset))
            pygame.draw.line(screen, line_color, (offset, LINE_START), (offset, LINE_END))
        # 画圆
        for x in range(BOARD_SIZE):
            for y in range(BOARD_SIZE):
                chess = core.board[x][y]
                if chess is not None:
                    center = (LINE_START + x * BLOCK_SIZE, LINE_START + y * BLOCK_SIZE)
                    pygame.draw.circle(screen, black_color if chess else white_color, center, BLOCK_SIZE / 3)
        # 提示
        text = ''
        if core.result == Core.Result.DRAW:
            text = '平局，点击重新开始'
        elif core.result == Core.Result.BLACK_WIN:
            text = '黑棋胜，点击重新开始'
        elif core.result == Core.Result.WHITE_WIN:
            text = '白棋胜，点击重新开始'
        else:
            if core.is_black_turn:
                text = '黑棋落子'
            else:
                text = '白棋落子'
        render = myfont.render(text, True, white_color)
        text_w, text_h = render.get_size()
        text_x = (WINDOW_SIZE - text_w) / 2
        text_y = (LINE_START - text_h) / 2
        screen.blit(render, (text_x, text_y))
        pygame.display.update()  # 更新屏幕内容

        # 循环获取事件，监听事件状态
        for event in pygame.event.get():
            # 判断用户是否点了"X"关闭按钮,并执行if代码段
            if event.type == pygame.QUIT:
                # 卸载所有模块
                pygame.quit()
                # 终止程序，确保退出程序
                sys.exit()
            # 落子
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x = event.pos[0]
                y = event.pos[1]
                if core.result is not None and text_x < x < text_x + text_w and text_y < y < text_y + text_h:
                    core.reset()
                else:
                    try:
                        x = int((x - LINE_START / 2) / BLOCK_SIZE)
                        y = int((y - LINE_START / 2) / BLOCK_SIZE)
                        core.drop(x, y)
                    except:
                        pass
