# 学んだ事を記述 

# pylint
"""""""""""""""""
Pythonのコードチェッカー

エラー：
Final newline missing = 最後は一行の空行を入れる
"""""""""""""""""

# イテレータ = 反復子
"""""""""""""""""
2021/1/1
リスト等の複数の要素を持った配列型のオブジェクトに対して、要素を順番に取り出す機能のこと
"""""""""""""""""

# 2021/1/2｜コンテナオブジェクト = 配列型オブジェクト?

# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

num_str = input()

def revers(x):
    len_li = len(x)
    if len_li == 3:
        a = x[0]
        b = x[len_li - 1]
        x[0] = b
        x[len_li - 1] = a
        result = ''.join(x)
    elif len_li == 4:
        a = x[0]
        b = x[len_li - 1]
        x[0] = b
        x[len_li - 1] = a

        c = x[1]
        d = x[len_li - 2]
        x[1] = d
        x[len_li - 2] = c
        result = ''.join(x)
    return result

num_li = list(num_str)
func_result = revers(num_li)

while True:
    n = abs(int(num_str) + int(func_result))
    li_str = list(str(n))
    len_n = len(li_str)123
    if len_n == 3:
        if li_str[0] == li_str[len_n - 1]:
            print(n)
            break
        else:
            num_str = n
            func_result = revers(list(str(n)))
    elif len_n == 4:
        if li_str[0] == li_str[len_n - 1]:
            if li_str[1] == li_str[len_n - 2]:
                print(n)
                break
        else:
            num_str = n
            func_result = revers(list(str(n)))
    

