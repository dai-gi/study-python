# いちばんやさしいPython入門教室
# 関数を定義
def tashizan(a, b):
    total = 0
    for i in range(a, b + 1):
        total = total + i
    return total
result = tashizan(1, 2)
print(result)
print('-----------')

# スコープを理解
# test関数内で、変数aに再代入することはできない
a = "abc" # <- グローバル変数(グローバルスコープ)
def test():
    a = 1 # <- ローカル変数(ローカルスコープ)　＊関数ないで新しい変数aを生成することになる
    print(a)
    return

test()
print(a)

# 関数からグローバルスコープにアクセスする
a = "abc"

def test():
    global a # グローバル変数にアクセスする場合は、「global」と宣言する必要がある
    global a = "def"
    return a

test()
print(a)