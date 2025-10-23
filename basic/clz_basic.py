class Student:
    name = '阿海'
    def welcome(self):
        print('类: ',self.__class__) # <class '__main__.Student'>
        print('示例: ',self) # <__main__.Student object at 0x0000017DC4E26E40>

w = Student() # 创建对象|实例
w.welcome()

