# 文字列
"""""""""""""""""
【目次】

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
・エスケープシーケンス
・8進数・16進数に変換


【文字列で使う関数・メソッド】

関数：

メソッド：
・replaceメソッド
・splitメソッド
・rjustメソッド
・zfillメソッド
・tstartswithメソッド
・upperメソッド
・lowerメソッド
・lstlipメソッド
"""""""""""""""""

# いちばんやさしいPython入門教室
# 「"」と「'」の使い分けは自由
print("abc") # abc
print('abc') # abc
# NG
# print("abc') 
# 出力結果：SyntaxError: EOL while scanning string literal


# 文字列の連結
# 「+」は連結
print("abc" + "cde") # abccde
# 「＊」は繰り返し
print("abc" * 3) # abcabcabc
# NG
# print("abc" + 3) # TypeError: can only concatenate str (not "int") to str


# 改行
# エスケープシーケンスを利用する
print("こんにちは。今日の晩ご飯は何でしたか？\nおいしかったですか？\n何カロリーでしたか？")
"""
出力結果：こんにちは。今日の晩ご飯は何でしたか？
おいしかったですか？
何カロリーでしたか？
"""
# シングルクォーテーション
print('It\'s') # It's
# タブ文字
print('１行目\t２行目') # １行目  ２行目

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

# コードの可読性を良くする
# 「\」を利用する
print( "こんにちは。今日の晩ご飯は何でしたか？\
おいしかったですか？\
何カロリーでしたか？")
# 出力結果：こんにちは。今日の晩ご飯は何でしたか？おいしかったですか？何カロリーでしたか？

# in演算子(文字列の検索)
print('z' in test_str) # True
print('s' in test_str) # False









# @IT
# Pyhtonの文字列の操作
# find / rfindメソッド
sample_str = 'find, rfind, index, rindex'
print(sample_str.find('index'))
print(sample_str.rfind('index'))
print(sample_str.find('foo'))
print(sample_str.index('find'))
print(sample_str.rindex('find'))
print(sample_str.index('foo'))

# joinメソッド
alpha_list = 'abc def ghi'.split()
print(alpha_list)
alpha_list = ','.join(alpha_list)
print(alpha_list)

alpha_list = 'abc def ghi'.split()
print(alpha_list)
alpha_list = ''.join(alpha_list)
print(alpha_list)

# isdigitメソッド(文字種の判定)
num = 'not a number!'
user_input = input('input number: ')
num = int(user_input)
print(num)

num = 'not a number!'
user_input = input('input number: ')
if user_input.isdigit():
    num = int(user_input)
print(num)

# swapcase／title／lowerメソッド
sample_str = 'abc def GHI JKL'
print(sample_str.swapcase())
print(sample_str.title())
print(sample_str.lower())

# endswithメソッド
sample_str = 'this is a sample string'
print(sample_str.endswith('string'))

sample_str = 'this is a sample string'
print(sample_str.endswith(('sample', 'ing')))

# ljust／centerメソッド
sample_str = 'Python'
print(sample_str.ljust(12, '+'))
print(sample_str.center(12, '*'))

import mojimoji

zenkaku = '１２３４５ＡＢＣ'
hankaku = mojimoji.zen_to_han(zenkaku)
print(hankaku)  # 12345ABC

import unicodedata

text = u'ＡＢＣａｂｃ１２３カキク①（！％＠＃＄￥～'
hankaku = unicodedata.normalize("NFKC", text)
print(hankaku)