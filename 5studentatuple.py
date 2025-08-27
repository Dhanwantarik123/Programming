stud = []
print("********Enter the information:*****")
for i in range(2):
    name = input("Enter name of student: ")
    usn = input("Enter USN of student: ")
    contact = int(input("Enter contact number of student: "))
    stream = input("Enter stream of student: ")
    per = float(input("Enter percentage: "))  

    print("\nPrinting the tuple element")
    thistuple = (name, usn, contact, stream, per)
    print(thistuple)

    stud.append(thistuple)

highest = stud[0]
for student in stud[1:]:
    if student[4] > highest[4]:  
        highest = student

print("\nAll student records:",stud)

print("\nStudent with highest percentage:")
print(highest)

