# いちばんやさしいPython入門教室
# calendarモジュール

# as
import calendar as cal # <- 「as」を使うとモジュール名を変更する事ができる
print(cal.month(2020,1))

# from
from calendar import month
print(month(2020,1)) # <- 「from」を使うとモジュール名を省略できる