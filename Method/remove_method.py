# removeメソッド(要素の削除)
list_1 = ['http://www.', '-', 'izm', '.']
list_1.remove('http://www.') # <- 要素を指定して削除
print(list_1) # ['-', 'izm', '.']
print('------------------')

# @IT｜[Python入門] リストの操作

foo = 'foo'
bar = 'bar'
baz = 'baz'
strlist = [foo, bar, baz]

intlist = [-6, 4, 1, 0, -2, 4, 3, 6]
intlist.remove(4)
print(intlist) # [-6, 1, 0, -2, 4, 3, 6]
intlist.remove(False)
print(intlist) # [-6, 1, -2, 4, 3, 6]
# intlist.remove(100) # ValueError: list.remove(x): x not in list

