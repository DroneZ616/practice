from random import choice   # 让电脑能随机出拳
import json
import os

# 定义赢的规则
options = ['石头', '剪刀', '布']
def show_rule():
    print("石头赢剪刀，剪刀赢布，布赢石头")
#玩家初始数据
player_data={'name':'玩家','level':1,'win':0,'lose':0}
if os.path.exists('rps_save.json'):  # 如果存档文件存在
    with open('rps_save.json', 'r', encoding='utf-8') as f:
        player_data = json.load(f)
    print(f"欢迎回来，{player_data['name']}！当前战绩：{player_data['win']}胜 {player_data['lose']}负")
else:
    print("首次游玩，欢迎你！")
    player_data['name']=input('给自己起个名字吧!')
    print(f"你好,{player_data['name']}!")

# --- 游戏中间：每次赢了就改数据 ---
# 比如你赢了：player_data['win'] += 1
# 你输了：player_data['lose'] += 1


print("=== 欢迎来到石头剪刀布 ===")

while True:
    print("\n请选择：")
    print("1. 石头")
    print("2. 剪刀")
    print("3. 布")
    print("0. 退出游戏")
    show_rule()
    try:
        player_choice = int(input("请输入编号："))
        if player_choice == 0:
            print(f"最终战绩：{player_data['win']} 胜 {player_data['lose']} 负")
            print("谢谢游玩，再见！")
            break
        if player_choice not in [1, 2, 3]:
            print("输入无效，请重新选择。")
            continue
        # 获取你的出拳
        player = options[player_choice - 1]
        # 电脑随机出拳
        computer =choice(options)
        print(f"你出了：{player}")
        print(f"电脑出了：{computer}")
    except ValueError:
        print("请输入数字！")
        continue

        # 判断胜负（核心逻辑）
    if player == computer:
        print("🤝 平局！")
    elif (player == '石头' and computer == '剪刀') or \
        (player == '剪刀' and computer == '布') or \
        (player == '布' and computer == '石头'):
        print("🎉 你赢了！")
        player_data['win'] += 1
        print("调试：赢了，当前 win =", player_data['win'])
    else:
        print("😅 电脑赢了！")
        player_data['lose'] += 1
    print(f"当前比分 你：{player_data['win']},电脑：{player_data['lose']}")
    

# --- 游戏结束：存档（覆盖保存） ---
# 就在 with open 上面一行加
print("调试：准备保存的数据是", player_data)
with open('rps_save.json', 'w', encoding='utf-8') as f:
    json.dump(player_data, f, ensure_ascii=False)
print("战绩已保存！")
print("游戏结束")