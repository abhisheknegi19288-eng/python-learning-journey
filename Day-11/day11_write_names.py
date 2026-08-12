names = input("Enter names (comma-separated): ")

with open("names.txt", "w") as file:
    for name in names.split(","):
        file.write(name.strip() + "\n")
