class Person(object):
    count=0
    @classmethod
    def show_count(cls):
        print("我是一个类方法,count数：%d"%Person.count)
    def __init__(self,name):
        self.name=name
        Person.count += 1

person = Person("小明")
Person.show_count()