import random


class Player:
    def __init__(self, name):
        self.name = name
        self.game = None
        self.guess_first = False
        self.win = False

    def enter_game(self, game):
        self.game = game

    def guess_maximum_take(self):
        # 玩家猜测每次取子上限的逻辑
        return random.randint(2, 7)

    def take_stones(self, maximum_take, remaining_stones):
        # 玩家取子的逻辑
        return random.randint(1, min(maximum_take, remaining_stones))

    def run(self):
        # 玩家执行操作
        print(f"{self.name} 正在思考...")
