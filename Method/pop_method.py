# popメソッド(要素を取得して削除)
print(list_1) # ['http://www.', 'python', '-', 'izm', '.', 'com']
print(list_1.pop(1)) # python

print(list_1) # ['http://www.', '-', 'izm', '.', 'com']
print(list_1.pop()) # com <- インデックスを指定しないとリストの末尾が取得される

print(list_1) # ['http://www.', '-', 'izm', '.']
print('------------------')
