import numpy as np

days = ["Mon","Tue","Wed","Thu","Fri"]
arr = np.array([[4500,5200,4800,5000,5300],[4000,4100,3900,4200,4600],[6000,5800,5900,6100,6200]])
name = ["Jan:   ","Cheo:  ","Justin:"]

print(f"         {days[0]}  {days[1]}  {days[2]}  {days[3]}  {days[4]}")
counter = 0
for s in arr:
    print(f"{name[counter]} {s}")
    counter += 1

day_total = []

for i in range(len(arr[0])):
    total = 0
    for j in arr:
        total += j[i]
    day_total.append(total)

print("Results:")
counter = 0
for s in day_total:
    print(f"{days[counter]}: {s}")
    counter += 1

most_active = max(day_total)

day = day_total.index(most_active)

match day:
    case 0:
        weekday = "Monday"
    case 1:
        weekday = "Tuesday"
    case 2:
        weekday = "Wednesday"
    case 3:
        weekday = "Thursday"
    case 4:
        weekday = "Friday"


print(f"The most active day is {weekday}, with {most_active} total steps!")