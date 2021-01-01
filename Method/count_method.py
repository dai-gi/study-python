# countメソッド(指定した要素の数を取得)
list_2 = ['100', '200', '300', '200', '100']
print(list_2.count('200')) # 2
print('------------------')

# @IT｜[Python入門] リストの操作

# 指定した要素が何個リストに格納されているかのカウント
intlist = [0, 10, 9, 2, -7, -10, -2, -9, -7, 3]

print(intlist.count(1)) # 0

idx = -1
count = intlist.count(-7)
for num in range(count):
    idx = intlist.index(-7, idx + 1) # 4: -7
    print(f'{idx}: {intlist[idx]}')  # 8: -7
