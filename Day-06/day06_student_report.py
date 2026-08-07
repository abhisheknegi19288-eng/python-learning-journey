def student(name, physics, chemistry, maths):
    total = physics + chemistry + maths
    average = total / 3
    print("------ Student Report ------")
    print(f"Name: {name}")
    print(f"Physics: {physics}")
    print(f"Chemistry: {chemistry}")
    print(f"Maths: {maths}")
    print(f"Total: {total}")
    print(f"Average: {average}")
student("Abhishek", 85, 90, 95)