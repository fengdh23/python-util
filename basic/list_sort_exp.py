list1=['1001','大海',20]

def sort_exp(x):
    if type(x) is not str:
        return '0' # 数字转换成最小字符串
    return x

list1.sort(key=sort_exp)
print(list1)