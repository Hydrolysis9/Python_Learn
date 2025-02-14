# 设计一个判断给定的大于1的正整数是不是质数的函数
def judgment(num:int) ->bool:
    for i in range(2,int(num ** 0.5) - 1):
        if num % i == 0:
            return False
    return True
print(judgment(67))

# 双色球随机选号
import random
red_ball = [i for i in range(1,34)]
blue_ball = [i for i in range(1,17)]

def choice():
    select_balls = random.sample(red_ball,6)
    select_balls.sort()
    select_balls.append(random.choice(blue_ball))
    return select_balls

def display(balls):
    for ball in balls[:-1]:
        print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
    print(f'\033[034m{balls[-1]:0>2d}\033[0m')

n = int(input('生成几注号码:'))
for _ in range(n):
    display(choice())


