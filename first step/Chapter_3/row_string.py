# いちばんやさしいPython入門教室：P60
# row string

# befor：
print("\10,000") # ,000
# row stringを利用しない場合の対処法
print("\\10,000") # \10,000

# after：
# row stringを利用することで「¥」と「\」を特殊文字として扱わなくなる。
print(r"\10,000") # \10,000
