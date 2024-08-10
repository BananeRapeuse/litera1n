import os
#import mydearpygui
import time
while True:
	print("###########################")
	print("#   Welcome to litera1n ! #")
	print("#      by Ph0qu3_111      #")
	print("###########################")
	print("# If you try to jailbreak #")
	print("#  a A11 device you must  #")
	print("#  disable your passcode  #")
	print("#       in settings       #")
	print("###########################")
	print(" ")
	print(" Please choose an option: ")
	print("[0] Install dependencies (YOU MUST)")
	print("[1] CLI Jailbreak        ")
	print("[2] GUI Jailbreak        ")
	print("[3] Github link          ")
	print("[4] Jailbreak guide      ")
	print("[5] exit                 ")
	print("[help] for help          ")

	choice = input("$ ")
	print(choice)
	if choice == "1":
		os.system("python confirm.py")
	#os.system("dir")
	#os.system("python ipwndfu")
	elif choice == "3":
		print("https://github.com/BananeRapseuse/litera1n")
	elif choice == "4":
		os.system("type Jailbreak.md")
	elif choice == "0":
		os.system("pip install -r requirements.txt")
		os.system("install.lnk")
	elif choice == "2":
		os.system("python gui.py")
	elif choice == "help":
		os.system("type README.md")
	elif choice == "5":
		break
