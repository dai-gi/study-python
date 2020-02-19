# # 繰り返し処理とは
# # for文
# message = 'Hello Python'

# for ch in message:
#     print(ch)

# message = ' '

# for ch in message:
#     print(ch)

# # for文とrange関数による繰り返し処理
# for number in range(10):
#     print(number)

# message = 'Hello Python'
# str_count = len(message)

# for index in range(str_count):
#     print(message[index])

# for num in range(5):
#     print(num)
# else:
#     print('terminated')

# # for文とリスト
# names = ['一色', 'かわさき', '遠藤']

# for name in names:
#     print(name)

# # break文とcontinue文による繰り返し処理の中断と継続
# names = ['一色', 'かわさき', '遠藤']
# target = 'かわさき'

# for name in names:
#     if target in name:
#         print(f'発見: {name}')
# else:
#     print('見つかりませんでした')

# # break文 
# names = ['一色', 'かわさき', '遠藤']
# target = 'かわさき'

# for name in names:
#     if target in name:
#         print(f'発見: {name}')
#         break
# else:
#     print('見つかりませんでした')

# # continue文 
# names = ['一色', 'かわさき','かわさきしんじ','遠藤']
# target = 'かわさき'

# for name in names:
#     if target in name:
#         print(f'発見: {name}')
#         break
#     print('繰り返し処理を継続します')
# else:
#     print('見つかりませんでした')

# names = ['一色', 'かわさき','かわさきしんじ','遠藤']
# target = 'かわさき'

# for name in names:
#     if target in name:
#         print(f'発見: {name}')
#         continue
#     print('繰り返し処理を継続します')
# else:
#     print('見つかりませんでした')

names = ['一色', 'かわさき','かわさきしんじ','遠藤']
target = 'かわさき'
found = False

for name in names:
    if target in name:
        found = True
        print(f'発見: {name}')
        continue
    print('繰り返し処理を継続します')

if not found:
    print('見つかりませんでした')
