def costliest_item(a,b,c):
	if a>b and a>c:
		costiest =a
	elif b>a and b>c:
		costliest=b
	else:
		costliest=c
	print("The Price of Costliest Item\t:",costliest)

def cheapest_item(a,b,c):
	if a<b and a<c:
		cheapest =a
	elif b<a and b<c:
		cheapest=b
	else:
		cheapest=c
	print("The Price of Cheapest Item\t:",cheapest)

item1=int(input("Enter price of first Item:\t"))
item2=int(input("Enter price of second Item:\t"))
item3=int(input("Enter price of third Item:\t"))

costliest_item(item1, item2, item3)
costliest_item(item1, item2, item3)
