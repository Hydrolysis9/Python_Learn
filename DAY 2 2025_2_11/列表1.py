# 用[]定义列表
# list_name[] 位置索引
# list_name[ start : end : stride ] 切片运算 stride为正时,左闭右开;反之全闭
# 如果start值等于0，那么在使用切片运算符时可以将其省略
# 如果end值等于N，N代表列表元素的个数，那么在使用切片运算符时可以将其省略
# 如果stride值等于1，那么在使用切片运算符时也可以将其省略

#掷色子统计每种点数出现次数
import random

dice_list = [0] * 6
for _ in range(6000):
    face = random.randrange(1, 7)
    dice_list[face-1] += 1
for face in range(1,7):
    print(f'{face}点出现了{dice_list[face-1]}次')