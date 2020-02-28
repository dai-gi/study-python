import tkinter as tk
import tkinter.messagebox as tmsg

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="left")
        
        self.hi_there2 = tk.Button(self)
        self.hi_there2["text"] = "Hello World2\n(click me)"
        self.hi_there2["command"] = self.say_hi2
        self.hi_there2.pack(side="right")
        

        self.quit = tk.Button(self, text="QUIT", fg="red",
                                command=root.destroy)
        self.quit.pack(side="top")

    def say_hi(self):
        a = "hi there, everyone!"
        print(tmsg.showinfo("入力されたテキスト", a))

    def say_hi2(self):
        b = "hi there, everyone!"
        print(tmsg.showinfo("入力されたテキスト", b))




root = tk.Tk()
app = Application(master=root)
app.mainloop()