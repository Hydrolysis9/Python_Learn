# 将字典处理成JSON格式并写入文本文件
import json
my_dict = {'name':'小陈',
           'age' : 20,
           'friend': ['小延','小金'],
           'games':[{'name':'Delta Action','hour':250},
                    {'name':'Civilization','hour':213}]}
with open('data.json','w') as file:
    json.dump(my_dict,file)
    print(type(file))

# 将JSON格式的数据还原成Python中的字典
with open('data.json','r') as file:
    my_dict = json.load(file)
    print(type(my_dict))
    print(my_dict)
