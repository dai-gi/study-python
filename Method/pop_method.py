# # popメソッド(要素を取得して削除)
# list_1 = ['http://www.', 'python', '-', 'izm', '.', 'com']
# print(list_1) # ['http://www.', 'python', '-', 'izm', '.', 'com']
# print(list_1.pop(1)) # python

# print(list_1) # ['http://www.', '-', 'izm', '.', 'com']
# print(list_1.pop()) # com <- インデックスを指定しないとリストの末尾が取得される

# print(list_1) # ['http://www.', '-', 'izm', '.']
# print('------------------')

# # @IT｜[Python入門] リストの操作
# intlist = list(range(5))

# while intlist:
#     print(intlist.pop())
# """""""""""""""""
# 出力結果：
# 4
# 3
# 2
# 1
# 0
# """""""""""""""""

# @IT
# popメソッド
mydict = {'foo': 'foo', 'bar': 'bar', 'baz': 'baz'}
print(mydict) # {'foo': 'foo', 'bar': 'bar', 'baz': 'baz'}

# キー'bar'に対応する項目を削除
result = mydict.pop('bar')
print(result) # bar

# キー'bar'はないので、デフォルト値が戻り値になっている
result = mydict.pop('bar', 'not found')
print(result) # not found

# キー'bar'はもう存在しないのでエラー
# result = mydict.pop('bar') # KeyError: 'bar'
