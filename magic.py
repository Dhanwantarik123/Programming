num=int(input("Enter any number:"))
power=int(input("Enter length of given number:"))
sum=0
while num!=0:
	digit=num%10
	sum=sum+digit^(power)
	num=int(num/10)
if num==sum:
	print("The Magic number is:", sum)
else :
	print("The Magic number is Not found:")
