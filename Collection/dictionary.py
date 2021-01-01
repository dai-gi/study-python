# ディクショナリ
"""""""""""""""""
ディクショナリで使う関数・メソッド

構文：
・del文

関数：

メソッド：
・getメソッド
・keyメソッド
・valueメソッド
・itemメソッド

"""""""""""""""""

dict_1 = {'YEAR':'2010', 'MONTH':'1', 'DAY':'20'}
print(dict_1) # {'YEAR': '2010', 'MONTH': '1', 'DAY': '20'}

# for文でディクショナリの「key」と「value」を取り出す
for i in dict_1:
    print(i) # <- key
    # ↑↑ 出力結果：'YEAR'
    print(dict_1[i]) # <- [i] key を指定して value
    # ↑↑ 出力結果：'2010'
print('------------------')

# 要素の追加
print(dict_1) # {'YEAR': '2010', 'MONTH': '1', 'DAY': '20'}
dict_1['HAY'] = 'hi'
print(dict_1) # {'YEAR': '2010', 'MONTH': '1', 'DAY': '20', 'HAY': 'hi'}
print('------------------')

# del文(要素の削除)
print(dict_1) # {'YEAR': '2010', 'MONTH': '1', 'DAY': '20', 'HAY': 'hi'}
del dict_1['HAY']
print(dict_1) # {'YEAR': '2010', 'MONTH': '1', 'DAY': '20'}
print('------------------')

# keyとvalueを同時に取得する
for key, value in dict_1.items():
    print(key, value)
"""
出力結果：
YEAR 2010
MONTH 1
DAY 20
"""

# 指定した key が入っているか確認する
print('YEAR' in dict_1) # True
print('YEARS' in dict_1) # False
