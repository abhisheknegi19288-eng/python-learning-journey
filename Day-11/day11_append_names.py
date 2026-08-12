names = input("Enter names (comma-separated): ")

with open("names.txt", "a") as file:
    for name in names.split(","):
        file.write(name.strip() + "\n")
print("Names have been added to names.txt.")
