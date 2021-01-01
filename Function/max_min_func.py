# @IT｜[Python入門] リストの操作
# max・min関数(リスト内の最大値と最小値の要素を取得)
intlist = [7, 0, -9, 3, 2, -1, -3, 1, -5, 4]
print(max(intlist)) # 7
print(min(intlist)) # -9

print('max(abs):', max(intlist, key=abs)) # max(abs): -9
print('min(abs):', min(intlist, key=lambda x: -x if x < 0 else x)) # min(abs): 0
