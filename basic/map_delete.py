dict1={'姓名':'大海','年龄': 20}

# dict1.clear()
# print('1. 所有键',dict1.keys())

str1=dict1.pop('年龄') # 删除并返回值
print(str1)
print(dict1)

dict2=dict1.copy()
dict2.setdefault('性别','女')
print('popitem前: ',dict2)
dict2.popitem()
print('popitem 后: ',dict2)

dict3=dict1.copy()
dict3.setdefault('性别','女')
del dict3['性别'] # 不存在，报错
print(dict3)

del dict3 # 删除字典
# print(dict3) # 报错 not defined

dict4=dict1.copy()

if 'aa' in dict4:
    print('存在')

if 'aa' not in dict4:
    print('不存在')
