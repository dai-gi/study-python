# セットの基本
test_set_1 = {'python', '-', 'izm', '.', 'com'}
print(test_set_1)

print('--------------------------------------')

for i in test_set_1:
    print(i)


# 要素がない空のセットを作成
# これはディクショナリ
test_dict = {}

# これはセット
test_set = {'python'}

# 空のセット「set」を使う
empty_set = set()


# setは値が重複しない
test_set_1 = {'python', '-', 'izm', '.', 'com', 'python', 'izm'}
print(test_set_1)

print('--------------------------------------')

for i in test_set_1:
    print(i)


# 要素の追加
test_set_1 = set()

test_set_1.add('python')
test_set_1.update({'-', 'izm', '.', 'com'})

print(test_set_1)

# 要素の削除
test_set_1 = {'python', '-', 'izm', '.', 'com'}

test_set_1.remove('-')
test_set_1.discard('.')

print(test_set_1)

# frozenset
test_set_1 = frozenset({'python', '-', 'izm', '.', 'com'})

# test_set_1.remove('-')
# test_set_1.discard('.')

print(test_set_1)

