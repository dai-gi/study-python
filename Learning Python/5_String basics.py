# # エスケープシーケンス
# print('It\'s')

# # print('１行目\n２行目')
# print('１行目\'２行目')
# print('１行目\"２行目')
# print('１行目\t２行目')


# # 8進数・16進数
# code_point = ord('a')
# oct_code = oct(code_point)
# hex_code = hex(code_point)
# print(oct_code)
# print(hex_code)

# # 文字「a」を表示
# print('\141')
# print('\x61')

# code_point = ord('a')
# a_char = chr(code_point)
# print(a_char)
# print(code_point)

# # raw
# raw_str = r'C:\Users\deepinsider\Documents\work\data.txt'
# print(raw_str)
# # raw_str

# # フォーマット済み文字列（f文字列）
# x = 1
# y = 100
# result = f'{x} + {y} = {x + y}'
# print(result)

# # 文字列と数値の変換：str/int/float関数
# user_input = input('input some number:')
# result = user_input * 2
# print(result)

# # intに変換
# user_input = input('input some number:')
# int_value = int(user_input)
# result = int_value * 2
# print(result)

# # 計算結果を文字列と一緒に表示
# user_input = input('input some number:')
# int_value = int(user_input)
# result = str(int_value) + '* 2 = ' + str(int_value * 2)
# print(result)

# f文字列の場合
user_input = input('input some number:')
int_value = int(user_input)
result = f'{int_value}  * 2 = {+ int_value * 2}'
print(result)


