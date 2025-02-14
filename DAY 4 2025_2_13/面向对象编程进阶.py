# 可见性和属性装饰器
# 在 Python 中，可以通过给对象属性名添加前缀下划线的方式来说明属性的访问可见性
from sympy.plotting.textplot import is_valid


class Students:

    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def study(self, course_name):
        print(f'{self.__name}正在学习{course_name}.')

stu = Students('小陈','20')
stu.study('Python')

# 动态属性：Python 语言属于动态语言，在运行时可以改变其结构的语言，例如新的函数、对象、甚至代码可以被引进，已有的函数可以被删除或是其他结构上的变化
stu.sex = '男'  # 给学生对象动态添加sex属性
# 如果不希望在使用对象时动态的为对象添加属性，可以使用 Python 语言中的__slots__魔法
class Point:
    __slots__ = ('x','y')
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distance(self,other):
        result = ((self.x-other.x) ** 2 + (self.y - other.y) ** 2 ) ** 0.5
        return f'距离为{result:.2f}'

    def __str__(self):
        return f'({self.x},{self.y})'

p1 = Point(1,2)
# p1.z = 3  # AttributeError: 'Student' object has no attribute 'z'

# 静态方法和类方法
class Triangle(object):
    """三角形"""

    def __init__(self, a, b, c):
        """初始化方法"""
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def is_valid(a, b, c):
        """判断三条边长能否构成三角形(静态方法)"""
        return a + b > c and b + c > a and a + c > b

    @property # 将三角形类的 perimeter 和 area 变成属性
    def perimeter(self):
        """计算周长"""
        return self.a + self.b + self.c

    @property
    def area(self):
        """计算面积"""
        p = self.perimeter / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5


print(Triangle.is_valid(1,1,1))
t = Triangle(3,4,5)
print(f'周长: {t.perimeter}')
# print(f'面积: {t.area}')

# 继承和多态
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name}正在吃饭.')

    def sleep(self):
        print(f'{self.name}正在睡觉.')

class Student(Person):

    def __init__(self, name, age):
        super().__init__(name, age) #继承属性

    def study(self, course_name):
            print(f'{self.name}正在学习{course_name}.')

class Teacher(Person):

    def __init__(self, name, age, title):
            super().__init__(name, age)
            self.title = title

    def teach(self, course_name):
            print(f'{self.name}{self.title}正在讲授{course_name}.')