# いちばんやさしいPython入門教室
# if構文
for i in range(1,10+1):
    if i <= 5:
        print("小さいです")
    else:
        print("大きいです")
print('-----------')

# 複数の条件を組み合わせる
for i in range(1,10+1):
    print(i)
    if i % 2 == 0:
        print("x")
    if i % 3 == 0:
        print("y")
    if (i % 2 == 0) and (i % 3 == 0):
        print("z")
print('-----------')

# elif
for i in range(1,36+1):
    print(i)
    if(i % 12 == 0):
        print("a")
    elif(i % 4 == 0):
        print("b")
    elif(i % 2 == 0):
        print("c")
    else:
        print("d")
print('-----------')


# if not
# True(真)ならFalse(偽)・False(偽)ならTrue(真)
names = ['一色', 'かわさき','かわさきしんじ','遠藤']
target = 'かわさき'
found = False

for name in names:
    if target in name:
        found = True
        print(f'発見: {name}')
        continue
    print('繰り返し処理を継続します')

if not found: # <- foundがFalseなら下の処理を実行
    print('見つかりませんでした')


# 文字列の比較
a = '1926/12/05'
b = '1926/12/50'
c = '1926/12/5'
# b == c：'1926/12/5' <-「5」の後には「0」が有るのと同義

x = '1926/12/24'

print(a <= x) # True
print(b <= x) # False <- bはx以上
print(c <= x) # False <- cはx以上


