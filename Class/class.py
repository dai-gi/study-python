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