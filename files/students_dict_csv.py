import csv

students = []

with open("files/students_dict.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # students.append({"name": row["name"], "home": row["home"]})
        students.append(row)

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")


new_students = [
    {"name": "Cindy", "home": "Rome"},
    {"name": "Alvin", "home": "Madrid"}
]
fields = ["name", "home"]

with open("files/students_dict.csv", "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writerows(new_students)