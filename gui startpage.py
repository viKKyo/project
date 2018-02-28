import tkinter as tk
from tkinter import ttk
from tkinter import font  as tkfont
from tkinter import messagebox
from tkinter import *



class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "IT-forensik Projekt")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frame = {}
        for F in (StartPage, PageOne):
            frame = F(container, self)
            self.frame[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)


    def show_frame(self, cont):

        frame = self.frame[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        #parent class(SeaofBTCapp is the main class)
        tk.Frame.__init__(self, parent)


        self.label =tk.Label(self, text="Start Page", fg='red', font = "helvetica 16 bold italic")
        self.label.grid(row=0, column=2 ,columnspan=2, sticky='EWNS')


        self.button = tk.Button(self, text="visit page 1", fg='red', bg='black',
                                 command=lambda: controller.show_frame(PageOne))
        self.button.grid(row=1, column=2 ,columnspan=1, sticky='EWNS')


        self.label2 = tk.Label(self, text="Extrauppgifter", font="helvetica 12 bold italic")
        self.label2.grid(row=3, column=2 ,columnspan=2, sticky='EWNS')

        self.button1 = ttk.Button(self, text="visit page 2",
                                command=lambda: controller.show_frame(PageOne))
        self.button1.grid(row=2, column=2 ,columnspan=1, sticky='EWNS')


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.label = tk.Label(self, text="Pageone", font=("bold 15"))
        self.label.pack(pady=10, padx=10)

        self.entry = tk.Entry(self, width=70)
        self.entry.pack(pady=10, padx=10)
        self.button1 = tk.Button(self, text="Startpage",
                                 command=lambda: controller.show_frame(StartPage))
        self.button1.pack()


app = SeaofBTCapp()
app.mainloop()
