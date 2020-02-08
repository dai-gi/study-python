# フォントの種類とサイズを変える
# coding:utf-8
import tkinter as tk

root = tk.Tk()
root.geometry("400x150")
root.title("数を入力してね")

label1 = tk.Label(root, text="数を入力してね", font=("Helvetica", 14))#　フォントの種類をサイズを変更
label1.place(x = 20, y = 20)



editbox1 = tk.Entry(root, width = 4, font=("Helvetica", 28))#　フォントの種類をサイズを変更
editbox1.place(x = 120, y = 60)


root.mainloop()
