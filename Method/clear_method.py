# @IT｜[Python入門] リストの操作

# clearメソッドによる全要素の削除
intlist = list(range(10))
print(intlist) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(id(intlist)) # 140187150336880

intlist.clear()
print(intlist) # []
print(id(intlist)) # 140187150336880

intlist.append(5)
intlist = []
print(id(intlist)) # 140187134407136