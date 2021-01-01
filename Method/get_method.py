# getメソッド
print(dict_1.get('YEAR')) # '2010' 

print(dict_1.get('YEAES')) # None

print(dict_1.get('YEAR', 'NOT FOUND')) # '2010'

print(dict_1.get('YEARS', 'NOT FOUND')) # 'NOT FOUND'
                            # ↑↑ 第二引数に存在しなかった場合の返り値を指定できる
print('------------------')
