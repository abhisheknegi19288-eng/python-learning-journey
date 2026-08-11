python_students = {"Abhishek", "Rahul", "Aman", "Rohit"}
java_students = {"Rahul", "Rohit", "Vikas", "Karan"}

print("Students learning python and java both:",python_students & java_students)
print("Students learning only python:",python_students - java_students)
print("All unique :",(python_students | java_students))
