##### Licensed under AGPL-3.0 License #####
# Script made by DutchDoge#1409 on Discord.
# For questions feel free to contact!
# Also feel free to edit the code to your likings.

import os

print("\n##### Licensed under AGPL-3.0 License #####")
print("SCPCB Google Apps Script Creator")
print("Script made by DutchDoge#1409 on Discord.")
print("For questions feel free to contact!")
print("Also feel free to edit the code to your likings.\n")


# Checks if script.gs file already exists and if it does asks the user if they want to delete it.
if os.path.exists("script.gs"):
	deletefile = input("Do you want to delete the existing .GC file? (Yes/Y) ")
	if deletefile.lower() in ["yes","y"]:os.remove("script.gs")

# Necessary for loop
finished = 0

while finished == 0:
	# Prompts the user to input a folder.
	# User can also type all for all folders in current dir.
	# Typing none will break out of the script.
	path = input("\nType folder to add to GS file (to stop = none | all folders/files = all) ")
	filelist = []
	dirList = []
	confirmAll = "none"

	# Executes if user inputs "none".
	if path.lower() == "none":break

	# Executes if user inputs "all".
	if path.lower() == "all":
		# Prompts user to confirm the action.
		print("\nALL only work if in the root there is only the Python file and needed folders!")
		print("This will also add all files in the root to the GS file EXCEPT python files!")
		confirmAll = input("Are you sure you want to continue? (Yes/Y) ")
		if confirmAll.lower() in ["yes","y"]:path = ".\\"

	# Executes if user inputs a folder name.
	for root, dirs, files in os.walk(path):
		for file in files:
			# Skips python files thus skips this script
			# Any other files will still be added however
			if not (file.endswith(".py")):
				filelist.append(os.path.join(root,file))

    # Opens or makes the script.gs file and for each file it can find will add to the script.
	for name in filelist:
		gsfile = open("script.gs","a")
		if confirmAll.lower() in ["yes","y"]:gsfile.write('RedirectFile("'+name[2:]+'", getscriptpath()+"\\'+name[2:]+'")\n')
		else:gsfile.write('RedirectFile("'+name+'", getscriptpath()+"\\'+name+'")\n')
		gsfile.close()

	print("\nFinished\n")

	# If the user used "all" in folder selection, it will exit when finished
	if confirmAll.lower() in ["yes","y"]:break

##### Licensed under AGPL-3.0 License #####
