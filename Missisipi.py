def countP(s):
    num = 0
    for count in s:
        if count == "p":
            num = num + 1
    return num
print(countP("mississippi"))
    