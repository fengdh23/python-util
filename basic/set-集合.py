# 很多教程不把集合当作标准的数据结构

set1=set([1,200,39,50])
set2=([1,200,39,50]) # 列表
set3=set(['大海','男']) # 输出顺序不确定

print(set1)
print(set2)
print(set3)

print(set(set2))