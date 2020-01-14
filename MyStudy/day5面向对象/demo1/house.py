from MyStudy.day5面向对象.demo1.furniture import MyFurniture

class MyHouse:

    def __init__(self,layout,total_area):
        self.layout=layout
        self.total_area=total_area
    def __str__(self):
        return ("房子的户型是%s,总面积是%f,剩余面积是%s,家具名称列表:%s"%(self.layout,
                                                  self.total_area,surplus_area,furniture_namelist))
    def addFurniture(self,furniture_list,surplus_area):
        furniture_namelist=[]
        for furniture in furniture_list:
            furniture_namelist.append(furniture.name)
            surplus_area-=furniture.area
        return furniture_namelist,surplus_area

if __name__ == '__main__':
    # 定义房子和家具
    house=MyHouse("南北通透",100)
    surplus_area=house.total_area
    furniture_list=[MyFurniture("席梦思(bed)", 4),MyFurniture("衣柜(chest)", 2),MyFurniture("衣柜(chest)", 2)]
    # 摆放家具
    furniture_namelist,surplus_area =house.addFurniture(furniture_list,surplus_area)
    print(house)






