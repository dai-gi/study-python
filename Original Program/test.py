# -*- coding:utf-8 -*-
import sys
import tkinter

root = tkinter.Tk()
root.title("タイトル")
root.geometry("300x300")

# 画像の取得
img = tkinter.PhotoImage(file='bg.gif')

# 画像ウィジェットの配置(1行1列)
label1 = tkinter.Label(root, image=img)
label1.grid(row=1, column=1)

# 画像ウィジェットの配置(2行2列)
# label4 = tkinter.Label(root, image=img)
# label4.grid(row=10, column=100)

root.mainloop()