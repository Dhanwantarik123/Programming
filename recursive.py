def facto(num):
	if num==0 or num==1:
		return 1
	else:
		return num*facto(num-1)
	
num=int(input("enter any number:"))
result=facto(num)
print("Factorial of given number:",result)
