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
        for F in (StartPage, PageOne):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
# Runs the function made to show frame
        self.show_frame(StartPage)
# Function to show frame

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# the start page
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        l1 = tk.Button(self, text="Visit Page 1",
                       command=lambda: controller.show_frame(PageOne))
        l1.pack(side='top')


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        l1 = tk.Button(self, text="Back to Home",
                       command=lambda: controller.show_frame(StartPage))
        l1.pack(side='top')


# Just to run the entire app
App = FirstOne()
App.title("Test")
App.geometry("500x500")
App.mainloop()
