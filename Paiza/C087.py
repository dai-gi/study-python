# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

# from random import randint


def reverse_and_calc(li):
    n_1 = int(''.join(li))
    # print(n_1)
    
    reversed_li = list(reversed(li))
    n_2 = int(''.join(reversed_li))
    # print(reversed_li)
    
    result = n_1 + n_2
    return result
    
def jugement(number):
    n = ""
    m = str(number)
    for i in range(len(m),0,-1):
        n += m[i-1]
    if n == m:
        return int(m)
    else:
        return list(m)

# li_str = list(str(randint(1000, 9999)))
li_str = list(input())

isok = False
while isok == False:
    num = reverse_and_calc(li_str)
    result = jugement(num)
    if type(result) == int:
        print(result)
        isok = True
    else:
        li_str = result
