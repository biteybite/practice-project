#defines formatter as a string function with four string components
formatter = "{} {} {} {}"

#outputs strings 1 2 3 and 4 into terminal using previously defined function
print(formatter.format(1, 2, 3, 4))
#same as above but this time with new strings
print(formatter.format("one", "two", "three", "four"))
#and this time w/ true and false statements
print(formatter.format(True, False, False, True))
#and this is what happens when it's used as a string printed out into terminal
print(formatter.format(formatter, formatter, formatter, formatter))
#and this demonstrates you can break the code up into multiple lines
print(formatter.format(
        "Try your",
        "Own text here",
        "Maybe a poem",
        "Or a song about fear"
))
