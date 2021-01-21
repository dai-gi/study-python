# coding: utf-8
# 問題：クリスマスツリーに必要な電球を算出
# 与えられる入力例：'7 2 3'

# 0 <= N <= 100
# 0 <= X, Y <= 10 
N, X, Y = list(map(int, input().split()))

num = N - X
n = 1
li = [1]
while n <= num:
    n += X
    li.append(str(n))
    
result = round(len(li) * Y)
print(result)