# itemメソッド
print(dict_1.items()) # dict_items([('YEAR', '2010'), ('MONTH', '1'), ('DAY', '20')])

print(type(dict_1.items())) # <class 'dict_items'>

# 値を使って何か処理をしたい場合の方法

# list関数を使う
print(list(dict_1.items())) # [('YEAR', '2010'), ('MONTH', '1'), ('DAY', '20')]
                                    # ↑↑ リストの値はタプル
list_dict_1 = list(dict_1.items())
print(type(list_dict_1[0])) # <class 'tuple'>
