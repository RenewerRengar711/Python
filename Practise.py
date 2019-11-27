import tkinter as tk
from tkinter import font as tkfont
# Basic imports of files need for tkinter


# This class is the complete app and their windows
class FirstOne(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family="helevetica", size=18, weight="bold", slant="italic")
# A container for the frame that is being used
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
# A list of all the frames that there is to choose from
        self.frames = {}
        for F in (StartPage, ):
            # page_name is just the frame that is chosen to be used
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
# Runs the function made to show frame
        self.show_frame("StartPage")
# Function to show frame

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


# the start page3
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        l1 = tk.Label(self, text="I hope this worked!")
        l1.pack(side='top')


# Just to run the entire app
if __name__ == "__main__":
    App = FirstOne()
    App.geometry("500x500")
    App.mainloop()
