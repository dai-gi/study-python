# イテラブル（リストなどのオブジェクト）の全てに対して、map関数の第一引数で指定した関数を適用させることができる。
li = [1, 2, 3, 4, 5]
print(type(li[0])) # <class 'int'>

# リスト内の要素を全て文字列に変換する。
# 変数　= list(map(関数, イテラブル))
li_str = list(map(str, li))
print(type(li_str[0])) # <class 'str'>

# リスト関数を使わなかった場合、エラーになってしまう。
li_str = map(str, li)
print(type(li_str[0])) # TypeError: 'map' object is not subscriptable

# type関数を使わずに li_str を出力した場合
print(li_str) # <map object at 0x7ff4320c5410>