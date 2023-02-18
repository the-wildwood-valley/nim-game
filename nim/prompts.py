"""
    基本词汇（Basic Vocabularies）

    1. 选手（Player）
    2. 棋盘（Board）
    3. 棋子（Piece）
    4. 落子（Move）
    5. 胜利（Win）
    6. 失败（Lose）
    7. 平局（Draw）
    8. 比赛（Game）
    9. 比赛规则（Game Rules）
    10. 棋盘局面（Board State）
    13. 当前进展（Current Progress）
    14. 思考（Thought）
    15. 交流（Talk）
    16. 下一轮（Next Turn）
    16. 上一轮（Previous Turn）
"""


def progress(player, rival, experience, current_board, current_turn, thought, talks):
    return f"""
--------------------------
经过那么多年的磨炼，{player}已经成为了一名聪明的选手。
多年的经验告诉{player}，在比赛中最重要的是：{experience}

这一次比赛，{player}的对手是{rival}。

{current_turn}

当前的棋盘局面
{current_board}

{player}想：{thought}

选手的比赛又推进了一轮
{talks}
--------------------------
请扼要总结上文，把重要事项、重要规则和进展步骤作简明记录
--------------------------

""", "turns"


def retrieval(turns, analysis):
    return f"""
--------------------------
根据以下逐条的进展
--------------------------
{turns}
--------------------------
沿着如下思考方向
--------------------------
{analysis}
--------------------------
提取摘要
--------------------------

""", "turn"


def analysis(turn, current_board, player, thought, current_turn):
    return f"""
--------------------------
补全下文{player}的思考，注意{player}称呼自己为"我"。
--------------------------
{turn}

{player}原本想：{thought}

选手的比赛又推进了一轮
{current_turn}

当前的棋盘局面呈现
{current_board}

{player}该如何应对这个局面呢？

{player}分析道：
""", "analysis"


def play(current_turn, current_board, player, thought, last_analysis, talks):
    return f"""
{current_turn}

{player}原本想：{last_analysis}

选手的比赛又推进了一轮
{talks}

当前的棋盘局面呈现
{current_board}

{player}很快就理解了局面。
{player}想：{analysis}

{player}说：
""", "action"


def learn(player, rival, winner, success_or_failure, experience, game_record):
    return f"""
经过那么多年的磨炼，{player}已经成为了一名成熟的选手。
多年的经验告诉{player}，在比赛中最重要的是：{experience}

这一次比赛，{player}的对手是{rival}，取胜者是{winner}。

回顾整个比赛过程
{game_record}

{player}决定简明扼要的写一小段话，总结新的{success_or_failure}经验。
{player}写道:

""", "experience"
