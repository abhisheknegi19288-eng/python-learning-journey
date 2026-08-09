word = input("Enter a palindrome: ")
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
