# map関数

"""
構文：
map(関数, イテラブル)

返り値：
<map object at 0x7f94dd4b9510>
mapオブジェクトが返される。

イテラブル（リストなどのオブジェクト）の全てに対して、
map関数の第一引数で指定した関数を適用させることができる。
"""
li1 = [1, 2, 3, 4, 5]
print(type(li1[0])) # <class 'int'>

# リスト内の要素を全て文字列に変換する。
li_str = list(map(str, li1))
print(type(li_str[0])) # <class 'str'>
print('------------------')

# リスト関数を使わなかった場合、エラーになってしまう。
li2 = [1, 2, 3, 4, 5]
li_str = map(str, li2)
print(type(li_str[0])) # TypeError: 'map' object is not subscriptable
print('------------------')

# map関数
intlist = list(range(5))
result = map(lambda x: x * x, intlist)
print(intlist) # [0, 1, 2, 3, 4]
print(result) # <map object at 0x7f94dd4b9510>
print(list(result)) # [0, 1, 4, 9, 16]
#            ↑↑ リスト関数に「mapオブジェクト」の「result変数」を渡すと数値のリストに変換される

result = [x * x for x in intlist]
print(result) # [0, 1, 4, 9, 16]
