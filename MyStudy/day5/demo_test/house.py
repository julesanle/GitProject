from MyStudy.day5.demo_test.furniture import MyFurniture

class MyHouse:

    def __init__(self,layout,total_area):
        self.layout=layout
        self.total_area=total_area
    def __str__(self,total_area,):
        print("房子的户型是%s,总面积是%s,剩余面积是%s,家具名称列表%s"%(self.layout,
                                                  self.total_area,surplus_area,str(furniture_list)))
    def addFurniture(self,furniture,):
        self.furniture_name=furniture.name
        total_area-furniture.area

if __name__ == '__main__':
    # 定义房子和家具
    house=MyHouse("南北通透",100)
    furniture_list=MyFurniture("席梦思(bed)", 4), MyFurniture("衣柜(chest)", 2), MyFurniture("衣柜(chest)", 2)
    # 摆放家具
    house.addFurniture(furniture_list[0])
    print(house)






