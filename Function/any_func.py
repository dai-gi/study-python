
# any関数
"""""""""""""""""
構文：
any(イテラブル)

リストのいずれかの要素が真ならTrue、偽ならFalseが返される。
"""""""""""""""""
intlist1 = list(range(5))  # [0, 1, 2, 3, 4]
intlist2 = list(range(1, 6))  # [1, 2, 3, 4, 5]
intlist3 = [0] * 5  # [0, 0, 0, 0, 0]
strlist1 = ['', 'foo', 'bar']
strlist2 = ['foo', 'bar', 'baz']
strlist3 = [''] * 5
emptylist = []

print('intlist1:', any(intlist1))  # True
print('intlist2:', any(intlist2))  # True
print('intlist3:', any(intlist3))  # False <- 0は「偽」と見なされる

print('strlist1:', any(strlist1))  # True
print('strlist2:', any(strlist2))  # True
print('strlist3:', any(strlist3))  # False <- 空文字列は「偽」と見なされる

print('emptylist:', any(emptylist))  # False <- 空のリストを渡すと戻り値はFalse

