# dict関数
mydict = dict()
print(mydict) # {}
mydict = dict(foo='foo', bar='bar')
print(mydict) # {'foo': 'foo', 'bar': 'bar'}
mydict = dict({'foo': 'FOO', 'bar': 'BAR'})
print(mydict) # {'foo': 'FOO', 'bar': 'BAR'}
mydict = dict([('foo', 1), ['bar', 2]])
print(mydict) # {'foo': 1, 'bar': 2}
mydict = dict({'foo': 'FOO', 'bar': 'BAR'}, baz='baz'
print(mydict) # {'foo': 'FOO', 'bar': 'BAR', 'baz': 'baz'}