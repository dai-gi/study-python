# Python-izm｜クラス作成
class TestClass:

    def __init__(self, code, name):
        self.code = code
        self.name = name


classes = []
classes.append(TestClass(1, 'テスト1')) # <- インスタンス化
classes.append(TestClass(2, 'テスト2')) # <- インスタンス化

for test_cls in classes:
    print('===== Class =====')
    print(test_cls.code)
    print(test_cls.name)

"""""""""""""""""""""""
出力結果：

===== Class =====
1
テスト1
===== Class =====
2
テスト2

"""""""""""""""""""""""


# @IT
# オブジェクトとクラス
print(type('a')) # <class 'str'>

# クラスの定義
class Point:
    pass

# クラスからインスタンスを生成する
point1 = Point()
print(type(point1)) # <class '__main__.Point'>

# objectクラス
print(dir(point1))
"""['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
'__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
'__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
'__sizeof__', '__str__', '__subclasshook__', '__weakref__']"""


class Point(object):
    pass

# クラスやインスタンスの属性
# インスタンス変数
point1.x = 1.0
point1.y = 1.0

print(dir(point1))
"""['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
'__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', 
'__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', 
'__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'x', 'y']"""

# __init__メソッド
class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

point1 = Point(1.0, 1.0)
point2 = Point()
print(f'point1: ({point1.x}, ({point1.y})') # point1: (1.0, (1.0)
print(f'point2: ({point2.x}, ({point2.y})') # point2: (0.0, (0.0)

from math import sqrt
print(sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)) # 1.4142135623730951

# インスタンスメソッド
from math import sqrt

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
    def difference(self, point=None):
        if not point:
            point = Point()  # 原点を表すPointクラスのインスタンスを生成
        return sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)

point1 = Point(1.0, 1.0)
point2 = Point()
point3 = Point(5, 4)

print(point1.difference(point2)) # 1.4142135623730951
print(point1.difference()) # 1.4142135623730951
print(point3.difference(point1)) # 5.0

# クラスの属性
class Point:
    pass

point1 = Point() # <- インスタンス化
point1.x = 1.0 # <- インスタンス変数(アトリビュート)
point1.y = 1.0
point1.hello = lambda x: print('Hello', str(x))
point1.hello('hello') # Hello hello

# point2 = Point()
# point2.hello('world') # AttributeError: 'Point' object has no attribute 'hello'

# クラス変数の定義
class MyClass1:
    count = 0

# クラス変数へのアクセス
print(MyClass1.count) # 0

instance = MyClass1()
print(instance.count) # 0

instance.count = 100
print(instance.count) # 100
print(MyClass1.count) # 0

# クラスメソッド
class MyClass2:
    count = 0

    def __init__(self):
        MyClass2.count += 1
        print(f'you made {MyClass2.count} instance(s)')

    @classmethod  # <- クラスメソッド
    def get_count(cls): # <-「self」ではなく、「cls」になる
        print(cls.count)

MyClass2.get_count() # 0

instance1 = MyClass2() # you made 1 instance(s)
instance2 = MyClass2() # you made 2 instance(s)
instance2.get_count() # 2

class MyClass3:
    count = 0

    def __init__(self):
        MyClass3.count += 1
        print(f'you made {MyClass3.count} instance(s)')

    @classmethod
    def get_count(cls):
        cls.another_get_count()

    another_get_count = classmethod(lambda cls: print('count:', cls.count))

MyClass3.another_get_count() # count: 0
instance1 = MyClass3() # you made 1 instance(s)
instance1.another_get_count() # count: 1
instance1.get_count() # count: 1

# スタティックメソッド
class MyClass4:
    count = 0

    def __init__(self):
        MyClass4.count += 1
        print(f'you made {MyClass4.count} instance(s)')

    @classmethod  # クラスメソッドの定義
    def get_count(cls):
        cls.another_get_count()

    another_get_count = classmethod(lambda cls: print('count:', cls.count))

    @staticmethod
    def static_get_count():
        print('count:', MyClass4.count)

MyClass4.static_get_count() # count: 0
instance = MyClass4() # you made 1 instance(s)
instance.static_get_count() # count: 1