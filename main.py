import pygame
import sys


# =====================
# pygame 初始化
# =====================

pygame.init()


# 窗口大小
WIDTH = 800
HEIGHT = 600


# 创建窗口
screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)


# 标题
pygame.display.set_caption(
    "一箭又一箭"
)

# =====================
# 棋盘参数
# =====================

GRID_SIZE = 80

ROWS = 5
COLS = 5


BOARD_X = 200
BOARD_Y = 100

# =====================
# 游戏循环
# =====================

running = True

def draw_arrow(screen, row, col, direction):

    x = BOARD_X + col * GRID_SIZE
    y = BOARD_Y + row * GRID_SIZE


    center = (
        x + GRID_SIZE // 2,
        y + GRID_SIZE // 2
    )


    color = (30,30,30)


    # 右箭头
    if direction == "RIGHT":

        pygame.draw.line(
            screen,
            color,
            (x+20,y+40),
            (x+60,y+40),
            5
        )

        pygame.draw.polygon(
            screen,
            color,
            [
                (x+60,y+40),
                (x+45,y+25),
                (x+45,y+55)
            ]
        )



    # 左箭头
    elif direction == "LEFT":

        pygame.draw.line(
            screen,
            color,
            (x+60,y+40),
            (x+20,y+40),
            5
        )

        pygame.draw.polygon(
            screen,
            color,
            [
                (x+20,y+40),
                (x+35,y+25),
                (x+35,y+55)
            ]
        )



    # 上箭头
    elif direction == "UP":

        pygame.draw.line(
            screen,
            color,
            (x+40,y+60),
            (x+40,y+20),
            5
        )

        pygame.draw.polygon(
            screen,
            color,
            [
                (x+40,y+20),
                (x+25,y+35),
                (x+55,y+35)
            ]
        )



    # 下箭头
    elif direction == "DOWN":

        pygame.draw.line(
            screen,
            color,
            (x+40,y+20),
            (x+40,y+60),
            5
        )

        pygame.draw.polygon(
            screen,
            color,
            [
                (x+40,y+60),
                (x+25,y+45),
                (x+55,y+45)
            ]
        )


while running:

    # 处理事件
    for event in pygame.event.get():

        # 点击关闭窗口
        if event.type == pygame.QUIT:
            running = False


    # 背景颜色
    screen.fill(
        (245, 245, 245)
    )

    # 绘制棋盘

    for row in range(ROWS):

        for col in range(COLS):
            rect = pygame.Rect(
                BOARD_X + col * GRID_SIZE,
                BOARD_Y + row * GRID_SIZE,
                GRID_SIZE,
                GRID_SIZE
            )

            pygame.draw.rect(
                screen,
                (180, 180, 180),
                rect,
                2
            )

    draw_arrow(
        screen,
        1,
        1,
        "RIGHT"
    )

    draw_arrow(
        screen,
        1,
        2,
        "UP"
    )

    draw_arrow(
        screen,
        2,
        1,
        "DOWN"
    )

    draw_arrow(
        screen,
        2,
        2,
        "LEFT"
    )

    # 刷新显示
    pygame.display.update()



# 退出
pygame.quit()
sys.exit()