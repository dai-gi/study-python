# @IT｜[Python入門] リストの操作

# sortメソッド(リストの並べ替え)
intlist = [6, 8, -2, -10, -3, 2, 5, 6, -9, 8]
intlist.sort()
print(intlist) # [-10, -9, -3, -2, 2, 5, 6, 6, 8, 8]

intlist = [6, 8, -2, -10, -3, 2, 5, 6, -9, 8]
intlist.sort(reverse=True)
print(intlist) # [8, 8, 6, 6, 5, 2, -2, -3, -9, -10]

intlist = [6, 8, -2, -10, -3, 2, 5, 6, -9, 8]
intlist.sort(key=abs) # <- 絶対値を中心に並べ替え
print(intlist)  # 出力：[-2, 2, -3, 5, 6, 6, 8, 8, -9, -10]
