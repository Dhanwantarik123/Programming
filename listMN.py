L=[]
M=[]
N=[]
n=int(input("Enter number of element in  list :\n"))
print("Enter list of element in list L:\n")

for i in range(n):
	ele1=int(input())
	L.append(ele1)
print("Printing the list L:\n")
print(L)
print("Enter list of element in list M:\n")

for i in range(n):
	ele2=int(input())
	M.append(ele2)
print("Printing the list M :\n")
print(M)

for i in range(n):
	ele3=L[i]+M[i]
	N.append(ele3)
print("Printing the list N:\n")
print(N)
	
