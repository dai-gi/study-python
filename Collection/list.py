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

# id関数(組み込み関数)
"""""""""""""""""
id「アインデンティティー」
Pythonではオブジェクト(数値、文字列、リストなど...)を定義(例えば、x = 1 のこと...)すると「それを識別する値」が
割り当てられる。割り当てられた値はメモリに保存され変化することはない。

下記の2点は同義：
・somelist = somelist + anotherlist
・somelist += anotherlist

補足：
『「somelist = somelist + anotherlist」と「somelist += anotherlist」は「リストを結合する」という意味では同一
の操作だが、実際には最終的なオブジェクトのアイデンティティーが異なるので、完全に同一ではない。』らしい。
"""""""""""""""""
somelist = [0, 1, 2]
print(somelist) # [0, 1, 2]
print(id(somelist)) # 140517508198880
# リストとリストを結合
somelist = somelist + [3, 4]
print(somelist) # [0, 1, 2, 3, 4]
print(id(somelist)) # 140447345920592 <- アイデンティティーの値が変わっている
somelist += [5, 6]
print(somelist) # [0, 1, 2, 3, 4, 5, 6]
print(id(somelist)) # 140447345920592
print('')

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

# 書式指定
"""""""""""""""""
置換フィールドでは、表示幅の指定や、右寄せ／左寄せなどの指定も行える。これを「書式指定」と呼ぶ。
書式指定は、置換フィールドにコロン「:」を書き、その後に続けて記述する。

書式の一部：

【[fill]align】
fillには、埋め込まれる内容が、この置換フィールドの幅よりも少ないときに余った部分を
埋める文字を指定する（省略時は空白文字）。
alignには以下を指定：
「<」：左寄せ
「^」：中央寄せ
「>」：右寄せ
「=」：符号の後をfillで指定した文字で埋める
"""""""""""""""""
for row in result:
    for column in row:
        print(f'{column:<3}', end='')
    print()
"""""""""""""""""
出力結果：

2  4  6  8  10 12 14 16 18 
3  6  9  12 15 18 21 24 27 
4  8  12 16 20 24 28 32 36 
5  10 15 20 25 30 35 40 45 
6  12 18 24 30 36 42 48 54 
7  14 21 28 35 42 49 56 63 
8  16 24 32 40 48 56 64 72 
9  18 27 36 45 54 63 72 81

"""""""""""""""""