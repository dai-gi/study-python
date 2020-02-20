# # クラスの属性
# # クラス変数（とインスタンス変数）
# class Point:
#     pass
# point1 = Point()
# point1.x = 1.0
# point1.y = 1.0
# point1.hello = lambda x: print('Hello', str(x))
# point1.hello('world')

# point2 = Point()
# point2.hello('world')  # エラー：Pointクラスの定義ではhelloメソッドはない

# # クラス変数の定義
# class MyClass:
#     count = 0  # クラス変数countの定義

# # クラス変数へのアクセス
# print(MyClass.count)

# instance = MyClass()
# print(instance.count)

# instance.count = 100
# print(instance.count)
# print(MyClass.count)

# class MyClass:
#     count = 0

#     def __init__(self):
#         self.count += 1
#         print(f'you made {MyClass.count} instance(s)')

# instance1 = MyClass()
# instance2 = MyClass()

# class MyClass:
#     count = 0

#     def __init__(self):
#         MyClass.count += 1
#         print(f'you made {MyClass.count} instance(s)')

# # クラスメソッド
# class MyClass:
#     count = 0

#     def __init__(self):
#         MyClass.count += 1
#         print(f'you made {MyClass.count} instance(s)')

#     @classmethod  # クラスメソッドの定義
#     def get_count(cls):
#         print(cls.count)  # クラス変数には「cls.クラス変数」としてアクセス

# MyClass.get_count()

# instance1 = MyClass()
# instance2 = MyClass()
# instance2.get_count()

# class MyClass:
#     count = 0

#     def __init__(self):
#         MyClass.count += 1
#         print(f'you made {MyClass.count} instance(s)')

#     @classmethod  # クラスメソッドの定義
#     def get_count(cls):
#         cls.another_get_count()

#     another_get_count = classmethod(lambda cls: print('count:', cls.count))

# MyClass.another_get_count()
# instance1 = MyClass()
# instance1.another_get_count()
# instance1.get_count()

# スタティックメソッド
class MyClass:
    count = 0

    def __init__(self):
        MyClass.count += 1
        print(f'you made {MyClass.count} instance(s)')

    @classmethod  # クラスメソッドの定義
    def get_count(cls):
        cls.another_get_count()

    another_get_count = classmethod(lambda cls: print('count:', cls.count))

    @staticmethod
    def static_get_count():
        print('count:', MyClass.count)

MyClass.static_get_count()
instance = MyClass()
instance.static_get_count()