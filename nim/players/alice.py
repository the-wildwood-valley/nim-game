from nim.player import Player
from nim.util import extract_last_number, extract_last_paragraph


class Alice(Player):
    def __init__(self):
        super().__init__('Alice')

    def guess_maximum_take(self):
        context = ''
        for entry in self.game.history:
            context += f'{entry["role"]}：{entry["content"]}\n'
        question = '我应该猜测取子上限为多少？'
        self.ask(context, question)
        answer = self.answer()
        self.guess = int(extract_last_number(answer))

    def take_stones(self, maximum_take, remaining_stones):
        context = ''
        for entry in self.game.history:
            context += f'{entry["role"]}：{entry["content"]}\n'
        question = '我应该从棋面上取几个棋子？'
        self.ask(context, question)
        answer = self.answer()
        self.took = int(extract_last_number(answer))
