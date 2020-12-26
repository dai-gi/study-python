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


# Python-izm｜関数・メソッド

# 関数
def test_func1():
    print('call test_func1')

test_func1() # call test_func1
print('-----------')


# 引数の基礎
def test_func2(num_1, num_2, oprn):

    if oprn == 1:
        print('足し算開始')
        print(num_1 + num_2)

    elif oprn == 2:
        print('引き算開始')
        print(num_1 - num_2)

    elif oprn == 3:
        print('掛け算開始')
        print(num_1 * num_2)

    elif oprn == 4:
        print('割り算開始')
        print(num_1 / num_2)

    else:
        print('不明なオペレーション指定です')
        
test_func2(100, 10, 3)

"""""""""""""""""
出力結果：

掛け算開始
1000

"""""""""""""""""
print('-----------')


# 引数の初期値
def test_func3(num_1, num_2, oprn=1):

    if oprn == 1:
        print('足し算開始')
        print(num_1 + num_2)

    elif oprn == 2:
        print('引き算開始')
        print(num_1 - num_2)

    elif oprn == 3:
        print('掛け算開始')
        print(num_1 * num_2)

    elif oprn == 4:
        print('割り算開始')
        print(num_1 / num_2)

    else:
        print('不明なオペレーション指定です')
        
print('第三引数に値を渡さない場合')
test_func3(100, 10)
print('')
print('値を渡した場合')
test_func3(100, 10, 4)

"""""""""""""""""
出力結果：

第三引数に値を渡さない場合
足し算開始
110

値を渡した場合
割り算開始
10.0

"""""""""""""""""
print('-----------')


# 関数とメソッド
# モジュール内に「def」で定義されているものが関数
# クラス内に「def」で定義されているものがメソッド

def test_func():
    print('call test_func')

class TestClass:
    # メソッド
    def test_method():
        print('call test_method')

test_func() # call test_func
TestClass.test_method() # call test_method
print('')

print('型を確認')
print(type(test_func)) # <class 'function'>
print(type(TestClass.test_method)) # <class 'function'>
print('')

t = TestClass() # <- 変数にクラスを代入 = インスタンス化
print(type(t.test_method)) # <class 'method'>

