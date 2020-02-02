# while構文
# coding:utf-8
total = 0
a = 1
while total <= 50:
    total = total + a
    a = a + 1
print(total)

# for構文と同じ処理ををwhileで記述する
# coding:utf-8
for a in range(1,5+1):
    print(a)

a = 1
while a <= 5:
    print(a)
    a = a + 1

for i in range( 1 , 5 + 1 ):
    print(i)
else:
    print("この処理を終了する")


# 条件分岐する　if構文
# coding:utf-8
for i in range(1,10+1):
    if i <= 5:
        print("小さいです")
    else:
        print("大きいです")
