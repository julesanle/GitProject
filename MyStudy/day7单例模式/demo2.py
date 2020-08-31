class Player(object):
    instance = None
    init_flag = False
    # 重写 new,分配空间
    def __new__(cls, *args, **kwargs):
        if Player.instance is None:
            print("创建对象，分配空间")
            Player.instance = super().__new__(cls)
        return Player.instance
    def __init__(self):
        if Player.init_flag is True:
            return
        Player.init_flag = True
        print("初始化对象")

player1 = Player()
player2 = Player()
print(player1)
print(player2)