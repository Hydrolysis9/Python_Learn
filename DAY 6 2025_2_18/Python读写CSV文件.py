# CSV文件有以下特点：
# 纯文本，使用某种字符集（如ASCII、Unicode、GB2312）等）；
# 由一条条的记录组成（典型的是每行一条记录）；
# 每条记录被分隔符（如逗号、分号、制表符等）分隔为字段（列）；
# 每条记录都有同样的字段序列。

# 将数据写入CSV文件
import csv
import random

with open('scores.csv','w') as file:
    writer = csv.writer(file,delimiter='|',quoting=csv.QUOTE_ALL)
    writer.writerow(['姓名', '语文', '数学', '英语'])
    names = ['关羽', '张飞', '赵云', '马超', '黄忠']
    for name in names:
        scores = [random.randrange(50,101) for _ in range(3)] # 生成成绩
        scores.insert(0,name) # 插入名字
        writer.writerow(scores)

# 从CSV文件读取数据
with open('scores.csv','r') as file:
    reader = csv.reader(file,delimiter='|')
    for data_list in reader:
        print(reader.line_num,end='\t')
        for elem in data_list:
            print(elem,end='\t')
        print()