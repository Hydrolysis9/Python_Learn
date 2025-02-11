#输出斐波那契数列的前20个数
i , j = 0 , 1
for m in range(0,10):
    i , j = j , i + j
    print(i)


#找出100到999范围内的所有水仙花数。
#它是一个N位非负整数，其各位数字的N次方和刚好等于该数本身
for m in range(100,1000):
    if m == (m // 100) ** 3 + ((m % 100) // 10) ** 3 + (m % 10) ** 3:
        print(m)

print(2 // 10)

# 将一个不知道有多少位的正整数进行反转
num =int(input("请数入一个正整数："))
i = 0
while num > 0:
    i = num % 10 + i * 10
    num //= 10
print(i)

# 公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
for z in range(0,100,3):
    for x in range(0, 21):
        y = 100 - x - z
        if y % 1 == 0 and 5 * x + 3 * y + z / 3 == 100 and 33 >= y >= 0:
            print(f'公鸡：{x},母鸡：{y},小鸡：{z}')

# CRAPS赌博游戏
#玩家第一次摇骰子如果摇出了7点或11点，玩家胜；玩家第一次如果摇出2点、3点或12点，庄家胜；
#玩家如果摇出其他点数则游戏继续，玩家重新摇骰子；
#如果玩家摇出了7点，庄家胜；如果玩家摇出了第一次摇的点数，玩家胜
#其他点数玩家继续摇骰子，直到分出胜负。
#开始时玩家有1000元赌注，每局开始时可下注，输光赌注游戏结束

#我的版本
import random
bets = 1000
your_bet = int(input(f'请下注(您现在的注金为：{bets})：'))
dice_1 , dice_2 = random.randint(0, 6) , random.randint(0, 6)
the_score = dice_1 + dice_2
print(f'此回合点数为：{the_score}')
if the_score == 7 or the_score == 11:
    bets += your_bet
    print('玩家胜')
elif the_score == 2 or the_score == 3 or the_score == 12:
    bets -= your_bet
    if bets == 0:
        print('庄家胜,您的注金已用尽，游戏结束')
    else:print('庄家胜')
else:
    print('游戏继续')
while bets > 0:
    your_bet = int(input(f'请下注(您现在的注金为：{bets})：'))
    dice_1, dice_2 = random.randint(0, 6), random.randint(0, 6)
    score = dice_1 + dice_2
    print(f'此回合点数为：{score}')
    if score == 7:
        bets -= your_bet
        if bets == 0:
              print('庄家胜,您的注金已用尽，游戏结束')
        else:
             print('庄家胜')
    elif score == the_score:
        bets += your_bet
        print('玩家胜')
    else:
        print('游戏继续')

#参考版本,此版本与上版本有重复赋值，请注意
import random
money = 1000
while money > 0:
    print(f'你的总资产为: {money}元')
    # 下注金额必须大于0且小于等于玩家的总资产
    while True:
        debt = int(input('请下注: '))
        if 0 < debt <= money:
            break
    # 用两个1到6均匀分布的随机数相加模拟摇两颗色子得到的点数
    first_point = random.randrange(1, 7) + random.randrange(1, 7)
    print(f'\n玩家摇出了{first_point}点')
    if first_point == 7 or first_point == 11:
        print('玩家胜!\n')
        money += debt
    elif first_point == 2 or first_point == 3 or first_point == 12:
        print('庄家胜!\n')
        money -= debt
    else:
        # 如果第一次摇色子没有分出胜负，玩家需要重新摇色子
        while True:
            current_point = random.randrange(1, 7) + random.randrange(1, 7)
            print(f'玩家摇出了{current_point}点')
            if current_point == 7:
                print('庄家胜!\n')
                money -= debt
                break
            elif current_point == first_point:
                print('玩家胜!\n')
                money += debt
                break
print('你破产了, 游戏结束!')
