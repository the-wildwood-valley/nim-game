"""
欢迎来到 Nim 游戏！

游戏简述：
    棋盘上有 {total} 个棋子，比赛双方轮流取下棋子，每次最多取下的数量不超过自然数 {maximium_take}，谁取到棋盘上最后的棋子，谁获胜。

参赛人员：
    裁判
    选手 {player_left} 和 {palyer_right}

比赛规则：
    1. 裁判和选手 {player_left} 和 {palyer_right} 三人入场，裁判告知选手 {player_left} 和 {palyer_right} 双方的身份。
    2. 裁判随机决定棋盘上棋子的总数 {total}，总数小于三十；随机给出每次取子的数量上限 {maximium_take}，该上限介于二与七之间，包括二与七本身。
    裁判并不公布这两个数量。
    3. 裁判宣布猜先开始，给出猜先规则，从随机选择的一方开始，请选手轮流猜先。选手需要猜测取子上限，裁判判断是否猜对，首先猜对的一方获得先行的权利。
    若无人猜中，则比赛双方都记为猜先失败。裁判宣布猜先结果。猜先失败则比赛终止。
    4. 裁判将 {total} 个棋子置于盘面，并宣布每次取子的数量的上限 {maximium_take}，宣布比赛开始。
    6. 棋手双方轮流取子，每次最多取 {maximium_take} 个棋子，棋手需要公布自己取走的数量，裁判移走相应数量的棋子。比赛过程直到盘面上无子结束，
    取到最后棋子的选手获胜。比赛期间，裁判不得干预比赛过程，棋手如果违反规则，裁判将判负。比赛必须在 {total} 轮次内结束。
    7. 比赛结束后，裁判宣布比赛结果，比赛双方各自获得一定的积分，积分规则如下：
       a：猜先失败者获得 0 分，猜先成功者获得 1 分。
       b：比赛失败者获得 0 分，比赛成功者获得 9 分。
    8. 比赛结束后，裁判宣布比赛结果，比赛双方各自复盘，总结经验。
"""

import random
import time
import sys
import os
import json
import traceback
import logging
import logging.config
import argparse
import importlib
import inspect
import re
import threading
import queue
import time
import copy
import datetime
import collections
import functools
import itertools
import math
import multiprocessing
import random
import socket
import string
import subprocess

from typing import Any, Callable, Dict, List, Optional, Tuple, Union

from nim import config
from nim import utils
from nim import exceptions
from nim import constants
from nim import logger
from nim import player
from nim import referee

__all__ = [
    "Game",
]

class Game:
    def __init__(self, player_left: player.Player, player_right: player.Player, referee: referee.Referee):
        self.player_left = player_left
        self.player_right = player_right
        self.referee = referee

    def run(self):
        self.referee.run()

        while True:
            self.player_left.run()
            self.referee.run()
            if self.referee.is_guessing_over:
                break
            self.player_right.run()
            self.referee.run()
            if self.referee.is_guessing_over:
                break

        if self.referee.guess_first_result == constants.GuessFirstResult.LEFT:
            self.player_left.guess_first = True
            self.player_right.guess_first = False
        elif self.referee.guess_first_result == constants.GuessFirstResult.RIGHT:
            self.player_left.guess_first = False
            self.player_right.guess_first = True
        else:
            self.player_left.guess_first = False
            self.player_right.guess_first = False
            self.referee.is_game_over = True

        while not self.referee.is_game_over:
            self.player_left.run()
            self.referee.run()
            if self.referee.is_game_over:
                break
            self.player_right.run()
            self.referee.run()
            if self.referee.is_game_over:
                break

        if self.referee.game_result == constants.GameResult.LEFT:
            self.player_left.win = True
            self.player_right.win = False
        elif self.referee.game_result == constants.GameResult.RIGHT:
            self.player_left.win = False
            self.player_right.win = True
        else:
            self.player_left.win = False
            self.player_right.win = False

        self.player_left.run()
        self.player_right.run()
