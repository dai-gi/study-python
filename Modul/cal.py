# いちばんやさしいPython入門教室
# calendarモジュール

# from
from calendar import month # <- 「from」を使うとモジュール名を書かずにメソッドを使うことが出来るようになる
print(month(2020,1))

# as
import calendar as cal # <- 「as」を使うとモジュール名を変更する事ができる
print(cal.month(2020,1))


# Python-izm
# isleapメソッド = その年がうるう年か判定する
# 返り値は「boolean型」

import calendar as cal

print(cal.isleap(2015)) # False

print(cal.isleap(2016)) # True

print(cal.isleap(2017)) # False

# leapdaysメソッド = 指定期間内にうるう年が何回あるかをカウントする
# 返り値はカウント数
print(cal.leapdays(2010, 2020)) # 2
