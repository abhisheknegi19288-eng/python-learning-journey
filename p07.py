students = []
while True:
    print("1. Add student")
    print("2. Remove student")
    print("3. Display students")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        students.append(input("Enter student name: "))
    elif choice == "2":
        name = input("Enter student name to remove: ")
        if name in students:
            students.remove(name)
        else:
            print("Student not found.")
    elif choice == "3":
        print("Students:", students)
    elif choice == "4":
        break