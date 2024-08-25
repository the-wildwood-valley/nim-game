import random

from nim.participant import Participant


class Player(Participant):
    def __init__(self, name):
        super().__init__("选手", name)
        self.guess = -1
        self.took = -1

    def guess_maximum_take(self):
        raise NotImplementedError

    def take_stones(self, maximum_take, remaining_stones):
        raise NotImplementedError

    def run(self):
        if self.game.phase == "guessing":
            self.guess_maximum_take()
            self.talk(f"猜测取子上限为 {self.guess}。")
        elif self.game.phase == "playing":
            self.take_stones(self.game.maximum_take, self.game.total_stones)
            self.game.last_took = self.took
            self.take(f"{self.took} 个棋子。")
            self.game.total_stones -= self.took
