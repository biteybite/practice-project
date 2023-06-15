#creates function cheese_and_crackers, with arguments cheese_count and boxes_of_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    #prints format string using cheese_count argument to terminal
    print(f"You have {cheese_count} cheeses!")
    #prints format string using boxes_of_crackers argument, to terminal
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    #prints string to terminal
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

#guess where this string is going
print("We can just give the function numbers directly:")
#calls function cheese_and_crackers using arguments 20 & 30
cheese_and_crackers(20, 30)

#hey whats up im a string and im getting sent to terminal
print("OR, we can use variables from our script:")
#defines variable amount_of_cheese as 10
amount_of_cheese = 10
#defines variable amount_of_crackers as 50
amount_of_crackers = 50

#calls function cheese_and_crackers with variables amount_of_cheese and amount_of_crackers
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#yep straight to terminal lets go string
print("We can even do math inside too:")
#calls function cheese_and_crackers using arguments 10 + 20 and 5 + 6
cheese_and_crackers(10 + 20, 5 + 6)

#prints string to terminal
print("And we can combine the two, variables and math:")
#calls function cheese_and_crackers using amount_of_cheese + 100 and amount_of_crackers + 1000 as variables
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
