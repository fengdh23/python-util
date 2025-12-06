def count(n):
    x = 0
    while x < n:
        yield x # 没有 yield 就会报错
        x += 1
    # x += 1 # 注意 不能在这个位置

for i in count(6):
    print(i) # 0 1 2 3 4 5
