# @IT｜[Python入門] リストの操作

# copyメソッド(リストのコピー)
strlist1 = ['foo', 'bar', 'baz']
strlist2 = strlist1.copy() # ['foo', 'bar', 'baz']
strlist3 = strlist1 # <- 「intlist1」と「intlist3」は同じリストオブジェクトを参照する

print(strlist1) # ['foo', 'bar', 'baz']
print(strlist2) # ['foo', 'bar', 'baz']

# idの変化
print(id(strlist1)) # 140611019157984
print(id(strlist2)) # 140611019160544
print(id(strlist3)) # 140611019157984


intlist1 = [[1, 2], [3, 4], [5, 6]]
intlist2 = intlist1.copy()

print(intlist1) # [[1, 2], [3, 4], [5, 6]]
print(intlist2) # [[1, 2], [3, 4], [5, 6]]

print(id(intlist1)) # 140308963409104
print(id(intlist2)) # 140308964265488

# 浅いコピーの場合、コピー元の要素が変更されるとコピーも変更されてしまう
intlist1[0][0] = 101
print(intlist1) # [[101, 2], [3, 4], [5, 6]]
print(intlist2) # [[101, 2], [3, 4], [5, 6]]
