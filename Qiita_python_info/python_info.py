# pythonは動的型付け＝(自動で型を勝手に決めてくれる)言語

# 型ヒント
"""
IDEを利用してコードを書くときに、肩が違う変数を引数に
とったりしたときに警告してくれる
"""
# あくまで型ヒント
# コンパイルエラーになったりせずに実行できてしまう
a = 1
def hello(name: str) -> str:
    return f"Hello {name}"

print(hello(a))
print(type(a))


# Docstring
# """ で囲まれた部分がdocstringと呼ばれる部分
"""
ダブルクォーテーションx３で囲んだ文字列を関数・クラス・モジュールに
埋め込むことで特殊メソッド__doc__に文字列が格納される
"""
# help()やIDEでの参照など、開発が捗る便利機能が使えるようになる
# docstringの記法には色々なスタイルがある
def hello(name):
    """引数に入れた人に挨拶します"""
    return f"Hello {name}"

# help(hello)


# f-string
# 文字列に変数を埋め込む方法は２種類ある
# 1つ目
name = "nokonoko"
age = 5
print("{}は{}歳です".format(name, age))
# 2つ目
print("%sは%s歳です" % (name, age))

# 最新
print(f"{name}は{age}歳です")
print(f"{name=}, {age=}")


# セイウチ演算子 = ( := )
# if文やfor文などの中で変数へ代入が行える機能
if name := "nokonoko" == "nokonoko":
    print("イケメンです")
else:
    print("イケメンじゃないですね")