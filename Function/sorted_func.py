# @IT｜[Python入門] リストの操作

# sorted関数(リストの並べ替え)
strlist = ['abcd', 'abc', 'Abcd', 'abC']
print(sorted(strlist)) # ['Abcd', 'abC', 'abc', 'abcd']

print(sorted(strlist, key=str.lower)) # ['abc', 'abC', 'abcd', 'Abcd']
