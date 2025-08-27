def rev1(num):
	rev=0
	while num!=0:
		digit=num%10
		rev=rev*10+digit
		num=int(num/10)
	return rev
num=int(input("enter any number:"))
temp=rev1(num)
if temp==num:
	print("yes")
