# @IT｜[Python入門] リストの操作

# deepcopy関数
from copy import deepcopy

intlist1 = [[1, 2], [3, 4], [5, 6]]
intlist2 = deepcopy(intlist1)

print(intlist1) # [[1, 2], [3, 4], [5, 6]]
print(intlist2) # [[1, 2], [3, 4], [5, 6]]

print(id(intlist1)) # 140384493444944
print(id(intlist2)) # 140384493453872

intlist1[0][0] = 101
print(intlist1) # [[101, 2], [3, 4], [5, 6]]
print(intlist2) # [[1, 2], [3, 4], [5, 6]]