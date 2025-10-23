class Student:
    def __change(self, name, count):
        self.name = name
        self.count = count
        print('类: '+ str(count))


m=Student()
m.__change('flynn', 10) # Student' object has no attribute '__change'