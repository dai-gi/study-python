# いちばんやさしいPython入門教室
# 文字化け：P66

# 環境によっては文字化けが起こってしまう
print("abc") # SyntaxError：Non-UTF-8 code starthig ...

"""
対処法：

①　# coding:utf-8
②　# coding=utf-8

①
# coding:utf-8
プログラムを続けて書く...

②
# coding=utf-8
プログラムを続けて書く...
"""