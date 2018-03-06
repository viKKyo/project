import tkinter
from tkinter import messagebox
import glob
import os
import datetime
import string
import random
from datetime import date, timedelta

class SuperHaxxorForensicTool(tkinter.Tk):

    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)

        tkinter.Tk.wm_title(self, "IT-forensik Projekt")

        container = tkinter.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frame = {}
        for F in (StartPage, PageOne, PageTwo, PageThree, PageThreeOne, PageThreetwo, PageFive, PageSix, PageSeven, PageEight):
            frame = F(container, self)
            self.frame[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)


    def show_frame(self, cont):

        frame = self.frame[cont]
        frame.tkraise()


class StartPage(tkinter.Frame):

    def __init__(self, parent, controller):
        #parent class(SuperHaxxorForensicTool is the main class)
        tkinter.Frame.__init__(self, parent)


        self.label =tkinter.Label(self, text="SuperHaxxorForensicTool", fg='red', font = "Times 16 bold italic")
        self.label.grid(row=0, column=1 ,columnspan=1, sticky='EWNS')


        self.button1 = tkinter.Button(self, text="F1 Searchfiles", fg='black', bg='green',
                                 command=lambda: controller.show_frame(PageOne))
        self.button2 = tkinter.Button(self, text="F2 List of specific filetypes", fg='black', bg='green',
                                      command=lambda: controller.show_frame(PageTwo))
        self.button3 = tkinter.Button(self, text="F3-4 Find searchword matches", fg='black', bg='green',
                                      command=lambda: controller.show_frame(PageThree))
        self.button5 = tkinter.Button(self, text="F5 Search by modified date", fg='black', bg='green',
                                      command=lambda: controller.show_frame(PageFive))
        self.button6 = tkinter.Button(self, text="F6 Encrypt or Decrypt", fg='black', bg='green',
                                      command=lambda: controller.show_frame(PageSix))
        self.button7 = tkinter.Button(self, text="F7 Comparison", fg='black', bg='green',
                                command=lambda: controller.show_frame(PageSeven))
        self.button8 = tkinter.Button(self, text="F8 Differences", fg='black', bg='green',
                                command=lambda: controller.show_frame(PageEight))


        self.button1.grid(row=1, column=1 ,columnspan=1, sticky='EWNS')
        self.button2.grid(row=2, column=1 ,columnspan=1, sticky='EWNS')
        self.button3.grid(row=3, column=1, columnspan=1, sticky='EWNS')
        self.button5.grid(row=4, column=1, columnspan=1, sticky='EWNS')
        self.button6.grid(row=5, column=1, columnspan=1, sticky='EWNS')
        self.button7.grid(row=6, column=1 ,columnspan=1, sticky='EWNS')
        self.button8.grid(row=7, column=1 ,columnspan=1, sticky='EWNS')


        self.label2 = tkinter.Label(self, text="Extrauppgifter", font="Times 12 bold italic")
        self.label2.grid(row=9, column=1 ,columnspan=2, sticky='EWNS')



#Page1
class PageOne(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)

        self.label = tkinter.Label(self, text="Creates a list of Paths.", fg='red', font="Times 16 bold italic")
        self.folder_label = tkinter.Label(self, text="Input folder to search or press search computer")
        self.folder_entry = tkinter.Entry(self,width=25)

        self.label.grid(row=0, column=2, columnspan=2, sticky="EWNS")
        self.folder_label.grid(row=2, column=2, columnspan=2, sticky="EWNS")
        self.folder_entry.grid(row=3, column=2, columnspan=3, sticky="EWNS")


        self.result_button = tkinter.Button(self,text="Search",
                                            command=self.comp_search)
        self.button = tkinter.Button(self, text="Go to the start page",
                                     command=lambda: controller.show_frame(StartPage))

        self.result_button.grid(row=4, column=3, columnspan=1, sticky="EWNS")
        self.button.grid(row=4, column=2, columnspan=1, sticky="EWNS")

    def comp_search(self):

        folder = self.folder_entry.get()
        folder_list = []
        for name in glob.glob(folder + "\\**", recursive=True):
            folder_list.append(name+'\n')

        messagebox.showinfo('results', folder_list)

#Page2
class PageTwo(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)

        self.label = tkinter.Label(self, text="Creates a list of specific file-types", fg='red', font="Times 16 bold italic")
        self.label1 = tkinter.Label(self, text="Select the folder path you wish to search in: ")
        self.label2 = tkinter.Label(self, text="Which extension-type are you searching for?(t ex .txt)")

        self.entry_path = tkinter.Entry(self, width='40')
        self.entry_ext = tkinter.Entry(self, width='40')

        self.button = tkinter.Button(self, text='Search',
                                     command=self.comp_search)
        self.button1 = tkinter.Button(self, text="Go to the start page",
                                     command=lambda: controller.show_frame(StartPage))

        self.label.grid(row=1, column=2, columnspan=2, sticky="EWNS")
        self.label1.grid(row=2, column=1, columnspan=2, sticky="EWNS")
        self.label2.grid(row=3, column=1, columnspan=2, sticky="EWNS")
        self.entry_path.grid(row=2, column=3, columnspan=1, sticky="EWNS")
        self.entry_ext.grid(row=3, column=3, columnspan=1, sticky="EWNS")
        self.button.grid(row=4, column=3, columnspan=1, sticky="EWNS")
        self.button1.grid(row=4, column=2, columnspan=1, sticky="EWNS")

    def comp_search(self):

        folder = self.entry_path.get()
        search_ext = self.entry_ext.get()
        folder_list = []
        for name in glob.glob(folder + "\\**", recursive=True):
            folder_list.append(name+'\n')

        file_list = []
        for x in range(len(folder_list)):
            if search_ext in folder_list[x]:
                file_list.append(folder_list[x])

        temp_list = []
        only_name = ""
        for z in range(len(file_list)):
            temp_list = file_list[z].split("\\")
            only_name = only_name + " " + temp_list[-1]

        messagebox.showinfo('results', "found the following files with"+ search_ext+":")
        messagebox.showinfo('results', only_name)
#Page3
class PageThree(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)


        self.label = tkinter.Label(self, text='Search Information, Choose:', fg='red', font = "Times 16 bold italic")
        self.button = tkinter.Button(self, text='Search within one file',
                                     command=lambda: controller.show_frame(PageThreeOne))
        self.button1 = tkinter.Button(self, text='Search within several file',
                                      command=lambda: controller.show_frame(PageThreetwo))
        self.button2 = tkinter.Button(self, text="Go to the start page",
                                     command=lambda: controller.show_frame(StartPage))

        self.label.grid(row=0, column=1 ,columnspan=1, sticky='EWNS')
        self.button.grid(row=1, column=1 ,columnspan=1, sticky='EWNS')
        self.button1.grid(row=2, column=1 ,columnspan=1, sticky='EWNS')
        self.button2.grid(row=3, column=1 ,columnspan=1, sticky='EWNS')
#Page3-1
class PageThreeOne(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)

        self.label = tkinter.Label(self, text='Search Within One File', fg='red', font = "Times 16 bold italic")

        self.label_search = tkinter.Label(self, text='Enter your searchword:')
        self.entry_searchword = tkinter.Entry(self, width='40')
        self.label_file = tkinter.Label(self, text='Enter the Path to the file:')
        self.entry_file = tkinter.Entry(self, width='40')

        self.label2 = tkinter.Label(self, text='Are you searching for a Social Security number?')

        self.label.grid(row=0, column=1 ,columnspan=1, sticky='EWNS')
        self.label_search.grid(row=1, column=1 ,columnspan=1, sticky='EWNS')
        self.entry_searchword.grid(row=1, column=2 ,columnspan=1, sticky='EWNS')

        self.label_file.grid(row=2, column=1 ,columnspan=1, sticky='EWNS')
        self.entry_file.grid(row=2, column=2 ,columnspan=1, sticky='EWNS')

        self.button_search = tkinter.Button(self, text='Word-Search',
                                            command=self.search_word)
        self.button2 = tkinter.Button(self, text='Social Security Number Search',
                                      command=self.prs_nmr)
        self.button = tkinter.Button(self, text="RETURN",
                                     command=lambda: controller.show_frame(PageThree))

        self.button_search.grid(row=3, column=2 ,columnspan=1, sticky='EWNS')
        self.label2.grid(row=4, column=1 ,columnspan=1, sticky='EWNS')
        self.button2.grid(row=4, column=2 ,columnspan=1, sticky='EWNS')
        self.button.grid(row=5, column=1 ,columnspan=1, sticky='EWNS')

    def one_file(self):

        temp_list = []
        file = self.entry_file.get()

        cur_file = open(file, "r", errors="ignore")
        for word in cur_file:
            word = word.replace("\n", "")
            temp_list = temp_list + word.split(" ")

        return temp_list

    def search_word(self):

        perfect_match = 0
        semi_match = 0
        temp_list = self.one_file()
        searchword = self.entry_searchword.get()
        for pos in temp_list:
            if searchword.lower() in pos.lower():
                if len(searchword) == len(pos):
                    perfect_match = perfect_match + 1
                elif len(searchword) != len(pos):
                    semi_match = semi_match + 1
        messagebox.showinfo('results', "Found " + str(perfect_match) + " perfect matches.")
        messagebox.showinfo('results', "Found " + str(semi_match) + " semi matches.")

    def prs_nmr(self):
        perfect_match = 0
        semi_match = 0
        temp_list = self.one_file()
        for num in temp_list:
            if num.isdigit():
                if len(num) == 10 or len(num) == 12:
                    perfect_match = perfect_match + 1
                else:
                    semi_match = semi_match + 1
        messagebox.showinfo('results', "Found " + str(perfect_match) + " perfect matches.")
        messagebox.showinfo('results', "Found " + str(semi_match) + " semi matches.")

#Page3-2
class PageThreetwo(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)

        self.label = tkinter.Label(self, text='Search Within Several Files', fg='red', font = "Times 16 bold italic")

        self.label1 = tkinter.Label(self, text='Enter the Path to the folder:')
        self.entry = tkinter.Entry(self, width='40')

        self.label_search = tkinter.Label(self, text='Enter your searchword (if needed):')
        self.entry_searchword = tkinter.Entry(self, width='40')

        self.button_search = tkinter.Button(self, text='Word-Search',
                                            command=self.search_word)
        self.button2 = tkinter.Button(self, text='Social Security Number Search',
                                      command=self.prsnmr)
        self.button = tkinter.Button(self, text="RETURN",
                                     command=lambda: controller.show_frame(PageThree))

        self.label.grid(row=0, column=1 ,columnspan=1, sticky='EWNS')
        self.label1.grid(row=1, column=1 ,columnspan=1, sticky='EWNS')
        self.entry.grid(row=1, column=2 ,columnspan=1, sticky='EWNS')
        self.label_search.grid(row=2, column=1 ,columnspan=1, sticky='EWNS')
        self.entry_searchword.grid(row=2, column=2 ,columnspan=1, sticky='EWNS')
        self.button_search.grid(row=3, column=2 ,columnspan=1, sticky='EWNS')
        self.button2.grid(row=4, column=2 ,columnspan=1, sticky='EWNS')
        self.button.grid(row=5, column=1 ,columnspan=1, sticky='EWNS')

    def folder(self):
        folder = self.entry.get()

        folder_list = []
        for name in glob.glob(folder + "\\**", recursive=True):
            folder_list.append(name)
        return folder_list


    def multiple_files(self):
        temp_list = []
        folder_list = self.folder()

        for x in folder_list:
            try:
                cur_file = open(x, "r", errors="ignore")
            except:
                print("")
                continue

            for line in cur_file:
                for word in line.split():
                    word = word.replace("\n", "")
                    temp_list.append(word)
                    temp_list.append(x)
        return temp_list

    def search_word(self):

        perfect_match = 0
        semi_match = 0
        temp_list = self.multiple_files()
        searchword = self.entry_searchword.get()
        counter = 0
        counter_list = []
        counter_list2 = []
        for pos in temp_list:
            if searchword.lower() in pos.lower():
                if len(searchword) == len(pos):
                    perfect_match = perfect_match + 1
                    counter_list.append(temp_list[counter+1])
                elif len(searchword) != len(pos):
                    semi_match = semi_match + 1
                    counter_list2.append(temp_list[counter+1])
            counter += 1
        messagebox.showinfo('results', "Found " + str(perfect_match) + " perfect matches." + "\n" + str(counter_list))
        messagebox.showinfo('results', "Found " + str(semi_match) + " semi matches." + "\n"+ str(counter_list2))

    def prsnmr(self):

        perfect_match = 0
        temp_list = self.multiple_files()
        counter = 0
        counter_list = []
        for num in temp_list:
            num2 = num[0].split("-")
            if num2.isdigit():
                if len(num2[0]) == 6 or len(num2[0]) == 8 and len(num2[1]) == 4:
                    perfect_match = perfect_match + 1
                    counter_list.append(temp_list[counter + 1])

            counter += 1
        messagebox.showinfo('results', "Found " + str(perfect_match) + " perfect matches." + "\n" + str(counter_list))

#Page5
class PageFive(tkinter.Frame):

    # Testa på mötet
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)

        self.label0 = tkinter.Label(self, text="               ")
        self.label0.grid(row=0, column=1, columnspan=1, sticky="ESWN")

        # överskrift
        self.label = tkinter.Label(self, text="Modified or created time", fg='red', font="Times 16 bold italic")
        self.label.grid(row=1, column=2, columnspan=5, sticky="ESWN")

        # labels
        self.label2 = tkinter.Label(self, text="choose earliest date:")
        self.label3 = tkinter.Label(self, text="choose latest date:")
        self.label4 = tkinter.Label(self, text="Enter the Path:")
        self.label2.grid(row=2, column=2, columnspan=1, sticky="ESWN")
        self.label3.grid(row=3, column=2, columnspan=1, sticky="ESWN")
        self.label4.grid(row=4, column=2, columnspan=1, sticky="ESWN")

        # Entrys
        self.entry1 = tkinter.Entry(self, width=25)
        self.entry2 = tkinter.Entry(self, width=25)
        self.entry3 = tkinter.Entry(self, width=25)
        self.entry1.grid(row=2, column=3, columnspan=1, sticky="ESWN")
        self.entry2.grid(row=3, column=3, columnspan=1, sticky="ESWN")
        self.entry3.grid(row=4, column=3, columnspan=1, sticky="ESWN")

        # buttons
        self.button = tkinter.Button(self, text='Search',
                                     command=self.main)
        self.button1 = tkinter.Button(self, text="Go to the start page",
                                     command=lambda: controller.show_frame(StartPage))
        self.button.grid(row=5, column=3, columnspan=1, sticky="ESWN")
        self.button1.grid(row=5, column=2, columnspan=1, sticky="ESWN")


    def main(self):

        date_start = self.entry1.get()
        date_end = self.entry2.get()

        file_list1 = glob.glob(self.entry3.get())

        name_list = []
        filenames = []
        for name in file_list1:
            name_list = name.split("\\")
            filenames.append(name_list[-1])

        c_list = []
        m_list = []
        end_list = ""
        num = 0
        for x in file_list1:
            times = os.stat(x)
            c_time = datetime.datetime.fromtimestamp(times[9])
            m_time = datetime.datetime.fromtimestamp(times[8])

            test = self.date_check(date_start, date_end, datetime.datetime.fromtimestamp(times[8]))
            if test == True:
                end_list += format(filenames[num])+" "+str(m_time)+'\n'
            num = num + 1
        messagebox.showinfo('results', end_list)

    def date_check(self, start, end, modtime):


        modtime = modtime.strftime('%Y-%m-%d')
        m_list = []
        for z in modtime:
            m_list.append(z)
        m_year, m_month, m_day = self.date_format(m_list)
        moddate = date(int(m_year), int(m_month), int(m_day))

        s_list = []
        for x in start:
            s_list.append(x)
        s_year, s_month, s_day = self.date_format(s_list)

        e_list = []
        for y in end:
            e_list.append(y)
        e_year, e_month, e_day = self.date_format(e_list)

        begin = date(int(s_year), int(s_month), int(s_day))
        finish = date(int(e_year), int(e_month), int(e_day))
        count = finish - begin

        listan = []
        for i in range(count.days + 1):
            string_dates = begin + timedelta(days=i)
            if string_dates == moddate:
                return True

    def date_format(self, date_list):
        year = date_list[0] + date_list[1] + date_list[2] + date_list[3]

        month = date_list[5:7]
        if month[0] == "0":
            month = month.pop()
        else:
            month = date_list[5] + date_list[6]
        day = date_list[8:10]
        if day[0] == "0":
            day = day.pop()
        else:
            day = date_list[8] + date_list[9]
        return year, month, day
#Page6
class PageSix(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)

        self.label = tkinter.Label(self, text="Encryption or Decryption.", fg='red', font="Times 16 bold italic")
        self.label.grid(row=0, column=2, columnspan=2, sticky="EWNS")

        self.file_choice = tkinter.Label(self, text='Choose a file to either encrypt or decrypt: ')
        self.path_choice = tkinter.Entry(self, width=40)
        self.file_choice.grid(row=1, column=2, columnspan=2, sticky="EWNS")
        self.path_choice.grid(row=2, column=2, columnspan=2, sticky="EWNS")

        self.enc_file = tkinter.Label(self, text='Choose the name of the file you wish to write in:')
        self.name_choice = tkinter.Entry(self, width=40)
        self.enc_file.grid(row=3, column=2, columnspan=2, sticky="EWNS")
        self.name_choice.grid(row=4, column=2, columnspan=2, sticky="EWNS")

        self.to_file = tkinter.Button(self, text='Encrypt to file',
                                 command=self.write_to_file)
        self.to_file2 = tkinter.Button(self, text='Decrypt to file',
                                  command=self.write_to_file2)
        self.button = tkinter.Button(self, text="Go to the start page",
                                command=lambda: controller.show_frame(StartPage))

        self.to_file.grid(row=5, column=2, columnspan=2, sticky="EWNS")
        self.to_file2.grid(row=6, column=2, columnspan=2, sticky="EWNS")
        self.button.grid(row=7, column=2, columnspan=2, sticky="EWNS")

    def encrypt(self):

        filenamee = self.path_choice.get()

        enc_string = ""
        my_file = open(filenamee, 'r')
        readfile = my_file.read().rstrip()

        for letter in readfile.lower():
            if letter in kryp_dic:
                enc_string += kryp_dic[letter]
            else:
                enc_string += letter

        my_file.close()
        return enc_string

    def decrypt(self):

        filenamed = self.path_choice.get()

        dec_string = ""
        my_file = open(filenamed, 'r')
        readfile = my_file.read().rstrip()

        for letter in readfile.lower():
            if letter in kryp_dic:
                dec_string += kryp_dic[letter]
            else:
                dec_string += letter
        my_file.close()
        return dec_string

    def write_to_file(self):
        to_file = self.encrypt()
        filename = self.name_choice.get()
        myfile = open(filename, 'w')
        myfile.write(to_file)
        myfile.close()
        messagebox.showinfo('results', "filename is now encrypted to file: " + filename)


    def write_to_file2(self):
        to_file = self.decrypt()
        filename = self.name_choice.get()
        myfile = open(filename, 'w')
        myfile.write(to_file)
        myfile.close()
        messagebox.showinfo('results', "filename is now decrypted to file: " + filename)
#Page7
class PageSeven(tkinter.Frame):

    def __init__(self,parent, controller):
        tkinter.Frame.__init__(self,parent)

        self.label = tkinter.Label(self, text="Comparison of two files.", fg='red', font="Times 16 bold italic")
        self.promt_label_top = tkinter.Label(self,
                                             text = "Enter the core file with extension:")
        self.promt_entry_top = tkinter.Entry(self,
                                             width = 25)
        self.promt_label_middle = tkinter.Label(self,
                                                text = "Enter the comparison file with extension:")
        self.promt_entry_middle = tkinter.Entry(self,
                                                width = 25)

        self.label.grid(row = 0, column = 1, columnspan = 2, sticky = "EWNS")
        self.promt_label_top.grid(row = 1, column = 1, columnspan = 2, sticky = "EWNS")
        self.promt_entry_top.grid(row = 1, column = 4, columnspan = 2, sticky = "EWNS")

        self.promt_label_middle.grid(row = 2, column = 1, columnspan = 2, sticky = "EWNS")
        self.promt_entry_middle.grid(row = 2, column = 4, columnspan = 2, sticky = "EWNS")


        self.result_button = tkinter.Button(self,
                                            text = "Compare",
                                            command = self.fileanalysis)
        self.button = tkinter.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame(StartPage))

        self.result_button.grid(row = 4, column = 2, columnspan = 1, sticky = "EWNS")
        self.button.grid(row = 4, column = 1, columnspan = 1, sticky = "EWNS")

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
        difference_1 = str(difference_1)
        tkinter.messagebox.showinfo("Results",
                                    "This is whats in file 1 but not in file 2:" + difference_1)
#Page8
class PageEight(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)

        self.label = tkinter.Label(self, text="Writes the outputs in a different file.", fg='red', font="Times 16 bold italic")
        self.label.grid(row=0, column=2, columnspan=1, sticky="EWNS")

        self.file_1 = tkinter.Label(self, text='Input a name for file 1 (e.g info1.txt)')
        self.file1_choice = tkinter.Entry(self, width=40)
        self.file_1.grid(row=1, column=2, columnspan=1, sticky="EWNS")
        self.file1_choice.grid(row=2, column=2, columnspan=1, sticky="EWNS")

        self.file_2 = tkinter.Label(self, text='Input a name for file 2 (e.g info2.txt)')
        self.file_2_choice = tkinter.Entry(self, width=40)
        self.file_2.grid(row=3, column=2, columnspan=1, sticky="EWNS")
        self.file_2_choice.grid(row=4, column=2, columnspan=1, sticky="EWNS")

        self.button1 = tkinter.Button(self, text='Save sys info to files',
                                      command=self.system_information)
        self.button2 = tkinter.Button(self, text="Go to the start page",
                                     command=lambda: controller.show_frame(StartPage))
        self.button1.grid(row=5, column=2, columnspan=1, sticky="EWNS")
        self.button2.grid(row=6, column=2, columnspan=1, sticky="EWNS")


    def system_information(self):
        file_1 = self.file1_choice.get()
        file_2 = self.file_2_choice.get()

        cwd = os.getcwd()
        file_cmd1 = "systeminfo > " + cwd + "\\" + file_1
        file_cmd2 = "start /wait msinfo32.exe /report " + cwd + "\\" + file_2

        os.popen(file_cmd1)
        os.popen(file_cmd2)

        tkinter.messagebox.showinfo("Save",
                                    "Output has been Saved!")
#Extra

b = SuperHaxxorForensicTool()
b.mainloop()
