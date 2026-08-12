while True:
    print("\n1. Add student")
    print("2. View student")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter a name: ")
        age = input("Enter age: ")
        course = input("Enter course: ")

        with open("student.txt", "a") as file:
            file.write(f"Name: {name}\nAge: {age}\nCourse: {course}\n")

        print("Student added successfully!")

    elif choice == 2:
        with open("student.txt", "r") as file:
            for line in file:
                print(line.strip())

    elif choice == 3:
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")
