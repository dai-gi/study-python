class TestClass:

    def __init__(self, code, name):
        self.code = code
        self.name = name


classes = []
classes.append(TestClass(1, 'テスト1'))
classes.append(TestClass(2, 'テスト2'))

for test_cls in classes:
    print('===== Class =====')
    print(test_cls.code)
    print(test_cls.name)
