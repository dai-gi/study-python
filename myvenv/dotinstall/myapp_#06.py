# 文字列に値を埋め込む
name = "daisuke"
score = 52.8

print("name: %s, score: %f" % (name, score))
# 値が文字列の場合 = %s
# 値が浮動少数点数の場合 = %f
# 値が整数の場合 = %d

print("name: %-10s, score: %-10.2f" % (name, score))
# 文字列の表示数を指定する方法 = %[-(ハイフンを入れると左揃えになる)幅数]s
# 数値の表示する桁数を指定する方法 = %[-(ハイフンを入れると左揃えになる)幅数.桁数]f

print("name: {0}, score: {1}" .format(name, score))
print("name: {0:>10s}, score: {1:<10.2f}" .format(name, score))
# 文字列の表示数を指定する方法 = {0[:>(大なりを入れると右揃えになる)幅数s]}
# 数値の表示する桁数を指定する方法 = {0[:>(大なりを入れると右揃えになる)幅数.桁数f]}

