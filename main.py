import pygame
import sys


# =====================
# pygame 初始化
# =====================

pygame.init()

clock = pygame.time.Clock()

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
# 颜色设置
# =====================

BG_COLOR = (245, 247, 250)          # 整体背景
PANEL_COLOR = (255, 255, 255)       # 面板白色
BOARD_BG_COLOR = (250, 251, 253)    # 棋盘背景
GRID_COLOR = (210, 215, 223)        # 网格线颜色

TEXT_COLOR = (40, 44, 52)           # 主要文字
SUB_TEXT_COLOR = (110, 118, 129)    # 次要文字

PRIMARY_COLOR = (91, 143, 249)      # 主按钮蓝色
PRIMARY_BORDER = (60, 110, 210)

SUCCESS_COLOR = (95, 184, 120)      # 成功绿色
SUCCESS_BORDER = (60, 140, 90)

DANGER_COLOR = (225, 95, 95)        # 失败红色
DANGER_BORDER = (180, 65, 65)

NEUTRAL_BUTTON = (230, 233, 238)    # 中性按钮灰色
NEUTRAL_BORDER = (150, 155, 165)

CARD_LEVEL = (232, 242, 255)
CARD_ARROW = (235, 248, 235)
CARD_MISTAKE = (255, 240, 230)

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

home_button = pygame.Rect(
    300,
    430,
    200,
    55
)

# =====================
# 绘制箭头
# =====================

def draw_arrow(
    screen,
    row,
    col,
    direction,
    offset_x=0,
    offset_y=0,
    color=(70, 90, 120)
):

    x = BOARD_X + col * GRID_SIZE + offset_x
    y = BOARD_Y + row * GRID_SIZE + offset_y

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

def draw_button(screen, rect, text, bg_color, border_color, text_color=TEXT_COLOR):

    mouse_pos = pygame.mouse.get_pos()

    # 悬停时稍微变亮一点
    is_hover = rect.collidepoint(mouse_pos)

    if is_hover:
        draw_color = (
            min(bg_color[0] + 10, 255),
            min(bg_color[1] + 10, 255),
            min(bg_color[2] + 10, 255)
        )
    else:
        draw_color = bg_color

    pygame.draw.rect(
        screen,
        draw_color,
        rect,
        border_radius=12
    )

    pygame.draw.rect(
        screen,
        border_color,
        rect,
        2,
        border_radius=12
    )

    text_surface = font.render(
        text,
        True,
        text_color
    )

    text_rect = text_surface.get_rect(
        center=rect.center
    )

    screen.blit(
        text_surface,
        text_rect
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

def go_home():

    global game_state
    global current_level
    global arrows
    global mistakes_left

    global flying_arrow
    global fly_offset
    global blocked_arrow
    global blocked_until

    current_level = 0

    arrows = [
        arrow.copy()
        for arrow in LEVELS[current_level]
    ]

    mistakes_left = MAX_MISTAKES

    flying_arrow = None
    fly_offset = 0

    blocked_arrow = None
    blocked_until = 0

    game_state = "START"

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
# 动画状态
# =====================

# 当前正在飞出的箭头
flying_arrow = None

# 飞出的距离
fly_offset = 0

# 被阻挡、正在显示碰撞效果的箭头
blocked_arrow = None

# 碰撞效果结束时间
blocked_until = 0


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

                if game_state in ("WIN", "FAILED", "COMPLETE"):

                    if home_button.collidepoint(
                            mouse_x,
                            mouse_y
                    ):
                        go_home()

                        continue

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

                # 箭头飞行过程中暂时禁止继续点击
                if flying_arrow is not None:
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

                                blocked_arrow = arrow

                                blocked_until = pygame.time.get_ticks() + 350

                                # 扣除一次失误机会
                                mistakes_left -= 1

                                if mistakes_left <= 0:
                                    mistakes_left = 0

                                    game_state = "FAILED"

                                    print("游戏失败！")

                                print("剩余失误次数：", mistakes_left)

                            else:

                                print("前方没有箭头，可以飞出！")

                                # 开始飞出动画
                                flying_arrow = arrow

                                fly_offset = 0

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

    # =====================
    # 更新动画
    # =====================

    if flying_arrow is not None:

        # 每一帧飞行的距离
        speed = 12

        fly_offset += speed

        # 飞出足够远以后真正删除箭头
        if fly_offset > 500:

            arrows.remove(flying_arrow)

            flying_arrow = None

            fly_offset = 0

            print("剩余箭头数量：", len(arrows))

            # 当前关卡已经清空
            if len(arrows) == 0:

                # 最后一关
                if current_level == len(LEVELS) - 1:

                    game_state = "COMPLETE"

                    print("恭喜！全部关卡通过！")

                else:

                    game_state = "WIN"

                    print("恭喜，当前关卡通过！")


    # 背景颜色
    screen.fill(
        (245, 245, 245)
    )

    # =====================
    # 开始界面
    # =====================

    if game_state == "START":

        # 标题
        title_text = big_font.render(
            "一箭又一箭",
            True,
            TEXT_COLOR
        )
        title_rect = title_text.get_rect(
            center=(WIDTH // 2, 150)
        )
        screen.blit(title_text, title_rect)

        # 副标题
        subtitle_text = font.render(
            "Arrow Puzzle Game",
            True,
            SUB_TEXT_COLOR
        )
        subtitle_rect = subtitle_text.get_rect(
            center=(WIDTH // 2, 205)
        )
        screen.blit(subtitle_text, subtitle_rect)

        # 说明面板
        intro_rect = pygame.Rect(180, 250, 440, 90)
        pygame.draw.rect(
            screen,
            PANEL_COLOR,
            intro_rect,
            border_radius=16
        )
        pygame.draw.rect(
            screen,
            (220, 225, 232),
            intro_rect,
            2,
            border_radius=16
        )

        tip_text = font.render(
            "按照正确顺序点击箭头，让所有箭头飞出棋盘",
            True,
            SUB_TEXT_COLOR
        )
        tip_rect = tip_text.get_rect(
            center=intro_rect.center
        )
        screen.blit(tip_text, tip_rect)

        # 开始按钮
        draw_button(
            screen,
            start_button,
            "开始游戏",
            PRIMARY_COLOR,
            PRIMARY_BORDER,
            (255, 255, 255)
        )

    else:

        # 页面标题
        page_title = big_font.render(
            "一箭又一箭",
            True,
            TEXT_COLOR
        )
        screen.blit(page_title, (30, 20))

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

        # 信息卡片区域
        level_card = pygame.Rect(30, 100, 150, 70)
        arrow_card = pygame.Rect(30, 185, 150, 70)
        mistake_card = pygame.Rect(30, 270, 150, 70)

        pygame.draw.rect(screen, CARD_LEVEL, level_card, border_radius=14)
        pygame.draw.rect(screen, CARD_ARROW, arrow_card, border_radius=14)
        pygame.draw.rect(screen, CARD_MISTAKE, mistake_card, border_radius=14)

        pygame.draw.rect(screen, (200, 210, 220), level_card, 2, border_radius=14)
        pygame.draw.rect(screen, (200, 210, 220), arrow_card, 2, border_radius=14)
        pygame.draw.rect(screen, (200, 210, 220), mistake_card, 2, border_radius=14)

        level_label = font.render("当前关卡", True, SUB_TEXT_COLOR)
        arrow_label = font.render("剩余箭头", True, SUB_TEXT_COLOR)
        mistake_label = font.render("剩余失误", True, SUB_TEXT_COLOR)

        level_value = font.render(f"{current_level + 1}", True, TEXT_COLOR)
        arrow_value = font.render(f"{len(arrows)}", True, TEXT_COLOR)
        mistake_value = font.render(f"{mistakes_left}", True, TEXT_COLOR)

        screen.blit(level_label, (50, 112))
        screen.blit(level_value, (50, 138))

        screen.blit(arrow_label, (50, 197))
        screen.blit(arrow_value, (50, 223))

        screen.blit(mistake_label, (50, 282))
        screen.blit(mistake_value, (50, 308))

        board_panel = pygame.Rect(
            BOARD_X - 20,
            BOARD_Y - 20,
            COLS * GRID_SIZE + 40,
            ROWS * GRID_SIZE + 40
        )

        pygame.draw.rect(
            screen,
            PANEL_COLOR,
            board_panel,
            border_radius=18
        )

        pygame.draw.rect(
            screen,
            (220, 225, 232),
            board_panel,
            2,
            border_radius=18
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
                    BOARD_BG_COLOR,
                    rect,
                    border_radius=8
                )

                pygame.draw.rect(
                    screen,
                    GRID_COLOR,
                    rect,
                    2,
                    border_radius=8
                )

        # 根据 arrows 数据绘制所有箭头
        for arrow in arrows:

            offset_x = 0
            offset_y = 0

            color = (30, 30, 30)

            # =====================
            # 飞出动画
            # =====================

            if arrow is flying_arrow:

                direction = arrow["direction"]

                if direction == "RIGHT":
                    offset_x = fly_offset

                elif direction == "LEFT":
                    offset_x = -fly_offset

                elif direction == "UP":
                    offset_y = -fly_offset

                elif direction == "DOWN":
                    offset_y = fly_offset

            # =====================
            # 碰撞动画
            # =====================

            if (
                    arrow is blocked_arrow
                    and pygame.time.get_ticks() < blocked_until
            ):

                # 碰撞时变成红色
                color = (220, 50, 50)

                # 每隔约50毫秒改变晃动方向
                if (pygame.time.get_ticks() // 50) % 2 == 0:
                    shake = 6
                else:
                    shake = -6

                # 左右箭头沿水平方向晃动
                if arrow["direction"] in ("LEFT", "RIGHT"):
                    offset_x += shake

                # 上下箭头沿垂直方向晃动
                else:
                    offset_y += shake

            draw_arrow(
                screen,
                arrow["row"],
                arrow["col"],
                arrow["direction"],
                offset_x,
                offset_y,
                color
            )

        # =====================
        # 重新开始按钮
        # =====================
        if game_state in ("PLAYING", "FAILED"):
            draw_button(
                screen,
                restart_button,
                "重新开始",
                NEUTRAL_BUTTON,
                NEUTRAL_BORDER,
                TEXT_COLOR
            )

        # 如果当前关卡已经通过，显示下一关按钮
        if game_state == "WIN":
            if game_state == "WIN":
                draw_button(
                    screen,
                    next_button,
                    "下一关",
                    SUCCESS_COLOR,
                    SUCCESS_BORDER,
                    (255, 255, 255)
                )

        # =====================
        # 游戏结果提示
        # =====================

        if game_state == "WIN":

            result_text = big_font.render(
                "恭喜通关！",
                True,
                SUCCESS_BORDER
            )
            result_rect = result_text.get_rect(center=(WIDTH // 2, 60))
            screen.blit(result_text, result_rect)

            sub_text = font.render(
                "当前关卡已完成，点击下一关继续挑战",
                True,
                SUB_TEXT_COLOR
            )
            sub_rect = sub_text.get_rect(center=(WIDTH // 2, 105))
            screen.blit(sub_text, sub_rect)


        elif game_state == "FAILED":

            result_text = big_font.render(
                "游戏失败！",
                True,
                DANGER_BORDER
            )
            result_rect = result_text.get_rect(center=(WIDTH // 2, 60))
            screen.blit(result_text, result_rect)

            sub_text = font.render(
                "失误次数已耗尽，可以重新开始或返回首页",
                True,
                SUB_TEXT_COLOR
            )
            sub_rect = sub_text.get_rect(center=(WIDTH // 2, 105))
            screen.blit(sub_text, sub_rect)


        elif game_state == "COMPLETE":

            result_text = big_font.render(
                "全部关卡完成！",
                True,
                SUCCESS_BORDER
            )
            result_rect = result_text.get_rect(center=(WIDTH // 2, 60))
            screen.blit(result_text, result_rect)

            sub_text = font.render(
                "恭喜你完成了所有关卡挑战！",
                True,
                SUB_TEXT_COLOR
            )
            sub_rect = sub_text.get_rect(center=(WIDTH // 2, 105))
            screen.blit(sub_text, sub_rect)


    if game_state in ("WIN", "FAILED", "COMPLETE"):
        if game_state in ("WIN", "FAILED", "COMPLETE"):
            draw_button(
                screen,
                home_button,
                "返回首页",
                PRIMARY_COLOR,
                PRIMARY_BORDER,
                (255, 255, 255)
            )



    # 刷新显示
    pygame.display.update()

    clock.tick(60)


# =====================
# 退出游戏
# =====================

pygame.quit()
sys.exit()