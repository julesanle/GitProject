class Person:
    def __init__(self,name,weight):
        self.name=name
        self.weight=weight
    def __str__(self):
        return "%s的体重%.2fkg" % (self.name,self.weight)
    def eat(self):
        print("%s爱吃东西"%self.name)
        self.weight+=1
    def run(self):
        print("%s爱锻炼"%self.name)
        self.weight-=0.5
if __name__ == '__main__':
    person1=Person('fangfang',53)
    person1.eat()
    person1.run()
    print(person1)

