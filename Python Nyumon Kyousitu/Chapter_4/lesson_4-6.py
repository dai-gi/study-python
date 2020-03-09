# 関数を定義する

# coding:utf-8
def tashizan (a, b ):
    total = 0
    for i in range(a, b + 1):
        total = total + i
    return total

# 関数を利用する

# coding:utf-8
def tashizan(a, b):
    total = 0
    for i in range(a, b + 1):
        total = total + i
    return total

c = tashizan(1, 5)
print(c)

# スコープを理解する

# coding:utf-8

a = "abc"

def test():
    print(a)
    return

test()
print(a)


# グローバルスコープとローカルスコープ
# coding:utf-8

a = "abc"

def test():
    a = "def"
    print(a)
    return

test()
print(a)

# 関数からグローバルスコープにアクセスする
# coding:utf-8

a = "abc"

def test():
    global a
    a = "def"
    print(a)
    return

test()
print(a)