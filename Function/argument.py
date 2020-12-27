# Python-izm｜可変長引数 

# *args
def test_args1(*args):
    print(args)

test_args1(1, 2, 3, 4, 5) # (1, 2, 3, 4, 5)
print('-----------')
print('')

def test_args2(code, name, *args):
    print(code, name)
    print(args)

test_args2(100, 'python-izm', 'JP', 'US')

"""""""""""""""""
出力結果：

100 python-izm
('JP', 'US')

"""""""""""""""""
print('-----------')
print('')


# **kwargs
def test_args2(**kwargs):
    print(kwargs)

test_args2(email='xxx.com', city='Tokyo') # {'email': 'xxx.com', 'city': 'Tokyo'}
print('-----------')


# @IT｜引数
# 位置引数
def myfunc1(param1, param2, param3):
    return f'param1: {param1}, param2: {param2}, param3: {param3}'

# 関数に渡した値はmyfunc関数にある引数の順番通りに渡される
# 期待する結果：param1 = 1, param2 = 2, param3 = 3
print(myfunc1(1, 2, 3)) # param1: 1, param2: 2, param3: 3

# キーワード引数
print(myfunc1(param3=1, param2='string', param1=0.5)) # param1: 0.5, param2: string, param3: 1

# 位置引数とキーワード引数の混在
print(myfunc1(1, param3='param3', param2=2)) # param1: 1, param2: 2, param3: param3
# 第一引数をキーワード引数にするとエラーになる
# print(myfunc(param3='param3', 2, 1)) # SyntaxError: positional argument follows keyword argumentf
print('')


# 位置引数とキーワード引数
def myfunc2(param1, param2, param3):
    return f'param1: {param1}, param2: {param2}, param3: {param3}'

# 引数のアンパック（展開）
print(myfunc2(*'abc')) # param1: a, param2: b, param3: c
# print(myfunc(*'abcd')) # TypeError: myfunc() takes 3 positional arguments but 4 were given
print(myfunc2(1, *'23')) # param1: 1, param2: 2, param3: 3
print(myfunc2(*'12', 3)) # param1: 1, param2: 2, param3: 3

arg_dict = {'param3': 'param3', 'param2':2, 'param1': 1.0}
print(myfunc2(**arg_dict)) # param1: 1.0, param2: 2, param3: param3
print('')


# デフォルト引数
def myfunc3(param1='param1', param2='param2', param3='param3'):
    return f'param1: {param1}, param2: {param2}, param3: {param3}'

print(myfunc3()) # param1: param1, param2: param2, param3: param3
print(myfunc3(1)) # param1: 1, param2: param2, param3: param3
print('')


# print関数のパラメータ
print('some', 'value') # some value

import sys
print('some', 'value', sep=' ', end='\n', file=sys.stdout, flush=False) # some value
print('some', 'value', sep='') # somevalue
