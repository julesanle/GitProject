class Dog(object):
    def __init__(self,name):
        self.name=name

    def bark(self):
        print("%s汪汪叫"%self.name)

class XiaoTianQuan(Dog):
    def __init__(self,name):
        self.name=name
    def bark(self):
        print("%s会说话啦"%self.name)

class Person:
    def __init__(self,name):
        self.name=name
    def play(self,dog):
        print("%s惹%s叫起来啦"%(self.name,dog.name))
        dog.bark()

# dog = Dog("小黑")
dog = XiaoTianQuan("哮天犬")
person=Person("小明")
person.play(dog)