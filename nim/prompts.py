def progress(situation, board, player, thought, talks):
    return f"""
--------------------------
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


def retrieval(steps, query):
    return f"""
--------------------------
逐条进展
--------------------------
{situations}
--------------------------
查询
--------------------------
{query}
--------------------------
结果
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

{player}应该怎么应对这个局面呢？

{player}分析道：
""", "analysis"


def act(situation, board, player, thought, analysis, talks):
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
