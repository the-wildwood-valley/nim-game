import random

from nim.participant import Participant


class Player(Participant):
    def __init__(self, name):
        super().__init__("选手", name)
        self.guess = -1
        self.take = -1

    def guess_maximum_take(self):
        self.guess = random.randint(2, 7)

    def take_stones(self, maximum_take, remaining_stones):
        self.take = random.randint(1, min(maximum_take, remaining_stones))

    def run(self):
        if self.game.phase == "guessing":
            self.guess_maximum_take()
            self.talk(f"猜测取子上限为 {self.guess}。")
        elif self.game.phase == "playing":
            self.take_stones(self.game.maximum_take, self.game.total_stones)
            self.talk(f"取走 {self.take} 个棋子。")
            self.game.total_stones -= self.take
