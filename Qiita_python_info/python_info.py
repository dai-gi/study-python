# URL:https://qiita.com/nokonoko_1203/items/10402b31438daaa939e7

# pythonは動的型付け＝(自動で型を勝手に決めてくれる)言語
"""
静的型付けのメリット
・型判別がコード上ですでに終わっている為、動作が早い
・型がある事で原因不明のバグ発生の確率が下がる
・型が自白である為、動作を推測しやすい
"""

# 型ヒント
"""
IDEを利用してコードを書くときに、肩が違う変数を引数に
とったりしたときに警告してくれる
"""
a = 1
def hello(name: str) -> str:
    return f"Hello {name}"
print(hello(a))
print(type(a))
"""
注意点
・あくまで型ヒントな為、コンパイルエラーにならずに実行できてしまう
"""



# Docstring
# ダブルクォーテーション3つで囲まれた文字列をdocstringと呼ぶ
# コードにドキュメントを埋め込むことができる
"""
ダブルクォーテーション３つで囲んだ文字列を関数・クラス・モジュールに
埋め込むことで特殊メソッド__doc__に文字列が格納される
"""
# help()を使えばドキュメントを参照できる
def hello(name):
    """引数に入れた人に挨拶します"""
    return f"Hello {name}"
"""
追記
・sphinxを使えばドキュメントを自動で作成してくれる
・docstringには色々な記法がある
"""



# f-string
name = "nokonoko"
age = 5
# python3.7
# 1つ目
print("{}は{}歳です".format(name, age))
# 2つ目
print("%sは%s歳です" % (name, age))
# 3つ目
print(f"{name}は{age}歳です")

# python3.8
# 変数名＋＝を入れることによって自動で変数名も表示してくれる
# デバッグ時に便利
print(f"{name=}, {age=}")



# セイウチ演算子 = ( := )
# if文などの条件式ないで変数への代入を可能にする機能がある
if name := "nokonoko" == "nokonoko":
    print("イケメンです")
else:
    print("イケメンじゃないですね")
"""
デメリット
・可読性が落ちる
"""



# 内包表記
"""
変数などの値が複数格納されたオブジェクト（＝コンテナオブジェクト）をシンプルに作成する機能
"""
numbers = []
for i in range(10):
    numbers.append(i)
print(numbers)

# 内包表記使用した場合
numbers = [i for i in range(10)]
print(numbers)
# １行で定義できるようになる




