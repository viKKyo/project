#CLI Ready version:
def main_7():

    process()


def process():

    file1 = input("Input your core file: ")
    file2 = input("Input your comparisson file: ")

    fileanalysis(file1, file2)


def fileanalysis(file1, file2):
    
    file1_ = open(file1, "r")
    file2_ = open(file2, "r")

    file = []
    compare_file = []

    for lines in file1_.read().split(" "):
        file.append(lines)
    for lines in file2_.read().split(" "):
        compare_file.append(lines)

    difference_1 = set(file) - set(compare_file)
    print("This is whats in file 1 but not in file 2: ", difference_1)

main_7()















"""
Filanalys. Datafiler är oftast mycket stora. Många gånger
i forensiskt arbete vill man kunna se skillnader mellan
innehållet i två filer eller hitta en fil som är närmast
likt någon annan fil som man har som undersökningsfil. I
ditt program skall du kunna jämföra två olika filer för
att se skillnader i innehåll. För detta skall du använda
datastrukturen Set (kap 9) och operationerna som erbjuds.
"""

def fileanalysis(file1, file2):                                     #The user specifies the file and comparisson file.
    
    file1_ = open(file1, "r")
    file2_ = open(file2, "r")                                       #Opens specified files.

    file = []
    compare_file = []                                               #Empty lists for appending.

    for lines in file1_.read().split(" "):
        file.append(lines)                                          #Appends each word.
    for lines in file2_.read().split(" "):
        compare_file.append(lines)

    userinput = input("Press the number for the operand: \n1.The Intersection\n2.The Differences\n")

    if userinput == "1":                                            #Intersection for the similarities.
        intersection_set = set(file) & set(compare_file)
        print("The Similarities are:", intersection_set)
    if userinput == "2":                                            #Prints the differences.
        difference_1 = set(file) - set(compare_file)
        print("This is whats in file 1 but not in file 2: ", difference_1)
        difference_2 = set(compare_file) - set(file)
        print("This is whats in file 2 but not in file 1: ", difference_2)
    else:
        pass

fileanalysis("file1.txt", "file2.txt")                              #Calls functions.

