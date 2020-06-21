# モジュールでファイルの分割
# 別ファイルに書いたコードをモジュールと呼ぶ
# importで読み込んだ瞬間に別ファイルで書いたモジュールのファイルが実行されてしまう

# import user
# from user import AdminUser # モジュールから指定した関数やクラスだけを読み込む場合の方法
from user import AdminUser, User # 他のクラスも使いたい場合、カンマ区切りにすれば良い

# bob = user.AdminUser("bob", 23)
bob = AdminUser("bob", 23) # モジュールから指定したサブクラスなので、モジュール名はいらない

tom = User("tom")

print(bob.name)
bob.say_hi()
bob.say_hello()


