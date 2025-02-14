import random
import time
from functools import wraps

# 装饰器
def download(filename):
    print(f'开始下载{filename}.')
    time.sleep(random.random() * 6)
    print(f'{filename}下载完成.')

def record_time(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end =   time.time()
        print(f'{func.__name__}执行时间: {end - start:.2f}秒')
        return result
    return wrapper
download = record_time(download)
download('MySQL从删库到跑路.avi')

# 语法糖
@record_time
def upload(filename):
    print(f'开始上传{filename}.')
    time.sleep(random.random() * 6)
    print(f'{filename}上传完成.')

upload('MySQL从删库到跑路.avi')

# 保留被装饰前的函数
# Python标准库functools模块的wraps函数也是一个装饰，
# 我们将它放在wrapper函数上，这个装饰器可以帮我们保留被装饰之前的函数
# 在需要取消装饰器时，可以通过被装饰函数的__wrapped__属性获得被装饰之前的函数。
def record_time(func):

    @wraps(func)
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end =   time.time()
        print(f'{func.__name__}执行时间: {end - start:.2f}秒')
        return result
    return wrapper

@record_time
def delete(filename):
    print(f'开始删除{filename}.')
    time.sleep(random.random() * 6)
    print(f'{filename}删除完成.')

delete('Python从入门到住院.pdf')
delete.__wrapped__('Python从入门到住院.pdf')

# 递归调用
# 求阶乘
def fac(num):
    if num in (0,1):
        return 1
    return num * fac(num -1)
# 第n个斐波那契数
def fabor(num):
    if num in (1,2):
        return 1
    return fabor(num-1) + fabor(num-2)
print(fabor(10))






