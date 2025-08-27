def sum1(num):
	sum=0
	while num!=0:
		digit=num%10
		sum=sum+digit
		num=int(num/10)
	print(sum)
num=int(input("Enter digit:")
sum1(num)
