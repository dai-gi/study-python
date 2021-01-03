

# all関数
"""""""""""""""""
構文：
all(イテラブル)

リストの全ての要素が真の場合、Trueを返し、いずれかが偽の場合、Falseを返す。
"""""""""""""""""
intlist1 = list(range(5))  # [0, 1, 2, 3, 4]
intlist2 = list(range(1, 6))  # [1, 2, 3, 4, 5]
intlist3 = [0] * 5  # [0, 0, 0, 0, 0]
strlist1 = ['', 'foo', 'bar']
strlist2 = ['foo', 'bar', 'baz']
strlist3 = [''] * 5
emptylist = []

print('intlist1:', all(intlist1))  # intlist1: False <- 0は「偽」とみなされる
print('intlist2:', all(intlist2))  # intlist2: True
print('intlist3:', all(intlist3))  # intlist3: False <- 0は「偽」とみなされる

print('strlist1:', all(strlist1))  # strlist1: False <- 空の情報が入っていると「偽」が返される
print('strlist2:', all(strlist2))  # strlist2: True
print('strlist3:', all(strlist3))  # strlist3: False <- 空の情報が入っていると「偽」が返される

print('emptylist:', all(emptylist))  # emptylist: True <- 空のリストを渡すと戻り値はTrue
