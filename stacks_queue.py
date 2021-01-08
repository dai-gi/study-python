# @IT
# スタックとキュー
# スタックを定義する
# MyStackの定義
class MyStack:
    def __init__(self):
        self.stack = []  # 空のリストをスタックに保存するデータの入れ物とする
    def push(self, item):
        pass  # 取りあえず何もしない
    def pop(self):
        pass  # 取りあえず何もしない

# pushメソッドの定義
class MyStack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        pass  # 取りあえず何もしない

mystack = MyStack()
mystack.push(0)  # スタックに「0」をプッシュ（リストの末尾に「0」を追加）
mystack.push(1)  # スタックに「1」をプッシュ（リストの末尾に「1」を追加）
mystack.push(2)  # スタックに「2」をプッシュ（リストの末尾に「2」を追加）
print(mystack.stack)  # MyStackクラスのインスタンスのインスタンス変数の値を表示

# popメソッドの定義
class MyStack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        result = self.stack[-1]  # 末尾の要素を変数に取り出す
        del self.stack[-1]  # リストから要素を削除する
        return result  # リスト末尾から取り出したデータを返送する

mystack = MyStack()
mystack.push(0)
mystack.push(1)
print(mystack.pop())
print(mystack.pop())

class MyStack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop()

print(mystack.pop())

class MyStack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

mystack = MyStack()
mystack.push(0)
print(mystack.pop())
print(mystack.pop())

# キューを定義する
class MyQueue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        if len(self.queue) == 0:
            return None
        result = self.queue[0]
        del self.queue[0]
        return result

myq = MyQueue()
myq.enqueue(0)
myq.enqueue(1)
print(myq.dequeue())
print(myq.dequeue())
print(myq.dequeue())

# スタックをより使いやすくする
# 特殊メソッド
mystack = MyStack()
print(str(mystack))
print(repr(mystack))

# インスタンスの生成時に、初期値を与える
class MyStack:
    def __init__(self, *args):
        self.stack = []
        for item in args:
            self.stack.append(item)
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

mystack = MyStack(1, 2, [3, 4])
print(mystack.stack)

# print関数などに、インスタンスを渡したときにその要素が表示されるようにする
class MyStack:
    def __init__(self, *args):
        self.stack = []
        for item in args:
            self.stack.append(item)
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()
    def __repr__(self):
        return 'MyStack(' + repr(self.stack) + ')'

mystack = MyStack(1, 2, [3, 4])
print(repr(mystack))
print(mystack)

class MyStack:
    def __init__(self, *args):
        self.stack = []
        for item in args:
            self.stack.append(item)
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()
    def __repr__(self):
        return 'MyStack(' + repr(self.stack) + ')'
    def __str__(self):
        return str(self.stack)

mystack = MyStack(1, 2, [3, 4])
print(repr(mystack))
print(mystack)

mystack = MyStack(1, 2, [3, 4])
for item in mystack:
    print(item)

class MyStack:
    def __init__(self, *args):
        self.stack = []
        for item in args:
            self.stack.append(item)
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()
    def __repr__(self):
        return 'MyStack(' + repr(self.stack) + ')'
    def __str__(self):
        return str(self.stack)
    def __iter__(self):
        return iter(self.stack)

mystack = MyStack(1, 2, [3, 4])
for item in mystack:
    print(item)

# インデックス指定により、スタック中の特定の要素を取得する
class MyStack:
    def __init__(self, *args):
        self.stack = []
        for item in args:
            self.stack.append(item)
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()
    def __repr__(self):
        return 'MyStack(' + repr(self.stack) + ')'
    def __str__(self):
        return str(self.stack)
    def __iter__(self):
        return iter(self.stack)
    def __getitem__(self, key):
        return self.stack[key]

mystack = MyStack(1, 2, [3, 4])
print(mystack[0])

