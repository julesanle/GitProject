class Person:
    def __init__(self,name,weight):
        self.name=name
        self.weight=weight
    def eat(self):
        print("%s吃东西前的体重%.2f" % (self.name,self.weight))
        self.weight+=1
        print("%s吃东西后的体重%.2f" % (self.name,self.weight))
    def run(self):
        print('%s跑步前的体重是%.2f' % (self.name, self.weight))
        self.weight-=0.5
        print('%s跑步后的体重是%.2f'%(self.name,self.weight))
if __name__ == '__main__':
    person1=Person('fangfang',53)
    person1.eat()
    person1.run()


