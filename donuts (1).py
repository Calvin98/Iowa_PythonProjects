def donut_break(number):
    dozen = number // 12
    dozen_2 = number % 12
    cost = dozen*8
    cost_2 = dozen_2*0.75
    total = cost + cost_2
    print("Your total is", total ,"!")
    
    

    
