# frozenset
test_set4 = frozenset({'python', '-', 'izm', '.', 'com'})
print(type(test_set4)) # <class 'frozenset'>
print(test_set4) # frozenset({'-', 'python', 'izm', '.', 'com'})

# 定義すると要素を操作できなくなる
test_set4.remove('-') # AttributeError: 'frozenset' object has no attribute 'remove'
