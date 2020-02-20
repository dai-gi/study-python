# # 関数の基本と呼び出し方
# # 組み込み関数
# # ユーザー定義関数
# # def文：関数定義の構文
# # 簡単な関数の定義
# def hello(whom):
#     message = 'Hello ' + str(whom)
#     print(message)

# def hello(whom):
#     message = 'Hello ' + str(whom)
#     print(message)

# hello('World')

# # 値を返す関数
# def get_ans4ultimateQ():
#     return 42

# def get_ans4ultimateQ():
#     return 42 #関数の実行はここで終了
#     print('can not reach this line') #この行は実行されることはない

# result = get_ans4ultimateQ()
# print(result)

# # 関数の名前
# # FizzBuzzの答えを返す関数
# def fizzbuzz(number):
#     result = str(number)
#     if number % 3 and not number % 5:
#         result = 'FizzBuzz'
#     elif number % 3 == 0:
#         result = 'Fizz'
#     elif number % 5 == 0:
#         result = 'Buzz'
#     return result

# number = input('何か数値を入れてください:')
# number = int(number)

# print(fizzbuzz(number))

print(some_func())

def some_func():
    print('you nalled some_func')
