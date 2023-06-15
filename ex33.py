numbers = []

def loopy(meow):
    i = 0
    for x in range(meow):
        print(f"At the top i is {i}")
        numbers.append(i)
    
        i = i + 1
        print("Numbers now:", numbers)
        print(f"At the bottom i is {i}")

loopy(10)

print("The numbers: ")

for num in numbers:
    print(num)
