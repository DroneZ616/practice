import pygame
import random  # 导入随机数模块，用来让食物出现在随机位置

# 1. 初始化
pygame.init()

# 2. 窗口设置
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("吃苹果游戏 - 得分：0")

# 3. 颜色
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# 4. 玩家方块
player_x = 375
player_y = 275
player_size = 50
speed = 15

# 5. 食物（苹果）
food_size = 30
# 随机生成食物的初始位置（要保证完全在窗口内）
food_x = random.randint(0, WIDTH - food_size)
food_y = random.randint(0, HEIGHT - food_size)

# 6. 计分
score = 0
font = pygame.font.Font(None, 36)  # 准备一个字体用来显示文字（暂时不用，先放这）

# 7. 时钟
clock = pygame.time.Clock()

# 8. 游戏主循环
running = True
while running:
    # --- 事件处理 ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- 键盘控制移动 ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= speed
    if keys[pygame.K_RIGHT]:
        player_x += speed
    if keys[pygame.K_UP]:
        player_y -= speed
    if keys[pygame.K_DOWN]:
        player_y += speed

    # --- 边界限制（防止玩家跑出窗口） ---
    if player_x < 0:
        player_x = 0
    if player_x > WIDTH - player_size:
        player_x = WIDTH - player_size
    if player_y < 0:
        player_y = 0
    if player_y > HEIGHT - player_size:
        player_y = HEIGHT - player_size

    # --- 🍎 碰撞检测（核心！判断方块是否吃到了食物） ---
    # 条件：玩家的矩形和食物的矩形有重叠
    if (player_x < food_x + food_size and
        player_x + player_size > food_x and
        player_y < food_y + food_size and
        player_y + player_size > food_y):
        
        # 吃到了！分数加1
        score += 1
        pygame.display.set_caption(f"吃苹果游戏 - 得分：{score}")
        
        # 食物消失，并在新的随机位置重新出现
        food_x = random.randint(0, WIDTH - food_size)
        food_y = random.randint(0, HEIGHT - food_size)

    # --- 绘制画面 ---
    screen.fill(WHITE)                                  # 清屏
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))  # 玩家
    pygame.draw.rect(screen, RED, (food_x, food_y, food_size, food_size))          # 食物
    pygame.display.flip()                               # 刷新

    # --- 控制帧率 ---
    clock.tick(60)

# 9. 退出
pygame.quit()