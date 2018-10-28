#imports the argument variable
from sys import argv

#labels the argument order for the powershell input
script, filename = argv

#when inputting a txt file, it will open it and reveal its contents
txt = open(filename)

#this will print out "here's your file" and display the contents of the txt file
print(f"Here's your file {filename}")
print(txt.read())

#This will print "Type the filename again" and you can input your txt file again
print("Type the filename again")
file_again = input("> ")

#this forces to open the content of the txt file
txt_again = open(file_again)

#this prints the txt.file on the terminal
print(txt_again.read())
