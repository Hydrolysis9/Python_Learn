# 转义字符：字符串中使用反斜杠 \ 表示转义，表示其后字符不再是它原来的意义
s1 = '\'Hello world\''
s2 = '\\Hello world\\'

# 原始字符串：以 r 或 R 开头，表示字符串中的每个字符都是它本来的含义
# \t: 制表符 \r；回车符 \n：换行符
s3 = '\it \is \time \to \read \now'
s4 = r'\it \is \time\to \read \now'

# 拼接（+）与重复（*）
s5 = 'a' * 10 #aaaaaaaaaa

# 比较运算：比较每个字符对应编码大小，编码可用 ord 函数获得
# 成员运算：in or not in ，产生布尔值结果
# 索引与切片：与列表无区别，但是为不可变类型
# 字符串的方法
    # 大小写相关操作
        # str.capitalize() 字符串首字母大写
        # str.title() 字符串每个单词首字母大写
        # str.upper() 字符串变大写
        # str.lower() 字符串变小写

    # 查找操作：str.find('',num) or str.index('',num) num为起始位置 返回为位置数字

    # 性质判断
        # str.startswith() 判断是否由某个字符串开头，返回bool值
        # str.endswith() 判断是否由某个字符串结尾，返回bool值
        # str.isdigit() 判断字符串是否完全由数字构成
        # str.isalpha() 判断字符串是否完全由字母构成
        # str.isalnum() 判断字符串是否由字母和数字构成

    # 格式化
        # center、ljust、rjust 方法：居中、左对齐、右对齐
s = 'hello world'
print(s.center(20,'*'))
print(s.ljust(20))
print(s.rjust(20))
        # 占位符格式化 %d
        # format 方法格式化

    # 修剪操作：strip and lstrip and rstrip 默认裁剪空字符

    # 替换操作：str.replace(a,b,n) a被b替换(n次)

    # 拆分与合并
        # str.split('',n) 默认拆分空格(n次)，拆分后结果为一个列表list_str
        # join(''.list_str)
s = 'hello world'
list_s = s.split()
print(list_s)
print('*'.join(list_s))

    # 编码与解码: str.encode() and str.decode() 编码与解码方式需一致