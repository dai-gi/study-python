# ディクショナリ
"""
辞書は「格納されているデータに名前をつけることで付けることで扱いを容易にする」
「整数インデックスでは管理が難しいデータを扱う」ためのもの

ディクショナリで使う関数・メソッド

・ネスト
・内包表記

構文：
・del文

関数：
・dict関数

メソッド：
・getメソッド
・keyメソッド
・valueメソッド
・itemメソッド
・updateメソッド
・popメソッド
・popitemメソッド
・setdefaultメソッド

"""

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

# ２つのリストを使って、ディクショナリを生成する
scores = {'network':60, 'database':80, 'security':60}
key = list(scores) # ['network', 'database', 'security']
value = list(scores.values()) # [60, 80, 60]
print(dict(zip(key, value))) # {'network':60, 'database':80, 'security':60}
print('-----------')

# ネスト
matsuda_scores = {'network':40, 'database':80}
asagi_scores = {'network':50, 'database':70}
member_scores = {
    '松田':matsuda_scores, # <- matsuda_scoresディクショナリを値にしている
    '浅木':asagi_scores # <- asagi_scoresディクショナリを値にしている
}
print(member_scores)
# 出力結果： {'松田': {'network': 40, 'database': 80}, '浅木': {'network': 50, 'database': 70}}
#               　　　↑↑ 上記のディクショナリ in ディクショナリの状態をネストと言う ↑↑
print('-----------')

# 内包表記
urls = ['https://someurl1', 'https://someurl2', 'https://someurls3']
pvs = [12345, 123456, 1234567]
authors = ['kawasaki', 'isshiki', 'endo']

pv_data = {u: {'pv': p, 'author': a} for u, p, a in zip(urls, pvs, authors)}
for key, value in pv_data.items():
    print(key, value['pv'], value['author'])
"""出力結果：
https://someurl1 12345 kawasaki
https://someurl2 123456 isshiki
https://someurls3 1234567 endo
"""

# @IT
# 辞書の使いどころ
"""辞書は「格納されているデータに名前をつけることで付けることで扱いを容易にする」
「整数インデックスでは管理が難しいデータを扱う」ためのもの"""

page_data = {
    'https://www.atmarkit.co.jp/ait/articles/1906/14/news015.html':
    {
        'author': 'かわさき しんじ',
        'title': 'タプル',
        'pv': 123456
    },
    'https://www.atmarkit.co.jp/ait/articles/1906/13/news021.html':
    {
        'author': '一色 政彦',
        'title': 'Deep Learningコミュニティー……',
        'pv': 1234567
    },
    'https://www.atmarkit.co.jp/ait/articles/1906/04/news009.html':
    {
        'author': 'かわさき しんじ',
        'title': 'リストの操作',
        'pv': 123456789 # <- ＊＊
    }
}

pv = 1
for key, value in page_data.items():
    if value['pv'] > pv: # <- この条件分岐で、上記にある「＊＊」だけが出力されてしまう。またどこかで調べてみることにする。
        print(value['pv'])
        top_article = value
        top_article_url = key
        pv = value['pv']

print(f'top article is {top_article["title"]}')
print(f'top author is {top_article["author"]}')
print(f'top page view is {top_article["pv"]}')
print(f'top article url: {top_article_url}')


# 辞書のキーはイミュータブル(変更不可能)
"""文字列やタプル(=イミュータブル)は辞書のキーとして使えるが、リストと辞書は要素を
変更できるので辞書のキーとして、使うことができない"""

key_tuple1 = (1, 2)
key_tuple2 = ([0, 1], [2, 3])

mydict1 = {key_tuple1: 'foo'}
mydict2 = {key_tuple2: 'bar'} # TypeError: unhashable type: 'list'
print(mydict1) # {(1, 2): 'foo'}
# print(mydict2)
