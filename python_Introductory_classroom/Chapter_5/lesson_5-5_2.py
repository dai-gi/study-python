# 数当てゲームプログラムの完成形

# 　coding:utf-8
import random
# コンピュータが考えた4桁のランダムの数値
a =[random.randint(0,9),
    random.randint(0,9),
    random.randint(0,9),
    random.randint(0,9)]
# テストの為の答えを表示
print(str(a[0]) + str(a[1]) + str(a[2]) + str(a[3]))
# 4桁の数字かどうかを判定する
while True:
    
    isok = False
    while isok == False:
        