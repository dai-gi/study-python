# 条件分岐する　if構文

# coding:utf-8
for i in range(1,10+1):
    if i <= 5:
        print("小さいです")
    else:
        print("大きいです")

# 条件を組み合わせる

# coding:utf-8
for i in range(1,10+1):
    print(i)
    if i % 2 == 0:
        print("○")
    if i % 3 == 0:
        print("×")
    if (i % 2 == 0) and (i % 3 == 0):
        print("△")

"""

Pythonには、「倍数かどうか」を調べる命令は存在しません。しかし、それと同じ意味に
なるように「割ったときに、余りが０かどうか」と考え、Pythonでできる書き方に変更する
ことで、プログラミングができるようになります。
プログラミングするときには、「プログラムとして表現できる、同じ意味での考え方の置き
換え」は日常茶飯事で、いわば、「頭をちょっとひねる」が必要になってきます。

"""

# elifを使って「でないときの条件」を並べる
# ifとelseだけの場合

# coding:utf-8
for a in range(1,36+1):
    print(a)
    if (a % 12 == 0):
        print("○")
    else:
        if (a % 4 == 0):
            print("△")
        else:
            if (a % 2 == 0):
                print("×")
            else:
                print("☆")

# elifを使った場合

# 下記の記述は教材に記載されていたプログラム
# coding:utf-8
for i in range(1,36+1):
    print(i)
    if(i % 12 == 0):
        print("○")
    elif(i % 4 == 0):
        print("△")
    elif if(i % 2 == 0): #この行のifが原因でエラーが起きる
        print("×")
    else:
        print("☆")

# 下記の記述は上記記述の2個目のifを消したらエラーが起きなかった
# coding:utf-8
for i in range(1,36+1):
    print(i)
    if(i % 12 == 0):
        print("○")
    elif(i % 4 == 0):
        print("△")
    elif(i % 2 == 0): # ifを消した箇所
        print("×")
    else:
        print("☆")

# 条件が成り立ったときに繰り返しをやめる
# 永遠に繰り返すを「break」を使って止める

# coding:utf-8
total = 0
a = 1
while True:
    total = total + a
    a = a + 1
    if total > 50:
        break
print(total)

# Pythonには「何もしない文」が用意されている

# coding:utf-8
total = 0
a = 0
while total <= 50:
    total = total + a
    a = a + 1
    if total <= 50:
        pass
    else:　# elseを記入するとエラーが出る





