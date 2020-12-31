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


# @IT｜[Python入門] リストの基本
# list関数でリストを定義
strlist = list('Python') # ['P', 'y', 't', 'h', 'o', 'n']
print(strlist)
intlist = list(range(10)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(intlist)
somelist = list(intlist) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(somelist)

# 様々な型の要素をリストに格納できる
somelist = ['python', 1, 100.5]
print(somelist) # ['python', 1, 100.5]

# リストの要素をスライスで取得
intlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(intlist[1:4]) # [1, 2, 3]
print(intlist[:3]) # [0, 1, 2]
print(intlist[5:]) # [5, 6, 7, 8, 9]
print(intlist[1:9:2]) # [1, 3, 5, 7]

# リストの要素の変更
languages = ['Python', 'Ruby', 'PHP']
print(languages) # ['Python', 'Ruby', 'PHP']
languages[2] = 'JabaScript'
print(languages) # ['Python', 'Ruby', 'JabaScript']

# スライスで要素を変更
intlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
intlist[0:5] = [10, 11, 12, 13, 14]
print(intlist)  # [10, 11, 12, 13, 14, 5, 6, 7, 8, 9]
intlist[0:2] = [20, 21, 22]
print(intlist)  # [20, 21, 22, 12, 13, 14, 5, 6, 7, 8, 9]
intlist[0:6] = [0, 1, 2]
print(intlist)  # [0, 1, 2, 5, 6, 7, 8, 9]

# リストの結合
cs = 'C＃'
number = 99
print(languages) # ['Python', 'Ruby', 'JabaScript']
languages = languages + [cs, number]
print(languages) # ['Python', 'Ruby', 'JabaScript', 'C＃', 99]
