price=(101,255,55,50,40,48,68,99,199,299,101,101)
def costliest():
	costliest=price[0]
	for i in range(1,len(price)):
		if costliest<price[i]:
			costliest=price[i]
	return costliest
def cheapest():
	cheapest=price[0]
	for i in range(1,len(price)):
		if cheapest>price[i]:
			cheapest=price[i]
	return cheapest
	
def total():
	count=0
	for x in price:
		count+=1
	return count


def same():
	m=1
	x=101
	for i in range(1,len(price)):
		if price[i]==101:
			m+=1
	return m
print("**Daily shop**")
print("Prices:",price)
a=costliest()
print("costliest:",a)
b=cheapest()
print("cheapest:",b)
print("Total item sold:",total())
print("item with price 101:",same())
