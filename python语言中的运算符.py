f = float(input("请输入华氏温度： "))
c = (f-32)/1.8
# %表示占位符
# %d int 类型
# %s str 类型
print("%.1f华氏度 = %.1f摄氏度"%(f,c))
#也可用如下方法
print(f"{f:.1f}华氏度 = {c:.1f}摄氏度")

#输入一个1582年以后的年份，判断该年份是不是闰年。
year = int(input("请输入年份："))
if year%4 == 0:
    print("%d年是闰年" %year)
else:print("%d年不是是闰年" %year)

year = int(input('请输入年份: '))
is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(f'{is_leap = }')
