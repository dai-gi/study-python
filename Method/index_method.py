# indexメソッド(指定した要素のインデックスを取得)
print(list_1.index('-')) # 0
print('------------------')

# @IT｜[Python入門] リストの操作

intlist = [0, 10, 9, 2, -7, -10, -2, -9, -7, 3]
print(intlist.index(-7)) # 4
print(intlist.index(-7, 5)) # 8

# リストに無い要素を指定した場合
# print(intlist.index(3, 0, 9)) # ValueError: 3 is not in list