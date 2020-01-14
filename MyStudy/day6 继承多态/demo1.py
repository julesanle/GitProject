class Animal:
    def eat(self):
        print("吃东西啦----")
    def sleep(self):
        print("睡觉啦-----")
class Dog(Animal):
    def bark(self):
        print("汪汪叫----")
class XiaoTianQuan(Dog):
    def fly(self):
        print("哮天犬飞起来了---")

dog = Dog()
dog.eat()
dog.sleep()
dog.bark()
xiao_dog=XiaoTianQuan()
xiao_dog.eat()
xiao_dog.fly()
