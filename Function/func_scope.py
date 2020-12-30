# @IT｜[Python入門] 関数のローカル変数とスコープ
# 名前空間
"""""""""""""""
作成した変数名・関数名が保管される場所

関数内で定義した変数 = ローカルスコープ
変数 = グローバルスコープ

スコープとは...
現時点での解釈：2020/12/27
作成した変数や関数の名前が保管される場所の範囲のこと

(範囲)
1. ローカルスコープ
2. グローバルスコープ
3. ビルドインスコープ

名前を呼び出した時に検索される順番も (範囲)1 ~ 3 の順に検索される
"""""""""""""""
print(__name__)  # <- 現在のモジュール名を調べることができる 評価結果： '__main__'

"""""""""""""""
現時点での解釈：2020/12/27
今現在、「__main__」モジュール内で変数の定義やら色々な作業している。例えば、「some_var」の変数を定義したとすると、
それを外から見たとしたら「__main__」モジュールのローカルスコープ内で定義されたことにり、「__main__」モジュール内で
見た場合は、グローバルスコープで定義されたことになる。つまり、グローバル変数となる。
"""""""""""""""


# ローカル名前空間
some_var = 'some_var'

def myfunc():
    a = 'Python'
    # print('a:', a)
    print(locals())
    print('')

myfunc() # {'a': 'Python'}
print(locals())
"""""""""""""""
出力結果：
{'__name__': '__main__', '__doc__': '\n作成した変数名・関数名が保管される場所\n\n関数
内で定義した変数 = ローカルスコープ\n変数 = グローバルスコープ\n\nスコープとは...\n現
時点での解釈：2020/12/27\n作成した変数や関数の名前が保管される場所の範囲のこと\n\n(範
囲)\n1. ローカルスコープ\n2. グローバルスコープ\n3. ビルドインスコープ\n\n名前を呼び出
した時に検索される順番も (範囲)1 ~ 3 の順に検索される\n', '__package__': None, '__load
er__': <_frozen_importlib_external.SourceFileLoader object at 0x7fec68751190>, '__spec
__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__f
ile__': '/Users/uedadaisuke/Development/github/study_python/Python入門 - Learning Pyth
on/14_Function local variables and scope.py', '__cached__': None, 'some_var': 'some_va
r', 'myfunc': <function myfunc at 0x7fec687bd440>}

上記の出力結果はモジュールのトップレベルで定義されている名前とその値が格納されていることを表示している
"""""""""""""""
print('')

def myfunc():
    a = 'Python'
    print('a:', a)
    print(dir()) # ['a'] <- 関数のローカルスコープ


myfunc()
print(dir())
"""""""""""""""
出力結果：
['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
'__name__', '__package__', '__spec__', 'myfunc', 'some_var']

モジュールのトップレベルのローカルスコープ(=グローバルスコープ)に存在する名前を含んだリストを戻す
"""""""""""""""
print('')

# グローバル名前空間
print(locals())
"""""""""""""""
出力結果：
{'__name__': '__main__', '__doc__': '\n作成した変数名・関数名が保管される場所\n\n関数
内で定義した変数 = ローカルスコープ\n変数 = グローバルスコープ\n\nスコープとは...\n現
時点での解釈：2020/12/27\n作成した変数や関数の名前が保管される場所の範囲のこと\n\n(範
囲)\n1. ローカルスコープ\n2. グローバルスコープ\n3. ビルドインスコープ\n\n名前を呼び出
した時に検索される順番も (範囲)1 ~ 3 の順に検索される\n', '__package__': None, '__load
er__': <_frozen_importlib_external.SourceFileLoader object at 0x7fec68751190>, '__spec
__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__f
ile__': '/Users/uedadaisuke/Development/github/study_python/Python入門 - Learning Pyth
on/14_Function local variables and scope.py', '__cached__': None, 'some_var': 'some_va
r', 'myfunc': <function myfunc at 0x7fec687bd440>}

"""""""""""""""

print(locals() == globals()) # True

def myfunc():
    a = 'Python'
    print('locals:', locals())
    print('globals:', globals())

myfunc()
"""""""""""""""
出力結果：
locals: {'a': 'Python'}
globals: {'__name__': '__main__', '__doc__': '\n作成した変数名・関数名が保管される場所
\n\n関数内で定義した変数 = ローカルスコープ\n変数 = グローバルスコープ\n\nスコープとは...
\n現時点での解釈：2020/12/27\n作成した変数や関数の名前が保管される場所の範囲のこと\n\n(範囲)
\n1. ローカルスコープ\n2. グローバルスコープ\n3. ビルドインスコープ\n\n名前を呼び出した時に
検索される順番も (範囲)1 ~ 3 の順に検索される\n', '__package__': None, '__loader__': 
<_frozen_importlib_external.SourceFileLoader object at 0x7ff9e8159150>, '__spe
c__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>
, '__file__': '/Users/uedadaisuke/Development/github/study_python/Python入門 - 
Learning Python/14_Function local variables and scope.py', '__cached__': None, 
'some_var': 'some_var', 'myfunc': <function myfunc at 0x7ff9e843e050>}

"""""""""""""""
