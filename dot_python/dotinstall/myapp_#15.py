# クラス変数

# class User:
#     pass

# tom = User() # Userクラスのインスタンス
# tom.name = "tom"
# tom.score = 20

# bob = User() # Userクラスのインスタンス
# bob.name = "bob"
# bob.level = 5

# print(bob.name)
# print(tom.score)

class User:
    count = 0 # クラス変数 0で初期化
    def __init__(self, name="tom", count=5): # selfは、Userクラスのインスタンス(tom・bob)を指す
        # コンストラクタの引数はインスタンス変数の順番通りでないとエラーが出る
        User.count += 1 # クラス変数にアクセスする方法：クラス名の後に続けて書けば良い
        self.name = name # インスタンス変数
        self.count = count

print(User.count)
tom = User() # Userクラスのインスタンス　変数に入れた時インスタンス化される
bob = User("bob") # Userクラスのインスタンス
print(tom.name)
print(User.count)

print(tom.count) # クラス変数をインスタンスから呼ぶ場合、同名のインスタンス変数がない場合はクラス変数が呼び出される