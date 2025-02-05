import json

grades = "mike 3.4, noel 3.2, obby 3.5, peta 3.4"
grades_list = grades.split(", ")
grades_json = []
for grade in grades_list:
    name, gpa = grade.split()
    grades_json.append({name: float(gpa)})
print(grades_json)
with open("Challenges/grades.json", "w") as f:
    json.dump(grades_json, f)