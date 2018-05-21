print("Hi welcome to the donut shop! It's 75 cents each, a dozen is 8 dollars!")
number = int(input("How many would you like to order?"))
dozen = number // 12
dozen_2 = number % 12
cost = dozen*8
cost_2 = dozen_2*0.75
total = cost + cost_2
print("That will be ", total) 
