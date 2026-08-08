student = {
    "name": "Abhishek",
    "roll_no": 101,
    "course": "BCA",
    "marks": {
        "Python": 90,
        "Maths": 85,
        "English": 80
    }
}
print(f"Name: {student['name']}")
print(f"Roll no: {student['roll_no']}")
print(f"Course: {student['course']}")
for subject, marks in student["marks"].items():
    print(subject, ":", marks)
