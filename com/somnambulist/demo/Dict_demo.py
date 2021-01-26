d1 = {'name': 'runoob', 'age': 22, 'url': 'www.baidu.com'}
print(d1)
print("d1['name']:", d1['name'])
print("d1['age']:", d1['age'])

# 修改字典

d1['age'] = 23
print(d1)

# 删除字典元素
del d1['age']
print(d1)
# 清空字典
d1.clear()
print(d1)
# 删除字典
# del d1
# print(d1)

print('---------------------------------------------------------------------------------------')
dict1 = {'name': 'runoob', 'age': 22, 'url': 'www.baidu.com'}
# 计算字典元素个数，即键的总数。
print(len(dict1))
# 输出字典，以可打印的字符串表示。
print(str(dict1))
# 返回输入的变量类型，如果变量是字典就返回字典类型。
print(type(dict1))
# 返回指定键的值，如果键不在字典中返回 default 设置的默认值
print(dict1.get('name', 'error'))
# 如果键在字典dict里返回true，否则返回false
if 'name' in dict1:
    print(dict1['name'])
else:
    print('error')
print('---------------------------------------------------------------------------------------')
# radiansdict.items() 以列表返回可遍历的(键, 值) 元组数组
dict1 = {'name': 'runoob', 'age': 22, 'url': 'www.baidu.com'}
for k, v in dict1.items():
    print(k + '--' + str(v))

print('---------------------------------------------------------------------------------------')
# radiansdict.keys()
# 返回一个迭代器，可以使用 list() 来转换为列表
for key in dict1.keys():
    print(dict1[key])

#radiansdict.update(dict2)
#把字典dict2的键/值对更新到dict里
dict2={}
dict2.update(dict1)
print(dict2)


