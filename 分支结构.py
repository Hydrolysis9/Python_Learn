#Python 3.10 中增加了一种新的构造分支结构的方式
# 通过使用match和case关键字
# 我们可以轻松的构造出多分支结构。

#如果使用通常的分支结构，代码如下
status_code = int(input('响应状态码: '))
if status_code == 400:
    description = 'Bad Request'
elif status_code == 401:
    description = 'Unauthorized'
elif status_code == 403:
    description = 'Forbidden'
elif status_code == 404:
    description = 'Not Found'
elif status_code == 405:
    description = 'Method Not Allowed'
elif status_code == 418:
    description = 'I am a teapot'
elif status_code == 429:
    description = 'Too many requests'
else:
    description = 'Unknown status Code'
print('状态码描述:', description)

#下面是使用match和case语法实现的代码
status_code = int(input('响应状态码: '))
match status_code:
    case 400:description = 'Bad Request'
    case 401:description = 'Unauthorized'
    case 403: description = 'Forbidden'
    case 404: description = 'Not Found'
    case 405:description = 'Method Not Allowed'
    case _:description = 'Unknown Status Code'
print('状态码描述:', description)
#_ 在代码中起通配符作用，如果前面未执行，代码将会来到 case_，通配符并非必须。
#case_只能放在分支结构的末尾，其后的分支是不可达的

#分段函数求值
x = float(input("x = "))
if x > 1:
    y = 3 * x-5
elif -1 <= x <= 1:
    y = x + 2
elif x > 1:
    y = 5 * x + 3
print(f'{y =}')
