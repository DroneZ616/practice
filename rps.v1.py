print('2026.7.2.v1')
from random import choice
import json
import os

# ===== 全局配置（不变） =====
options = ['石头', '剪刀', '布']



# ===== 新武器：纯判断函数（只负责算结果，不负责打印） =====
def judge(player, computer):
    #"""返回 'win'、'lose' 或 'draw'"""
    if player == computer:
        return 'draw'
    if (player == '石头' and computer == '剪刀') or \
       (player == '剪刀' and computer == '布') or \
       (player == '布' and computer == '石头'):
        return 'win'
    else:
        return 'lose'

# ===== 游戏主体：全部装进 main() 里 =====
def main():
    # 1. 初始化或读取存档
    player_data = {'name': '玩家', 'level': '奶龙战神级', 'win': 0, 'lose': 0}
    
    if os.path.exists('rps_save.json'):  # 如果存档文件存在
        with open('rps_save.json', 'r', encoding='utf-8') as f:
            player_data = json.load(f)
        print(f"欢迎回来，{player_data['name']}！当前战绩：{player_data['win']}胜 {player_data['lose']}负")
    else:
        print("首次游玩，欢迎你！")
        player_data['name']=input('给自己起个名字吧!')
        print(f"你好,{player_data['name']}!")
        
    
    print("=== 欢迎来到石头剪刀布 ===" \
    "你将和一个电脑对战(我知道这个游戏很sb)")

    # 2. 主游戏循环
    while True:
        
        print("\n请选择：")
        print("1. 石头")
        print("2. 剪刀")
        print("3. 布")
        print("0. 退出游戏")
        def shucuo():
            if i>=5:
                print('sb别乱搞！')
            if i>=10:
                print('别搞了，再输错不会有反应了')
            if i>=20:
                print('你怎么不信呢？再输错真没反应了')
            if i>=100:
                print('呃。。。你居然真的有这么闲')
        

        try:
            player_choice = int(input("请输入编号："))
            
            if player_choice == 0:
                print(f"最终战绩：{player_data['win']} 胜 {player_data['lose']} 负")
                print("谢谢游玩，再见你这个sb！")
                break
            
            if player_choice not in [1, 2, 3]:
                i+=1
                print("只能输1230啊，懂不懂？")
                shucuo()
                continue

            # 出拳
            player = options[player_choice - 1]
            computer = choice(options)
            print(f"你出了：{player}")
            print(f"电脑出了：{computer}")

            # 3. 调用 judge 函数判定，再根据结果更新数据和打印
            result = judge(player, computer)
            
            if result == 'draw':
                print("🤝 平局！")
            elif result == 'win':
                print("🎉 你赢了，sb！")
                player_data['win'] += 1
                i1=0
            else:  # result == 'lose'
                i1+=1
                print("😅 电脑赢了！")
                player_data['lose'] += 1
            if i1>=5:
                print('电脑赢麻了')

            print(f"当前比分 你：{player_data['win']}，电脑：{player_data['lose']}")

        except ValueError:
            i+=1
            print("别乱输,好不好？")
            shucuo()
            continue
        
        if player_data['win']==30:
            print('其实有个彩蛋，你自己找吧')
    # 4. 游戏结束，保存存档
    with open('rps_save.json', 'w', encoding='utf-8') as f:
        json.dump(player_data, f, ensure_ascii=False)
    print("战绩已保存！")
    print("游戏结束")

# ===== 经典入口：只有直接运行这个文件时才执行 main() =====
if __name__ == "__main__":
    main()