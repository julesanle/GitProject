class MyFurniture:
    def __init__(self,name,area):
        self.name=name
        self.area=area
    def __str__(self):
        return '[%s占地面积%.2f]'%(self.name,self.area)