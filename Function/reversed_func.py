# range関数でカウントする値を逆順にする
for i in range(1, 5+1):
    print(i)
# 1
# 2
# 3
# 4
# 5
print('-----------')

for i in reversed(range(1, 5+1)):
    print(i)
# 5
# 4
# 3
# 2
# 1

# @IT｜[Python入門] リストの操作

intlist2 = list(range(7))
intlist3 = list(reversed(intlist2))
print(intlist2) # [0, 1, 2, 3, 4, 5, 6]
print(intlist3) # [6, 5, 4, 3, 2, 1, 0]
