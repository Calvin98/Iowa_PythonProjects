def time_string(time):
    for i in range(0, len(time)):
        if time[i] == ":":
            return i
    return -1
def minutes(time):
    index = time_string(time)
    hours = time[ :index]
    int_hours = int(hours) * 60
    minutes = time[index + 1: ]
    int_minutes = int(minutes)
    result = int_minutes + int_hours
    print(result)

minutes("10:30")


    
        