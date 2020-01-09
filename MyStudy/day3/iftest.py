import random

for i in range(0,5):
        mychoice = int(input("请输入您要出的拳 1-石头 2-剪刀 3-布:"))
        print("我出的拳是%d" % mychoice)
        mycomchoice=random.randint(1,3)
        print("电脑出的拳是:%d"%mycomchoice)
        if ((mychoice==1 and mycomchoice==2)
            or (mychoice==2 and mycomchoice==3)
            or(mychoice == 3 and mycomchoice == 1)):
            print("我赢了")
        elif mychoice==mycomchoice:
            print("咱俩一样")
        else:
            print("电脑赢了")



