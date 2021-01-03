# iter関数(リストの要素を反復するためのイテレータを取り出す)
intlist = [0, 1, 2]
iterator = iter(intlist) # <- イテレータオブジェクトを生成
print(iterator) # <list_iterator object at 0x7fe4fa67d490>

# next関数(「iter関数」が実行され、イテレータオブジェクトを数値に変換した値が返される)
print(next(iterator)) # 0
print(next(iterator)) # 1
print(next(iterator)) # 2

# nextメソッド(「iter関数」が実行され、イテレータオブジェクトを数値に変換した値が返される)
# print(iterator.__next__()) # 0
# print(iterator.__next__()) # 1
# print(iterator.__next__()) # 2
