import random
secret=random.randint(1,100)
guess=None
count=0
print('请开始猜测,你只有10次机会')
for i in range(10):
    guess=int(input('请输入数字'))
    count+=1
    if guess==secret:
        print(f"恭喜你，就是{secret}!你一共猜了{count}次！")
        break
    if guess<secret:
        print('太小了')
    if guess>secret:
        print('太大了')
else:
    print(f"没次数了，答案是{secret}")
