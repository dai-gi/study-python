# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
from random import randint

# num_str = input()
n_str = str(randint(1000, 9999))
print(n_str)

n_li = list(n_str)

def revers(x):
    l_n = len(x)
    
    n = 0
    m = 1
    o = 2
    while True:
        a = x[n]
        print
        b = x[l_n - m]
        x[n] = b
        x[l_n - m] = a
        n += 1
        m += 1
        if l_n == o:
            break
        else:
            o += 1
        
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
    



