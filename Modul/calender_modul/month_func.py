# いちばんやさしいPython入門教室
# calendar.month関数

# from
from calendar import month # <- 「from」を使うとモジュール名を書かずにメソッドを使うことが出来るようになる
print(month(2020,1))
"""""""""""""""""
出力結果：

　    January 2020
　Mo Tu We Th Fr Sa Su
　     1  2  3  4  5
　 6  7  8  9 10 11 12
　13 14 15 16 17 18 19
　20 21 22 23 24 25 26
　27 28 29 30 31

"""""""""""""""""

# as
import calendar as cal # <- 「as」を使うとモジュール名を変更する事ができる
print(cal.month(2020,1))

"""""""""""""""""
出力結果：

　    January 2020
　Mo Tu We Th Fr Sa Su
　       1  2  3  4  5
　 6  7  8  9 10 11 12
　13 14 15 16 17 18 19
　20 21 22 23 24 25 26
　27 28 29 30 31

"""""""""""""""""