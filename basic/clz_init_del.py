from pyarrow import nulls


class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Person2 init, 有参数')

    def __del__(self):
        print('Person2 __del__, 无参数')
        pass

class Person1:
    def __init__(self):
        print('Person1 init, 无参数')

    def __del__(self): # 正确的析构方法不应该接收除self外的其他参数。
        print('Person1 __del__, 无参数')
        pass



m = Person1()
m2 = Person2('大海',18)
# m2 =None
m2.__del__() # Person2 __del__, 无参数
