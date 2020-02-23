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

# class Point:
#     def __init__(self, x = 0.0, y = 0.0):
#         self.x = x
#         self.y = y
#         # print(self.x)
#         # print(self.y)



import random

class Buttons:
    def __init__(self, random):
        self.x = random
        print(self.x)

a, b, c, d, e, f, g, h, i  = 1, 2, 3, 4, 5, 6, 7, 8, 9

for Button1 in (a, b, c, d, e, f, g, h, i):
    pass
Button1 = random.randint(a, i)
# print(Button1)

print('===================================')

Buttons(Button1)
