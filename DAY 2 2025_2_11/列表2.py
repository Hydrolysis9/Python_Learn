# list_name.append('') 添加元素
# list_name.insert(num,'') 插入元素
# list_name.remove('') 删除元素
# list_name.pop() 默认删除最后一个元素，填入编号可删除编号数字 删除的元素可被赋值
# del list_name[num]
# list_name.clear() 清空列表
languages = ['Python', 'SQL', 'Java', 'C++', 'JavaScript' , 'Python']
languages.remove('Python')
print(languages) # ['SQL', 'Java', 'C++', 'JavaScript', 'Python'] 只删除了第一个

# list_name.index('',start) 从 start 位置（非必要）开始索引
# list_name.count('') 统计元素出现次数
# list_name.sort() 排序
# list_name.reverse() 反转

# 列表生成式

# 创建一个取值范围在1到99且能被3或者5整除的数字构成的列表
items = [i for i in range(1,100) if i % 3 == 0 or i % 5 ==0]

# 有一个整数列表nums1，创建一个新的列表nums2，nums2中的元素是nums1中对应元素的平方
nums1 = [35, 12, 97, 64, 55]
nums2 = [num ** 2 for num in nums1]

# 有一个整数列表nums1，创建一个新的列表nums2，将nums1中大于50的元素放到nums2中
nums1 = [35, 12, 97, 64, 55]
nums3 = [num for num in nums1 if num > 50]

# 嵌套列表

# 通过键盘输入的方式来录入5个学生3门课程的成绩并保存在列表中
scores = []
for _ in range(5):
    temp = []
    for _ in range(3):
        score = int(input("请输入："))
        temp.append(score)            # temp[a,b,c]
    scores = scores.append(temp)      # scores[[a,b,c],...]

# 通过产生随机数的方式来生成5个学生3门课程的成绩并保存在列表中
import random
scores_1 = [[random.randint(0,101) for _ in range(5)] for _ in range(5)]

# 双色球随机选号
# 每注投注号码由6个红色球和1个蓝色球组成
# 红色球号码从1到33中选择，蓝色球号码从1到16中选择。每注需要选择6个红色球号码和1个蓝色球号码
import random
t = int(input("生成几注号码："))
for _ in range(t):
    red_ball = [random.randint(1,33) for _ in range(6)]
    blue_ball = random.randint(1,16)
    red_ball.sort()
    for ball in red_ball:
        print(f'\033[031m{ball: }\033[0m', end='')
    print(f'\033[034m{blue_ball: }\033[034m')