# zip関数(2つのリストの操作をすることが出来る)
namelist = ['一色', 'かわさき', '遠藤', '島田', '小川']
weightlist = [65, 80, 70, 75, 72]

for name, weight in zip(namelist, weightlist):
    print(f'{name}さんの体重は{weight}kgです')
"""""""""""""""""
出力結果：

色さんの体重は65kgです
かわさきさんの体重は80kgです
遠藤さんの体重は70kgです
島田さんの体重は75kgです
小川さんの体重は72kgです

"""""""""""""""""

shortlist = list(range(4))
longlist = list(range(10, 20))
for x, y in zip(shortlist, longlist):
    print(x, y)
"""""""""""""""""
出力結果：

0 10
1 11
2 12
3 13

"""""""""""""""""