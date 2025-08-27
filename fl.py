#L=[]
terms=int(input("Enter numbers of terms:\n")
n1 = 1
n2 = 3
i=1

while i < terms-1:
	next=n1+n2
	print(next)
	n1=n2
	n2=next
	i+=1
#for i in range(terms):
#	ele1=int(input)
	#L.append(ele1)
#print(L)
