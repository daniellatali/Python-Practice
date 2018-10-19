#Cars is equal to 100
cars = 100
#space in the car is 4.0 which is a floating point
space_in_a_car = 4.0
#driver is equal to 30
drivers = 30
#passengers is equal to 90
passengers = 90
#cars not driven is cars minus the drivers
cars_not_driven = cars - drivers
#cars driven is equal to drivers
cars_driven = drivers
#carpool_capacity is cars driven times the space in the cars
carpool_capacity = cars_driven * space_in_a_car
#average_passengers_per_car equals to passengers divided by the amount of cars driven
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
