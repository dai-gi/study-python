# asでモジュールを読み込む

import calendar as cal
print(cal.month(2020,1))

# fromでモジュール名を書かずに済むようにする    
from calendar import month
print(month(2020,1))