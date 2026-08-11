numbers = []

for i in range(5):
    num = int(input(f"Enter number {i +1}:"))
    numbers.append(num)
if len(numbers) != len(set(numbers)):
    print("Duplicate numbers found. Please enter unique numbers.")
else:
    print("All numbers entered are unique.")
