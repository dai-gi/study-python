# ランダムに1桁の整数を選ぶプログラム
# coding:utf-8

import random
import tkinter as tk
import tkinter.messagebox as tmsg
from functools import partial



class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        
        # ラベルを作成
        self.label1 = tk.Label(master, text="ボタン当ててね", font = ('Helvetica', 28))
        self.label1.place(x = 105, y = 35)

        # 履歴を表示
        self.rirekibox = tk.Text(master, font=("Helvetica", 14))
        self.rirekibox.place(x=500, y=0, width=200, height=500)

        self.random = random.randint(1, 9)

        # 9個のボタンを作成
        # 1段目
        self.button1 = tk.Button(master, text = ' 1 ', font=('Helvetica',80),command=partial(self.click_button,'1'))
        self.button1.place(x = 100, y = 130)
        self.button2 = tk.Button(master, text = ' 2 ', font=('Helvetica',80),command=partial(self.click_button,'2'))
        self.button2.place(x = 200, y = 130)
        self.button3 = tk.Button(master, text = ' 3 ', font=('Helvetica',80),command=partial(self.click_button,'3'))
        self.button3.place(x = 300, y = 130)
        # 2段目
        self.button4 = tk.Button(master, text = ' 4 ', font=('Helvetica',80),command=partial(self.click_button,'4'))
        self.button4.place(x = 100, y = 230)
        self.button5 = tk.Button(master, text = ' 5 ', font=('Helvetica',80),command=partial(self.click_button,'5'))
        self.button5.place(x = 200, y = 230)
        self.button6 = tk.Button(master, text = ' 6 ', font=('Helvetica',80),command=partial(self.click_button,'6'))
        self.button6.place(x = 300, y = 230)
        # 3段目
        self.button7 = tk.Button(master, text = ' 7 ', font=('Helvetica',80),command=partial(self.click_button,'7'))
        self.button7.place(x = 100, y = 330)
        self.button8 = tk.Button(master, text = ' 8 ', font=('Helvetica',80),command=partial(self.click_button,'8'))
        self.button8.place(x = 200, y = 330)
        self.button9 = tk.Button(master, text = ' 9 ', font=('Helvetica',80),command=partial(self.click_button,'9'))
        self.button9.place(x = 300, y = 330)
    
    

    # def hantei():
    #     if self.random == num:
    #         tmsg.showinfo("正解")
    #     elif self.random != num:
    #         tmsg.showinfo("不正解")
    #     else:
    #         pass


        # ボタンが押された時の処理
    def click_button(self,num):
        self.rirekibox.insert(tk.END, num + "\n")


# ウィンドウを作成する
root = tk.Tk()
root.geometry('700x500')
root.title('Random Button')
app = Application(master=root)
app.mainloop()

