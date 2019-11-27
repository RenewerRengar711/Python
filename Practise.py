import tkinter as tk
from tkinter import font as tkfont


class FirstOne(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family="helevetica", size=18, weight="bold", slant="italic")

        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, ):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        l1 = tk.Label(self, text="I hope this worked!")
        l1.pack(side='top')


if __name__ == "__main__":
    App = FirstOne()
    App.geometry("500x500")
    App.mainloop()
