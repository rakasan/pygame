PyGame testing enviroment

1st issue : pip has an issue with python 3.11, in which setup.py does not work. I had to downgrade to 3.10 in order to make it work.
2nd issue : if you get a syntax error, with only the import pygame, you are tryng to run a Python program from inside a python shell. Change it to PowerShell, and close the python one (https://www.reddit.com/r/pygame/comments/sczt01/syntax_error_import_pygame/)

How to convert from a py file into exec : 
install pyinstaller ( pip install pyinstaller)
go to the location of the script you want to convert and run pyinstall --onefile -w main.py
-w ( to not show the console)

NSIS - tool for converting from an zip to un install package