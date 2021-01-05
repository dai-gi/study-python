# getメソッド
print(dict_1.get('YEAR')) # '2010' 

print(dict_1.get('YEAES')) # None

print(dict_1.get('YEAR', 'NOT FOUND')) # '2010'

print(dict_1.get('YEARS', 'NOT FOUND')) # 'NOT FOUND'
                            # ↑↑ 第二引数に存在しなかった場合の返り値を指定できる
print('------------------')


# @ITでの学習内容
# getメソッド
sk = {'first_name': 'shinji', 'family_name': 'kawasaki', 'weight': 80}
print(sk.get('first_name')) # shinji
print(sk.get('age')) # None <- 存在しないキーを指定した場合
print(sk.get('age', 'not found')) # not found <- 存在しないキーと、デフォルト値を指定した場合
