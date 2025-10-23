dict1={'姓名':'大海','年龄': 20}

print('1. 所有键',dict1.keys())
print('2. 所有值',dict1.values())
print('3. 所有键-值',dict1.items())

dict2=dict1 # 浅copy
dict3=dict1.copy() # 深copy

print('4. 浅copy 和深 copy',id(dict1),id(dict2),id(dict3))

score1=(1,2,3,4)
dict4=dict1.fromkeys(score1) # 之前的不会被覆盖
print('5. 通过元祖创建字典: ',dict4)
print('6. get 年龄:', dict1.get('年龄'))

dict1.setdefault('年龄',30) #  不存在则新增
print('7. setdefault 年龄:', dict1)
# print('7. setdefault 年龄:', dict1.get('年龄'))

dict1.setdefault('年纪大小',30) # 不会修改
print('8. setdefault 年纪大小:', dict1)

dict5={'成绩':'优良'}
dict1.update(dict5) # 新增
dict5={'成绩':'100'}
dict1.update(dict5) # 新增
print('9. update 成绩: ',dict1)
