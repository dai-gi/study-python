# セット
test_set1 = {'python', '-', 'izm', '.', 'com'}
print(test_set1) # {'izm', 'python', '-', 'com', '.'} <- 順番で出力されない
print('-----------')

# ↓↓ 下記の {'python'} の様に記述し、代入すると「set」になる  
test_set2 = {'python'}
test_set3 = {1}
print(type(test_set2)) # <class 'set'>
print(type(test_set3)) # <class 'set'>
print('-----------')


# set関数
set_func = set('python') # {'o', 'y', 'n', 'p', 't', 'h'}
print(set_func)
print('-----------')


# addメソッド・updateメソッド(要素の追加)
test_set2.add('pandas')
print(test_set2) # {'python', 'pandas'}

test_set3.update({2, 3})
print(test_set3) # {1, 2, 3}
print('-----------')


# removeメソッド・discardメソッド(要素の削除)
test_set1.remove('-')
print(test_set1) # {'.', 'izm', 'com', 'python'}

test_set1.discard('.')
print(test_set1) # {'izm', 'com', 'python'}
print('-----------')


# frozenset
test_set4 = frozenset({'python', '-', 'izm', '.', 'com'})
print(type(test_set4)) # <class 'frozenset'>
print(test_set4) # frozenset({'-', 'python', 'izm', '.', 'com'})

# 定義すると要素を操作できなくなる
test_set4.remove('-') # AttributeError: 'frozenset' object has no attribute 'remove'


