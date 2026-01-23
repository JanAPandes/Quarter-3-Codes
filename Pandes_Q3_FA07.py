#Quarter 3 - FA 07 - (Based on SG 5: Activity 2: Summarizing Your Dataset with Arrays)

students = []

for i in range(3):
    dict = {
    "name":"",
    "age":0,
    "grade":0
}
    name = str(input("Enter name: "))
    dict["name"] = name
    age = int(input("Enter age: "))
    dict["age"] = age
    grade = int(input("Enter grade: "))
    dict["grade"] = grade
    students.append(dict)
    print("")

print("Class Directory:")
counter = 0
for s in students:
    print(f"{students[counter]["name"]} | Age: {students[counter]["age"]} | Grade: {students[counter]["grade"]}")
    counter += 1
