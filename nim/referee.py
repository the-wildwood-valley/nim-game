import random


class Referee:
    def __init__(self):
        self.game = None
        self.total_stones = random.randint(10, 30)
        self.maximum_take = random.randint(2, 7)
        self.is_guessing_over = False
        self.is_game_over = False
        self.guess_first_result = None
        self.game_result = None

    def enter_game(self, game):
        self.game = game
        self.total_stones = random.randint(10, 30)
        self.game.set_total_stones(self.total_stones)

    def introduce(self):
        print("欢迎来到 Nim 游戏！")
        print(f"两位参赛选手，左侧是 {self.game.player_left.name}， 右侧是 {self.game.player_right.name}")
        print(f"本次比赛共有 {self.total_stones} 个棋子。")

    def init_game(self):
        # 初始化游戏，可能包括一些前置工作
        print("正在初始化游戏...")

    def decalre_guessing_start(self):
        print("猜测取子上限的环节开始！")

    def run(self):
        # 裁判执行操作，例如宣布阶段结果
        pass

    def evaluate_guess(self, player_guess):
        if player_guess == self.maximum_take:
            return True
        return False

    def decalre_guessing_result(self):
        if self.guess_first_result:
            if self.guess_first_result == "LEFT":
                print(f"左侧选手 {self.game.player_left.name} 猜先成功！")
            else:
                print(f"右侧选手 {self.game.player_right.name} 猜先成功！")
        else:
            print("无人猜中，游戏结束。")
            self.is_game_over = True

    def decalre_game_start(self):
        if not self.is_game_over:
            print("游戏现在开始！")
        else:
            print("由于猜先环节失败，游戏结束。")

    def check_game_over(self, remaining_stones):
        if remaining_stones == 0:
            self.is_game_over = True

    def declare_winner(self, winner):
        if winner == "LEFT":
            self.game_result = "LEFT"
            print(f"左边的选手 {self.game.player_left.name} 获胜！")
        elif winner == "RIGHT":
            self.game_result = "RIGHT"
            print(f"右边的选手 {self.game.player_right.name} 获胜！")
        else:
            self.game_result = None
