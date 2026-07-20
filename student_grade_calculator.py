# Student Grade Calculator

student_name = input("Enter student name: ")

subjects = ["Math", "Science", "English", "Computer", "Hindi"]
marks = []

for subject in subjects:
    while True:
        mark = int(input(f"Enter marks for {subject}: "))

        if 0 <= mark <= 100:
            marks.append(mark)
            break
        else:
            print("Invalid marks! Please enter marks between 0 and 100.")

total = sum(marks)
average = total / len(marks)
percentage = (total / 500) * 100

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

result = "PASS"

for mark in marks:
    if mark < 33:
        result = "FAIL"
        break

# Display Report
print("\n========== STUDENT REPORT ==========\n")

print(f"Student Name : {student_name}\n")

for i in range(len(subjects)):
    print(f"{subjects[i]:<12} : {marks[i]}")

print("-----------------------------------")
print(f"Total        : {total}/500")
print(f"Percentage   : {percentage:.2f}%")
print(f"Average      : {average:.2f}")
print(f"Grade        : {grade}")
print(f"Result       : {result}")

print("===================================")
