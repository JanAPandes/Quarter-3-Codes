import numpy as np

days = ["Mon","Tue","Wed","Thu","Fri"]
arr = np.array([[4500,5200,4800,5000,5300],[4000,4100,3900,4200,4600],[6000,5800,5900,6100,6200]])
name = ["Jan:   ","Cheo:  ","Justin:"]

print(f"         {days[0]}  {days[1]}  {days[2]}  {days[3]}  {days[4]}")
counter = 0
for s in arr:
    print(f"{name[counter]} {s}")
    counter += 1

counter = 0
for s in name:
    print(f"{name[counter]} - Total Steps: {np.sum(arr[counter])} | Average: {np.average(arr[counter])} | Min: {np.min(arr[counter])} | Max: {np.max(arr[counter])}")
    counter += 1