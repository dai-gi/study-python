# set関数
set_func = set('python') # {'o', 'y', 'n', 'p', 't', 'h'}
print(set_func)
print('-----------')

# セットに変換
scores = {'network':60, 'database':80, 'security':60}
print(set(scores)) # {'network', 'security', 'database'}
# ディクショナリの値をセット化する
print(set(scores.values())) # ['network', 'database', 'security']
print('-----------')
