# 四則演算
test_integer = 100

# 足し算
print(test_integer + 10) # 100

# 引き算
print(test_integer - 10) # 90

# 乗算
print(test_integer * 10) # 1000

# 除算
print(test_integer / 10) # 10.0
print('------------------')


# 浮動小数点
test_str = '100.5'
print(float(test_str) + 100) # 200.5

test_float = .5
print(test_float) # 0.5
print('------------------')

# 虚数(j)・複素数
test_complex = 100 + 5j
print(test_complex) # (100+5j)

# realメソッド(複素数から実部を取得)
print(test_complex.real) # 100.0 <- 実部

# imagメソッド(複素数から虚部を取得)
print(test_complex.imag) # 5.0 <- 虚部
print('------------------')
