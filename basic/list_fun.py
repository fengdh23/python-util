stu_list1=['1001', 'flynn']
stu_list1.append('男')
stu_list1.append(18)

stu_list2=['1002', 'tom']
stu_list2.append('男')

stu_list1.extend(stu_list2)

print(stu_list1) # ['1001', 'flynn', '男', 18, '1002', 'tom', '男']

print('男 出现的次数', stu_list1.count('男'))

print('获取男的位置', stu_list1.index('男')) # 第一个出现的位置

stu_list1.insert(5, 100)

stu_list1.pop(3)

stu_list1.remove('男')

stu_list1.reverse() # 颠倒顺序O
stu_list1.sort(reverse=True) # 排序 类型一致

print(stu_list1)