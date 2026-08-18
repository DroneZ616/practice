import pygame
import random
import math

# ----- 初始化 -----
pygame.init()
WIDTH, HEIGHT = 1600, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("粒子战争 - 原型 0.1")
clock = pygame.time.Clock()
particles = []  # 这里应该存放多个字典或对象

# ----- 颜色 -----
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# ----- 粒子数据（你要自己填） -----
for i in range(300):
    particle_x0 = random.randint(0, WIDTH)
    particle_y0 = random.randint(0, HEIGHT)
    particle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    particle_vx = random.uniform(-2, 2)
    particle_vy = random.uniform(-2, 2)
    particle = {
        "x": particle_x0,
        "y": particle_y0,
        "color": particle_color,
        "vx": particle_vx,
        "vy": particle_vy,
        "radius": 5
    }
    particles.append(particle)




# ----- 游戏主循环 -----
running = True
while running:
    # 1. 处理退出事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. 更新粒子位置（你要自己写）
    for p in particles:
        p["x"] += p["vx"]
        p["y"] += p["vy"]

        # 边界反弹逻辑也要你写
        if p["x"] < 0 or p["x"] > WIDTH:
            p["x"] = max(0, min(WIDTH, p["x"]))
            p["vx"] = -p["vx"]
        if p["y"] < 0 or p["y"] > HEIGHT:
            p["y"] = max(0, min(HEIGHT, p["y"]))
            p["vy"] = -p["vy"]

    for i in range(len(particles)):
        for j in range(i + 1, len(particles)):
            p1 = particles[i]
            p2 = particles[j]
            #距离的绝对值
            dx = abs(p2["x"] - p1["x"])  
            dy = abs(p2["y"] - p1["y"])
            # 计算位置向量
            p1_x = p2["x"] - p1["x"]
            p1_y = p2["y"] - p1["y"]
            p2_x = p1["x"] - p2["x"]
            p2_y = p1["y"] - p2["y"]

            distance = math.sqrt(dx ** 2 + dy ** 2)
            if distance <= p1["radius"] + p2["radius"]:
                # 简单的弹性碰撞处理
                p1["vx"], p2["vx"] = p2["vx"], p1["vx"]
                p1["vy"], p2["vy"] = p2["vy"], p1["vy"]
            if (distance > p1["radius"] + p2["radius"]) and (distance < p1["radius"] + p2["radius"]+10):  # 如果距离20像素，计算线性斥力
                # 计算线性斥力
                force = 1 / distance  # 简单的线性斥力公式
                p1["vx"] -= force * p1_x / distance
                p1["vy"] -= force * p1_y / distance
                p2["vx"] -= force * p2_x / distance
                p2["vy"] -= force * p2_y / distance
            if (distance > p1["radius"] + p2["radius"]+10) and (distance < 50):  # 如果距离小于80并大于20像素，计算斥力
                
                # 计算斥力
                force = 5 / (distance ** 2)  # 简单的万有斥力公式
                p1["vx"] -= force * p1_x / distance
                p1["vy"] -= force * p1_y / distance
                p2["vx"] -= force * p2_x / distance
                p2["vy"] -= force * p2_y / distance
            if (distance > 80) :  # 如果距离大于80像素，计算引力
                # 计算非线性引力
                force = 5 / (distance ** 2)  # 简单的万有引力公式
                p1["vx"] += force * p1_x / distance
                p1["vy"] += force * p1_y / distance
                p2["vx"] += force * p2_x / distance
                p2["vy"] += force * p2_y / distance
                

    # 3. 绘制
    screen.fill(BLACK)
    for p in particles:
        pygame.draw.circle(screen, p["color"], (p["x"], p["y"]), p["radius"])
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()