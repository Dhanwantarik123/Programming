str = []
print("********Enter the information:*****")
n=int(input("Number of student :"))
for i in range(n):
	name = input("Enter name of student: ")
	c1 = int(input("Enter marks in Dsa: "))
	c2 = int(input("Enter marks in EDC: "))
	c3 = int(input("Enter marks in NT: "))
	total=float(c1+c2+c3)
	per=float(total/5.0)
	mytuple=(name,c1,c2,c3,total,per)
	print(mytuple)
	str.append(mytuple)
print(str)
	

def H():
	H=price[0]
	for i in range(1,len(price)):
		if H>price[i]:
			H=price[i]
	return H
	
def L():
	L=price[0]
	for i in range(1,len(price)):
		if L>price[i]:
			L=price[i]
	return L
print("Highest",H)

print("Lowest",L)
