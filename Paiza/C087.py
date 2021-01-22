# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
from random import randint

# num_str = input()
n_str = str(randint(1000, 9999))
print(n_str, end='')

n_li = list(n_str)

def revers(x):
    l_n = len(x)
    
    n = 0
    m = 1
    while True:
        a = x[n]
        b = x[l_n - m]
        x[n] = b
        x[l_n - m] = a
        if l_n == 3:
            break
        elif l_n == 4:
            break
        elif l_n == 5:
            break
        elif l_n == 6:
            break
        n += 1
        m += 1
    
    result = ''.join(x)
    print(result)
    
revers(n_li)    


# while True:
#     result = abs(int(num_str) + int(func_result))
#     result_li = list(str(result))
#     len_li1 = len(result_li)
#     if result_li[0] == result_li[len_li1 - 1]:
#         print(result)
#         break
#     else:
#         num_str = result
#         func_result = revers(list(str(result)))
    



