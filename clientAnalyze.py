Name=[]
n=int(input("Enter number of day work done by client:"))
print("Enter Name of client :")
for i in range(n):
	ele=input()
	Name.append(ele)
print("The Name of client:")
print(Name)

c=[]
print("Enter hours worked for each client :")
for i in range(n):
	ele=int(input())
	c.append(ele)
print("The work of all day:")
print(c)

r=[]
print("Enter hours worked for each client :")
for i in range(n):
	ele=int(input())
	r.append(ele)
print("The Hourly rate for each client:")
print(r)
t=[]
total=0
for i in range(n):
	total=total+c[i]*r[i]
print("Total  income for the month:",total)

