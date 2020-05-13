# URL:https://www.headboost.jp/python-scope-global-local-variables/

# スコープとは
# スコープ = 変数の有効範囲

"""
・pythonで変数を作成 → ネームスペースに保管される
・コードの中の何処で作られたかによって有効範囲（スコープ）が変わってくる
"""

v = 25
def printer():
    v = 50
    return v

print(v)
# 25

printer()
# 50

# pythonの4つのスコープ（LEGBルール）

"""
Local（ローカル変数）
・関数（defやlambda）に代入された変数で、グローバルに宣言されていないもの
"""
"""
Enclosign Local（エンクロージング関数ローカル変数）
・内側から外側までの、あらゆるエンクロージング関数（defやlambda）の変数名
・def文やlambda文などのブロックの中で、定義された変数は『ローカル変数』と言って、その関数の中だけで機能する
"""
number = lambda x:5
# print(x)
number(x)


"""
Global（グローバル変数）
・ファイルのトップレベルに代入された変数名で、ファイルの中でグローバルに宣言されている
"""

"""
Built-in（組み込み関数の変数名）
・組み込み関数に予め代入されている変数名。print,rangeなど
"""
