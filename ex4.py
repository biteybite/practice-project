cars = 100 #defines variable cars
space_in_a_car = 4 #defines variable space_in_a_car
drivers = 30 #defines variable drivers
passengers = 90 #defines variable passengers
cars_not_driven = cars - drivers #defines variable cars_not_driven, takes total cars and subtracts drivers
cars_driven = drivers #cars driven is just how many drivers you have
carpool_capacity = cars_driven * space_in_a_car #drivers * cars to get total capacity
average_passengers_per_car = passengers / cars_driven #passengers / drivers to get average passengers


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
