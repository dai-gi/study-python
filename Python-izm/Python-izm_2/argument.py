# Python-izm｜可変長引数 

# *args
def test_args1(*args):
    print(args)

test_args1(1, 2, 3, 4, 5) # (1, 2, 3, 4, 5)
print('-----------')
print('')

def test_args2(code, name, *args):
    print(code, name)
    print(args)

test_args2(100, 'python-izm', 'JP', 'US')

"""""""""""""""""
出力結果：

100 python-izm
('JP', 'US')

"""""""""""""""""
print('-----------')
print('')


# **kwargs
def test_args2(**kwargs):
    print(kwargs)

test_args2(email='xxx.com', city='Tokyo') # {'email': 'xxx.com', 'city': 'Tokyo'}
