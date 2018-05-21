def egg_cost(num):
    dozen = num // 12
    half_dozen = num % 12
    actual = half_dozen // 6
    remainder = half_dozen % 6
    dozen_cost = dozen * 3
    half_cost = actual * 1.75
    rem_cost = remainder * 0.30
    total = rem_cost + half_cost + dozen_cost
    return total
print(egg_cost(30))
