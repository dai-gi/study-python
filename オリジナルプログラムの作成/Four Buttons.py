# ランダムに1桁の整数を選ぶプログラム
# coding:utf-8

import random
import tkinter as tk
import tkinter.messagebox as tmsg
from functools import partial



class Application(tk.Frame):
    def __init__(self, master=None,):
        super().__init__(master)
        self.pack()
        
        # ラベルを作成
        self.label1 = tk.Label(master, bg = 'SlateGray3', text="ボタン当ててね", font = ('Helvetica', 35), fg='gray45')
        self.label1.place(x = 70, y = 15)

        # 履歴を表示
        self.rirekibox = tk.Text(master, font=("Helvetica", 14), bg = 'SlateGray3', fg='gray45')
        self.rirekibox.place(x=255, y=75, width=90, height=200) 

        self.button1 = tk.Button(master, text = ' 1 ', font=('Helvetica',80),fg='gray45',bg="pink", command=partial(self.click_button,'1'))
        self.button1.place(x = 46, y = 74)
        self.button1.config(bg="pink")
        self.button2 = tk.Button(master, text = ' 2 ', font=('Helvetica',80),fg='gray45', command=partial(self.click_button,'2'))
        self.button2.place(x = 150, y = 74)
        self.button3 = tk.Button(master, text = ' 4 ', font=('Helvetica',80),fg='gray45', command=partial(self.click_button,'4'))
        self.button3.place(x = 150, y = 179)
        self.button4 = tk.Button(master, text = ' 3 ', font=('Helvetica',80),fg='gray45', command=partial(self.click_button,'3'))
        self.button4.place(x = 46, y = 179)
    
        
    def click_button(self,num):

        self.random = random.randint(1, 4)
        
        # 押下したボタンを判定
        if self.random == int(num):
            tmsg.showinfo("正解")
            self.rirekibox.insert(tk.END, '  ' + num + ' : ' + "正解 " + "\n" )
        elif self.random != int(num):
            self.rirekibox.insert(tk.END, '  ' + num + ' : ' + "不正解 " + "\n" )
            tmsg.showerror("error message", "不正解")
                
# ウィンドウを作成する
root = tk.Tk()
root.geometry('400x350')
root.title('Random Button')
root.configure(bg='SlateGray3')

app = Application(master=root)

app.mainloop()

