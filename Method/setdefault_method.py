# @IT
# setdefaultメソッド(項目の存在確認と追加)
mydict = {'foo': 'foo', 'bar': 'bar'}
print(mydict) # {'foo': 'foo', 'bar': 'bar'}

# 存在するキーを指定すれば、その値が返される
print(mydict.setdefault('foo')) # foo

# 存在しないキーを指定
print(mydict.setdefault('baz', 'baz')) # baz
print(mydict) # {'foo': 'foo', 'bar': 'bar', 'baz': 'baz'}
