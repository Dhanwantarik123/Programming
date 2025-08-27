def facto(num):
	temp=num
	count=1
	while count<temp:
		num=num*count
		count+=1
	print("The factorial is:",num)
num=int(input("enter any number:"))
facto(num)
