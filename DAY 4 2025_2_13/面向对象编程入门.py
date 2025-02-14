# 定义类
class Students:
    def study(self,course_name):
        print(f'学生正在学习{course_name}')

    def play(self,game_name):
        print(f'学生正在玩{game_name}')

# 创建和使用对象
student1 = Students()
Students.study(student1,'程序设计')
student1.study('python')

# 初始化方法
class Students:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def study(self,course_name):
        print(f'{self.name}正在学习{course_name}')

    def play(self,game_name):
        print(f'{self.name}正在玩{game_name}')

stu1 = Students('小陈','022002')
stu1.play('Delta Action')

# 封装
import time
# 定义一个类描述数字时钟
class Clock:
    def __init__(self,hour=0,minute=0,second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def run(self):
        self.second += 1
        if self.second == 60:
            self.minute += 1
            self.second =0
            if self.minute == 60:
                self.hour += 1
                self.minute = 0
                if self.hour == 24:
                    self.hour = 0

    def show(self):
        return f'{self.hour}:{self.minute}:{self.second}'

clock1 = Clock()
# 时钟启动
# while True:
#     print(clock1.show())
#     time.sleep(1)
#   clock.run

# 定义一个类描述平面上的点，要求提供计算到另一个点距离的方法
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distance(self,other):
        result = ((self.x-other.x) ** 2 + (self.y - other.y) ** 2 ) ** 0.5
        return f'距离为{result:.2f}'

    def __str__(self):
        return f'({self.x},{self.y})'
point1 = Point(1,2)
point2 = Point(2,3)
print(point1.distance(point2))
print(point1)