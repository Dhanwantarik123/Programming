str=[]
n=int(input("Enter number of element in  list of integer:\n"))
print("Enter list of integer:\n")
for i in range(n):
	ele=int(input())
	str.append(ele)
print("Printing the ist of integer:\n")
print(str)
l=len(str)
print("Total number of item:\n",l)

print("Last item in list:",str[l-1])
print("Reverse order:",str[::-1])
if 5 in str:
	print("5 is present-Yes\n")
else:
	print("5 is present-No\n")

cnt=0
for i in range(n):
	if str[i]==5:
		cnt+=1
	
print("The number 5  element in list:\n",cnt)
print("1st and last is remove:\n",str[1:-1])
print("Printing the list in sort\n",sorted(str))
