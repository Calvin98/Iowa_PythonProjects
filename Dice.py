import random

def dice_roll(n):
    num = 0
    for i in range(n):
        dice1 = random.randrange(1, 7)
        dice2 = random.randrange(1, 7)
        if dice1 == dice2:
            num = num + 1
    print(num)
        

dice_roll(1000)