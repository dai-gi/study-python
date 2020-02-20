# # ローカル変数
# def myfunc():
#     a = 'Python'
#     print('a:', a)

# myfunc()
# print(a)

# def myfunc():
#     a = 'Python'
#     print('a:', a)

# a = 'Ruby'
# myfunc()
# print('a:', a)

# # スコープの種類
# # 名前解決
# # ローカルスコープのみ
# def myfunc():
#     print('b:', b)

# # myfunc()

# b = 'Python'
# myfunc()

# # global文
# def myfunc():
#     global a
#     a = 'Python'
#     print('a:', a)

# a = 'Ruby'
# myfunc()
# print(a)

# # 名前空間
# __name__

# # ローカル名前空間
# some_var = 'some_var'

# def myfunc():
#     a = 'Python'
#     # print('a:', a)
#     print(locals())

# myfunc()
# print(locals())

# def myfunc():
#     a = 'Python'
#     # print('a:', a)
#     print(dir())

# myfunc()
# print(dir())

# globals()

# locals() == globals()

def myfunc():
    a = 'Python'
    print('locals:', locals())
    print('globals:', globals())

myfunc()