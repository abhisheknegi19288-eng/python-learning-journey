student_name = input("Student Name: ")
marks_phy = int(input("Enter Physics marks: "))
marks_math = int(input("Enter Maths marks: "))
marks_chemi = int(input("Enter Chemistry marks: "))
marks_total = marks_phy + marks_math + marks_chemi
marks_avg = marks_total/3
print("------ Student Report ------")
print("Student Name: ", student_name)
print("Physics: ", marks_phy)
print("chemistry:", marks_chemi)
print("maths:", marks_math)
print("Total:", marks_total)
print("Average: ", marks_avg)