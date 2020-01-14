class MyHouse:
    def __init__(self,layout,total_area):
        self.layout=layout
        self.total_area=total_area
        self.surplus_area=total_area
        self.furniture_namelist=[]
    def __str__(self):
        return ("房子的户型是%s\n总面积是%.2f\n剩余面积是%.2f\n家具名称列表:%s\n"
        %(self.layout,self.total_area,self.surplus_area,self.furniture_namelist))

    def add_furniture(self,furniture_list):
        for furniture in furniture_list:
            if self.surplus_area<furniture.area:
                print("面积太大了，无法添加%s"%furniture.name)
                return
            self.furniture_namelist.append(furniture.name)
            self.surplus_area -= furniture.area

class MyFurniture:
    def __init__(self,name,area):
        self.name=name
        self.area=area
    def __str__(self):
        return '[%s占地面积%.2f]'%(self.name,self.area)

if __name__ == '__main__':
    # 定义房子和家具
    house = MyHouse("南北通透", 100)
    furniture_list = [MyFurniture("沙发(bed)", 6),MyFurniture("席梦思(bed)", 4),
                      MyFurniture("衣柜(chest)", 4),MyFurniture("书桌(chest)", 91)]
    # 摆放家具
    house.add_furniture(furniture_list)
    print(house)