class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("构造方法=========")
    def eat(self):
        print("%s今年%d岁，要好好吃饭"%(self.name,self.age))
    def sleep(self):
        print ("%s今年%s岁，要好好睡觉"%(self.name,self.age))

if __name__ == '__main__':
    s1=Student("小A",10)
    s1.eat()
    s1.sleep()
