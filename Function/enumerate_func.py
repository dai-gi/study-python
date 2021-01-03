# enumerate関数(リストから取り出した要素に「0」からのインデックスを割り当てる)
languages = ['Python', 'Ruby', 'PHP']

print(languages) # ['Python', 'Ruby', 'PHP']
print(enumerate(languages)) # <enumerate object at 0x7fa4f0bc4320>

for (index, language) in enumerate(languages):
    languages[index] = f'{index}: {language}'

print(languages) # ['0: Python', '1: Ruby', '2: PHP']


namelist = ['一色', 'かわさき', '遠藤', '島田', '小川']
weightlist = [65, 80, 70, 75, 72]

for index, name in enumerate(namelist):
    print(f'{name}さんの体重は{weightlist[index]}kgです')
"""""""""""""""""
出力結果：

一色さんの体重は65kgです
かわさきさんの体重は80kgです
遠藤さんの体重は70kgです
島田さんの体重は75kgです
小川さんの体重は72kgです

"""""""""""""""""