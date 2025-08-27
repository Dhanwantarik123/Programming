def facto(num):
		if num==0 or num==1:
			return 1
		else:
			return num*facto(num-1)
	

n=int(input("enter value of n number:"))

i=1
total=0
while i<=n:
	total=facto(i)
	result=total+facto(i)/i
	i+=1
print("Factorial of given number:",result)
