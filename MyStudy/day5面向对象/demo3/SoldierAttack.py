class Soldier:
    def __init__(self,name):
        self.name= name
        self.gun= None

    def __str__(self):
        return ("士兵的名字是：%s\n拥有的枪支是：%s\n"%(self.name,self.gun))

    def Fire(self):
        if self.gun is None:
            print("%s还没有枪"%self.name)
            return
        print("拥有枪支:%s"%gun.type)
        self.gun.FillBullet(8)
        self.gun.FireBullet()

class Gun:
    def __init__(self,type):
        self.type=type
        self.bullet=0

    def __str__(self):
        return '[枪的型号是：%s，剩余%d颗子弹]'%(self.type,self.bullet)

    def FireBullet(self):
        if self.bullet <=0:
            print("%s没有子弹了，无法发射，请填充子弹")
            return
        self.bullet-=1
        print("发射成功")
    def FillBullet(self,count):
        self.bullet+=count
        print("子弹装填成功！")

if __name__ == '__main__':
    # 定义枪和士兵
    gun=Gun("AK47")
    soldier = Soldier("许三多")
    soldier.gun=gun
    soldier.Fire()
