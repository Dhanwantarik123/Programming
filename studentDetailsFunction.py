def read_data():
	name=input("Enter  name of student:")
	usn=input("Enter USN:")
	dept=input("Enter Department:")
	sem=input("Enter Semester:")
	display_data(name,usn,dept,sem)
def display_data(name,usn,dept,sem):
	print("Name of student\t\t:"+name)
	print("USN of student\t\t:"+usn)
	print("Department of student\t:"+dept)
	print("Semester of student\t:"+sem)
	
read_data()

