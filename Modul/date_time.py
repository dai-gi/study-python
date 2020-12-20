# datetimeモジュール
import datetime

today = datetime.date.today()
todaydetail = datetime.datetime.today()

# # 今日
# print(today) # 2020-12-20

# print(todaydetail) # 2020-12-20 16:56:35.889743

# print(todaydetail.year) # 2020

# print(today.month) # 12

# print(today.day) # 20

# print(todaydetail.hour) # 16

# print(todaydetail.minute) # 56

# print(todaydetail.second) # 35

# print(todaydetail.microsecond) # 889743


# # 日付のフォーマット
# print(today.isoformat()) # 2020-12-20

# print(todaydetail.strftime("%Y/%m/%d %H:%M:%S")) # 2020/12/20 17:01:30


# 明日の日付(実行日の日付：2020-12-20)
print(today + datetime.timedelta(days=1)) # 2020-12-21

# 2010年、年始の日付
newyear = datetime.datetime(2010, 1, 1)
print(newyear) # 2010-01-01 00:00:00

# 2010年1月1日の1週間後
print(newyear + datetime.timedelta(days=7)) # 2010-01-08 00:00:00

# 2010年1月1日から今日までの日数
calc = todaydetail - newyear
print(calc.days) # 4006


