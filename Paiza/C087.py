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
    
# it-swarm-ja.tech｜「Pythonを使用して、整数を反転し、回文を確認します」の質問に対する回答を参照
def jugement(number):
    a="" # 空の文字列を代入
    x=str(number) # 文字列の整数を生成
    # print(x)
    for i in range(len(x),0,-1): # len(x) = x変数の桁数
        # print(i)
        a+=x[i-1] # 「x」の値を末尾から「a」に累積代入(複合代入)
        # print(x[i-1])
        # print(a)
    if a==x: # a = 「x」の値を反転した文字列、これを「x」と比較し同じであれば、回文と判定
        # print(x)
        # print(a)
        return True
    else:
        print(x)
        print(a)
        return False


# li_str = list(str(randint(1000, 9999)))
li_str = list(input())
num = reverse_and_calc(li_str)

print(jugement(1222))
