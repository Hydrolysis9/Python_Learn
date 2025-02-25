# 验证输入用户名和QQ号是否有效并给出对应的提示信息
# 要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为0
import re
user_name = input('请输入您的用户名：')
qq = input('请输入您的QQ号：')
m1 = re.match(r'^[0-9a-zA-Z_]{6,20}&',user_name)
    # fullmatch函数要求字符串和正则表达式完全匹配
    # 所以正则表达式没有写起始符和结束符
m2 = re.fullmatch(r'[1-9]\d{4-11}',qq)
if not m1:
    print('请输入有效的用户名.')
if not m2:
    print('请输入有效的QQ号.')
if m1 and m2:
    print('你输入的信息是有效的!')

# 从一段文字中提取出国内手机号码
sentence = '''重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
不是15600998765，也是110或119，王大锤的手机号才是15600998765。'''
pattern = re.compile(r'(?<=\D)1[345678]\d{9}(?=\D)')
tel_list = re.findall(pattern,sentence)
print(tel_list)

# 替换字符串中的不良内容
sentence = 'Oh, shit! 你是傻逼吗? Fuck you.'
purified = re.sub('shit|fuck|[傻逼]','*',sentence,flags=re.IGNORECASE)
print(purified)

# 拆分长字符串
poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
sentence_list = re.split('[，。]',poem)
print(sentence_list)
for sentence in sentence_list:
    if sentence:
        print(sentence)
