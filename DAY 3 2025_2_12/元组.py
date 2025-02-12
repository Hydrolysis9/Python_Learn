# 元组中有n个元素称为n元组而一元组的表示中需在元素后加上一个逗号
# 打包与解包操作

# 打包操作
a = 1, 2, 3
type(a) #tuple
# 解包操作
b, c, d =  a
print(b, c, d) #1 2 3

# 交换变量的值
tup = 1, 2, 3, 4
e, f, g, h = tup

# 元组与列表的相互转换
# 将元组转换为列表：infos = ()
#                print(list(infos))
# 将列表转换为元组：frts = []
#                print(tuple(frts))
