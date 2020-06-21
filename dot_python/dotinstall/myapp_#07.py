# 条件分岐

score = int(input("score ?"))

if score > 80:
    print("Great!")
elif score > 60:
    print("Good!")
else:
    print("so so ...")56

# 単に値を返したい場合
print("Great!" if score > 80 else "so so ...")