stud=[]
print("********Enter the information:*****")
for i in range(0,2):
	name=input("Enter name student:")
	usn=input("Enter USN student:")
	contact=int(input("Enter Contact student:"))
	stream=input("Enter Stream student:")
	per=input("Enter percentage:")
	print("\n")
	print("Printing the tuple element")
	thistuple=(name,usn,contact,stream,per)
	print(thistuple)
	thistuple.append(stud)
print(stud)

