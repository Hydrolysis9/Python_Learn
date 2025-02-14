# 排列组合
def fac(top,bottle):
    res1 = 1
    res2 = 1
    res3 = 1
    for num in range(1,top + 1):
        res1 *= num
    for num in range(1,bottle + 1):
        res2 *= num
    for num in range(1,bottle -top+1):
        res3 *= num
    res = res2 / (res1 * res3)
    return res
print(fac(2,4))

# 判断三条边是否能构成三角形
def make_judgement(a,b,c):
    return a + b > c and a + c > b and b + c > a

# 强制位置参数 \ 与命名关键字参数 *
# def make_judgement(a, b, c, /):
#     return a + b > c and b + c > a and a + c > b
# 调用函数时只能按照参数位置来接收参数值的参数
# 若 print(make_judgement(b=2, c=3, a=1))则会报错
# def make_judgement(*, a, b, c):
#     return a + b > c and b + c > a and a + c > b
# 只能通过“参数名=参数值”的方式来传递和接收参数
# print(make_judgement(1, 2, 3))则会报错

# 参数允许拥有默认值
from random import randrange
def roll_dice(n=2):
    total = 0
    for _ in range(n):
        total += randrange(1,7)
    return total

print(roll_dice())
print(roll_dice(3))

# 可变参数
def add(*args): # * + args 表示可以接受0个或任意多个参数
    total = 0
    for val in args:
        total += val
    return total

def foo(*args,**kwargs): #**kwargs可以接收0个或任意多个关键字参数(组成字典)
    print(args)
    print(kwargs)




