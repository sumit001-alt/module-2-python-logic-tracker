print("Welcome to Smart Eligibility & Performance Checker\n\n")
name = input("Enter name: ")
age = int(input("Enter age: "))
exam_score = float(input("Enter exam numbers(0-100): "))
Monthly_income = float(input("Enter monthly income: "))


print("\n")
if age<18:
    print("You are not eligible due to age restriction.")
else:
    print("Age requirement passed.")

if exam_score>=90:
    grade="A"
elif exam_score>=75:
    grade="B"
elif exam_score>=60:
    grade="C"
else:
    grade="Fail"
print("Grade: ",grade)

if Monthly_income <20000 and exam_score > 75:
    scolarship="Eligible"
    print("Eligible for scholarship support.")
else:
    scolarship="Not Eligible"
    print("Not eligible for scholarship.")

if age> 18 or age==18:
    if exam_score>=60:
        print("You passed the program.")
    else:
        print("You failed the program.")
else:
    print("Program access denied")

print("\n\n----- Final Summary -----")
print("Name: ",name)
print("Age: ",age)
print("Score: ",exam_score)
print("Grade: ",grade)
print("Scholarship: ",scolarship)






