# Python-izm｜コマンドライン引数
import sys

args = sys.argv

print(args)
print('第1引数：' + args[1])
print('第2引数：' + args[2])
print('第3引数：' + args[3])

# @IT
# 環境のバージョンを確認
import sys
print(sys.version)
"""出力結果：
3.7.4 (default, Aug 13 2019, 15:17:50) 
[Clang 4.0.1 (tags/RELEASE_401/final)]
"""