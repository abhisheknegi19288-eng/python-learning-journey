name = input("Enter a name: ")
age = input("Enter age: ")
course = input("Enter course: ")
with open("student.txt", "a") as file:
    file.write(f"Name: {name}\nAge: {age}\nCourse: {course}\n")
