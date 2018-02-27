import tkinter
from tkinter import *

class SampleGUI:

    def __init__(self):
        self.main_menu = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_menu)
        self.middle_frame = tkinter.Frame(self.main_menu)                                       #Creates the frames.
        self.result_frame = tkinter.Frame(self.main_menu)
        self.bottom_frame = tkinter.Frame(self.main_menu)

        self.promt_label_top = tkinter.Label(self.top_frame,
                                         text = "Enter the core file with extension:")
        self.promt_entry_top = tkinter.Entry(self.top_frame,                                    #Assigning a label and a entry point for the top and middle frame.
                                             width = 25)
        self.promt_label_middle = tkinter.Label(self.middle_frame,
                                                text = "Enter the comparison file with extension:")
        self.promt_entry_middle = tkinter.Entry(self.middle_frame,
                                             width = 25)

        self.promt_label_top.pack(side = "left")                                                #Packs the top and middle widgets.
        self.promt_entry_top.pack(side = "left")

        self.promt_label_middle.pack(side = "left")
        self.promt_entry_middle.pack(side = "left")


        self.result_label = tkinter.Label(self.result_frame,                                    #Creates a result label widget.
                                          text = "This is whats in file 1 but not in file 2: ")
        self.value = tkinter.StringVar()                                                        #A empty StringVar that will be used to take teh result from function.
        self.value_label = tkinter.Label(self.result_frame,
                                         textvariable = self.value)                             #The results from StringVar will be printed here.

        self.result_label.pack(side = "left")                                                   #Packs the result and value widgets.
        self.value_label.pack(side = "left")


        self.result_button = tkinter.Button(self.bottom_frame,                                  #A button widget that activates the fileanalysis function.
                                            text = "Compare",
                                            command = self.fileanalysis)
        self.quit_button = tkinter.Button(self.bottom_frame,                                    #A EXIT button widget that ends the loop.
                                          text = "EXIT",
                                          command = self.main_menu.destroy)

        self.result_button.pack(side = "left")                                                  #Packs Button Widgets.
        self.quit_button.pack(side = "left")


        self.top_frame.pack()                                                                   #Packs the frames.
        self.middle_frame.pack()
        self.result_frame.pack()
        self.bottom_frame.pack()


        tkinter.mainloop()                                                                      #Initializes the loop.

    def fileanalysis(self):
    
        file1_ = open(self.promt_entry_top.get(), "r")
        file2_ = open(self.promt_entry_middle.get(), "r")                                   #Should read the input given by the GUI entries.

        file = []
        compare_file = []                                                                   #Empty lists for appending.

        for lines in file1_.read().split(" "):
            file.append(lines)                                                              #Appends each word.
        for lines in file2_.read().split(" "):
            compare_file.append(lines)

        difference_1 = set(file) - set(compare_file)                                        #Sets the lists and saves the differences.
        self.value.set(difference_1)                                                        #Assigning the list to the empty StringVar.


b = SampleGUI()
