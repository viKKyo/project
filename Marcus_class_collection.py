import tkinter
from tkinter import *

class PageSeven(tkinter.Frame):

    def __init__(self,parent, controller):
        tkinter.Frame.__init__(self,parent)


        self.promt_label_top = tkinter.Label(self,
                                             text = "Enter the core file with extension:")
        self.promt_entry_top = tkinter.Entry(self,
                                             width = 25)
        self.promt_label_middle = tkinter.Label(self,
                                                text = "Enter the comparison file with extension:")
        self.promt_entry_middle = tkinter.Entry(self,
                                                width = 25)

        self.promt_label_top.grid(row = 1, column = 1, columnspan = 2, sticky = "EWNS")
        self.promt_entry_top.grid(row = 1, column = 3, columnspan = 2, sticky = "EWNS")

        self.promt_label_middle.grid(row = 2, column = 1, columnspan = 3, sticky = "EWNS")
        self.promt_entry_middle.grid(row = 2, column = 4, columnspan = 2, sticky = "EWNS")


        self.result_label = tkinter.Label(self,
                                          text = "This is whats in file 1 but not in file 2: ")
        self.value = tkinter.StringVar()                                                        #A empty StringVar that will be used to take teh result from function.
        self.value_label = tkinter.Label(self,
                                         textvariable = self.value)                             #The results from StringVar will be printed here.

        self.result_label.grid(row = 3, column = 1, columnspan = 2, sticky = "EWNS")
        self.value_label.grid(row = 3, column = 3, columnspan = 4, sticky = "EWNS")


        self.result_button = tkinter.Button(self,
                                            text = "Compare",
                                            command = self.fileanalysis)
        self.button = tkinter.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame(StartPage))

        self.result_button.grid(row = 4, column = 1, columnspan = 5, sticky = "EWNS")
        self.button.grid(row = 4, column = 2, columnspan = 2, sticky = "EWNS")



    def fileanalysis(self):
    
        file1_ = open(self.promt_entry_top.get(), "r")
        file2_ = open(self.promt_entry_middle.get(), "r")                                   #Reads the input given by the GUI entries.

        file = []
        compare_file = []                                                                   #Empty lists for appending.

        for lines in file1_.read().split(" "):
            file.append(lines)                                                              #Appends each word.
        for lines in file2_.read().split(" "):
            compare_file.append(lines)

        difference_1 = set(file) - set(compare_file)                                        #Sets the lists and saves the differences.
        self.value.set(difference_1)                                                        #Assigning the list to the empty StringVar.


