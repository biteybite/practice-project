#defines types_of_people as 10
types_of_people = 10
#defines x as string, includes types_of_people
x = f"There are {types_of_people} types of people."

#defines variable binary as a string
binary = "binary"
#defines variable do_not as a string
do_not = "don't"
#defines y as a string with variables binary and do_not
y = f"Those who know {binary} and those who {do_not}."

#outputs string x in terminal
print(x)
#outputs string y in terminal
print(y)

#outputs string with string x in the terminal
print(f"I said: {x}")
#outputs string with string y in the terminal
print(f"I also said: '{y}'")

#defines variable hilarious as false
hilarious = False
#defines variable joke_evaluation as string with an operator
joke_evaluation = "Isn't that joke so funny?! {}"

#outputs string joke_evaluation in terminal, inserting value from hilarious
print(joke_evaluation.format(hilarious))

#defines variables w and e as strings
w = "This is the left side of..."
e = "a string with a right side."

#outputs string into terminal, w followed by e
print(w + e)
