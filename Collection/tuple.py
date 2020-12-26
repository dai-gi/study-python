# Python-izm｜タプル
import datetime

def get_today():
    
    today = datetime.datetime.today()
    value = (today.year, today.month, today.day)

    return value


test_tuple = get_today()
print(test_tuple) # (2020, 12, 26)
print(test_tuple[0]) # 2020
print(test_tuple[1]) # 12
print(test_tuple[2]) # 26
