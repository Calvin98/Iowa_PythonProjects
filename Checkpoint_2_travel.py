def how_long(given_amount, stripend, rate):
    count = 0
    while given_amount >= 0:
        given_amount = given_amount - stripend
        given_amount = given_amount + given_amount * rate
        count = count + 1
        print(given_amount)
    print(count - 1, "months until out of money.")
    
        
how_long(10000, 400, .005)
