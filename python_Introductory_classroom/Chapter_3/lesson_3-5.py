# 『lesson３-５ 文字列と数値を一度に表示するには　文字列を連結してみよう 』
# 【「＋」で連結する】
print("abc"+"cde") # 「＋」の記号を使うと文字を連結できる。

# 【いくつでも連結できる】
print("abc"+"cde"+"def"+"hig")
print("abc"*3) #「＊」（アスタリスク）は繰り返しを意味する。

# 【文字列と数値は連結できない】
# print("abc"+123)
# 「＋」で文字列と数値を連結できない。
# 実行すると、「TypeError: can only concatenate str (not "int") to str」というエラーが出てしまう。
# 「＋」という記号は「文字列の場合は連結」「数値の場合は足し算」とそれぞれ違う意味で作用する為,エラーになってしまう。
# 解決法 = 数値を文字列に変換すればいい。数値を「”」or「’」で括れば、文字列に変換される。
print("abc"+"123")

# 【計算結果と連結したいとき】
# print("abc"+"123*234")と記述して実行しても数値は計算されずに「abc123*234」のような実行結果が表示される。
# 解決法 = str関数を使う。
# 「関数」= 何か「値」を関数に渡す → 「値」を計算や加工をする → 「値」を計算や加工した結果にして戻してくれる。= 「関数を呼び出す（call）」という。
# 「str関数」= 括弧の中に数値を入力。その数値を計算した後、文字列に変換した値にして実行結果に表示してくれる関数。
print("abc"+str(123*234))
