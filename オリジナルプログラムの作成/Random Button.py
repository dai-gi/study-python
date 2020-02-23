# ランダムに1桁の整数を選ぶプログラム
# coding:utf-8

import random

# classで「Buttons関数」を作成
class Buttons:
    def __init__(self, random):
        self.x = random
        print(self.x)

# 9個の変数に整数を
a, b, c, d, e, f, g, h, i  = 1, 2, 3, 4, 5, 6, 7, 8, 9

for Button1 in (a, b, c, d, e, f, g, h, i):
    pass
Button1 = random.randint(a, i)
# print(Button1)

print('===================================')

Buttons(Button1)
