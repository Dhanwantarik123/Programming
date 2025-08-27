temp=[]
n=int(input("Enter number of day  -"))
print("Enter Temperature of  Days -")
for i in range(n):
	ele=int(input())
	temp.append(ele)
print("The temperature of all day:")
print(temp)
total=0
for i in range(1,n):
	total=total+temp[i]
avg=total/n
print("Average:",avg)
lowest=temp[0]
highest=temp[0]
for i in range(1,n):
	if temp[i]<lowest:
		lowest=temp[i]
	if temp[i]>highest:
		highest=temp[i]
print("Highesttemperature:",highest)
print("Lowest temperature:",lowest)
Diff=highest-lowest
print("Differnece:",Diff)
