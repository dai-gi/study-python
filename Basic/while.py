# いちばんやさしいPython入門教室
# while構文
"""
while 条件式:
    条件が成り立っている場合に実行したい文
"""

total = 0
a = 1
while total <= 50:
    total = total + a
    a = a + 1
print(total)
print('-----------')


a = 1
while a <= 5:
    print(a)
    a = a + 1
print('-----------')

# 永久に繰り返したい場合
"""
＊何か事が起きるまでまつという場面で使われることがある

while True:
    実行したい文

Trueと指定しておくと、いかなるときでも条件が成り立つ
(止めたい場合は、win：ctrl + c  mac：control + c)

"""

# else
"""
＊最後に一回だけ実行したい処理を書きたいときに使う
ver = 0
while 条件式:
    繰り返す文
else:
    繰り返しが終わったときに実行する文
"""

# break
"""
＊途中で処理を止めたいときに使う
ver = 0
while 条件式:
    繰り返す文
    if 条件式:
        break
"""

# continue
"""
＊特定の処理だけスキップしたいときに使う
ver = 0
while 条件式:
    if 条件式:
        continue
    繰り返す文
"""