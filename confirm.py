import os
query = input("are you sure (y/n)? ")
print(query)
if query != "n":
	os.system("python dfu-steps.py")
elif query == "n":
	print("ok")
elif query == "N":
	print("ok")
