# len関数
str_len = len('Hello World')
print(str_len)
msg = 'Good-bye World'
str_len = len(msg)
print(str_len)

# インデックス
msg = 'Hello'
print(msg[0])

# 負の値
msg = 'Hello'
# print(msg[len(msg)-1])
# print(msg[-1])

# 文字列のスライス
print(msg[::])

# ↓インタラクティブモードに入力↓

# 'Setagaya' in 'Yoyogi, Shibuya-ku, Tokyo, Japan'
# 'Setagaya' not in 'Yoyogi, Shibuya-ku, Tokyo, Japan'

# find / rfindメソッド 
# index / rindex
sample_str = 'find, rfind,  index, rindex'
# print(sample_str.find('index'))
# print(sample_str.rfind('index'))
# print(sample_str.find('foo'))
# print(sample_str.index('find'))
# print(sample_str.rindex('find'))
# print(sample_str.index('foo'))

a = len(sample_str)
print(a)