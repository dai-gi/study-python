# いちばんやさしいPython入門教室
# if構文
for i in range(1,10+1):
    if i <= 5:
        print("小さいです")
    else:
        print("大きいです")
print('-----------')

# 複数の条件を組み合わせる
for i in range(1,10+1):
    print(i)
    if i % 2 == 0:
        print("x")
    if i % 3 == 0:
        print("y")
    if (i % 2 == 0) and (i % 3 == 0):
        print("z")
print('-----------')

# elif
for i in range(1,36+1):
    print(i)
    if(i % 12 == 0):
        print("a")
    elif(i % 4 == 0):
        print("b")
    elif(i % 2 == 0):
        print("c")
    else:
        print("d")