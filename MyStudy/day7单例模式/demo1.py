class Player(object):
    # 重写 new,分配空间
    def __new__(cls, *args, **kwargs):
        print("创建对象，分配空间")
        return super().__new__(cls)
    def __init__(self):
        print("初始化对象")

player = Player()