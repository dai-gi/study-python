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
