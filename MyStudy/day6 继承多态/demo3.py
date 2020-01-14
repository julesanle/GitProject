class A:
    def __init__(self):
        self.num1=100
        self.__num2=200
    def method1(self):
        print("方法1,num1:%s,num2:%s"%(self.num1,self.__num2))
    def __method2(self):
        print("方法1,num1:%s,num2:%s"%(self.num1,self.__num2))

class B(A):
   def demo(self):
       print("方法1,num1:%s,num2:%s" % (self.num1, self.__num2))


# test1=A()
# test1.method1()
# test1.__method2()

test2=B()
print(test2.num1)
# print(test2.__num2)
# test2.demo()
test2.method1()