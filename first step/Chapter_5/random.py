import random

# ランダムな1桁の数を表示する
# coding:utf-8

import random

a = random.randint(0,9)
print(a)

# 文字入力をする
# coding:utf-8

b = input("数を入れてね>")
print(b)

# 当たりかどうか判定する
if a == b:
    print("当たり")
else:
    print("はずれ")


# 1桁の数当てゲーム「完成形」
# coding:utf-8

import random

a = random.randint(0,9)
print(a)

# b = input("数を入れてね＞") 　【　関数の型を文字列から整数に変更する為、この行を記述を下記に変更　】
b = int(input("数を入れてね＞"))
if a == b:
    print("当たり")
else:
    print("はずれ")


