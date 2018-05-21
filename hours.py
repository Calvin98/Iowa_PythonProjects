hours = float(input("How many hours do you work"))
exempt = input("Are you exempt?")
if hours >= 40:
    if exempt == "T":
        print("Your pay is 440 dollars")
    else:
        print("Your pay mis 460 dollars")
else:
    if exempt == "T":
        print("Your pay is 200 dollars")
    else:
        print("Your pay mis 200 dollars")
        