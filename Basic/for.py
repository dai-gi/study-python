# いちばんやさしいPython入門教室
# for構文：P82
"""
記述方法：
for 変数 in シーケンス:
    処理内容

シーケンスとは：
順序立てているものの意味
例）リスト等...
"""

for a in[1,2,3,4,5]:
    print(a)
# 1
# 2
# 3
# 4
# 5

for b in[1,100]:
    print(b)
# 1
# 100

for i in range(1,100+1):
    print(i)
    print("こんにちは")
# 1
# こんにちは
# 2
# こんにちは
# ...100まで同じように表示される

for i in "Hello":
    print(i)
# H
# e
# l
# l
# o

# else
"""
＊最後に一回だけ実行したい処理を書きたいときに使う

for i in シーケンス:
    print(i)
else:
    繰り返しが終わったときに実行する文
"""

# break
"""
＊途中で処理を止めたいときに使う

for i in シーケンス:
    print(i)
    if 条件式:
        break
"""

# continue
"""
＊特定の処理だけスキップしたいときに使う

for i in シーケンス:
    if 条件式:
        continue
    print(i)
"""