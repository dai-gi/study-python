# @IT
# popitemメソッド
mydict = {'foo': 'foo', 'bar': 'bar', 'baz': 'baz'} # <- 3つの要素が入っている
print(mydict.popitem()) # ('baz', 'baz')
print(mydict.popitem()) # ('bar', 'bar')
print(mydict.popitem()) # ('foo', 'foo')
print(mydict.popitem()) # <- 4回目：KeyError: 'popitem(): dictionary is empty'
