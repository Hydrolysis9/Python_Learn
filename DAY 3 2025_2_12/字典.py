# 创建和使用字典
xinhua = {
    '麓': '山脚下',
    '路': '道，往来通行的地方；方面，地区：南～货，外～货；种类：他俩是一～人',
    '蕗': '甘草的别名',
    '潞': '潞水，水名，即今山西省的浊漳河；潞江，水名，即云南省的怒江'
}
print(xinhua)
person = dict(name = '小陈',age = 20,height = 183,weight = 63)
print(person)
# 生成式语法
item1 = {x:x ** 3 for x in range(7)}
print(item1)

# 字典的运算
# 成员运算：in or not in
# 索引运算
print(person["name"])
person['school'] = '南方医科大学'
for item in person:
    print(f'{item}:{person[item]}')

# 字典的方法
print(person.get('name'))
print(person.get('e_mail','')) # 当键不存在时返回特定值，默认为None
print(person.keys()) # 返回所有键
print(person.values()) # 返回所有值
print(person.items()) # 返回所有键值对
for key,value in person.items():
    print(f'{key}: {value}')
person_add = {'e_mail' : '945228305@qq.com'}
person.update(person_add) # {'name': '小陈', 'age': 20, 'height': 183, 'weight': 63, 'school': '南方医科大学', 'e_mail': '945228305@qq.com'}
print(person.pop('e_mail'))
print(person.popitem())
del person["age"]

# 输入一段话，统计每个英文字母出现的次数，按出现次数从高到低输出
sentence = input('请输入一段话：')
alpha_dict = {}
for i in sentence:
    if 'A' <= i <= 'Z' or 'a' <= i <= 'z':
        alpha_dict[i] =  alpha_dict.get(i,0) + 1
alpha_dict_1 = sorted(alpha_dict,key=alpha_dict.get,reverse=True)
for o in alpha_dict_1:
    print(f'{o}出现了{alpha_dict[o]}次')

# 在一个字典中保存了股票的代码和价格，找出股价大于100元的股票并创建一个新的字典
stocks = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}
stock_2 = {x:y for x,y in stocks if y >= 100}
print(stock_2)