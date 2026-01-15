import numpy as np

days = ["Mon","Tue","Wed","Thu","Fri"]
arr = np.array([[4500,5200,4800,5000,5300],[4000,4100,3900,4200,4600],[6000,5800,5900,6100,6200]])
name = ["Jan   ","Cheo  ","Justin"]

print(f"         {days[0]}  {days[1]}  {days[2]}  {days[3]}  {days[4]}")
counter = 0
for s in arr:
    print(f"{name[counter]}: {s}")
    counter += 1

total_jan = np.sum(arr[0])
total_cheo = np.sum(arr[1])
total_justin = np.sum(arr[2])
print("Totals:")
print(f"Jan:    {total_jan}")
print(f"Cheo:   {total_cheo}")
print(f"Justin: {total_justin}")

if total_jan > total_cheo:
    if total_jan > total_justin:
        highest = name[0]
        index = 0
if total_cheo > total_jan:
    if total_cheo > total_justin:
        highest = name[1]
        index = 1
if total_justin > total_jan:
    if total_justin > total_cheo:
        highest = name[2]
        index = 2

print(f"HIGHEST Total: {highest} at {np.sum(arr[index])} steps!")

if total_jan < total_cheo:
    if total_jan < total_justin:
        lowest = name[0]
        difference = np.sum(arr[index]) - np.sum(arr[0])
if total_cheo < total_jan:
    if total_cheo < total_justin:
        lowest = name[1]
        difference = np.sum(arr[index]) - np.sum(arr[1])
if total_justin < total_jan:
    if total_justin < total_cheo:
        lowest = name[2]
        difference = np.sum(arr[index]) - np.sum(arr[2])

print(f"The difference between the highest ({highest}) and the lowest ({lowest}) is {difference}")