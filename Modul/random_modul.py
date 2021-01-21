# @IT
# import文：モジュールをインポートする
import random

print(random.randint(1, 20)) # 14

# import as文：指定した名前でインポート
import random as rnd

print(rnd.randint(1, 20)) # 1
print(random.randint(1, 20)) # 15

# from import文：特定の関数だけをインポート
from random import randint

print(randint(1, 20)) # 4

# 桁数を指定
# 3桁
print(randint(100, 999)) # 787
# 4桁
print(randint(1000, 9999)) # 3296
