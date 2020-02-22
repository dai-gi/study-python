# ランダムに1桁の整数を選ぶプログラム
# coding:utf-8
# import random

# a, b, c, d, e, f, g, h, i  = 1, 2, 3, 4, 5, 6, 7, 8, 9
# Button1 = []

# for Button1 in (a, b, c, d, e, f, g, h, i):
#     print(Button1)

# print('===================================================')
# random.randint(a, i)
# Button1 = random.randint(a, i)

# print(Button1)


# クラスを使って9個のボタンを作成する
import random
class NineButtons:
    def __init__(self, a, b, c, d, e, f, g, h, i):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g = g
        self.h = h
        self.i = i

    def Button1(self):
        

