class Student1:
    __count = 0  # 实际存储名称变为 _Student1__count
    __name = 'flynn'

    def __init__(self, name, count):  # 一个类不能像Java那样定义多个不同参数的 init 方法
        Student1.__count += count
        self.__name = name

    def seek(self):
        print(self.__name + '积分为:' + str(self.__count))


m = Student1('flynn', 100)
m.seek()
m.__count = 1000  # 实际创建了一个新的实例属性，而非修改类属性
m._Student1__count = 99  # 实例访问 无效
Student1._Student1__count = 9999999  # 类访问 有效
print(Student1._Student1__count)  # 访问原始类属性
