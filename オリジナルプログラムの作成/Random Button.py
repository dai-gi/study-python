# ランダムに1桁の整数を選ぶプログラム
# coding:utf-8

import random
import tkinter as tk
import tkinter.messagebox as tmsg

# classで「Buttons関数」を作成
class Buttons:
    def __init__(self, random):
        self.x = random
        print(self.x)
    # def ButtonClick(self,random):
        # tmsg.showinfo("ボタンが押されました")


# 9個の変数に9個の整数を代入する
a, b, c, d, e, f, g, h, i  = 1, 2, 3, 4, 5, 6, 7, 8, 9

# for文を使用してButton1に整数の入った9個の変数を代入をする
for Button1 in (a, b, c, d, e, f, g, h, i):
    pass

# 9個の変数をランダムに選ぶ
Button1 = random.randint(a, i)

print('===================================')
Buttons(Button1)

# ウィンドウを作成する
root = tk.Tk()
root.geometry('500x500')
root.title('Random Button')

# ラベルを作成
label1 = tk.Label(root, text="ボタンを押して下さい", font = ('Helvetica', 28))
label1.place(x = 105, y = 35)

# 9個のボタンを作成
# 1段目
button1 = tk.Button(root, text = ' 1 ', font=('Helvetica',80), command=Buttons)
button1.place(x = 100, y = 130)
# button1 = tk.Button(root, text = ' 2 ', font=('Helvetica',80), command=Buttons)
# button1.place(x = 200, y = 130)
# button1 = tk.Button(root, text = ' 3 ', font=('Helvetica',80), command=Buttons)
# button1.place(x = 300, y = 130)

# # 2段目
# button1 = tk.Button(root, text = ' 4 ', font=('Helvetica',80), command=Buttons)
# button1.place(x = 100, y = 230)
# button1 = tk.Button(root, text = ' 5 ', font=('Helvetica',80), command=Buttons)
# button1.place(x = 200, y = 230)
# button1 = tk.Button(root, text = ' 9 ', font=('Helvetica',80), command=Buttons)
# button1.place(x = 300, y = 230)

# # 3段目
# button1 = tk.Button(root, text = ' 7 ', font=('Helvetica',80), command=Buttons)
# button1.place(x = 100, y = 330)
# button1 = tk.Button(root, text = ' 8 ', font=('Helvetica',80), command=Buttons)
# button1.place(x = 200, y = 330)
# button1 = tk.Button(root, text = ' 9 ', font=('Helvetica',80), command=Buttons)
# button1.place(x = 300, y = 330)






# ウィンドウを表示する
root.mainloop()
