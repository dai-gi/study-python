# # for文でのリスト処理の基本
# intlist = [44, 99, 78, 36, 86, 100, 89, 48, 50, 58]
# result = intlist[0] + intlist[1] + intlist[2] + intlist[3] + intlist[4] +\
#         intlist[5] + intlist[6] + intlist[7] + intlist[8] + intlist[9]
# print(result)

# result = 0

# for number in intlist:
#     result = result + number

# print(result)

# # for文でリストの要素を変更する
# languages = ['Python', 'Ruby', 'PHP']

# print(languages)

# counter = 0
# for language in languages:
#     language = f'{counter}: {language}'
#     counter += 1

# print(languages)

# languages = ['Python', 'Ruby', 'PHP']

# print(languages)

# for index in range(len(languages)):
#     languages[index] = f'{index}: {languages[index]}'

# print(languages)

# # enumerate関数
# languages = ['Python', 'Ruby', 'PHP']

# print(languages)

# for index, language in enumerate(languages):
#     languages[index] = f'{index}: {language}'

# print(languages)

# # zip関数
# namelist = ['一色', 'かわさき', '遠藤', '島田', '小川']
# weightlist = [65, 80, 70, 75, 72]

# for index, name in enumerate(namelist):
#     print(f'{name}さんの体重は{weightlist[index]}kgです')

# for name, weight in zip(namelist, weightlist):
#     print(f'{name}さんの体重は{weight}kgです')

# shortlist = list(range(4))      # [0, 1, 2, 3]
# longlist = list(range(10, 20))  # [10, 11, 12, ..., 19]
# for x, y in zip(shortlist, longlist):
#     print(x, y)

# # イテレータと反復可能オブジェクト
# intlist = [0, 1, 2]
# iterator = iter(intlist)

# print(iterator.__next__())
# print(next(iterator))
# print(iterator.__next__())
# print(next(iterator))

# # map関数
# intlist = list(range(5))
# result = map(lambda x: x * x, intlist)
# print(intlist)
# print(list(result))  # map関数の戻り値（イテレータ）からリストを作成

# result = [x * x for x in intlist]
# print(result)

# # filter関数
# intlist = list(range(10))  # [0, 1, 2, ..., 9]
# result = filter(lambda x: x % 2 == 0, intlist)  # 偶数だけを選択
# print(intlist)
# print(list(result))

# all関数とany関数
intlist1 = list(range(5))  # [0, 1, 2, 3, 4]
intlist2 = list(range(1, 6))  # [1, 2, 3, 4, 5]
intlist3 = [0] * 5  # [0, 0, 0, 0, 0]
strlist1 = ['', 'foo', 'bar']
strlist2 = ['foo', 'bar', 'baz']
strlist3 = [''] * 5
emptylist = []

print('all(intlist1):', all(intlist1))  # False：0は「偽」と見なされる
print('all(intlist2):', all(intlist2))  # True
print('all(intlist3):', all(intlist3))  # False：0は「偽」と見なされる

print('any(strlist1):', any(strlist1))  # True
print('any(strlist2):', any(strlist2))  # True
print('any(strlist3):', any(strlist3))  # False：空文字列は「偽」と見なされる

print('all(emptylist):', all(emptylist))  # True：空のリストを渡すと戻り値はTrue
print('any(emptylist):', any(emptylist))  # False：空のリストを渡すと戻り値はFalse

