# 4桁のランダムな値を作る
# coding:utf-8

import random

# a1 = random.randint(0,9)
# a2 = random.randint(0,9)
# a3 = random.randint(0,9)
# a4 = random.randint(0,9)

# 上記のランダムな数値の変数をリストを使って作りなをす為、上記をコメントアウトした

# 教材通りに記述
a = [random.randint(0, 9),
     random.randint(0, 9),
     random.randint(0, 9),
     random.randint(0, 9)]

print(str(a[0]) + str(a[1]) + str(a[2]) + str(a[3])) #上記変更の為、変数の数値を変更