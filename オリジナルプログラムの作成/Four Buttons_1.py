# ランダムに1桁の整数を選ぶプログラム
# coding:utf-8

import random
import tkinter as tk
import tkinter.messagebox as tmsg



root = tk.Tk()
root.geometry('400x350')
root.title('Random Button')

button1 = tk.Button(root, text = ' 1 ', font=('Helvetica',80),fg='red',bg="red")
button1.place(x = 46, y = 74)
# button1.config(bg="pink")


root.mainloop()

