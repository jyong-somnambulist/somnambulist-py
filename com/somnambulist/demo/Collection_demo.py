list1 = ['a', 'b', 'c', 'd']
list2 = [1, 2, 3, 4, 6, 7]
print('list[0]=', list1[0])
print('list2[1:5]=', list2[1:5])
print('---------------更新列表--------------------')
list3 = []
list3.append('a')
list3.append('b')
print(list3)
print('---------------删除列表元素--------------------')
del list1[1]
print(list1)
print('---------------列表API--------------------')
list4 = ['a', 'b', 'c', 'a']
print(list4.count('a'))  # 统计某个字符出现的次数
list5 = [1, 2, 3, 4]
list4.extend(list5)  # 两个集合合并
print(list4)
list5.insert(2, 'a')  # 将对象插入列表
print(list5)
list5.pop()  # 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
print(list5)
list5.remove('a')  # 移除列表中某个值的第一个匹配项
print(list5)
list5.reverse()  # 反转
print(list5)
list5.sort(reverse=False)  # 排序
print(list5)


# 获取都二个元素
def getFirstEle(elem):
    return elem[1]


# 列表
random = [(2, 2), (3, 4), (1, 3)]
# 按照第二个元素排序
random.sort(key=getFirstEle)
print('排序列表:', random)
print('----------------------------------------------------------------------------------------------------')
list6 = {'a', 'b', 'c', 'd'}
list7 = {'a', 'b'}
print(list6 - list7)  # 集合a中包含而集合b中不包含的元素
print(list6 | list7)  # 集合a或b中包含的所有元素
print(list6 & list7)  # 集合a和b中都包含了的元素
print(list6 ^ list7)  # 不同时包含于a和b的元素
print('----------------------------------------------------------------------------------------------------')
a = {x for x in 'asadfasdfljla' if x not in 'asdf'}
print(a)
print('----------------------------------------------------------------------------------------------------')
set1 = set(('a', 'b', 'c'))
set1.add('c')
set1.add('e')
print(set1)
