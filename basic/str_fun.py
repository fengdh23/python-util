intab= '最'
outtab='*'
trantab = str.maketrans(intab, outtab) # 创建转换表

str1='最棒'
print(str1.translate(trantab)) # *棒