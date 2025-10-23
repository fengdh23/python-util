from basic.map_01 import score1

list1=['1001','张小','男'] # 都是 字符串
list1.sort() # 字典序（ASCII码顺序）
print(list1)

score1=[80,90,100,50]
score1.sort()
print(score1)


score11=[80,90,100,50]
score2=score11

score2.sort()

print('score1 成绩',score11) # 也进行了排序
print('score2 成绩',score2)
print('位置:',id(score11),id(score2)) # 地址相同

## 副本排序
score12=[80,90,100,50]
score3=score12[:] # 复制 和 copy 区别
score3.sort()
print('score12 成绩',score12) # 未进行排序
print('score3 成绩',score3) # 进行排序
print('位置:',id(score12),id(score3)) # 位置相同

print('------深copy--------')
score13=[80,90,100,50]
score4= score13.copy()
score4.sort()
print('score12 成绩',score13) # 未进行排序
print('score3 成绩',score4) # 进行排序
print('位置:',id(score13),id(score4)) # 位置不相同
