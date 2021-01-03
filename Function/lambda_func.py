# lambda = 無名関数
"""""""""""""""""
構文：
lambda パラメータ(複数可能)：式
"""""""""""""""""
calc = lambda x, y: x + y + 1
print(calc(1, 1)) # 3

intlist = list(range(5))
print(intlist) # [0, 1, 2, 3, 4]

#                      1, 2, 3....
#                      |    1, 2, 3....
#                      |   |
#                      |←←←|←←←←←
#                      ↓   ↓    ↑
result = map(lambda x: x * x, intlist)

print(result) # <map object at 0x7f94dd4b9510>
print(list(result)) # [0, 1, 4, 9, 16]
#            ↑↑ リスト関数に「mapオブジェクト」の「result変数」を渡すと数値のリストに変換される

result = [x * x for x in intlist]
print(result) # [0, 1, 4, 9, 16]
