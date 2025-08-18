students = []

print("********Enter the information:*****")
n = int(input("Number of students: "))

for i in range(n):
    name = input("Enter name of student: ")
    c1 = int(input("Enter marks in DSA: "))
    c2 = int(input("Enter marks in EDC: "))
    c3 = int(input("Enter marks in NT: "))
    total = float(c1 + c2 + c3)
    per = float(total / 3.0)
    student_tuple = (name, c1, c2, c3, total, per)
    print(student_tuple)
    students.append(student_tuple)

print(students)

percentages = [student[5] for student in students]

def H():
    high = students[0]
    for i in range(1, len(students)):
        if students[i]>high:
            high = students[i]
    return high

def L():
    low = students[0]
    for i in range(1, len(students)):
        if students[i]<low:
            low = students[i]
    return low

print("Highest", H())
print("Lowest", L())
def avg():
	for i in range(1, len(students)):
		if per>=50:
			print(per)
	return per

