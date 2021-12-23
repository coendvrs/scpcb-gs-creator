# SCPCB Google Apps Script Creator
Python script to easily create Google Apps Scripts for SCP:CB and SCP:CB Multiplayer.\
This quickly makes a .gs script for modding purposes.

##

Within the script you can input a folder and it searches all of it contents and outputs it into a script.gs.\
It can also go through all the folders within the scripts directory.\
Every file it can find, that isn't a directory will be put inside of the script.gs file as a redirect.

Example is the 1449chunks.ini inside the data folder, this will turn into:\
`RedirectFile("Data\1499chunks.ini", getscriptpath()+"\Data\1499chunks.ini")` within the GS file.\
This removes the need to manually input all of the files inside of the GS file that you want to redirect.

##

Demonstration of the script\
![Demonstration GIF](https://coendvrs.com/ezgif-7-9ba253689b.gif)

##

