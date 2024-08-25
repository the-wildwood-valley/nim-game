import random

from nim.player import Player


class Randy(Player):
    def __init__(self):
        super().__init__('Randy')

    def guess_maximum_take(self):
        self.guess = random.randint(2, 7)

    def take_stones(self, maximum_take, remaining_stones):
        self.took = random.randint(1, min(maximum_take, remaining_stones))
