#Quarter 3 - FA 06 - (Based on SG5 : Activity Set 1: Student Profile Creator (Using Dictionary))

dict = {
    "name": "",
    "age": 0,
    "favorite subject": ""
}

name = str(input("Enter your name: "))
age = str(input("Enter your age: "))
fav_sub = str(input("Enter your favorite subject: "))

dict["name"] = name
dict["age"] = age
dict["favorite subject"] = fav_sub

print("\nStudent Record:")
print(f"Name: {dict["name"]}")
print(f"Age: {dict["age"]}")
print(f"Favorite Subject: {dict["favorite subject"]}")