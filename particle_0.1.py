import pygame
import random
import math

# ----- 初始化 -----
pygame.init()
WIDTH, HEIGHT = 1600, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("粒子运动 - 原型 0.1")
clock = pygame.time.Clock()
particles = []  # 这里应该存放多个字典或对象

# ----- 颜色 -----
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# ----- 粒子部分数据 -----
def create_particle():
    particle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    particle_vx = random.uniform(-0.5, 0.5)
    particle_vy = random.uniform(-0.5, 0.5)
    particle = {
            "x": particle_x0,
            "y": particle_y0,
            "color": particle_color,
            "vx": particle_vx,
            "vy": particle_vy,
            "radius": particle_r
        }
    particles.append(particle)

MAX_ATTEMPTS = 101

for i in range(450):  # 生成450个粒子
    particle_r = 1  # 粒子半径
    
    

    #检测粒子生成时是否重叠
    for attempt in range(MAX_ATTEMPTS):
        particle_x0 = random.randint(particle_r, WIDTH - particle_r)
        particle_y0 = random.randint(particle_r, HEIGHT - particle_r)
        
        overlap = False
        for p in particles:
            dx = p["x"] - particle_x0
            dy = p["y"] - particle_y0
            dist = math.hypot(dx, dy)

            if dist < p["radius"] + particle_r: #重叠时
                overlap = True
                break

        if attempt == MAX_ATTEMPTS - 1 and overlap: #尝试次数用尽仍重叠

            print(f"警告：粒子 {i} 生成时与其他粒子重叠，强制生成该粒子。")
            break
        
        if not overlap: #不重叠时
            break  # 成功生成粒子，跳出尝试循环

    create_particle()
                
    

        





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
            
            # 计算位置向量
            p1_x = p2["x"] - p1["x"]
            p1_y = p2["y"] - p1["y"]
            p2_x = -p1_x
            p2_y = -p1_y

            distance = math.sqrt(p1_x ** 2 + p1_y ** 2)
            if (distance <= p1["radius"] + p2["radius"]) and (distance > 0):
                # 简单的弹性碰撞处理
                p1["vx"], p2["vx"] = p2["vx"], p1["vx"]
                p1["vy"], p2["vy"] = p2["vy"], p1["vy"]
                overlap_distance = (p1["radius"] + p2["radius"] - distance) / 2
                p1["x"] -= overlap_distance * p1_x / distance
                p1["y"] -= overlap_distance * p1_y / distance
                p2["x"] += overlap_distance * p1_x / distance
                p2["y"] += overlap_distance * p1_y / distance
            if (distance > 0) and (distance < 2):  # 如果距离2像素，计算线性斥力
                # 计算线性斥力
                force = -2.5* distance + 7.5  # 简单的线性斥力公式
                p1["vx"] -= force * p1_x / distance
                p1["vy"] -= force * p1_y / distance
                p2["vx"] -= force * p2_x / distance
                p2["vy"] -= force * p2_y / distance
            if (distance > 2) :  # 如果距离大于2像素，计算非线性斥力
                
                # 计算非线性斥力
                force = 10 / (distance ** 2)  # 简单的万有斥力公式
                p1["vx"] -= force * p1_x / distance
                p1["vy"] -= force * p1_y / distance
                p2["vx"] -= force * p2_x / distance
                p2["vy"] -= force * p2_y / distance
            

                

    # 3. 绘制
    screen.fill(BLACK)
    for p in particles:
        pygame.draw.circle(screen, p["color"], (p["x"], p["y"]), p["radius"])
    
    pygame.display.flip()
    clock.tick(70)

pygame.quit()