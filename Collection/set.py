# セット
"""""""""""""""""
セットで使う関数・メソッド

関数：
・set関数
・frozenset関数

メソッド：
・addメソッド
・updateメソッド
・removeメソッド
・discardメソッド

"""""""""""""""""
test_set1 = {'python', '-', 'izm', '.', 'com'}
print(test_set1) # {'izm', 'python', '-', 'com', '.'} <- 順番で出力されない
print('-----------')

# ↓↓ 下記の {'python'} の様に記述し、代入すると「set」になる  
test_set2 = {'python'}
test_set3 = {1}
print(type(test_set2)) # <class 'set'>
print(type(test_set3)) # <class 'set'>
print('-----------')
