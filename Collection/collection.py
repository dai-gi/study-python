scores = {'network':60, 'database':80, 'security':60}

リストに変換 
print(list(scores)) # ['network', 'database', 'security']
# ディクショナリの値をリスト化する
print(list(scores.values())) # [60, 80, 60]
print('-----------')


# タプルに変換
print(tuple(scores)) # ('network', 'database', 'security')
# ディクショナリの値をタプル化する
print(tuple(scores.values())) # ['network', 'database', 'security']
print('-----------')


# セットに変換
print(set(scores)) # {'network', 'security', 'database'}
# ディクショナリの値をセット化する
print(set(scores.values())) # ['network', 'database', 'security']
print('-----------')


# ２つのリストを使って、ディクショナリを生成する
key = list(scores) # ['network', 'database', 'security']
value = list(scores.values()) # [60, 80, 60]
print(dict(zip(key, value))) # {'network':60, 'database':80, 'security':60}
print('-----------')


# コレクションのネスト
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
