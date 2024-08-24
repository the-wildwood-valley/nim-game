
class Participant:
    def __init__(self, role, name):
        self.game = None
        self.role = role
        self.name = name

    def enter_game(self, game):
        self.game = game

    def talk(self, content):
        print(f"【{self.role} {self.name}】：{content}")
