def sum_1(num):
	sum=0
	while num != 0:
		digit = num%10
		sum = sum+digit
		num = int(num/10)
	
	
num = int(input("Enter digit:"))

if(sum==num):
	sum_1(num)
	print(num)
	
