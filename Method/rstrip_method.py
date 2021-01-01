# rstripメソッド(末尾の削除)
test_str = 'python-izm.com     '
print(test_str + '/') # python-izm.com     /

test_str = test_str.rstrip()
print(test_str + '/') # python-izm.com/

test_str = test_str.rstrip("com")
print(test_str) # python-izm.
