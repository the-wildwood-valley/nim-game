# Path: nim/config.py
"""
Nim 游戏配置文件
"""

game_config = {
    "name": "Nim",
    "version": "0.1",
    "author": "Mike",
    "description": "Nim 游戏",
    "max_tokens": 1024,
    "temperature": 0.7,
    "top_p": 1,
    "stop": ["\n", "。", "！", "？", "……"],
    "max_turns": 10,
}