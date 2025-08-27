terms=int(input("Enter numbers of terms:\n")
n1 = 1
n2 = 3
i=1
while i < terms:
	next=n1+n2
	print(next)
	n1=n2
	n2=next
	i+=1
