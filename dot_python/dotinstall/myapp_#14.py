# コンストラクタ

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
    def __init__(self, name): # selfは、Userクラスのインスタンス(tom・bob)を指す
        # インスタンス変数
        self.name = name

tom = User("tom") # Userクラスのインスタンス　変数に入れた時インスタンス化される
bob = User("bob") # Userクラスのインスタンス

print(tom.name)
print(bob.name)
