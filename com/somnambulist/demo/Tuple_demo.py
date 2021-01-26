tuple1 = ('a', 'b', 'c', 'd')
tuple2 = (1, 2, 3, 4, 5, 6, 7, 8)

print('tuple1[0]=', tuple1[0])
print('tuple2[1:5]=', tuple2[1:5])

# 修改元组
tuple3 = tuple1 + tuple2
print(tuple3)
# 删除元祖
# del tuple1
# print(tuple1)

# 计算元组元素个数。
print(len(tuple1))
# 返回元组中元素最大值。
print(max(tuple2))
# list 转为元祖
list1 = [1, 2, 3, 4]
tuple4 = tuple(list1)
print(tuple4)
