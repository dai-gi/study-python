# クラスの多重継承
# A, B -> C # 複数の親クラスを継承

class A:
    def say_a(self):
        print("A!")
    
    def say_hi(self):
        print("hi from A!")
    

class B:
    def say_b(self):
        print("B!")

    def say_hi(self):
        print("hi from B!")
    
class C(A, B):
    pass

c = C()
c.say_a()
c.say_b()
"""
A, Bのスーパーユーザー共に同じメソッドがあった場合、Cクラスで継承したsay_hi()のメソッドの呼び出したら、
Cクラスの第1引数で継承したスーパーユーザーのメソッドが呼び出される。
"""
c.say_hi() 