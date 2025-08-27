total=0
def pasta(num):
	global total
	result=250*num
	total=total+result
	print("The price of Pasta\t:",result)
def dosa(num):
	global total
	result=150*num
	total=total+result
	print("The price of Dosa\t:",result)
def noodles(num):
	global total
	result=100*num
	total=total+result
	print("The price of Noodles\t:",result)
def paneer(num):
	global total
	result=300*num
	total=total+result
	print("The price of Paneer Butter Masala\t:",result)
def samosa(num):
	global total
	result=50*num
	total=total+result
	print("The price of Samosa\t:",result)
def bill():
	global total
	print("--------------------------")
	print("The Total Bill\t:",total)
	print("--------------------------")

choice=1
while choice==1:
	print("\n")
	print("****List of Menu****")
	print("Press1-Pasta:")
	print("Press2-Dosa:")
	print("Press3-Noodles:")
	print("Press4-paneer butter masala:")
	print("Press5-Samosa:")
	print("Press6-Bill")
	print("Press7-Exit")
	press=int(input("Enter your choice:"))
	
	if press==1:
		num=int(input("Enter quantity:"))
		pasta(num)
	elif press==2:
		num=int(input("Enter quantity:"))
		dosa(num)
	elif press==3:
		num=int(input("Enter quantity:"))
		noodles(num)
	elif press==4:
		num=int(input("Enter quantity:"))
		paneer(num)
	elif press==5:
		num=int(input("Enter quantity:"))
		samosa(num)
	elif press==6:
		bill()
	elif press==7:
		print("****************Thankyou ! Visit again.************")
		exit()
	else:
		print("Invalid Choice,try again.")
	choice=int(input("do you want to perform another operation(1-yes/0-no):"))

