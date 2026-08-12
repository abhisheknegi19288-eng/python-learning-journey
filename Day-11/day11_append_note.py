note = input("Enter your note: ")
with open("notes.txt", "a") as file:
    file.write(note + "\n")
print("Note has been added to notes.txt.")
