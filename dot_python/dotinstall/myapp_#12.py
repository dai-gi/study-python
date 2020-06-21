# 変数のスコープ

# msg = "hello" #グローバル変数

# def say_hi():
#     msg = "hi" #ローカル変数
#     print(msg)

# say_hi()
# print(msg)

# msg = "hello" #グローバル変数

# 関数の中から(msg変数)を参照
# def say_hi():
#     print(msg)

# say_hi()
# print(msg)

msg = "hello" #グローバル変数

# 関数内でグローバル変数(msg変数)を書換え
def say_hi():
    global msg
    msg = "hello global"
    print(msg)

say_hi()
print(msg)