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
