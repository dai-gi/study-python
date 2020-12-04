# いちばんやさしいPython入門教室

# 文字列：P57
# 「"」と「'」の使い分けは自由
print("abc") # abc
print('abc') # abc

# NG例
print("abc') 
# 出力結果：SyntaxError: EOL while scanning string literal


# 文字列の連結：P61
# 「+」は連結
print("abc" + "cde") # abccde

# 「＊」は繰り返し
print("abc" * 3) # abcabcabc

# 文字列と数値は連結できない
print("abc" + 3) # TypeError: can only concatenate str (not "int") to str

# 文字列型に変換
x = 3 
print(type(x)) # <class 'int'>
x_str = str(x)
print(type(x_str)) # <class 'str'>