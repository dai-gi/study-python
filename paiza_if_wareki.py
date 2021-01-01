# paizaラーニング/レベルアップ問題集/日付セット(言語選択)/問題一覧Python3編/西暦の和暦変換
# ランクC相当

# 条件
# ・明治は1912年7月29日まで
# ・大正は1912年7月30日から1926年12月24日まで
# ・昭和は1926年12月25日から1989年1月7日まで
# ・平成は1989年1月8日から2019年4月30日まで
# ・令和は2019年5月1日から

# 解答コード例： 
y, m, d = map(int, input().split())

if y < 1912:
    print(f"明治年{m}月{d}日")
elif y == 1912:
    if (m < 7) or (m == 7 and d < 30):
        print(f"明治年{m}月{d}日")
    else:
        print(f"大正年{m}月{d}日")
elif y < 1926:
    print(f"大正年{m}月{d}日")
elif y == 1926:
    if (m < 12) or (m == 12 and d < 25):
        print(f"大正年{m}月{d}日")
    else:
        print(f"昭和年{m}月{d}日")
elif y < 1989:
    print(f"昭和年{m}月{d}日")
elif y == 1989:
    if m == 1 and d < 8:
        print(f"昭和年{m}月{d}日")
    else:
        print(f"平成年{m}月{d}日")
elif y < 2019:
    print(f"平成年{m}月{d}日")
elif y == 2019:
    if m < 5:
        print(f"平成年{m}月{d}日")
    else:
        print(f"令和年{m}月{d}日")
else:
    print(f"令和年{m}月{d}日")
