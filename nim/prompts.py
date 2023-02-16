def progress(player, rival, board, experience, situation, thought, talks):
    return f"""
--------------------------
经过那么多年的磨炼，{player}已经成为了一名聪明的选手。
多年的经验告诉{player}，在比赛中最重要的是：{experience}

这一次比赛，{player}的对手是{rival}。

{situation}

当前的棋盘局面
{board}

{player}想：{thought}

选手的比赛又推进了一轮
{talks}
--------------------------
请扼要总结上文，把重要事项、重要规则和进展步骤作简明记录
--------------------------

""", "situations"


def retrieval(situations, analysis):
    return f"""
--------------------------
根据以下逐条的进展
--------------------------
{situations}
--------------------------
沿着如下思考方向
--------------------------
{analysis}
--------------------------
提取摘要
--------------------------

""", "situation"


def analysis(situation, board, player, thought, talks):
    return f"""
--------------------------
补全下文{player}的思考，注意{player}称呼自己为"我"。
--------------------------
{situation}

{player}原本想：{thought}

选手的比赛又推进了一轮
{talks}

当前的棋盘局面呈现
{board}

{player}该如何应对这个局面呢？

{player}分析道：
""", "analysis"


def play(situation, board, player, thought, analysis, talks):
    return f"""
{situation}

{player}原本想：{thought}

选手的比赛又推进了一轮
{talks}

当前的棋盘局面呈现
{board}

{player}很快就理解了局面。
{player}想：{analysis}

{player}说：
""", "action"


def learn(player, rival, winner, success_or_failure, experience, situations):
    return f"""
经过那么多年的磨炼，{player}已经成为了一名成熟的选手。
多年的经验告诉{player}，在比赛中最重要的是：{experience}

这一次比赛，{player}的对手是{rival}，取胜者是{winner}。

回顾整个比赛过程
{situations}

{player}决定简明扼要的写一小段话，总结新的{success_or_failure}经验。
{player}写道:

""", "experience"
