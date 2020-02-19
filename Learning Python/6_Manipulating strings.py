# # len 関数
# str_len = ('Hello World')
# print(str_len)
# msg = 'Good-bye World'
# str_len = len(msg)
# print(str_len)

# # インデックス
# msg = 'Hello'
# print(msg[0])

# print(msg[5])

# print(msg[4])

# print(msg[len(msg)-1])

# print(msg[-1])

# msg[0] = 'h'

# # スライス
# print(msg[1:4])

# print(msg[:3])

# print(msg[2:])

# print(msg[:])

# print(msg[::2])

# # 文字列の結合
# msg = 'Hello ' "World"'''!
# Good-bye'''""" World"""
# print(msg)

# world = 'World'
# msg = 'Hello'world
# print(msg)

# world = 'World'
# msg = 'Hello' + world
# print(msg)

# result = '1' + 1
# print(result)

# # 文字列の乗算
# print('a' * 5)

# # find / rfind / index / rindexメソッド
# # in 演算子
# 'Setagaya' in 'Sakura-Jousui, Setagaya-Ku, Tokyo, Japan'    

# 'Setagaya' in 'Yoyogi, Sibuya-Ku, Tokyo, Japan'    

# 'Setagaya' not in 'Sakura-Jousui, Setagaya-Ku, Tokyo, Japan'    

# 'Setagaya' not in 'Yoyogi, Sibuya-Ku, Tokyo, Japan'    

# address = '東京都世田谷区桜上水'
# ward = '世田谷区'

# if (ward in address):
#     print(address + 'は' + ward + 'にあります')
# else:
#     print(address + 'は' + ward + 'にありません')

# # find / rfindメソッド
# sample_str = 'find, rfind, index, rindex'
# print(sample_str.find('index'))
# print(sample_str.rfind('index'))
# print(sample_str.find('foo'))
# print(sample_str.index('find'))
# print(sample_str.rindex('find'))
# print(sample_str.index('foo'))

# # splitメソッド
# 'abc def ghi'.split(' ')

# 'abc def ghi'.split(' ', 1)

# # joinメソッド
# alpha_list = 'abc def ghi'.split()
# print(alpha_list)
# alpha_list = ','.join(alpha_list)
# print(alpha_list)

# alpha_list = 'abc def ghi'.split()
# print(alpha_list)
# alpha_list = ''.join(alpha_list)
# print(alpha_list)

# # strip / lstrip / rstripメソッド
# data = 'abc, def, ghi'
# data_list = data.split(',')
# print(data_list)

# sample_str = '   sample   '
# print('begin' + sample_str.strip() + ':end')
# print('begin' + sample_str.lstrip() + ':end')
# print('begin' + sample_str.rstrip() + ':end')
# print(sample_str)

# sample_str = '**++**sample**+**'
# print(sample_str.strip('*'))
# print(sample_str.strip('+*se'))

# # 文字種の判定
# num = 'not a number!'
# user_input = input('input number: ')
# num = int(user_input)
# print(num)

# num = 'not a number!'
# user_input = input('input number: ')
# if user_input.isdigit():
#     num = int(user_input)
# print(num)

# replace／swapcase／title／lower／upperメソッド
# sample_str = 'abc def GHI JKL'
# print(sample_str.replace('abc', 'xyz'))
# print(sample_str.swapcase())
# print(sample_str.title())
# print(sample_str.lower())
# print(sample_str.upper())

# # startswith／endswithメソッド
# sample_str = 'this is a sample string'
# print(sample_str.startswith('this'))
# print(sample_str.endswith('string'))

# sample_str = 'this is a sample string'
# print(sample_str.startswith(('that', 'those')))
# print(sample_str.endswith(('sample', 'ing')))

# ljust／center／rjustメソッド
sample_str = 'Python'
print(sample_str.ljust(12, '+'))
print(sample_str.center(12, '*'))
print(sample_str.rjust(12))