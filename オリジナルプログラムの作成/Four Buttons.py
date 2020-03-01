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
        self.label1 = tk.Label(master, text="ボタン当ててね", font = ('Helvetica', 35))
        self.label1.place(x = 141, y = 45)

        # 履歴を表示
        self.rirekibox = tk.Text(master, font=("Helvetica", 14))
        self.rirekibox.place(x=325, y=125, width=90, height=200)


        # ４つのボタン
        self.button1 = tk.Button(master, text = ' 1 ', font=('Helvetica',80),command=partial(self.click_button,'1'))
        self.button1.place(x = 116, y = 124)
        self.button2 = tk.Button(master, text = ' 2 ', font=('Helvetica',80),command=partial(self.click_button,'2'))
        self.button2.place(x = 220, y = 124)
        self.button3 = tk.Button(master, text = ' 4 ', font=('Helvetica',80),command=partial(self.click_button,'3'))
        self.button3.place(x = 220, y = 229)
        self.button4 = tk.Button(master, text = ' 3 ', font=('Helvetica',80),command=partial(self.click_button,'4'))
        self.button4.place(x = 116, y = 229)
        
        # ボタンが押された時の処理
    def click_button(self,num):

        self.random = random.randint(1, 3)
        seikai = "正解"

        # 押下したボタンを判定
        if self.random == int(num):
            tmsg.showinfo("正解")
            self.rirekibox.insert(tk.END, '  ' + num + ' : ' + "正解 " + "\n" )
        elif self.random != int(num):
            self.rirekibox.insert(tk.END, '  ' + num + ' : ' + "不正解 " + "\n" )
            tmsg.showinfo("不正解")
        else:
            if seikai == seikai:
                self.destroy()


# ウィンドウを作成する
root = tk.Tk()
root.geometry('550x400')
root.title('Random Button')
app = Application(master=root)
app.mainloop()

