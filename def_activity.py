# This function calculates the average of three grades
def calculate_average(grade1, grade2, grade3):
    return (grade1 + grade2 + grade3) / 3

#this is where to input grades from 1-3
#I use int  for input numbers float works but int is simpler for me
grade1 = int(input("Enter first grade: "))
grade2 = int(input("Enter second grade: "))
grade3 = int(input("Enter third grade: "))

average = calculate_average(grade1, grade2, grade3)

#prints or displays your average grade
print("Your average is:", average)
