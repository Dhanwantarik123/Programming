str=[]
n=int(input("Enter number of element in  list of integer:"))
print("Enter list of integer:")
for i in range(n):
	ele=int(input())
	str.append(ele)
print(str)
l=len(str)
print("Total number of item:",l)

print("Last item in list:",(str[l-0]))
print("Reverse order:",str[::-1])
if str[i]==5:
	print("5 is present-Yes")
else:
	print("5 is present""No")
print("The fifth element:",(str[4]))
print("1st and last is remove:",(str[1:-1]))
	
