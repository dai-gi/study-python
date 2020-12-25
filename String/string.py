# いちばんやさしいPython入門教室

"""
目次

・文字列
・文字列の連結
・改行
・コードの可読性を良くする
・文字列の置き換え
・文字列の分割
・文字列の桁揃え
・文字列の検索
・大文字・小文字変換
・先頭の削除
・末尾の削除
"""


# 文字列：P57
# 「"」と「'」の使い分けは自由
print("abc") # abc
print('abc') # abc
# NG
# print("abc') 
# 出力結果：SyntaxError: EOL while scanning string literal


# 文字列の連結：P61
# 「+」は連結
print("abc" + "cde") # abccde
# 「＊」は繰り返し
print("abc" * 3) # abcabcabc
# NG
# print("abc" + 3) # TypeError: can only concatenate str (not "int") to str


# 改行：P69
# エスケープシーケンスを利用する
print("こんにちは。今日の晩ご飯は何でしたか？\nおいしかったですか？\n何カロリーでしたか？")
"""
出力結果：こんにちは。今日の晩ご飯は何でしたか？
おいしかったですか？
何カロリーでしたか？
"""
# 「三重クォート」を利用する
print( """こんにちは。今日の晩ご飯は何でしたか？
おいしかったですか？
何カロリーでしたか？
""")
"""
出力結果：こんにちは。今日の晩ご飯は何でしたか？
おいしかったですか？
何カロリーでしたか？

"""
# NG
# print("こんにちは。今日の晩ご飯は何でしたか？
# おいしかったですか？
# 何カロリーでしたか？
# ")
"""
出力結果：実行されない

"""


# コードの可読性を良くする：P69
# 「\」を利用する
print( "こんにちは。今日の晩ご飯は何でしたか？\
おいしかったですか？\
何カロリーでしたか？")
# 出力結果：こんにちは。今日の晩ご飯は何でしたか？おいしかったですか？何カロリーでしたか？

# 「end=""」を利用する
print("こんにちは。今日の晩ご飯は何でしたか？",end="")
print("おいしかったですか？",end="")
print("何カロリーでしたか？")  
# 出力結果：こんにちは。今日の晩ご飯は何でしたか？おいしかったですか？何カロリーでしたか？


# 文字列の置き換え
test_str = 'python-izm'
print(test_str.replace('izm', 'ism')) # python-ism


# 文字列の分割
test_str = 'python-izm'
print(test_str.split('-')) # ['python', 'izm']


# 文字列の桁揃え
test_str = '1234'
print(test_str.rjust(10, '0')) # 0000001234

print(test_str.rjust(10, '!')) # !!!!!!1234

print(test_str.zfill(10)) # 0000001234

print(test_str.zfill(3)) # 1234


# 文字列の検索
test_str = 'python-izm'
print(test_str.startswith('python')) # True

print(test_str.startswith('izm')) # False

print('z' in test_str) # True

print('s' in test_str) # False


# 大文字・小文字変換
test_str = 'Python-Izm.Com'
print(test_str.upper()) # PYTHON-IZM.COM

print(test_str.lower()) # python-izm.com


# 先頭の削除
test_str = '     python-izm.com'
print(test_str) #      python-izm.com

test_str = test_str.lstrip()
print(test_str) # python-izm.com

test_str = test_str.lstrip('python')
print(test_str) # -izm.com



# 末尾の削除
test_str = 'python-izm.com     '
print(test_str + '/') # python-izm.com     /

test_str = test_str.rstrip()
print(test_str + '/') # python-izm.com/

test_str = test_str.rstrip("com")
print(test_str) # python-izm.
