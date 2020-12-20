# ディクショナリ
dict_1 = {'YEAR':'2010', 'MONTH':'1', 'DAY':'20'}
print(dict_1) # {'YEAR': '2010', 'MONTH': '1', 'DAY': '20'}

# for文でディクショナリの「key」と「value」を取り出す
for i in dict_1:
    print(i) # <- key
    # ↑↑ 出力結果：'YEAR'
    print(dict_1[i]) # <- [i] key を指定して value
    # ↑↑ 出力結果：'2010'
print('------------------')


# getメソッド
print(dict_1.get('YEAR')) # '2010' 

print(dict_1.get('YEAES')) # None

print(dict_1.get('YEAR', 'NOT FOUND')) # '2010'

print(dict_1.get('YEARS', 'NOT FOUND')) # 'NOT FOUND'
                            # ↑↑ 第二引数に存在しなかった場合の返り値を指定できる
print('------------------')

# 要素の追加
print(dict_1) # {'YEAR': '2010', 'MONTH': '1', 'DAY': '20'}
dict_1['HAY'] = 'hi'
print(dict_1) # {'YEAR': '2010', 'MONTH': '1', 'DAY': '20', 'HAY': 'hi'}
print('------------------')

# delメソッド(要素の削除)
print(dict_1) # {'YEAR': '2010', 'MONTH': '1', 'DAY': '20', 'HAY': 'hi'}
del dict_1['HAY']
print(dict_1) # {'YEAR': '2010', 'MONTH': '1', 'DAY': '20'}
print('------------------')

# keyメソッド
print(dict_1.keys()) # dict_keys(['YEAR', 'MONTH', 'DAY'])

# valueメソッド
print(dict_1.values()) # dict_values(['2010', '1', '20'])
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

# itemメソッド
print(dict_1.items()) # dict_items([('YEAR', '2010'), ('MONTH', '1'), ('DAY', '20')])

print(type(dict_1.items())) # <class 'dict_items'>

# 値を使って何か処理をしたい場合の方法

# list関数を使う
print(list(dict_1.items())) # [('YEAR', '2010'), ('MONTH', '1'), ('DAY', '20')]
                                    # ↑↑ リストの値はタプル
list_dict_1 = list(dict_1.items())
print(type(list_dict_1[0])) # <class 'tuple'>

# 指定した key が入っているか確認する
print('YEAR' in dict_1) # True
print('YEARS' in dict_1) # False
