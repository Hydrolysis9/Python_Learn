#判断素数
#要求输入一个大于1的正整数，判断它是不是素数

num = int(input("请输入一个大于1的正整数："))
end = int(num ** 0.5)
is_prime = True
for i in range(2,end +1):
    if num % i == 0:
        is_prime = False
        break
if is_prime:
      print(f'{num}是素数')
else:
    print(f'{num}不是素数')

#最大公约数
#输入两个大于0的正整数，求两个数的最大公约数。
i = int(input("i = "))
j = int(input("j = "))
for m in range(i ,0,-1):
    if  i % m ==0 and j % m == 0:
        print(f'最大公约数{m}')
        break

#猜数字小游戏
#计算机出一个1到100之间的随机数
# 玩家输入自己猜的数字
# 计算机给出对应的提示信息“大一点”、“小一点”或“猜对了”
# 如果玩家猜中了数字，计算机提示用户一共猜了多少次，游戏结束，否则游戏继续。

import random
answer = random.randint(1,101)
i = int(input('请输入您猜的数字(0-100): '))
t = 1
while i != answer:
    if i > answer:
        print("小一些")
    elif i < answer:
        print("大一些")
    i = int(input('请再输入您猜的数字: '))
    t += 1
print("猜对了,您一共猜了%d次"%t)

import random
answer = random.randint(1,101)
i = int(input('请输入您猜的数字(0-100): '))
for t in range(1,100):
    if i > answer:
        print("小一些")
    elif i < answer:
        print("大一些")
    else:
        print("猜对了,您一共猜了%d次"%t)
        break
    i = int(input('请再输入您猜的数字: '))

















