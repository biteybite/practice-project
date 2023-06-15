#imports function argv from module sys
from sys import argv

#uses argv to import a filename from the command line
script, filename = argv

#defines variable txt as open file with the previously defined argv (by default, for reading text)
txt = open(filename)

#displays a message in terminal using print function, inserts filename into the string
print(f"Here's your file {filename}:")
#runs variable txt to read file w/ no parameters and outputs to terminal
print(txt.read())
#closes file :)
txt.close()


#outputs string to terminal
#print("Type the filename again:")
#requests input from user to define variable file_again, prompts with a brief string
#file_again = input("> ")

#defines variable txt_again as open function w/ default parameters, using previously defined user input
#txt_again = open(file_again)

#uses read function for the previously defined file, and exports the contents to terminal
#print(txt_again.read())
