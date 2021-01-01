# リスト
"""""""""""""""""
リストで使う関数・メソッド

構文：
・del文
・内包表記
・ネスト

関数：
・list関数

メソッド：
・appendメソッド
・insertメソッド

"""""""""""""""""

list_1 = ['python','izm',]
print(list_1) # ['python', 'izm']
print('------------------')

# @IT｜[Python入門] リストの基本

# 様々な型の要素をリストに格納できる
somelist = ['python', 1, 100.5]
print(somelist) # ['python', 1, 100.5]

# リストの要素の変更
languages = ['Python', 'Ruby', 'PHP']
print(languages) # ['Python', 'Ruby', 'PHP']
languages[2] = 'JabaScript'
print(languages) # ['Python', 'Ruby', 'JabaScript']

# リストの結合
cs = 'C＃'
number = 99
print(languages) # ['Python', 'Ruby', 'JabaScript']
languages = languages + [cs, number]
print(languages) # ['Python', 'Ruby', 'JabaScript', 'C＃', 99]

# リストの要素をスライスで取得
intlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(intlist[1:4]) # [1, 2, 3]
print(intlist[:3]) # [0, 1, 2]
print(intlist[5:]) # [5, 6, 7, 8, 9]
print(intlist[1:9:2]) # [1, 3, 5, 7]

# スライスで要素を変更
intlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
intlist[0:5] = [10, 11, 12, 13, 14]
print(intlist)  # [10, 11, 12, 13, 14, 5, 6, 7, 8, 9]
intlist[0:2] = [20, 21, 22]
print(intlist)  # [20, 21, 22, 12, 13, 14, 5, 6, 7, 8, 9]
intlist[0:6] = [0, 1, 2]
print(intlist)  # [0, 1, 2, 5, 6, 7, 8, 9]

# del文(要素の削除)
intlist = [1, 2, 3, 1, 2, 3]
print(intlist) # [1, 2, 3, 1, 2, 3]
del intlist[5]
print(intlist) # [1, 2, 3, 1, 2]
del intlist # リストを削除
# print(intlist) # NameError: name 'intlist' is not defined <- リストが削除されていることが分かる
print('')

# 内包表記
# [処理内容(変数 * 2) for 変数 in range(10)]
print([num * 2 for num in range(10)]) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# [変数 * 変数 for 変数 in range(10) 条件分岐]
print([num * num for num in range(10) if num % 2 == 0]) # [0, 4, 16, 36, 64]
print('')


for row in [[x * y for y in range(1, 10)]for x in range(1, 10)]:
    print(row)
print('')
"""""""""""""""""
出力結果：

[1, 2, 3, 4, 5, 6, 7, 8, 9]
[2, 4, 6, 8, 10, 12, 14, 16, 18]
[3, 6, 9, 12, 15, 18, 21, 24, 27]
[4, 8, 12, 16, 20, 24, 28, 32, 36]
[5, 10, 15, 20, 25, 30, 35, 40, 45]
[6, 12, 18, 24, 30, 36, 42, 48, 54]
[7, 14, 21, 28, 35, 42, 49, 56, 63]
[8, 16, 24, 32, 40, 48, 56, 64, 72]
[9, 18, 27, 36, 45, 54, 63, 72, 81]

仕組み：

　　  ↓--------------------- リスト１の要素を変数「row」に代入 ----------------------↓
　  　↓      ↓----------- リスト１の要素をリスト２に代入 -----------↓　　　           ↓
for row in[[x * y for y in range(1, 10)]<- リスト２  for x in range(1, 10)]<- リスト１:
    　　　　  　　                             ↑「x」にリスト１の要素を代入し、その要素の倍数のリスト２を生成

"""""""""""""""""


# リストのネスト
"""""""""""""""""
ネストとは：
・for文 in for文
・if文 in if文
"""""""""""""""""
result = []
for x in range(1, 10):
    z = []
    for y in range(1, 10):
        z.append(x * y)
    result.append(z)
print(result)
"""""""""""""""""
出力結果：

[[1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 4, 6, 8, 10, 12, 14, 16, 18], 
[3, 6, 9, 12, 15, 18, 21, 24, 27], [4, 8, 12, 16, 20, 24, 28, 32, 36],
[5, 10, 15, 20, 25, 30, 35, 40, 45], [6, 12, 18, 24, 30, 36, 42, 48, 54], 
[7, 14, 21, 28, 35, 42, 49, 56, 63], [8, 16, 24, 32, 40, 48, 56, 64, 72], 
[9, 18, 27, 36, 45, 54, 63, 72, 81]]

"""""""""""""""""
print('')
print(result[0][1]) # 2
print('')

