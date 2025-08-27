total=0
def starter ():
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
def main():
	def MaharastraThali(num):
		global total
		result=250*num
		total=total+result
		print("The price of Maharastra Thali\t:",result)
	def MaharajaThali(num):
		global total
		result=250*num
		total=total+result
		print("The price of Maharaja Thali\t:",result)
	def GujratiThali(num):
		global total
		result=250*num
		total=total+result
		print("The price of Gujrati Thali\t:",result)
def desert():
	def gulabjamun(num):
		global total
		result=250*num
		total=total+result
		print("The price of Gulab Jamun\t:",result)
	def shahitukda(num):
		global total
		result=250*num
		total=total+result
		print("The price of Shahi Tukda\t:",result)
	def cheesecake(num):
		global total
		result=250*num
		total=total+result
		print("The price of cheesecake\t:",result)
def bill():
	global total
	print("--------------------------")
	print("The Total Bill\t:",total)
	print("--------------------------")

choice=1
while choice==1:
	print("\n")
	print("****List of Menu****")
	print("Press1-Starter:")
	print("Press2-Main:")
	print("Press3-Desert:")
	print("Press6-Bill")
	print("Press7-Exit")
	press=int(input("Enter your choice:"))
	
	if press==1:
		print("****List of Menu****")
		print("Press1-Starter:")
		print("Press2-Main:")
		print("Press3-Desert:")
		print("Press4-Bill")
		print("Press5-Exit")
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
		elif press==4:
			print("****************Thankyou ! Visit again.************")
			exit()
	elif press==2:
		print("****List of Menu****")
		print("Press1-Starter:")
		print("Press2-Main:")
		print("Press3-Desert:")
		print("Press4-Bill")
		print("Press5-Exit")
		if press==1:
			num=int(input("Enter quantity:"))
			MaharastraThali(num)
		elif press==2:
			num=int(input("Enter quantity:"))
			MaharajaThali(num)
		elif press==3:
			num=int(input("Enter quantity:"))
			GujratiThali(num)
		elif press==4:
			bill()
		elif press==5:
			print("****************Thankyou ! Visit again.************")
			exit()
	elif press==3:
		print("****List of Menu****")
		print("Press1-Starter:")
		print("Press2-Main:")
		print("Press3-Desert:")
		print("Press4-Bill")
		print("Press5-Exit")
		if press==1:
			num=int(input("Enter quantity:"))
			MaharastraThali(num)
		elif press==2:
			num=int(input("Enter quantity:"))
			MaharajaThali(num)
		elif press==3:
			num=int(input("Enter quantity:"))
			GujratiThali(num)
		elif press==4:
			bill()
		elif press==5:
			print("****************Thankyou ! Visit again.************")
			exit()
		else:
			print("Invalid Choice,try again.")
		choice=int(input("do you want to perform another operation(1-yes/0-no):"))

