def addition(num1,num2):
	result=num1+num2
	print("Addition of two number is\t:",result)
def substraction(num1,num2):
	result=num1-num2
	print("Substraction of two number is\t:",result)
def multiplication(num1,num2):
	result=num1*num2
	print("Multiplication of two number is\t:",result)
def division(num1,num2):
	result=num1/num2
	print("Division of two number is\t:",result)
def modulus(num1,num2):
	result=num1%num2
	print("Modulus of two number is\t:",result)

num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
choice=1
while choice==1:
	print("\n")
	print("****List of operations****")
	print("Press1-Addition:")
	print("Press2-Substraction:")
	print("Press3-Multiplication:")
	print("Press4-Division:")
	print("Press5-Modulus:")
	print("Press6-Exit")
	press=int(input("Enter your choice:"))
	
	if press==1:
		addition(num1,num2)
	elif press==2:
		substraction(num1,num2)
	elif press==3:
		multiplication(num1,num2)
	elif press==4:
		division(num1,num2)
	elif press==5:
		modulus(num1,num2)
	elif press==6:
		print("****************Exiting from application************")
		exit()
	choice=int(input("do you want to perform another operation(1-yes/0-no):"))

