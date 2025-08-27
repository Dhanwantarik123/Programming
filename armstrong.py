def magic(num):
	sum=0
	temp=num
	l=0
	while temp!=0:
		l=l+1
		temp=temp//10
	
	while num!=0:
		digit=num%10
		sum=sum+digit**l
		num=int(num//10)
	if temp==sum:
		print("The arstrong number is:", sum)
	else :
		print("The number is not armstrong number.")
num=int(input("Enter any number:"))
magic(num)

