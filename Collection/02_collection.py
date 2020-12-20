# # コレクションの応用

# # ディクショナリをリスト・タプル・セットに変換
# scores = {'network':60, 'database':80, 'security':60}
# print(list(scores))
# print(tuple(scores))
# print(set(scores))
# print(list(scores.values()))
# print(tuple(scores.values()))
# print(set(scores.values()))

# print('------------------------------')
# # ２つのリストからディクショナリを生成
# key = list(scores)
# value = list(scores.values())
# print(key)
# print(value)
# print(dict(zip(key, value)))

# print('------------------------------')
# # コレクションのネスト
# matsuda_scores = {'network':40, 'database':80}
# asagi_scores = {'network':50, 'database':70}

# member_scores = {
#     '松田':matsuda_scores,
#     '浅木':asagi_scores
# }
# print(member_scores)

# print('------------------------------')
# 練習問題
# ２−１
# (1) ディクショナリ
# (2) リスト
# (3) セット
# (4) セット
# (5) ディクショナリ

# ２−２
japanease = input('点数を入力して下さい>>')
count = input('点数を入力して下さい>>')
science = input('点数を入力して下さい>>')
social = input('点数を入力して下さい>>')
english = input('点数を入力して下さい>>')

dic = {'国語':japanease, '算数':count, '理科':science, '社会':social, '英語':english}
