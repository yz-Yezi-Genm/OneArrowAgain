import pygame
import sys
import random
import math

# =====================
# pygame 初始化
# =====================

pygame.init()

# 初始化音频系统
pygame.mixer.init()

clock = pygame.time.Clock()

# =====================
# UI 配色
# =====================

BLOCKED_ARROW_COLOR = (205, 82, 72)

BG_COLOR = (247, 246, 240)          # 暖米白背景

DARK_GREEN = (31, 73, 62)           # 主深绿色
TEXT_MAIN = (42, 72, 63)            # 主文字
TEXT_SECONDARY = (130, 143, 135)    # 次要文字

LIGHT_GREEN = (229, 236, 226)        # 箭头格子
LIGHT_GREEN_2 = (238, 242, 235)      # 更浅的格子
CARD_COLOR = (253, 253, 249)         # 卡片背景

ORANGE = (235, 153, 92)              # 强调橙色
ORANGE_LIGHT = (247, 219, 197)

LINE_COLOR = (221, 226, 217)         # 分割线
WHITE = (255, 255, 255)

# 游戏按钮颜色
BUTTON_GREEN = (66, 111, 78)
BUTTON_GREEN_HOVER = (78, 128, 90)

BUTTON_LIGHT = (255, 252, 244)
BUTTON_BORDER = (66, 111, 78)

BUTTON_SHADOW = (210, 207, 194)

# =====================
# 结果界面配色
# =====================

RESULT_PANEL = (255, 252, 244)

RESULT_GREEN = (78, 132, 91)
RESULT_RED = (205, 92, 78)
RESULT_ORANGE = (228, 145, 74)

RESULT_TEXT = (65, 75, 66)
RESULT_SUB_TEXT = (125, 125, 110)

# =====================
# 游戏棋盘配色
# =====================

GAME_BG = (248, 244, 233)          # 暖米白

EMPTY_CELL_COLOR = (213, 226, 194) # 空格浅绿
ARROW_CELL_COLOR = (101, 145, 91)  # 箭头格深绿

CELL_BORDER_COLOR = (188, 205, 172)

ARROW_COLOR = (255, 255, 255)      # 白色箭头

# 鼠标悬停在箭头格子时
ARROW_CELL_HOVER = (121, 165, 108)

# 悬停边框
HOVER_BORDER_COLOR = (235, 153, 92)

# =====================
# 底部提示栏配色
# =====================

TIP_BG = (255, 250, 238)          # 淡米黄色
TIP_BORDER = (232, 216, 183)      # 浅棕边框
TIP_ICON_BG = (235, 153, 92)      # 橙色提示图标
TIP_TEXT = (96, 92, 74)           # 提示文字

# =====================
# 窗口参数
# =====================

WIDTH = 1100
HEIGHT = 760

screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)

pygame.display.set_caption(
    "一箭又一箭"
)

# =====================
# 加载生命值图片
# =====================

HEART_HEIGHT = 22

heart_full_image = pygame.image.load(
    "assets/heart_full.png"
).convert_alpha()

heart_empty_image = pygame.image.load(
    "assets/heart_empty.png"
).convert_alpha()

heart_ratio = (
    heart_full_image.get_width()
    / heart_full_image.get_height()
)

HEART_WIDTH = int(
    HEART_HEIGHT * heart_ratio
)

heart_full_image = pygame.transform.scale(
    heart_full_image,
    (HEART_WIDTH, HEART_HEIGHT)
)

heart_empty_image = pygame.transform.scale(
    heart_empty_image,
    (HEART_WIDTH, HEART_HEIGHT)
)

# =====================
# 加载音效
# =====================

error_sound = pygame.mixer.Sound(
    "assets/error.mp3"
)

# 设置音量
# 0.0 = 静音
# 1.0 = 最大
error_sound.set_volume(0.5)

# =====================
# 加载开始界面背景图
# =====================

start_background = pygame.image.load(
    "assets/start_background.png"
).convert()

# 将图片缩放到游戏窗口大小
start_background = pygame.transform.smoothscale(
    start_background,
    (WIDTH, HEIGHT)
)

# =====================
# 加载开始按钮图片
# =====================

start_button_image = pygame.image.load(
    "assets/start_button2.png"
).convert_alpha()

# 自动找到真正有内容的区域
button_content_rect = start_button_image.get_bounding_rect()

# 裁掉四周透明区域
start_button_image = start_button_image.subsurface(
    button_content_rect
).copy()

# 按钮基础大小
START_BUTTON_WIDTH = 380
START_BUTTON_HEIGHT = 110

start_button_image = pygame.transform.smoothscale(
    start_button_image,
    (START_BUTTON_WIDTH, START_BUTTON_HEIGHT)
)

# 按钮在背景图上的原始中心位置
START_BUTTON_CENTER = (550, 620)

# 固定的按钮区域
start_button = start_button_image.get_rect(
    center=START_BUTTON_CENTER
)

# 动画参数
start_button_scale = 1.0
start_button_float = 0.0

small_font = pygame.font.SysFont(
    "Microsoft YaHei",
    18
)

font = pygame.font.SysFont(
    "Microsoft YaHei",
    24
)

medium_font = pygame.font.SysFont(
    "Microsoft YaHei",
    32
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

CELL_MARGIN = 5

GRID_SIZE = 80

ROWS = 6
COLS = 6

# 棋盘整体尺寸
BOARD_WIDTH = COLS * GRID_SIZE
BOARD_HEIGHT = ROWS * GRID_SIZE

# 将棋盘放到窗口正中央
BOARD_X = (WIDTH - BOARD_WIDTH) // 2
BOARD_Y = (HEIGHT - BOARD_HEIGHT) // 2

# =====================
# 游戏控制按钮
# =====================

restart_button = pygame.Rect(
    850,
    310,
    190,
    58
)

home_button = pygame.Rect(
    850,
    390,
    190,
    58
)

# =====================
# 底部提示栏
# =====================

hint_bar = pygame.Rect(
    BOARD_X - 20,
    675,
    BOARD_WIDTH + 40,
    52
)

# =====================
# 结果界面
# =====================

result_panel = pygame.Rect(
    WIDTH // 2 - 260,
    HEIGHT // 2 - 200,
    520,
    400
)

result_primary_button = pygame.Rect(
    WIDTH // 2 - 195,
    HEIGHT // 2 + 120,
    180,
    55
)

result_home_button = pygame.Rect(
    WIDTH // 2 + 15,
    HEIGHT // 2 + 120,
    180,
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



def draw_game_button(
        screen,
        rect,
        text,
        primary=True
):

    mouse_pos = pygame.mouse.get_pos()

    # 判断鼠标是否悬停
    is_hover = rect.collidepoint(mouse_pos)

    # =====================
    # 阴影
    # =====================

    shadow_rect = rect.copy()
    shadow_rect.y += 4

    pygame.draw.rect(
        screen,
        BUTTON_SHADOW,
        shadow_rect,
        border_radius=16
    )

    # =====================
    # 按钮颜色
    # =====================

    if primary:

        if is_hover:
            bg_color = BUTTON_GREEN_HOVER
        else:
            bg_color = BUTTON_GREEN

        text_color = WHITE
        border_color = BUTTON_GREEN

    else:

        bg_color = BUTTON_LIGHT
        text_color = BUTTON_GREEN
        border_color = BUTTON_GREEN

    # =====================
    # 按钮主体
    # =====================

    pygame.draw.rect(
        screen,
        bg_color,
        rect,
        border_radius=16
    )

    pygame.draw.rect(
        screen,
        border_color,
        rect,
        2,
        border_radius=16
    )

    # =====================
    # 文字
    # =====================

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

def draw_hint_bar():

    # =====================
    # 提示栏阴影
    # =====================

    shadow_rect = hint_bar.copy()
    shadow_rect.y += 3

    pygame.draw.rect(
        screen,
        (222, 218, 205),
        shadow_rect,
        border_radius=16
    )

    # =====================
    # 提示栏主体
    # =====================

    pygame.draw.rect(
        screen,
        TIP_BG,
        hint_bar,
        border_radius=16
    )

    pygame.draw.rect(
        screen,
        TIP_BORDER,
        hint_bar,
        2,
        border_radius=16
    )

    # =====================
    # 左侧橙色提示图标
    # =====================

    icon_center = (
        hint_bar.x + 30,
        hint_bar.centery
    )

    pygame.draw.circle(
        screen,
        TIP_ICON_BG,
        icon_center,
        15
    )

    # 不用 emoji，避免字体无法显示
    icon_text = font.render(
        "!",
        True,
        WHITE
    )

    icon_rect = icon_text.get_rect(
        center=icon_center
    )

    screen.blit(
        icon_text,
        icon_rect
    )

    # =====================
    # 提示文字
    # =====================

    hint_text = small_font.render(
        "观察箭头前方是否有阻挡，按正确顺序清空棋盘",
        True,
        TIP_TEXT
    )

    hint_text_rect = hint_text.get_rect(
        midleft=(
            hint_bar.x + 58,
            hint_bar.centery
        )
    )

    screen.blit(
        hint_text,
        hint_text_rect
    )

# =====================
# 绘制五角星
# =====================

def draw_star(
        surface,
        color,
        center,
        outer_radius,
        inner_radius
):

    points = []

    # 五角星一共有10个顶点
    # 5个外顶点 + 5个内顶点
    for i in range(10):

        angle = math.radians(
            -90 + i * 36
        )

        # 偶数点使用外半径
        if i % 2 == 0:
            radius = outer_radius

        # 奇数点使用内半径
        else:
            radius = inner_radius

        x = (
            center[0]
            + math.cos(angle) * radius
        )

        y = (
            center[1]
            + math.sin(angle) * radius
        )

        points.append(
            (x, y)
        )

    pygame.draw.polygon(
        surface,
        color,
        points
    )

def draw_result_panel(state):

    # =====================
    # 半透明黑色遮罩
    # =====================

    overlay = pygame.Surface(
        (WIDTH, HEIGHT),
        pygame.SRCALPHA
    )

    overlay.fill(
        (35, 45, 38, 100)
    )

    screen.blit(
        overlay,
        (0, 0)
    )


    # =====================
    # 卡片阴影
    # =====================

    shadow_rect = result_panel.copy()

    shadow_rect.x += 5
    shadow_rect.y += 7

    pygame.draw.rect(
        screen,
        (190, 187, 175),
        shadow_rect,
        border_radius=24
    )


    # =====================
    # 主卡片
    # =====================

    pygame.draw.rect(
        screen,
        RESULT_PANEL,
        result_panel,
        border_radius=24
    )


    # =====================
    # 根据状态决定内容
    # =====================

    if state == "WIN":

        main_color = RESULT_GREEN

        title = "当前关卡完成"

        subtitle = "所有箭头已经清空，继续挑战下一关吧！"

        button_text = "下一关"


    elif state == "FAILED":

        main_color = RESULT_RED

        title = "挑战失败"

        subtitle = "失误次数已经耗尽，再试一次吧！"

        button_text = "重新开始"


    else:  # COMPLETE

        main_color = RESULT_ORANGE

        title = "全部关卡完成"

        subtitle = "恭喜你完成了所有箭头挑战！"

        button_text = "再玩一次"

    # =====================
    # 计算本关星级
    # =====================

    mistakes_used = (
            MAX_MISTAKES - mistakes_left
    )

    star_count = max(
        0,
        3 - mistakes_used
    )

    # =====================
    # 顶部圆形图标
    # =====================

    icon_center = (
        WIDTH // 2,
        result_panel.y + 75
    )

    pygame.draw.circle(
        screen,
        main_color,
        icon_center,
        38
    )

    # =====================
    # 图标内部符号
    # =====================

    # =====================
    # 图标内部符号
    # =====================

    if state == "WIN":

        # 对勾第一笔
        pygame.draw.line(
            screen,
            WHITE,
            (
                icon_center[0] - 16,
                icon_center[1]
            ),
            (
                icon_center[0] - 4,
                icon_center[1] + 13
            ),
            5
        )

        # 对勾第二笔
        pygame.draw.line(
            screen,
            WHITE,
            (
                icon_center[0] - 4,
                icon_center[1] + 13
            ),
            (
                icon_center[0] + 20,
                icon_center[1] - 15
            ),
            5
        )


    elif state == "FAILED":

        pygame.draw.line(
            screen,
            WHITE,
            (
                icon_center[0] - 14,
                icon_center[1] - 14
            ),
            (
                icon_center[0] + 14,
                icon_center[1] + 14
            ),
            5
        )

        pygame.draw.line(
            screen,
            WHITE,
            (
                icon_center[0] + 14,
                icon_center[1] - 14
            ),
            (
                icon_center[0] - 14,
                icon_center[1] + 14
            ),
            5
        )


    elif state == "COMPLETE":

        # 完成状态暂时画一个圆点/小太阳，
        # 后面也可以单独设计星形
        draw_star(
            screen,
            WHITE,
            icon_center,
            20,
            9
        )


    # =====================
    # 标题
    # =====================

    title_surface = medium_font.render(
        title,
        True,
        RESULT_TEXT
    )

    title_rect = title_surface.get_rect(
        center=(
            WIDTH // 2,
            result_panel.y + 145
        )
    )

    screen.blit(
        title_surface,
        title_rect
    )


    # =====================
    # 副标题
    # =====================

    subtitle_surface = small_font.render(
        subtitle,
        True,
        RESULT_SUB_TEXT
    )

    subtitle_rect = subtitle_surface.get_rect(
        center=(
            WIDTH // 2,
            result_panel.y + 190
        )
    )

    screen.blit(
        subtitle_surface,
        subtitle_rect
    )

    # =====================
    # 本关星级
    # =====================

    STAR_GOLD = (240, 180, 65)
    STAR_EMPTY = (215, 215, 205)

    star_y = result_panel.y + 235

    star_spacing = 55

    first_star_x = (
            WIDTH // 2 - star_spacing
    )

    for i in range(3):

        star_center = (
            first_star_x + i * star_spacing,
            star_y
        )

        # 已获得的星星
        if i < star_count:

            star_color = STAR_GOLD

        # 没获得的星星
        else:

            star_color = STAR_EMPTY

        draw_star(
            screen,
            star_color,
            star_center,
            19,
            8
        )

    # =====================
    # 本关用时
    # =====================

    minutes = elapsed_time // 60
    seconds = elapsed_time % 60
    mistakes_used = (
            MAX_MISTAKES - mistakes_left
    )

    result_info_text = small_font.render(
        f"失误 {mistakes_used} 次    用时 {minutes:02d}:{seconds:02d}",
        True,
        RESULT_SUB_TEXT
    )

    result_info_rect = result_info_text.get_rect(
        center=(
            WIDTH // 2,
            result_panel.y + 275
        )
    )

    screen.blit(
        result_info_text,
        result_info_rect
    )

    # =====================
    # 主操作按钮
    # =====================

    draw_game_button(
        screen,
        result_primary_button,
        button_text,
        primary=True
    )


    # =====================
    # 返回首页
    # =====================

    draw_game_button(
        screen,
        result_home_button,
        "返回首页",
        primary=False
    )

def draw_header():

    # Logo
    logo_rect = pygame.Rect(
        55,
        35,
        55,
        55
    )

    pygame.draw.rect(
        screen,
        DARK_GREEN,
        logo_rect,
        border_radius=14
    )

    # Logo 内部画一个简单右箭头
    pygame.draw.line(
        screen,
        WHITE,
        (70, 62),
        (95, 62),
        5
    )

    pygame.draw.polygon(
        screen,
        WHITE,
        [
            (95, 62),
            (84, 51),
            (84, 73)
        ]
    )

    # 主标题
    title_text = medium_font.render(
        "一箭又一箭",
        True,
        DARK_GREEN
    )

    screen.blit(
        title_text,
        (130, 38)
    )

    # 副标题
    subtitle_text = small_font.render(
        "单格箭头解谜",
        True,
        TEXT_SECONDARY
    )

    screen.blit(
        subtitle_text,
        (132, 78)
    )

    # 顶部分隔线
    pygame.draw.line(
        screen,
        LINE_COLOR,
        (55, 120),
        (1045, 120),
        2
    )

def is_flying_arrow_outside(arrow, offset):

    row = arrow["row"]
    col = arrow["col"]
    direction = arrow["direction"]

    # 箭头当前格子的左上角
    x = BOARD_X + col * GRID_SIZE
    y = BOARD_Y + row * GRID_SIZE

    if direction == "RIGHT":
        return x + offset > WIDTH + GRID_SIZE

    elif direction == "LEFT":
        return x - offset < -GRID_SIZE

    elif direction == "UP":
        return y - offset < -GRID_SIZE

    elif direction == "DOWN":
        return y + offset > HEIGHT + GRID_SIZE

    return False

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

# =====================
# 随机生成可通关关卡
# =====================

def generate_solvable_level(num_arrows):

    # 棋盘所有可能的位置
    all_cells = [
        (row, col)
        for row in range(ROWS)
        for col in range(COLS)
    ]

    # 最多尝试100次，避免极端随机情况
    for attempt in range(100):

        # 随机选取不重复的位置
        solution_cells = random.sample(
            all_cells,
            num_arrows
        )

        generated_arrows = []

        success = True

        # 按“正确消除顺序”的反方向生成
        for row, col in reversed(solution_cells):

            valid_directions = []

            # 尝试四种方向
            for direction in (
                "UP",
                "DOWN",
                "LEFT",
                "RIGHT"
            ):

                candidate = {
                    "row": row,
                    "col": col,
                    "direction": direction
                }

                # 临时把候选箭头加入关卡，
                # 检查它在当前状态下是否可以飞出去
                test_arrows = (
                    generated_arrows
                    + [candidate]
                )

                if not is_blocked(
                    candidate,
                    test_arrows
                ):
                    valid_directions.append(
                        direction
                    )

            # 如果四个方向全都被挡住，
            # 本次随机生成失败，重新生成
            if not valid_directions:

                success = False
                break

            # 从可行方向中随机选择一个
            direction = random.choice(
                valid_directions
            )

            generated_arrows.append(
                {
                    "row": row,
                    "col": col,
                    "direction": direction
                }
            )

        if success:
            return generated_arrows

    # 理论上很少执行到这里
    raise RuntimeError(
        "无法生成可通关关卡"
    )

def generate_random_levels():

    return [
        generate_solvable_level(10),
        generate_solvable_level(1),
        generate_solvable_level(1)
    ]

def start_game():

    global current_level
    global arrows
    global mistakes_left
    global game_state
    global LEVELS

    global level_start_time
    global elapsed_time

    # 每次新游戏重新随机生成关卡
    LEVELS = generate_random_levels()

    current_level = 0

    arrows = [
        arrow.copy()
        for arrow in LEVELS[current_level]
    ]

    mistakes_left = MAX_MISTAKES

    # 开始计时
    level_start_time = pygame.time.get_ticks()
    elapsed_time = 0

    game_state = "PLAYING"

def restart_game():

    global arrows
    global mistakes_left
    global game_state

    global flying_arrow
    global fly_offset
    global blocked_arrow
    global blocked_until

    global level_start_time
    global elapsed_time

    arrows = [
        arrow.copy()
        for arrow in LEVELS[current_level]
    ]

    mistakes_left = MAX_MISTAKES

    # 重新计时
    level_start_time = pygame.time.get_ticks()
    elapsed_time = 0

    flying_arrow = None
    fly_offset = 0

    blocked_arrow = None
    blocked_until = 0

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
    global level_start_time
    global elapsed_time

    current_level = 0

    level_start_time = 0
    elapsed_time = 0

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

    global level_start_time
    global elapsed_time

    if current_level < len(LEVELS) - 1:

        current_level += 1

        arrows = [
            arrow.copy()
            for arrow in LEVELS[current_level]
        ]

        mistakes_left = MAX_MISTAKES

        # 下一关重新计时
        level_start_time = pygame.time.get_ticks()
        elapsed_time = 0

        game_state = "PLAYING"

        print(
            "进入第",
            current_level + 1,
            "关"
        )

    else:

        game_state = "COMPLETE"

# =====================
# 关卡数据
# =====================

# =====================
# 随机关卡
# =====================

LEVELS = generate_random_levels()


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
# 计时器
# =====================

# 当前关卡开始的时间
level_start_time = 0

# 当前关卡已经经过的秒数
elapsed_time = 0

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

                if game_state == "PLAYING":

                    # =====================
                    # 重新开始
                    # =====================

                    if restart_button.collidepoint(
                            mouse_x,
                            mouse_y
                    ):
                        restart_game()

                        print("重新开始当前关卡")

                        continue

                    # =====================
                    # 返回首页
                    # =====================

                    if home_button.collidepoint(
                            mouse_x,
                            mouse_y
                    ):
                        go_home()

                        continue

                # 开始页面
                if game_state == "START":

                    if start_button.collidepoint(
                            mouse_x,
                            mouse_y
                    ):
                        start_game()

                    continue

                # =====================
                # 结算页面
                # =====================

                if game_state in (
                        "WIN",
                        "FAILED",
                        "COMPLETE"
                ):

                    if result_primary_button.collidepoint(
                            mouse_x,
                            mouse_y
                    ):

                        if game_state == "WIN":
                            next_level()

                        elif game_state == "FAILED":
                            restart_game()

                        elif game_state == "COMPLETE":
                            start_game()

                        continue

                    if result_home_button.collidepoint(
                            mouse_x,
                            mouse_y
                    ):
                        go_home()

                        continue

                    continue

                if game_state != "PLAYING":
                    continue

                # 箭头飞行过程中暂时禁止继续点击
                if flying_arrow is not None:
                    continue

                # 碰撞动画播放期间禁止继续点击
                if (
                        blocked_arrow is not None
                        and pygame.time.get_ticks()
                        < blocked_until
                ):
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

                                # 播放错误提示音
                                error_sound.play()
                                print("播放error音效")

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

                                print("剩余箭头数量：", len(arrows))

                            break


    # =====================
    # 绘制游戏画面
    # =====================

    # =====================
    # 更新计时器
    # =====================

    if game_state == "PLAYING":
        elapsed_time = (
                               pygame.time.get_ticks()
                               - level_start_time
                       ) // 1000

    # =====================
    # 更新动画
    # =====================

    if flying_arrow is not None:

        # 每一帧飞行的距离
        speed = 14

        fly_offset += speed

        # 飞出足够远以后真正删除箭头
        if is_flying_arrow_outside(
                flying_arrow,
                fly_offset
        ):

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

    # =====================
    # 更新碰撞动画
    # =====================

    if blocked_arrow is not None:

        if pygame.time.get_ticks() >= blocked_until:
            blocked_arrow = None

    # 背景颜色
    screen.fill(
        GAME_BG
    )

    # =====================
    # 开始界面
    # =====================

    if game_state == "START":

        # =====================
        # 1. 绘制背景
        # =====================

        screen.blit(
            start_background,
            (0, 0)
        )

        # =====================
        # 2. 绘制静态按钮
        #    永远盖住背景图里的原按钮
        # =====================

        screen.blit(
            start_button_image,
            start_button
        )

        # =====================
        # 3. 判断鼠标悬停
        # =====================

        mouse_pos = pygame.mouse.get_pos()

        if start_button.collidepoint(mouse_pos):

            # 放大
            target_scale = 1.10

            # 向上浮动 8 像素
            target_float = -8

        else:

            target_scale = 1.0
            target_float = 0

        # =====================
        # 4. 平滑动画
        # =====================

        start_button_scale += (
                                      target_scale - start_button_scale
                              ) * 0.18

        start_button_float += (
                                      target_float - start_button_float
                              ) * 0.18

        # =====================
        # 5. 计算动画按钮大小
        # =====================

        button_width = int(
            START_BUTTON_WIDTH * start_button_scale
        )

        button_height = int(
            START_BUTTON_HEIGHT * start_button_scale
        )

        scaled_button = pygame.transform.smoothscale(
            start_button_image,
            (button_width, button_height)
        )

        # =====================
        # 6. 动画按钮的位置
        # =====================

        scaled_button_rect = scaled_button.get_rect(
            center=(
                START_BUTTON_CENTER[0],
                START_BUTTON_CENTER[1]
                + int(start_button_float)
            )
        )

        # =====================
        # 7. 在静态按钮上再画动画按钮
        # =====================

        screen.blit(
            scaled_button,
            scaled_button_rect
        )


        '''
        # 调试：显示开始按钮点击区域
        pygame.draw.rect(
            screen,
            (255, 0, 0),
            start_button,
            3
        )
        '''

    else:

        # 页面标题
        page_title = medium_font.render(
            "一箭又一箭",
            True,
            DARK_GREEN
        )

        page_title_rect = page_title.get_rect(
            center=(WIDTH // 2, 28)
        )

        screen.blit(
            page_title,
            page_title_rect
        )

        # =====================
        # 顶部状态卡片
        # =====================

        CARD_Y = 62
        CARD_WIDTH = 175
        CARD_HEIGHT = 52
        CARD_GAP = 16

        HEART_HEIGHT = 20
        HEART_GAP = 4

        # 四张卡片整体居中
        total_width = CARD_WIDTH * 4 + CARD_GAP * 3

        start_x = (
                          WIDTH - total_width
                  ) // 2

        level_card = pygame.Rect(
            start_x,
            CARD_Y,
            CARD_WIDTH,
            CARD_HEIGHT
        )

        arrow_card = pygame.Rect(
            start_x + CARD_WIDTH + CARD_GAP,
            CARD_Y,
            CARD_WIDTH,
            CARD_HEIGHT
        )

        mistake_card = pygame.Rect(
            start_x + (CARD_WIDTH + CARD_GAP) * 2,
            CARD_Y,
            CARD_WIDTH,
            CARD_HEIGHT
        )

        time_card = pygame.Rect(
            start_x + (CARD_WIDTH + CARD_GAP) * 3,
            CARD_Y,
            CARD_WIDTH,
            CARD_HEIGHT
        )

        # 绘制四张状态卡片
        for card in (
                level_card,
                arrow_card,
                mistake_card,
                time_card
        ):

            pygame.draw.rect(
                screen,
                CARD_COLOR,
                card,
                border_radius=14
            )

            pygame.draw.rect(
                screen,
                CELL_BORDER_COLOR,
                card,
                2,
                border_radius=14
            )

        level_label = small_font.render(
            "当前关卡",
            True,
            SUB_TEXT_COLOR
        )

        level_value = font.render(
            f"{current_level + 1} / {len(LEVELS)}",
            True,
            DARK_GREEN
        )

        screen.blit(
            level_label,
            (
                level_card.x + 16,
                level_card.y + 7
            )
        )

        screen.blit(
            level_value,
            (
                level_card.x + 105,
                level_card.y + 12
            )
        )

        arrow_label = small_font.render(
            "剩余箭头",
            True,
            SUB_TEXT_COLOR
        )

        arrow_value = font.render(
            str(len(arrows)),
            True,
            DARK_GREEN
        )

        screen.blit(
            arrow_label,
            (
                arrow_card.x + 16,
                arrow_card.y + 7
            )
        )

        screen.blit(
            arrow_value,
            (
                arrow_card.x + 140,
                arrow_card.y + 12
            )
        )

        mistake_label = small_font.render(
            "剩余失误",
            True,
            SUB_TEXT_COLOR
        )

        # =====================
        # 用时
        # =====================

        time_label = small_font.render(
            "用时",
            True,
            SUB_TEXT_COLOR
        )

        # 秒转换成 分:秒
        minutes = elapsed_time // 60
        seconds = elapsed_time % 60

        time_value = font.render(
            f"{minutes:02d}:{seconds:02d}",
            True,
            DARK_GREEN
        )

        screen.blit(
            time_label,
            (
                time_card.x + 16,
                time_card.y + 7
            )
        )

        screen.blit(
            time_value,
            (
                time_card.x + 75,
                time_card.y + 12
            )
        )


        screen.blit(
            mistake_label,
            (
                mistake_card.x + 16,
                mistake_card.y + 7
            )
        )

        # =====================
        # 剩余生命值
        # =====================

        HEART_GAP = 4

        # 三颗爱心总共占多宽
        hearts_total_width = (
                HEART_HEIGHT * MAX_MISTAKES
                + HEART_GAP * (MAX_MISTAKES - 1)
        )

        # 从卡片右侧往左排列
        heart_start_x = (
                mistake_card.right
                - 10
                - hearts_total_width
        )

        heart_y = (
                mistake_card.centery
                - HEART_HEIGHT // 2
        )

        for i in range(MAX_MISTAKES):

            heart_x = (
                    heart_start_x
                    + i * (HEART_HEIGHT + HEART_GAP)
            )

            # 还有生命
            if i < mistakes_left:

                heart_image = heart_full_image

            # 已失去生命
            else:

                heart_image = heart_empty_image

            screen.blit(
                heart_image,
                (heart_x, heart_y)
            )

        board_panel = pygame.Rect(
            BOARD_X - 20,
            BOARD_Y - 20,
            COLS * GRID_SIZE + 40,
            ROWS * GRID_SIZE + 40
        )

        # 先阴影
        board_shadow = board_panel.copy()

        board_shadow.x += 4
        board_shadow.y += 6

        pygame.draw.rect(
            screen,
            (220, 216, 203),
            board_shadow,
            border_radius=22
        )

        # 再主体
        pygame.draw.rect(
            screen,
            CARD_COLOR,
            board_panel,
            border_radius=22
        )

        # 最后边框
        pygame.draw.rect(
            screen,
            CELL_BORDER_COLOR,
            board_panel,
            2,
            border_radius=22
        )

        # =====================
        # 获取鼠标当前所在的棋盘格
        # =====================

        mouse_x, mouse_y = pygame.mouse.get_pos()

        hover_row = -1
        hover_col = -1

        # 先计算格子
        if (
                BOARD_X <= mouse_x < BOARD_X + COLS * GRID_SIZE
                and
                BOARD_Y <= mouse_y < BOARD_Y + ROWS * GRID_SIZE
        ):
            hover_col = (
                                mouse_x - BOARD_X
                        ) // GRID_SIZE

            hover_row = (
                                mouse_y - BOARD_Y
                        ) // GRID_SIZE

        # 再判断是否是箭头
        hovering_arrow = any(
            arrow["row"] == hover_row
            and arrow["col"] == hover_col
            for arrow in arrows
        )

        # 最后设置鼠标
        if (
                hovering_arrow
                and game_state == "PLAYING"
        ):

            pygame.mouse.set_cursor(
                pygame.SYSTEM_CURSOR_HAND
            )

        else:

            pygame.mouse.set_cursor(
                pygame.SYSTEM_CURSOR_ARROW
            )

        # 只有鼠标在棋盘内部时才计算
        if (
                BOARD_X <= mouse_x < BOARD_X + COLS * GRID_SIZE
                and
                BOARD_Y <= mouse_y < BOARD_Y + ROWS * GRID_SIZE
        ):
            hover_col = (
                                mouse_x - BOARD_X
                        ) // GRID_SIZE

            hover_row = (
                                mouse_y - BOARD_Y
                        ) // GRID_SIZE

        # =====================
        # 绘制棋盘
        # =====================

        for row in range(ROWS):

            for col in range(COLS):

                # 判断当前位置是否有箭头
                has_arrow = any(
                    arrow["row"] == row
                    and arrow["col"] == col
                    for arrow in arrows
                )

                # 每个格子之间留出一点间隔
                rect = pygame.Rect(
                    BOARD_X + col * GRID_SIZE + CELL_MARGIN,
                    BOARD_Y + row * GRID_SIZE + CELL_MARGIN,
                    GRID_SIZE - CELL_MARGIN * 2,
                    GRID_SIZE - CELL_MARGIN * 2
                )

                # 当前格子是否正被鼠标悬停
                is_hover = (
                        row == hover_row
                        and col == hover_col
                )

                # 有箭头
                if has_arrow:

                    # 鼠标悬停到箭头
                    if is_hover and game_state == "PLAYING":
                        cell_color = ARROW_CELL_HOVER

                    else:
                        cell_color = ARROW_CELL_COLOR

                # 空格
                else:

                    cell_color = EMPTY_CELL_COLOR

                # 鼠标悬停时增加轻微外圈
                if (
                        has_arrow
                        and is_hover
                        and game_state == "PLAYING"
                ):
                    glow_rect = rect.inflate(
                        6,
                        6
                    )

                    pygame.draw.rect(
                        screen,
                        ORANGE_LIGHT,
                        glow_rect,
                        border_radius=14
                    )

                # 绘制格子
                pygame.draw.rect(
                    screen,
                    cell_color,
                    rect,
                    border_radius=12
                )

                # 悬停在箭头上时使用橙色边框
                if (
                        has_arrow
                        and is_hover
                        and game_state == "PLAYING"
                ):

                    border_color = HOVER_BORDER_COLOR
                    border_width = 3

                else:

                    border_color = CELL_BORDER_COLOR
                    border_width = 2

                pygame.draw.rect(
                    screen,
                    border_color,
                    rect,
                    border_width,
                    border_radius=12
                )
        # 根据 arrows 数据绘制所有箭头
        for arrow in arrows:

            offset_x = 0
            offset_y = 0

            color = ARROW_COLOR

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
                color = BLOCKED_ARROW_COLOR

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
        # 底部玩法提示
        # =====================

        if game_state == "PLAYING":
            draw_hint_bar()

        # =====================
        # 游戏控制按钮
        # =====================

        if game_state == "PLAYING":
            draw_game_button(
                screen,
                restart_button,
                "重新开始",
                primary=True
            )

            draw_game_button(
                screen,
                home_button,
                "返回首页",
                primary=False
            )

    # =====================
    # 游戏结果界面
    # =====================

    if game_state in (
            "WIN",
            "FAILED",
            "COMPLETE"
    ):
        draw_result_panel(
            game_state
        )

    # 刷新显示
    pygame.display.update()

    clock.tick(60)


# =====================
# 退出游戏
# =====================

pygame.quit()
sys.exit()