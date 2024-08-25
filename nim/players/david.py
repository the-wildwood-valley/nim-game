"""
我是 Carole，一个有快速学习能力的 Nim 选手。我知道这个比赛的精髓在于，要在猜先阶段尽可能获得先手地位，而在比赛阶段要尽可能获得优势地位。

我有若干的经验总结于下：

1. 在猜先阶段总要猜对手和自己之前没猜过的数，这样才能容易获得先手地位。

"""

from nim.player import Player
from nim.util import extract_last_number, extract_last_paragraph


class David(Player):
    def __init__(self):
        super().__init__('David')
        self.strategy = __doc__

    def guess_maximum_take(self):
        context = ''
        for entry in self.game.history:
            context += f'{entry["role"]}：{entry["content"]}\n'
        question = '我应该猜测取子上限为多少？'
        self.ask(context, question)
        self.think(self.strategy)
        answer = self.answer()
        self.guess = int(extract_last_number(answer))

    def take_stones(self, maximum_take, remaining_stones):
        context = ''
        for entry in self.game.history:
            context += f'{entry["role"]}：{entry["content"]}\n'
        question = '我应该从棋面上取几个棋子？'
        self.ask(context, question)
        self.think(self.strategy)
        answer = self.answer()
        self.took = int(extract_last_number(answer))

    def learn(self):
        context = ''
        for entry in self.history:
            context += f'{entry["role"]}：{entry["content"]}\n'

        question = '我胜利或失败的原因是什么？'
        self.ask(context, question)
        answer = self.answer('最后一段', '结论')
        conculsion = extract_last_paragraph(answer)

        context = f'{context}\n\n{question}\n\n{conculsion}'
        question = '我调整后的策略应该是什么？'
        self.ask(context, question)
        answer = self.answer('本文', '策略全文')
        self.strategy = '\n\n'.join(answer.split('\n\n')[1:])
