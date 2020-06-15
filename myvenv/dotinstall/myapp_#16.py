# メソッド
# クラスに定義した関数 = メソッド

class User:
    count = 0 
    def __init__(self, name): # コンストラクタもメソッドの一種になる
        User.count += 1
        self.name = name
    # インスタンスメソッド
    def say_hi(self):
        print("hi {0}".format(self.name))
    # クラスメソッド = デコレーター
    @classmethod
    def show_info(cls): 
        print("{0} instances".format(cls.count)) # クラスには cls でアクセスできる
        # クラスメソッドはインスタンス化せずに使える

tom = User("tom")
bob = User("bob") 

# tom.say_hi()
# bob.say_hi()

User.show_info()