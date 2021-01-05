# updateメソッド(要素の追加)
test_set3.update({2, 3})
print(test_set3) # {1, 2, 3}
print('-----------')

# @IT
# updateメソッド
mydict = {'foo': 'FOO', 'bar': 'BAR', 'baz': 'BAZ'}
print(mydict) # {'foo': 'FOO', 'bar': 'BAR', 'baz': 'BAZ'}

# キーワード引数による辞書の更新
mydict.update(foo='fooo', somekey='somevalue')
print(mydict) # {'foo': 'fooo', 'bar': 'BAR', 'baz': 'BAZ', 'somekey': 'somevalue'}

# 辞書による辞書の更新
mydict.update({'bar': 'new BAR'})
print(mydict) # {'foo': 'fooo', 'bar': 'new BAR', 'baz': 'BAZ', 'somekey': 'somevalue'}

# リストによる辞書の更新
mydict.update([('baz', 'new Baz'), ['x', 1]])
print(mydict) # {'foo': 'fooo', 'bar': 'new BAR', 'baz': 'new Baz', 'somekey': 'somevalue', 'x': 1}

# リストとキーワード引数の組み合わせによる更新
mydict.update([('y', 2)], z=3) 
print(mydict) # {'foo': 'fooo', 'bar': 'new BAR', 'baz': 'new Baz', 'somekey': 'somevalue', 'x': 1, 'y': 2, 'z': 3}
