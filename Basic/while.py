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

# for構文と同じ処理ををwhileで記述する
for a in range(1,5+1):
    print(a)
print('-----------')
a = 1
while a <= 5:
    print(a)
    a = a + 1

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

while 条件式:
    繰り返す文
else:
    繰り返しが終わったときに実行する文
"""