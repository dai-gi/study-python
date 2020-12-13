<<<<<<< HEAD
<<<<<<< HEAD
# map関数
=======
# # map関数について
>>>>>>> 4329b503a766e4681d13b8533dcaaa6ecc78afea
=======
# # map関数について
>>>>>>> 4329b503a766e4681d13b8533dcaaa6ecc78afea

"""
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
