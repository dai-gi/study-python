# coding: utf-8
# 問題：n置きの木にクリスマスツリーの飾り付けに必要な電球を算出する問題
# 与えられる入力例：'7 2 3'

# 0 <= N <= 100 [N = 木]
# 0 <= X, Y <= 10 [X = n置き, Y = 一つの木に取り付ける電球の数]
N, X, Y = list(map(int, input().split()))

num = N - X
n = 1
li = [1]
while n <= num:
    n += X
    li.append(str(n))
    
result = round(len(li) * Y)
print(result)