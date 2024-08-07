import os
#import mydearpygui
import time
while True:
	print("###########################")
	print("#   Welcome to litera1n ! #")
	print("#      by Ph0qu3_111      #")
	print("###########################")
	print("[0]. Install dependencies (MUST DO once)")
	print("[1]. Terminal Jailbreak")
	print("[2]. GUI Jailbreak")
	print("[3]. Github link")
	print("[4]. Jailbreak guide")
	print("[5]. exit")
	print("type help for help")
	choice = input("$ ")
	print(choice)
	if choice == "1":
		os.system("python confirm.py")
	#os.system("dir")
	#os.system("python ipwndfu")
	elif choice == "3":
		print("https://github.com/BananeRapseuse/litera1n")
	elif choice == "4":
		print("Go to the github repository or check README.md")
	elif choice == "0":
		os.system("pip install -r requirements.txt")
		os.system("install.lnk")
	elif choice == "2":
		os.system("python gui.py")
	elif choice == "help":
		os.system("type README.md")
	elif choice == "5":
		break

