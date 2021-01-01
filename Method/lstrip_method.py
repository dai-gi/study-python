# lstripメソッド(先頭の削除)
test_str = '     python-izm.com'
print(test_str) #      python-izm.com

test_str = test_str.lstrip()
print(test_str) # python-izm.com

test_str = test_str.lstrip('python')
print(test_str) # -izm.com
