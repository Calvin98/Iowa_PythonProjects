hours = float(input("How many hours do you work"))
exempt = input("Are you exempt?")
T = 't' and ' t'
F = 'f' and ' f'
total_2 = hours * 10
if hours >= 40:
    if exempt == F:
        total_1 = hours * (10/11/2 + 10)
        print("Your pay is" , total_1 ,"dollars")
    else:
        print("Your pay is" , total_2, "dollars")
        
elif exempt == F:
    print("Your pay is" , total_2, "dollars")
    
else:
    print("Your pay is" , total_2, "dollars")
        