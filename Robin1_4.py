import glob
import os
import datetime
import string
import random
from datetime import date, timedelta

"""
The program starts of by using this function to create a list of either
a specific directory or an entire harddrive, that list is then used
in some of the other functions.
"""
def comp_search():
	print("\nChoose to either search a specific path or an entire ")
	print("hardrive (menu/exit to see main menu).\n")
	
	#While loop för att undvika error och se till så att användaren gör
	#ett val som finns nedan i form av if statements
	while True:
		#Nedan får användaren ange vart i datorn vi ska söka, sök resultatet
		#sparas sedan till en lista som returneras och återanvänds senare.
		print("\nWould you like to search a specific directory(y/n)?")
		where = input("Write 'no' to search the entire hardrive. \n>>>")
		
		#Första if statement skapar en lista under en specifik path
		if where.lower() in ["y", "ye", "yes", "", " "]:
			folder = input("\nInput path you want to search\n>>> ")
			folder_list = []
			for name in glob.glob(folder + "\\**", recursive=True):
				folder_list.append(name)
			return(folder_list)
			break	
		
		#andra "if" skapar en lista av en hel hårddisk
		elif where.lower() in ["n", "no", "noo"]:
			drive = input("\nWhich hardrive do you want to search (e.g C:, D:)\n>>> ")
			drive_list = []
			for name in glob.glob(drive.lower() + "\\**", recursive=True):
				drive_list.append(name)
			return(drive_list)
			break
		
		#återgå till meny
		elif where.lower() in ["menu", "exit", "quit", "q"]:
			menu()
		
		#vid felaktig input följer det nedan
		else:
			print("Try again.")


"""
This function relys on the list created at comp_search. The user gets
to choose what filetypes to search for all of the files found that
mathces the user input will then be saved to a file.
"""
def list_search(list_of_paths):
	while True:
		print("\nWrite menu/exit to return to previous menu.")
		filename = input("\nInput a name for the file you want to save to\n>>>")
		if filename.lower() in ["menu", "exit"]:
			break
		
		save_to = open(filename, "w")
		
		searchword = input("\nWhat filetype do you want to find (e.g .txt)\n>>> ")
		if searchword.lower() in ["menu", "exit"]:
			break
			
		"""Första for loopen går igenom "list_of_paths" och lägger till matchar
		i listan "file_list" gentemot sökordet "filetype"."""
		file_list = []
		for x in range(len(list_of_paths)):
			if searchword in list_of_paths[x]:
				file_list.append(list_of_paths[x])
		
		"""Andra for loopen är enbart till för att skapa en "ren string" som 
		användaren lättare kan läsa av. "temp_list" är bara temporär och 
		oanvändbar efter att for loopen körts"""
		temp_list=[]
		only_name= ""
		for z in range(len(file_list)):
			temp_list = file_list[z].split("\\")
			only_name = only_name + " " + temp_list[-1]
		
		#Skriver ut matchar till användaren
		print("\nFound the following files ending with " + searchword + ":")
		print("\n" + only_name + "\n")
		print("\nSaving filepaths to '" + filename + "'.\n\n\n")
		for loc in range(len(file_list)):
			save_to.writelines(file_list[loc] + "\n")
		save_to.close


"""
This function will let the user choose to search a specific file or a
list of files, if the user wants to search a list of files the search
will use the list from the function comp_search to renew the list
simply use function comp_search
"""
def info_search_choice(list_of_paths):
	while True: 
		print("\nWould you like to search a single file(1) or a list of files(2), (exit) to return")
		print("Reading several files at once might take a while.\n")
		file_choice = input("Input 1 or 2.\n >>> ")
		temp_list = []
		perfect_match = 0
		semi_match = 0
		
		if file_choice == "1":
			try:
				input_search = input("\nInput file you want to search through\n>>>")
				cur_file = open(input_search, "r", errors="ignore")
			except:
				print("\nUnable to read file")
				continue

			for word in cur_file:
				word = word.replace("\n", "")
				temp_list = temp_list + word.split(" ")
			info_search(temp_list)
		
		
		elif file_choice == "2":
			for x in list_of_paths:
				try:
					cur_file = open(x, "r", errors="ignore")
				except:
					print("\nUnable to read that file.")
					continue
				for word in cur_file:
					word = word.replace("\n", "")
					temp_list = temp_list + word.split(" ")
			info_search(temp_list)
		
		elif file_choice.lower() in ["menu", "exit"]:
			menu(list_of_paths)
		elif file_choice not in ["1", "2"]:
			print("\nPlease input 1 or 2 (exit to return to previous menu).")
		else:
			print("\nPlease input 1 or 2 (exit to return to previous menu).")


"""
part of info_search_choice, this is were the user gets to input what
the program should look for in the files specified at info_search_choice
"""
def info_search(temp_list):
	while True:
		perfect_match = 0
		semi_match = 0
		print("\nWhat would you like to search for")
		print("1.  Names or specific words")
		print("2.  Personal or social security numbers")
		print("3.  Numbers matching specific range")
		print("4.  Exit / Next File")
		choice = input("\nInput a number from the menu\n>>>")
		
		if choice == "1":
			searchword = input("Input the name or word you want to search for\n>>>")
			for pos in temp_list:
				if searchword.lower() in pos.lower():
					if len(searchword) == len(pos):
						perfect_match = perfect_match +1
					elif len(searchword) != len(pos):
						semi_match = semi_match +1
			
			print("Found " + str(perfect_match) + " perfect matches.")
			print("Found " + str(semi_match) + " semi matches.")	
				
		elif choice == "2":
			for num in temp_list:
				if num.isdigit():
					if len(num) == 10 or len(num) == 12:
						perfect_match = perfect_match +1
					else:
						semi_match = semi_match +1
			print("Found " + str(perfect_match) + " perfect matches.")
			print("Found " + str(semi_match) + " matches containing numbers.")
		
		elif choice == "3":
			min_length = int(input("Input min length of number\n>>>"))
			max_length = int(input("Input max length of number\n>>>"))
			for num in temp_list:
				if num.isdigit():
					if len(num) >= min_length and len(num) <= max_length:
						perfect_match = perfect_match +1
			print("Found " + str(perfect_match) + " matches.")
			
		elif choice == "4":
			break
			
		elif choice not in ["1", "2", "3", "4"]:
			print("Input a valid number")
		else:
			print("Input a valid number")
			

