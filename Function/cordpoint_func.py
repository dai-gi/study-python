# @IT｜Python入門
# 8進数・16進数に変換
code_point = ord('a')
print(code_point) # 97 <- コードポイント
print('')
# 文字列「a」のコードポイントを8進数値にする
oct_code = oct(code_point)
print(oct_code) # 0o141
print('\141') # a
print('')
# 文字列「a」のコードポイントを16進数値にする
hex_code = hex(code_point)
print(hex_code) # 0x61
print('\x61') # a
print('')
# 引数に渡したコードポイントに対応する文字列に変換する
a_char = chr(code_point)
print(a_char) # a
print('-----------')
