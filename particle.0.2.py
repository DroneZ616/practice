import pygame
import random
import math

# ----- 初始化 -----
pygame.init()
WIDTH, HEIGHT = 1600, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("粒子运行 - Verlet 积分 + 连续地图")
clock = pygame.time.Clock()

# ----- 颜色 -----
BLACK = (0, 0, 0)

# ----- 物理参数 -----
DT = 0.8          # 时间步长（越小越稳定，通常 0.5~1.0）
DAMPING = 0.999   # 极微弱阻尼（抵消数值误差，几乎看不见）

# ----- 粒子生成（Verlet 格式）-----
def create_particle(x, y, radius):
    # 初始时，让上一帧位置稍微偏移一点，产生初始速度
    vx = random.uniform(-1, 1)
    vy = random.uniform(-1, 1)
    return {
        "x": x,
        "y": y,
        "px": x - vx,   # 上一帧位置 = 当前位置 - 初始速度
        "py": y - vy,
        "radius": radius,
        "color": (random.randint(30, 255), random.randint(30, 255), random.randint(30, 255))
    }

particles = []
MAX_ATTEMPTS = 100
for _ in range(30):
    radius = 5
    for attempt in range(MAX_ATTEMPTS):
        x = random.randint(radius, WIDTH - radius)
        y = random.randint(radius, HEIGHT - radius)
        overlap = False
        for p in particles:
            dx = p["x"] - x
            dy = p["y"] - y
            # 周期性边界下的最短距离（用于生成时防重叠）
            if dx > WIDTH / 2: dx -= WIDTH
            if dx < -WIDTH / 2: dx += WIDTH
            if dy > HEIGHT / 2: dy -= HEIGHT
            if dy < -HEIGHT / 2: dy += HEIGHT
            if math.hypot(dx, dy) < p["radius"] + radius:
                overlap = True
                break
        if not overlap:
            particles.append(create_particle(x, y, radius))
            break

# ----- 游戏主循环 -----
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ---------- 1. 计算所有粒子受到的加速度 ----------
    # 先清零加速度（因为 Verlet 需要每帧重新算）
    for p in particles:
        p["ax"] = 0.0
        p["ay"] = 0.0

    # 计算粒子间的相互作用力
    REPULSE_STRENGTH = 0.5   # 调节斥力大小
    for i in range(len(particles)):
        for j in range(i + 1, len(particles)):
            p1 = particles[i]
            p2 = particles[j]

            # --- 周期性边界下的最短距离 ---
            dx = p2["x"] - p1["x"]
            dy = p2["y"] - p1["y"]
            if dx > WIDTH / 2: dx -= WIDTH
            if dx < -WIDTH / 2: dx += WIDTH
            if dy > HEIGHT / 2: dy -= HEIGHT
            if dy < -HEIGHT / 2: dy += HEIGHT

            dist = math.hypot(dx, dy)
            if dist < 0.001:
                continue

            # --- 使用 Lennard-Jones 风格的力（连续、平滑） ---
            # 距离小于半径和时产生强排斥，略大时产生弱吸引，远处归零
            sigma = p1["radius"] + p2["radius"]
            if dist < sigma * 2.5:  # 只在有效范围内计算力
                # 简化的 12-6 势能（力）
                # 为了稳定，我们只使用排斥部分 + 微弱的短程吸引
                if dist < sigma:
                    # 强排斥（防止重叠）
                    force = 2.0 * (sigma - dist) / sigma
                elif dist < sigma * 1.8:
                    # 微弱吸引（模拟粒子间的凝聚力）
                    force = -0.05 * (dist - sigma) / sigma
                else:
                    force = 0.0
                
                # 方向向量（归一化）
                nx = dx / dist
                ny = dy / dist
                
                # 施加力（加速度 = 力 / 质量，假设质量=1）
                p1["ax"] += force * nx
                p1["ay"] += force * ny
                p2["ax"] -= force * nx
                p2["ay"] -= force * ny

    # ---------- 2. Verlet 积分更新位置 ----------
    for p in particles:
        # 计算新位置
        new_x = 2 * p["x"] - p["px"] + p["ax"] * DT * DT
        new_y = 2 * p["y"] - p["py"] + p["ay"] * DT * DT

        # 更新上一帧位置（保存当前帧）
        p["px"], p["py"] = p["x"], p["y"]
        p["x"], p["y"] = new_x, new_y

        # --- 周期性边界（出界即穿越） ---
        if p["x"] < 0:
            p["x"] += WIDTH
            p["px"] += WIDTH   # 关键！同时平移上一帧位置，避免虚假速度
        elif p["x"] > WIDTH:
            p["x"] -= WIDTH
            p["px"] -= WIDTH
        if p["y"] < 0:
            p["y"] += HEIGHT
            p["py"] += HEIGHT
        elif p["y"] > HEIGHT:
            p["y"] -= HEIGHT
            p["py"] -= HEIGHT

        # 极微弱阻尼（去掉这行也可以，但保留能让系统长期稳定）
        # 注意：阻尼系数接近 1，几乎不改变总能量
        p["x"] = p["x"] * DAMPING + (1 - DAMPING) * p["px"]
        p["y"] = p["y"] * DAMPING + (1 - DAMPING) * p["py"]

    # ---------- 3. 绘制 ----------
    screen.fill(BLACK)
    for p in particles:
        pygame.draw.circle(screen, p["color"], (int(p["x"]), int(p["y"])), p["radius"])
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()