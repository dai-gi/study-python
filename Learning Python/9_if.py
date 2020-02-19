# # 制御構造とは
# # 条件分岐
# number = input('何か数値を入れてください:')
# number = int(number)

# if number %2 == 0:
#     print('even')

# # if～else文
# number = input('何か数値を入れてください:')
# number = int(number)

# if number %2 == 0:
#     print('even')
# else:
#     print('odd')

# # if～elif～else文
# number = input('何か数値を入れてください:')
# number = int(number)

# if number % 3 == 0:
#     print('Fizz')
# elif number % 5 == 0:
#     print('Buzz')
# elif number % 15 == 0:
#     print('FizzBuzz')
# else:
#     print(number)

# number = input('何か数値を入れてください:')
# number = int(number)

# if number % 15 == 0:
#     print('FizzBuzz')
# elif number % 3 == 0:
#     print('Fizz')
# elif number % 5 == 0:
#     print('Buzz')
# else:
#     print(number)

# print(7 % 2 == 0)

# print(6 % 2 == 0)

number = input('何か数値を入れてください:')
number = int(number)

if not number % 3 and not number % 5:
    print('FizzBuzz')
elif not number % 3:
    print('Fizz')
elif not number % 5:
    print('Buzz')
else:
    print(number)