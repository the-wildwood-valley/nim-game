import re

from nim.player import Player


def extract_last_number(text):
    # 使用正则表达式来查找所有的数字段
    matches = re.findall(r'\d+', text)
    if matches:
        return matches[-1]  # 返回最后一个匹配的数字段
    else:
        return None


class Bob(Player):
    def __init__(self):
        super().__init__('Bob')

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
