import random
class Game:
    top_score=50
    @classmethod
    def shou_history_store(cls):
        print("历史最高分是：%d"%Game.top_score)
    @staticmethod
    def show_help():
        print("帮助信息：请下载最新版再开始游戏，下载和游戏操作方法请参照引导信息------")
    def __init__(self,name):
        self.name=name
        # 默认得分0
        self.score=0
    def start_play(self):
        print("当前玩家：%s"%self.name)
        self.score=random.randint(0,100)
        print("当前得分是：%d"%self.score)
        # 当前得分>历史得分，历史最高得分刷新
        if self.score>Game.top_score:
            Game.top_score=self.score
game1 = Game("xiaoming")
game1.show_help()
# 未开始前最高历史得分
game1.shou_history_store()
game1.start_play()
# 玩完一局后最高历史得分
game1.shou_history_store()

