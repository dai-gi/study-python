# スライス
test_slice = ['https', 'www', 'python', 'izm', 'com']
print(test_slice[:]) # ['https', 'www', 'python', 'izm', 'com']
print(test_slice[::]) # ['https', 'www', 'python', 'izm', 'com']
print('-----------')


# 要素の取得
print(test_slice[:4]) # ['https', 'www', 'python', 'izm']

print(test_slice[2:]) # ['python', 'izm', 'com']

print(test_slice[3:5]) # ['izm', 'com']


# 末尾の要素を取得
print(test_slice[-1:]) # [com']
print('-----------')


#末尾以外の全ての要素を取得
print(test_slice[:-1]) # ['https', 'www', 'python', 'izm']
print('-----------')


# 逆順にして要素を取得
print(test_slice[::-1]) # ['com', 'izm', 'python', 'www', 'https']
print('-----------')


# 全ての要素を取得
print(test_slice[:999]) # ['https', 'www', 'python', 'izm', 'com']
print('-----------')


# 要素の代入
print(test_slice) # ['https', 'www', 'python', 'izm', 'com']
test_slice[0:3] = ('WWW', 'PYTHON')
print(test_slice) # ['WWW', 'PYTHON', 'izm', 'com']
