import pygame
import sys


# =====================
# pygame 初始化
# =====================

pygame.init()


# =====================
# 窗口参数
# =====================

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)

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
# 绘制箭头
# =====================

def draw_arrow(screen, row, col, direction):

    # 根据行列计算箭头所在格子的左上角坐标
    x = BOARD_X + col * GRID_SIZE
    y = BOARD_Y + row * GRID_SIZE

    color = (30, 30, 30)

    # 右箭头
    if direction == "RIGHT":

        pygame.draw.line(
            screen,
            color,
            (x + 20, y + 40),
            (x + 60, y + 40),
            5
        )

        pygame.draw.polygon(
            screen,
            color,
            [
                (x + 60, y + 40),
                (x + 45, y + 25),
                (x + 45, y + 55)
            ]
        )

    # 左箭头
    elif direction == "LEFT":

        pygame.draw.line(
            screen,
            color,
            (x + 60, y + 40),
            (x + 20, y + 40),
            5
        )

        pygame.draw.polygon(
            screen,
            color,
            [
                (x + 20, y + 40),
                (x + 35, y + 25),
                (x + 35, y + 55)
            ]
        )

    # 上箭头
    elif direction == "UP":

        pygame.draw.line(
            screen,
            color,
            (x + 40, y + 60),
            (x + 40, y + 20),
            5
        )

        pygame.draw.polygon(
            screen,
            color,
            [
                (x + 40, y + 20),
                (x + 25, y + 35),
                (x + 55, y + 35)
            ]
        )

    # 下箭头
    elif direction == "DOWN":

        pygame.draw.line(
            screen,
            color,
            (x + 40, y + 20),
            (x + 40, y + 60),
            5
        )

        pygame.draw.polygon(
            screen,
            color,
            [
                (x + 40, y + 60),
                (x + 25, y + 45),
                (x + 55, y + 45)
            ]
        )


# =====================
# 箭头数据
# =====================

arrows = [
    {"row": 1, "col": 1, "direction": "RIGHT"},
    {"row": 1, "col": 2, "direction": "UP"},
    {"row": 2, "col": 1, "direction": "DOWN"},
    {"row": 2, "col": 2, "direction": "LEFT"}
]


# =====================
# 游戏循环
# =====================

running = True

while running:

    # =====================
    # 处理事件
    # =====================

    for event in pygame.event.get():

        # 点击窗口关闭按钮
        if event.type == pygame.QUIT:
            running = False

        # 鼠标按下
        if event.type == pygame.MOUSEBUTTONDOWN:

            # 只检测鼠标左键
            if event.button == 1:

                # 获取鼠标点击位置
                mouse_x, mouse_y = event.pos

                # 判断鼠标是否点击在棋盘范围内
                if (
                    BOARD_X <= mouse_x < BOARD_X + COLS * GRID_SIZE
                    and
                    BOARD_Y <= mouse_y < BOARD_Y + ROWS * GRID_SIZE
                ):

                    # 将鼠标坐标转换成棋盘的行列坐标
                    col = (mouse_x - BOARD_X) // GRID_SIZE
                    row = (mouse_y - BOARD_Y) // GRID_SIZE

                    print("点击位置：", row, col)

                    # 查找这个位置是否存在箭头
                    for arrow in arrows:

                        if (
                            arrow["row"] == row
                            and arrow["col"] == col
                        ):

                            print(
                                "点击到了箭头：",
                                arrow["direction"]
                            )

                            break


    # =====================
    # 绘制游戏画面
    # =====================

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


    # 根据 arrows 数据绘制所有箭头
    for arrow in arrows:

        draw_arrow(
            screen,
            arrow["row"],
            arrow["col"],
            arrow["direction"]
        )


    # 刷新显示
    pygame.display.update()


# =====================
# 退出游戏
# =====================

pygame.quit()
sys.exit()