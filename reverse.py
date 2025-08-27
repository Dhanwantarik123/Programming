def rev(num):
	rev=0
	while num!=0:
		digit=num%10
		rev=rev*10+digit
		num=int(num/10)
	print("Reverse numbers are:",rev)
num=int(input("enter any number:"))
rev(num)
