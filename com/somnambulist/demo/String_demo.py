str='hello word'

print(str)              # 打印完整字符串
print(str[0:-1])        # 打印从第一个字符串到倒数第二个字符串
print(str[0])           # 打印第一个字符串
print(str[2:5])         # 打印第三个字符串到第五个
print(str[2:])          # 打印第三个后所有的字符
print(str[1:5:1])       # 打印从第二个开始到第五个且每隔一个字符
print(str*2)            # 打印两次字符串
print(str+"xxxx")       # 字符串连接
print("---------------------------------------------------------------------------------------------------------")

print("hellow\nworld")  # 转行 发生转义
print(r'hello\nworld')  # 不转行 不发生转义
print("---------------------------------------------------------------------------------------------------------")

#input('\n\n按下 enter 键后退出')

import sys;x='runjob';sys.stdout.write(x+'\n')

print("---------------------------------------------------------------------------------------------------------")

x='a'
y='b'

# 换行输出
print(x)
print(y)

print("---------------------------------------------------------------------------------------------------------")
# 不换行输出
print(x, end=' ')
print(y, end= ' ')
print()




