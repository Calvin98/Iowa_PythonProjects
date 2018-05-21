def mousetrap_cost(num):
    if num >= 20:
        box = num // 20
        left = num % 20
        cost_box = box * 50
        cost_left = left * 3
        ship_left = (left * .25) + cost_left
        ship_box = (box * 4) + cost_box
        total = ship_left + ship_box
        plus_tax = total * 1.065
        
    else:
        cost = num * 3
        total = (num * .25) + cost
        plus_tax = total * 1.065
    return plus_tax


    