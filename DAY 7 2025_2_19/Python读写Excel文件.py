# 读Excel文件
import xlrd
wb = xlrd.open_workbook('阿里巴巴2020年股票数据.xls')
sheet_name = wb.sheet_names()
print(sheet_name)
sheet = wb.sheet_by_name(sheet_name[0])
print(sheet.nrows,sheet.ncols)
for row in range(sheet.nrows):
    for col in range(sheet.ncols):
        value = sheet.cell(row,col).value
        # 对除首行外的其他行进行数据格式化处理
        if row > 0:
            if col == 0:
                # xldate_as_tuple函数的第二个参数只有0和1两个取值
                # 其中0代表以1900-01-01为基准的日期，1代表以1904-01-01为基准的日期
                value = xlrd.xldate_as_tuple(value,0)
                value = f'{value[0]}年{value[1]:>02d}月{value[2]:>02d}日'
            # 其他列的number类型处理成小数点后保留两位有效数字的浮点数
            else:
                value = f'{value:.2f}'
        print(value,end='\t')
    print('')
# 获取最后一个单元格的数据类型
# 0 - 空值，1 - 字符串，2 - 数字，3 - 日期，4 - 布尔，5 - 错误
last_cell_type = sheet.cell_type(sheet.nrows - 1,sheet.ncols - 1)
print(last_cell_type)
print(sheet.row_values(0))
# 获取指定行指定列范围的数据（列表）
# 第一个参数代表行索引，第二个和第三个参数代表列的开始（含）和结束（不含）索引
print(sheet.row_slice(3,0,5))

# 写Excel文件
import random
import xlwt

student_names = ['关羽', '张飞', '赵云', '马超', '黄忠']
scores = [[random.randrange(50,101) for _ in  range(3)]for _ in range(5)]
wb = xlwt.Workbook()
sheet = wb.add_sheet('一年级二班')
titles =('姓名', '语文', '数学', '英语')
# 添加表头数据
for index,title in enumerate(titles): # enumerate() 用于将可迭代对象组合为索引序列
    sheet.write(0,index,title)
for row in range(len(scores)):
    sheet.write(row + 1,0,student_names[row])
    for col in range(len(scores[row])):
        sheet.write(row + 1, col + 1, scores[row][col])
wb.save('考试成绩表.xls')