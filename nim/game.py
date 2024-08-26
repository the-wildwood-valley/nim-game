"""
欢迎来到 Nim 游戏！

规则简述：
    棋盘上有若干个棋子，比赛双方轮流取下棋子，每次最多取下的数量不超过给定的数量上限，谁取到棋盘上最后的棋子谁获胜。

参赛人员：
    裁判
    左侧选手
    右侧选手

比赛规则：
    1. 裁判和左侧选手和右侧选手三人入场，裁判告知选手双方的身份。
    2. 裁判随机决定棋盘上棋子的总数，总数小于30；随机给出每次取子的数量上限，该上限介于2与7之间，包括2与7本身。裁判并不公布这两个数量。
    3. 裁判宣布猜先开始，给出猜先规则，从随机选择的一方开始，请选手轮流猜先。选手需要猜测取子上限，裁判判断是否猜对，首先猜对的一方获得先行权利。
    若无人猜中，则比赛双方都记为猜先失败。裁判宣布猜先结果。猜先失败则比赛终止。
    4. 裁判将给定数量的棋子置于盘面，并宣布每次取子的数量的上限，宣布比赛开始。
    6. 棋手双方轮流取子，每次最少取子一枚，每次最多取子小于或等于给定上限，棋手需要公布自己取走的数量，裁判移走相应数量的棋子。比赛过程直到盘面上无子结束，
    取到最后棋子的选手获胜。比赛期间，裁判不得干预比赛过程，棋手如果违反规则，裁判将判负。
"""

import time

from nim.player import Player
from nim.players.alice import Alice
from nim.players.bob import Bob
from nim.players.carole import Carole
from nim.players.david import David
from nim.players.randy import Randy
from nim.referee import Referee


class Game:
    def __init__(self, player_left: Player, player_right: Player, referee: Referee):
        self.rules = __doc__
        self.phase = "init"  # init -> guessing -> playing -> finished
        self.history = []
        self.participants = []

        self.total_stones = -1
        self.maximum_take = -1
        self.last_took = -1
        self.current_player = None

        self.player_left = player_left
        self.player_right = player_right
        self.referee = referee

        self.player_left.enter_game(self)
        self.player_right.enter_game(self)
        self.referee.enter_game(self)

    def enter_game(self, participant):
        self.participants.append(participant)

    def play(self, participant, action):
        role = f"{participant.role} {participant.name}"
        self.history.append({"role": role, "content": action})
        for p in self.participants:
            if p is not participant:
                p.observed({"role": role, "content": action})

    def run(self):
        while not self.phase == "finished":
            time.sleep(1)
            self.referee.run()
            if self.current_player is not None:
                self.current_player.run()


if __name__ == "__main__":
    import random

    referee = Referee()
    players = [Randy(), Alice(), Bob(), Carole(), David()]

    for i in range(20):
        random.shuffle(players)
        player_left = players[0]
        player_right = players[1]
        game = Game(player_left, player_right, referee)
        game.run()
        player_left.learn()
        player_right.learn()
