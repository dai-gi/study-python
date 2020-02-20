# # 位置引数とキーワード引数
# # 位置引数
# def myfunc(param1, param2, param3):
#     return f'param1: {param1}, param2: {param2}, param3: {param3}'

# print(myfunc(1, 2, 3))

# # キーワード引数
# print(myfunc(param3=1, param2='string', param1=0.5))

# # 位置引数とキーワード引数の混在
# print(myfunc(1, param3='param3', param2=2))

# print(myfunc(param3='param3', 2, 1))

# # 引数のアンパック（展開）
# print(myfunc(*'abc'))
# print(myfunc(1, *'23'))
# print(myfunc(*'12', 3))

# print(myfunc(*'abcd'))

# arg_dict = {'param3': 'param3', 'param2':2, 'param1': 1.0}
# print(myfunc(**arg_dict))

# # デフォルト引数
# def myfunc(param1='param1', param2='param2', param3='param3'):
#     return f'param1: {param1}, param2: {param2}, param3: {param3}'

# print(myfunc()) # 引数を全て省略
# print(myfunc(1)) # 第2引数と第3引数を省略
# print(myfunc()) # パラメーターparam2の値だけを指定して、他は省略

# def myfunc(param1='param1', param2=, param3='param3'):
#     return f'param1: {param1}, param2: {param2}, param3: {param3}'

# print('some', 'value')

# import sys
# print('some', 'value', sep=' ', end='¥n', file=sys.stdout, flush=False)

# print('some', 'value', sep='')

# # 可変長引数
# # 可変長位置引数
# def myfunc(param1, param2, *args):
#     return f'param1: {param1}, param2: {param2}, other: {args}'

# print(myfunc(1, 2))
# print(myfunc(1, 2, 3))
# print(myfunc(1 ,2, 3, 4))

# def myfunc(param1, param2, *args):
#     tmp = f'param1: {param1}, param2: {param2}'
#     index = 3 #「paramX」という文字列を作成するのに使う
#     for item in args: #args（タプル）の各要素を取り出して文字列を作成
#         tmp += f', param{index}: {item}'
#         index += 1
#     return tmp

# print(myfunc(1, 2)) #引数を2つだけ渡す
# print(myfunc(1, 2, 3)) #引数を3つ渡す
# print(myfunc(1 ,2, 3, 4)) #引数を4つ渡す

# # 可変長キーワード引数
# def myfunc(param1, **kwargs):
#     return f'param1: {param1}, others: {kwargs}'

# print(myfunc(param2='param2', param1=1, foo='foo'))

def myfunc(param1, **kwargs):
    tmp = f'param1: {param1}'
    for item in kwargs.items():
        tmp += f', {item[0]}: {item[1]}'
    return tmp

print(myfunc(param2='param2', param1=1, foo='foo'))

