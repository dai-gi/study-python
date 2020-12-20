# リスト
list_1 = ['python','izm',]
print(list_1) # ['python', 'izm']
print('------------------')


# appendメソッド(要素の追加)
list_1.append('com')
print(list_1) # ['python', '-', 'izm', '.', 'com']
print('------------------')


# インデックスを指定して追加
list_1.insert(0, 'http://www.')
list_1.insert(2, '-')
list_1.insert(4, '.')
print(list_1) # ['http://www.', 'python', '-', 'izm', '.', 'com']
print('------------------')


# popメソッド(要素を取得して削除)
print(list_1) # ['http://www.', 'python', '-', 'izm', '.', 'com']
print(list_1.pop(1)) # python

print(list_1) # ['http://www.', '-', 'izm', '.', 'com']
print(list_1.pop()) # com <- インデックスを指定しないとリストの末尾が取得される

print(list_1) # ['http://www.', '-', 'izm', '.']
print('------------------')


# removeメソッド(要素の削除)
list_1.remove('http://www.') # <- 要素を指定して削除
print(list_1) # ['-', 'izm', '.']
print('------------------')


# indexメソッド(指定した要素のインデックスを取得)
print(list_1.index('-')) # 0
print('------------------')


# countメソッド(指定した要素の数を取得)
list_2 = ['100', '200', '300', '200', '100']
print(list_2.count('200')) # 2
print('------------------')