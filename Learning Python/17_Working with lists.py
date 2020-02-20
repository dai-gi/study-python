# # リストの要素数を求める：len関数
# intlist = list(range(5))
# print(len(intlist)) #出力結果

# intlist = [7, 0, -9, 3, 2, -1, -3, 1, -5, 4]
# print(max(intlist)) #出力結果:7
# print(min(intlist)) #出力結果:-9

# intlist = [7, 0, -9, 3, 2, -1, -3, 1, -5, 4]
# print('max(abs):', max(intlist, key=abs))
# print('min(abs):', min(intlist, key=lambda x: -x if x < 0 else x))

# リストの結合と乗算
# リストに特定の要素が含まれているかの確認：in演算子
# 要素が格納されているインデックスの取得：indexメソッド

# intlist = [0, 10, 9, 2, -7, -10, -2, -9, -7, 3]
# print(intlist.index(-7))        #出力結果:4(「-2」の最小のインデックス) 
# print(intlist.index(-7, 5))     #出力結果:8(インデックス5以降を検索するため)
# print(intlist.index(3, 0, 9))   #エラー

# # 指定した要素が何個リストに格納されているかのカウント：countメソッド
# intlist = [0, 10, 9, 2, -7, -10, -2, -9, -7, 3]

# print(intlist.count(1)) #出力:0

# idx = -1
# count = intlist.count(-7)
# for num in range(count):
#     idx = intlist.index(-7, idx + 1) #インデックスidx以降を検索範囲とする
#     print(f'{idx}: {intlist[idx]}')  #インデックスとその要素を表示

# # リストへの要素の追加：appendメソッド／extendメソッド
# intlist = list(range(5))
# intlist.append(5) # リストの末尾に要素「5」を追加
# intlist.append([6, 7]) # リストの末尾にリスト「[6, 7]」を追加
# intlist.extend([8, 9]) # リストの末尾に要素「8」と要素「9」を追加
# print(intlist) # 出力：[0, 1, 2, 3, 4, 5, [6, 7], 8, 9]

# # リストへの要素の挿入：insertメソッド
# # リストからの要素の削除：del文／removeメソッド／popメソッド／clearメソッド
# # del文による要素の削除
# foo = 'foo'
# bar = 'bar'
# baz = 'baz'
# strlist = [foo, bar, baz]
# print(strlist)
# del strlist[1] #strlistのインデックス１の要素を削除
# print(strlist) #出力結果 : ['foo', 'ba2'](リストから要素'bar'が削除された)
# print(bar) #出力結果：bar(変数barが参照している文字列’bar'は削除されていない)

# # removeメソッドによる要素の削除
# intlist = [-6, 4, 1, 0, -2, 4, 3, 6]
# intlist.remove(4)       # 値が「4」に等しい最初の要素を削除
# print(intlist)          # 出力結果：[-6, 1, 0, -2, 4, 3, 6]
# intlist.remove(False)   # 値が「False」に等しい最初の要素を削除
# print(intlist)          # 出力結果：[-6, 1, -2, 4, 3, 6]
# intlist.remove(100)     # エラー

# # popメソッドによる要素の削除
# intlist = list(range(5))

# while intlist:
#     print(intlist.pop())

# # clearメソッドによる全要素の削除
# intlist = list(range(10)) # 0～9の整数値を要素とするリストを作成
# print(intlist)
# print(id(intlist)) # intlistのアイデンティテイーを表示
# intlist.clear()    # リストの全要素を削除
# print(intlist)
# print(id(intlist)) # intlistのアイデンティテイーは変わらない
# intlist.append(5)
# intlist = []    # intlistに空のリストを代入（リストを削除）
# print(id(intlist)) # intlistのアイデンティテイーが変化する

# # リストの並べ替え：sortメソッド／sorted関数
# intlist = [6, 8, -2, -10, -3, 2, 5, 6, -9, 8]
# intlist.sort()  # intlistを並べ替える
# print(intlist)  # 出力：[-10, -9, -3, -2, 2, 5, 6, 6, 8, 8]

# intlist = [6, 8, -2, -10, -3, 2, 5, 6, -9, 8]
# intlist.sort(reverse=True)
# print(intlist)  # 出力：[8, 8, 6, 6, 5, 2, -2, -3, -9, -10]

# intlist = [6, 8, -2, -10, -3, 2, 5, 6, -9, 8]
# intlist.sort(key=abs)  # 絶対値を基に並べ替え
# print(intlist)  # 出力：[-2, 2, -3, 5, 6, 6, 8, 8, -9, -10]

# strlist = ['abcd', 'abc', 'Abcd', 'abC']
# print(sorted(strlist))

# print(sorted(strlist, key=str.lower))

# # リストの反転：reverseメソッド／reversed関数
# intlist1 = list(range(5))
# print(intlist1)

# intlist1.reverse()
# print(intlist1)

# intlist2 = list(range(7))
# intlist3 = list(reversed(intlist2))
# print(intlist2)
# print(intlist3)

# # リストのコピー：copyメソッド
# strlist1 = ['foo', 'bar', 'baz']
# strlist2 = strlist1.copy()  # 浅いコピーの作成
# strlist3 = strlist1  # intlist1とintlist3は同じリストオブジェクトを参照する

# print(strlist1)
# print(strlist2)

# print(id(strlist1))
# print(id(strlist2))
# print(id(strlist3))

# strlist1[0] = 'FOO'
# print(strlist3)  # ['FOO', 'bar', 'baz']

# strlist2[0] = 'Foo'
# print(strlist1)
# print(strlist2)

# # 「浅いコピー」とは
# intlist1 = [[1, 2], [3, 4], [5, 6]]
# intlist2 = intlist1.copy()

# print(intlist1)
# print(intlist2)

# print(id(intlist1))
# print(id(intlist2))

# intlist1[0][0] = 101
# print(intlist1)
# print(intlist2)

from copy import deepcopy
intlist1 = [[1, 2], [3, 4], [5, 6]]
intlist2 = deepcopy(intlist1)  # deepcopy関数で「深いコピー」を行う

print(intlist1)
print(intlist2)

intlist1[0][0] = 101
print(intlist1)  # この結果と
print(intlist2)  # この結果は異なる