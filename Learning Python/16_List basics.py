# # 多数のデータを扱う型
# # リストの定義
# languages = ['Python', 'Ruby', 'PHP']
# print(languages)

# # リストの定義
# emptylist = [] #空のリスト（要素が一つもないリスト）を定義
# print((emptylist)) #出力結果：[]

# strlist = list('Python') #'P', 'y', 't', 'h', 'o', 'n'を要素とするリストを作成
# print(strlist)
# intlist = list(range(10)) #整数値0〜9を要素とするリストを作成
# print(intlist)
# somelist = list(intlist) #リストからリストを作成
# print(somelist)

# # リストの要素
# languages[0]

# somelist = ['python', 1, 100.5]
# print(somelist)

# # リストの要素のスライス
# intlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(intlist[1:4]) #インデックス1からインデックス3までの3つの要素を取得
# print(intlist[:3]) #インデックス0からインデックス2までの3つの要素を取得
# print(intlist[5:]) #インデックス5以降の要素を取得
# print(intlist[1:9:2]) #インデックス1〜8までの範囲にある要素を1つ飛ばしで取得

# # リストの要素の変更
# languages = ['Python', 'Ruby', 'PHP']
# print(languages)
# languages[2] = 'JabaScript'
# print(languages)
# print(languages[2])

# intlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# intlist[0:5] = [10, 11, 12, 13, 14]  # 先頭から5つの要素を変更
# print(intlist)  # [10, 11, 12, 13, 14, 5, 6, 7, 8, 9]
# intlist[0:2] = [20, 21, 22]  # 先頭から2つの要素を書き換え（余った文は追加）
# print(intlist)  # [20, 21, 22, 12, 13, 14, 5, 6, 7, 8, 9]
# intlist[0:6] = [0, 1, 2]  # 先頭から6つの要素を変更（足りない部分は削除される）
# print(intlist)  # [0, 1, 2, 5, 6, 7, 8, 9]
# intlist[0:2] = 1  # エラー

# intlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# intlist[0:10:2] = [10, 12, 14, 16, 18]  # 先頭要素から1つ飛ばしで5個を変更
# print(intlist)  # [10, 1, 12, 3, 14, 5, 16, 7, 18, 9]
# intlist[0:10:2] = [20, 22]  # エラー

# # リストへの要素の追加
languages = ['Python', 'Ruby', 'PHP']
# languages.append('Perl')
# print(languages)

# # リストの結合
# cs = 'C＃'
# number = 99

# languages = languages + [cs, number]
# print(languages)

# languages + 'C++'

# somelist = [0, 1, 2]
# print(id(somelist))
# somelist = somelist + [3, 4]
# print(id(somelist))
# somelist += [5, 6]
# print(id(somelist))

# # リストからの要素の削除
# del languages[5]
# print(languages)

# intlist = [1, 2, 3, 1, 2, 3]
# intlist.remove(3)
# print(intlist)

# del languages
# print(languages)

# # リスト内包表記
# print([num * 2 for num in range(10)]) # 0、2、4、……、18を要素とするリスト
# print([num * num for num in range(10) if num % 2 == 0])  #numが偶数のときに二乗

# for row in [[x * y for y in range(1, 10)]for x in range(1, 10)]:
#     print(row)

# # リストのリスト
result = []
for x in range(1, 10):
    # zを計算
    z = []
    for y in range(1, 10):
        z.append(x * y)
    result.append(z)
print(result[0][1])

for row in result:
    for column in row:
        print(f'{column:>3}', end='')
    print()