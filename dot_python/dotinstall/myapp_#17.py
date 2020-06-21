# アクセス制限 
"""
クラスの変数やメソッドにアクセス制限をつける方法：
他言語のように private 等の仕組みはないので、慣習的に書くルールだけがある
"""

# 例）クラスの外から name とゆう属性にアクセスしてほしくないケース
# 慣習的の場合：nameの前にアンダースコアを入れる　※ 慣習的なお約束のため、普通にアクセス出来てしまう
# 厳密にしたい場合：nameの前にアンダースコアを2つ入れる ※ name の前に _User_ をつけるとアクセス出来てしまう

class User:
    def __init__(self, name):
        self.__name = name
    def say_hi(self):
        print("hi {0}".format(self._name))
    
tom = User("tom")
print(tom._User__name)

# tom.say_hi()
# bob.say_hi()

