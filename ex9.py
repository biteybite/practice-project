# Here's some strange stuff, remember type it exactly.

#defines var days as following string
days = "Mon Tue Wed Thu Fri Sat Sun"
#defines var months as following string, operator n creates a new line
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

#prints following string, then var days
print("Here are the days: ", days)
#same as above, but due to operator n prints in new lines when outputting var months
print("Here are the months: ", months)

#triple quotes allow you to define a string with multiple lines
print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")
