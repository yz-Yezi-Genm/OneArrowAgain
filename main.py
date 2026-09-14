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

font = pygame.font.SysFont(
    "Microsoft YaHei",
    26
)

big_font = pygame.font.SysFont(
    "Microsoft YaHei",
    48
)

# =====================
# 棋盘参数
# =====================

GRID_SIZE = 80

ROWS = 5
COLS = 5

BOARD_X = 200
BOARD_Y = 100

# 重新开始按钮
restart_button = pygame.Rect(
    620,
    520,
    140,
    50
)

next_button = pygame.Rect(
    620,
    450,
    140,
    50
)

# 开始游戏按钮
start_button = pygame.Rect(
    300,
    350,
    200,
    60
)

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
# 判断箭头前方是否被阻挡
# =====================

def is_blocked(arrow, arrows):

    row = arrow["row"]
    col = arrow["col"]
    direction = arrow["direction"]

    # 遍历其他所有箭头
    for other in arrows:

        # 不需要拿自己和自己比较
        if other is arrow:
            continue

        other_row = other["row"]
        other_col = other["col"]

        # 向右
        if direction == "RIGHT":

            # 同一行，并且其他箭头在自己的右边
            if other_row == row and other_col > col:
                return True

        # 向左
        elif direction == "LEFT":

            # 同一行，并且其他箭头在自己的左边
            if other_row == row and other_col < col:
                return True

        # 向上
        elif direction == "UP":

            # 同一列，并且其他箭头在自己的上方
            if other_col == col and other_row < row:
                return True

        # 向下
        elif direction == "DOWN":

            # 同一列，并且其他箭头在自己的下方
            if other_col == col and other_row > row:
                return True

    # 所有箭头都检查完仍然没发现障碍
    return False

def start_game():

    global current_level
    global arrows
    global mistakes_left
    global game_state

    # 从第一关开始
    current_level = 0

    arrows = [
        arrow.copy()
        for arrow in LEVELS[current_level]
    ]

    mistakes_left = MAX_MISTAKES

    game_state = "PLAYING"

def restart_game():

    global arrows
    global mistakes_left
    global game_state

    arrows = [
        arrow.copy()
        for arrow in LEVELS[current_level]
    ]

    mistakes_left = MAX_MISTAKES

    game_state = "PLAYING"

def next_level():

    global current_level
    global arrows
    global mistakes_left
    global game_state

    # 如果还有下一关
    if current_level < len(LEVELS) - 1:

        current_level += 1

        arrows = [
            arrow.copy()
            for arrow in LEVELS[current_level]
        ]

        mistakes_left = MAX_MISTAKES

        game_state = "PLAYING"

        print(
            "进入第",
            current_level + 1,
            "关"
        )

    else:

        # 所有关卡完成
        game_state = "COMPLETE"

        print("恭喜！全部关卡通过！")

# =====================
# 关卡数据
# =====================

LEVELS = [

    # 第 1 关
    [
        {"row": 1, "col": 1, "direction": "RIGHT"},
        {"row": 1, "col": 2, "direction": "UP"},
        {"row": 2, "col": 1, "direction": "DOWN"},
        {"row": 2, "col": 2, "direction": "LEFT"}
    ],

    # 第 2 关
    [
        {"row": 0, "col": 2, "direction": "UP"},
        {"row": 2, "col": 2, "direction": "UP"}
    ],

    # 第 3 关
    [
        {"row": 0, "col": 1, "direction": "UP"},
        {"row": 1, "col": 1, "direction": "UP"}
    ]
]


# 当前关卡编号
current_level = 0


# 加载当前关卡的箭头
arrows = [
    arrow.copy()
    for arrow in LEVELS[current_level]
]

# =====================
# 游戏状态
# =====================

MAX_MISTAKES = 3
mistakes_left = MAX_MISTAKES

# 程序启动后首先进入开始界面
game_state = "START"

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

                # =====================
                # 开始界面
                # =====================

                if game_state == "START":

                    if start_button.collidepoint(
                            mouse_x,
                            mouse_y
                    ):
                        start_game()

                        print("开始游戏")

                    continue

                # 点击下一关按钮
                if (
                        game_state == "WIN"
                        and next_button.collidepoint(
                    mouse_x,
                    mouse_y
                )
                ):
                    next_level()

                    continue

                # 点击重新开始按钮
                if restart_button.collidepoint(
                        mouse_x,
                        mouse_y
                ):

                    if game_state == "COMPLETE":
                        start_game()

                    else:
                        print("重新开始当前关卡")
                        restart_game()

                    continue


                if game_state != "PLAYING":
                    continue

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

                            # 判断箭头是否被阻挡
                            if is_blocked(arrow, arrows):

                                print("前方有箭头，被阻挡！")

                                # 扣除一次失误机会
                                mistakes_left -= 1

                                if mistakes_left <= 0:
                                    mistakes_left = 0

                                    game_state = "FAILED"

                                    print("游戏失败！")

                                print("剩余失误次数：", mistakes_left)

                            else:

                                print("前方没有箭头，可以飞出！")

                                # 从箭头列表中删除
                                arrows.remove(arrow)

                                # 如果已经没有箭头，说明当前关卡完成
                                if len(arrows) == 0:

                                    # 如果当前已经是最后一关
                                    if current_level == len(LEVELS) - 1:

                                        game_state = "COMPLETE"

                                        print("恭喜！全部关卡通过！")

                                    # 如果后面还有关卡
                                    else:

                                        game_state = "WIN"

                                        print("恭喜，当前关卡通过！")

                                print("剩余箭头数量：", len(arrows))

                            break


    # =====================
    # 绘制游戏画面
    # =====================

    # 背景颜色
    screen.fill(
        (245, 245, 245)
    )

    # =====================
    # 开始界面
    # =====================

    if game_state == "START":
        # 游戏标题
        title_text = big_font.render(
            "一箭又一箭",
            True,
            (40, 40, 40)
        )

        title_rect = title_text.get_rect(
            center=(WIDTH // 2, 180)
        )

        screen.blit(
            title_text,
            title_rect
        )

        # 游戏说明
        tip_text = font.render(
            "按照正确顺序点击箭头，让所有箭头飞出棋盘",
            True,
            (90, 90, 90)
        )

        tip_rect = tip_text.get_rect(
            center=(WIDTH // 2, 260)
        )

        screen.blit(
            tip_text,
            tip_rect
        )

        # 开始按钮
        pygame.draw.rect(
            screen,
            (190, 220, 190),
            start_button,
            border_radius=10
        )

        pygame.draw.rect(
            screen,
            (60, 120, 60),
            start_button,
            2,
            border_radius=10
        )

        start_text = font.render(
            "开始游戏",
            True,
            (30, 30, 30)
        )

        start_text_rect = start_text.get_rect(
            center=start_button.center
        )

        screen.blit(
            start_text,
            start_text_rect
        )

    else:

        # =====================
        # 显示游戏信息
        # =====================

        level_text = font.render(
            f"当前关卡：{current_level + 1}",
            True,
            (30, 30, 30)
        )

        arrow_text = font.render(
            f"剩余箭头：{len(arrows)}",
            True,
            (30, 30, 30)
        )

        mistake_text = font.render(
            f"剩余失误：{mistakes_left}",
            True,
            (30, 30, 30)
        )

        screen.blit(
            level_text,
            (30, 30)
        )

        screen.blit(
            arrow_text,
            (30, 70)
        )

        screen.blit(
            mistake_text,
            (30, 110)
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

        # =====================
        # 重新开始按钮
        # =====================

        pygame.draw.rect(
            screen,
            (210, 210, 210),
            restart_button,
            border_radius=8
        )

        pygame.draw.rect(
            screen,
            (80, 80, 80),
            restart_button,
            2,
            border_radius=8
        )

        restart_text = font.render(
            "重新开始",
            True,
            (30, 30, 30)
        )

        restart_text_rect = restart_text.get_rect(
            center=restart_button.center
        )

        screen.blit(
            restart_text,
            restart_text_rect
        )

        # 如果当前关卡已经通过，显示下一关按钮
        if game_state == "WIN":
            pygame.draw.rect(
                screen,
                (180, 220, 180),
                next_button,
                border_radius=8
            )

            pygame.draw.rect(
                screen,
                (60, 120, 60),
                next_button,
                2,
                border_radius=8
            )

            next_text = font.render(
                "下一关",
                True,
                (30, 30, 30)
            )

            next_text_rect = next_text.get_rect(
                center=next_button.center
            )

            screen.blit(
                next_text,
                next_text_rect
            )

        # =====================
        # 游戏结果提示
        # =====================

        if game_state == "WIN":

            result_text = big_font.render(
                "恭喜通关！",
                True,
                (40, 150, 70)
            )

            result_rect = result_text.get_rect(
                center=(WIDTH // 2, 50)
            )

            screen.blit(
                result_text,
                result_rect
            )


        elif game_state == "FAILED":

            result_text = big_font.render(
                "游戏失败！",
                True,
                (200, 60, 60)
            )

            result_rect = result_text.get_rect(
                center=(WIDTH // 2, 50)
            )

            screen.blit(
                result_text,
                result_rect
            )

        elif game_state == "COMPLETE":

            result_text = big_font.render(
                "全部关卡完成！",
                True,
                (40, 150, 70)
            )

            result_rect = result_text.get_rect(
                center=(WIDTH // 2, 50)
            )

            screen.blit(
                result_text,
                result_rect
            )

    # 刷新显示
    pygame.display.update()


# =====================
# 退出游戏
# =====================

pygame.quit()
sys.exit()