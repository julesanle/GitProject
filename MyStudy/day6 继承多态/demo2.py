class Animal:
    def eat(self):
        print("吃东西啦----")
    def sleep(self):
        print("睡觉啦-----")
class Dog(Animal):
    __age=1
    def eat(self):
        print("吃骨头")
    def bark(self):
        print("汪汪叫----")
    def __test(self):
        print("私有方法")

class XiaoTianQuan(Dog):
    def fly(self):
        print("哮天犬飞起来了---")
    def eat(self):
        print("吃肉")
        super().bark()
        print("asfsaffgrtt")

dog = Dog()
dog.eat()
dog.sleep()
dog.bark()
xiao_dog=XiaoTianQuan()
xiao_dog.eat()