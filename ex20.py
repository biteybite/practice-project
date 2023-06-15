#imports function argv from module sys
from sys import argv

#defines variable input_file as argv
script, input_file = argv

#defines function print_all with argument f
def print_all(f):
    #reads file and prints it to terminal
    print(f.read())
    
#defines finction rewind with argument f
def rewind(f):
    #sets file's current position, 0 means absolute positioning
    f.seek(0)

#defines function print_a_line with arguments line_count and f
def print_a_line(line_count, f):
    #calls print function with arguments line_count and f.readline
    print(line_count, f.readline())

#defines variable current_file as open function with argument input_file
current_file = open(input_file)

#let's go, right to terminal, calling the print function with a string
print("First let's print the whole file:\n")

#calls function print_all with argument current_file, prints the file to terminal
print_all(current_file)

#wew another string in the print function
print("Now let's rewind, kind of like a tape.")

#calls function rewind with argument current_file
rewind(current_file)

#let's go more strings in the terminal
print("Let's print three lines:")

#defines variable current_line as 1
current_line = 1
#calls function print_a_line with arguments current_line and current_file
print_a_line(current_line, current_file)

#increments current_line by 1
current_line += 1
#calls function print_a_line with the new value for current_line
print_a_line(current_line, current_file)

#increments current_line by 1
current_line += 1
#calls function print_a_line with the new value
print_a_line(current_line, current_file)
