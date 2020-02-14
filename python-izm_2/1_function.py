# 関数の基本
# 引数の基礎
# ＋ 例外処理






def test_func(n_1, n_2, op):
    
    if op ==1:
        print('足し算')
        print(n_1 + n_2)
    else: 
        op ==2
        print('引き算')
        try:
            print(n_1 - n_2)
        except:
            print('計算出来ませんでした')
        finally:
            print('計算終了')
                
    

test_func(50, '50', 2)


