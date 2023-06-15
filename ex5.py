name = 'Zed A. Shaw'
age = 35 #not a lie
height = 74 #inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

height_m = height * 2.54
weight_m = weight * 0.45

print(f"Let's talk about {name}.")
print(f"He's {height_m} cm tall.")
print(f"He's {weight_m} kg heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} and {teeth} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

#this line is tricky, try to get it exactly right
total = round(age + height_m + weight_m)
print(f"If I add {age}, {height_m}, and {weight_m} I get {total}.")
