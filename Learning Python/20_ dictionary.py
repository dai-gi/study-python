# # 辞書とは
# # 辞書の定義
# sk = {'first_name': 'shinji', 'family_name': 'kawasaki', 'weight': 80}
# print(sk)

# sk = {'first_name': 'shinji', 'family_name': 'kawasaki', 'weight': 80,
#     'family_name': 'okazaki'}
# print(sk)

# # dict関数による辞書の作成
# mydict = dict()  # 空の辞書の作成
# print(mydict)
# mydict = dict(foo='foo', bar='bar')  # キーワード引数による辞書作成
# print(mydict)
# mydict = dict({'foo': 'FOO', 'bar': 'BAR'})  # 辞書を基にした辞書作成
# print(mydict)
# mydict = dict([('foo', 1), ['bar', 2]])  # 反復可能オブジェクトを使った辞書作成
# print(mydict)
# mydict = dict({'foo': 'FOO', 'bar': 'BAR'}, baz='baz')  # 組み合わせ
# print(mydict)

# # # 辞書の内包表記
# urls = ['https://someurl1', 'https://someurl2', 'https://someurls3']
# pvs = [12345, 123456, 1234567]
# authors = ['kawasaki', 'isshiki', 'endo']

# pv_data = {u: {'pv': p, 'author': a} for u, p, a in zip(urls, pvs, authors)}
# for key, value in pv_data.items():
#     print(key, value['pv'], value['author'])

# # 辞書の要素の取り出し
# sk = {'first_name': 'shinji', 'family_name': 'kawasaki', 'weight': 80}
# print(sk['first_name'])

# sk = {'first_name': 'shinji', 'family_name': 'kawasaki', 'weight': 80}
# print(sk['age'])  # 年齢はこのデータには含まれていない

# # getメソッド
# sk = {'first_name': 'shinji', 'family_name': 'kawasaki', 'weight': 80}
# print(sk.get('first_name'))  # 存在するキーを指定
# print(sk.get('age'))         # 存在しないキーを指定
# print(sk.get('age', 'not found'))  # 存在しないキーと、デフォルト値を指定

# # 辞書の項目の変更と追加
# sk['family_name'] = 'okazaki'
# print(sk)

# sk['age'] = 150
# print(sk)

# # どちらもエラー（TypeError例外）となる
# sk = sk + {'height': 220}
# sk += {'height': 220}

# # 辞書の操作
# mydict = {'foo': 'FOO', 'bar': 'BAR', 'baz': 'BAZ'}
# print(mydict)  # 元の辞書
# mydict.update(foo='fooo', somekey='somevalue')  # キーワード引数による辞書の更新
# print(mydict)
# mydict.update({'bar': 'new BAR'})  # 辞書による辞書の更新
# print(mydict)
# mydict.update([('baz', 'new Baz'), ['x', 1]])  # リストによる辞書の更新
# print(mydict)
# mydict.update([('y', 2)], z=3)  # 両者の組み合わせ
# print(mydict)

# # popメソッドによる値の取得と削除
# mydict = {'foo': 'foo', 'bar': 'bar', 'baz': 'baz'}
# print(mydict)
# result = mydict.pop('bar')  # キー'bar'に対応する項目を削除
# print(result)  # 削除した項目が戻り値になる
# result = mydict.pop('bar', 'not found')  # デフォルト値を指定
# print(result)  # キー'bar'はないので、デフォルト値が戻り値になっている
# result = mydict.pop('bar')  # キー'bar'はもう存在しないのでエラー

# # popitemメソッドによる項目の取得と削除
# import sys
# print(sys.version)  # この環境のPythonのバージョンを確認する

# mydict = {'foo': 'foo', 'bar': 'bar', 'baz': 'baz'}
# print(mydict.popitem())
# print(mydict.popitem())
# print(mydict.popitem())
# print(mydict.popitem())

# # setdefaultメソッドによる項目の存在確認と追加
# mydict = {'foo': 'foo', 'bar': 'bar'}
# print(mydict.setdefault('foo'))  # 存在するキーを指定すれば、その値が返される
# print(mydict.setdefault('baz', 'baz'))  # 存在しないキーを指定
# print(mydict)

# # 辞書の項目の反復処理とkeys／values／itemsメソッド
# sk = {'first_name': 'shinji', 'family_name': 'kawasaki', 'weight': 80}
# for item in sk:
#     print(item)

# sk = {'first_name': 'shinji', 'family_name': 'kawasaki', 'weight': 80}
# for item in sk:
#     print(item, sk[item])

# sk = {'first_name': 'shinji', 'family_name': 'kawasaki', 'weight': 80}
# for key, value in sk.items():
#     print(key, value)

# mydict = {'foo': 'foo'}
# myview = mydict.keys()
# print(myview)
# mydict['bar'] = 'bar'
# print(myview)

# # 辞書の使いどころ
# pv = 0
# for key, value in page_data.items():
#     if value['pv'] > pv:
#         top_article = value
#         top_article_url = key
#         pv = value['pv']

# print(f'top article is {top_article["title"]}')
# print(f'top author is {top_article["author"]}')
# print(f'top page view is {top_article["pv"]}')
# print(f'top article url: {top_article_url}')

# 辞書のキーはイミュータブル
key_tuple1 = (1, 2)
key_tuple2 = ([0, 1], [2, 3])  # タプルの要素のリストは変更可能

mydict1 = {key_tuple1: 'foo'}
mydict2 = {key_tuple2: 'bar'}  # エラー

