str =[]
n=int(input("Enter number of string:"))
for i in range(n):
	ele=input()
	str.append(ele)
print("Original string:")
print(str)
new=[]
print("New string winthout first character")
for i in range(n):
	if len(str[i])>0:
		new.append(str[i][1:])
	else:
		new.append("")
print(new)
