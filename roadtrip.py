#Calvin Low
#Shows the total price for a road trip based on set prices of gas and hotel stays and variables for length of road trip, gas mileage and miles traveled in a day
print("Hi, I can calculate how much it would cost for a road trip!")
print()
print("Please keep in mind that gas is 3 dollars per gallon")
print("A stop at a hotel to spend the night is 75 dollars a night")
print()
length = float(input("How long will your trip be in miles?"))
print()
mpg = float(input("How many miles per gallon can you get out of your car?"))
print()
miles_per_day = float(input("How long in miles do you want to travel per day?"))
print()
t1 = length / mpg
t2 = round(t1)
t3 = float(3) * t2
t4 = length / miles_per_day
t5 = round (t4)
t6 = float(75) * t5
total = t3 + t6
print("Okay the total of your trip is", "$"+str(total))
print()
print("Have a good trip!")
input('Press ENTER to exit')
