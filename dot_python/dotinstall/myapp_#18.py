# クラスの継承
# 親クラス = スーパークラス
# 子クラス = サブクラス

class User:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print("hi {0}".format(self.name))

class AdminUser(User): # 引数に親クラス（スーパーユーザー）を入れれば、継承はOK
    def __init__(self, name, age):
        super().__init__(name) # super()でスーパーユーザーのnameを継承
        self.age = age
    def say_hello(self):
        print("hello {0} ({1})".format(self.name, self.age))
    def say_hi(self): # 親クラスのメソッドを上書きする事ができる = メソッドのオーバーライド(override)
        print("hi {0}".format(self.name))

bob = AdminUser("bob", 23)
print(bob.name)
bob.say_hi()
bob.say_hello()
