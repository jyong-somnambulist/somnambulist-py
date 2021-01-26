list1 = ['a', 'b', 'c', 'd']
list2 = [1, 2, 3, 4, 6, 7]
print('list[0]=', list1[0])
print('list2[1:5]=', list2[1:5])
print('---------------更新列表--------------------')
list3 = []
list3.append('a')
list3.append('b')
print(list3)
print('---------------删出列表元素--------------------')
del list1[1]
print(list1)
print('---------------列表API--------------------')
list4 = ['a', 'b', 'c', 'a']
print(list4.count('a'))  #
list5 = [1, 2, 3, 4]
list4.extend(list5)
print(list4)

