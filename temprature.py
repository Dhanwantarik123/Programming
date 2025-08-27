temp=int(input("Enter the Temperature:"))
if temp<-293:
	print("Invalid Temperature")
elif temp==-293:
	print("Absolute Zero Temperature")
elif temp>-293 and temp<0:
	print("Below Freezing point")
elif temp ==0:
	print("At Freezing point of Temperature")
elif temp>0 and temp<27:
	print("Normal room Temperature")
elif temp>27 and temp<100:
	print("bellow boiling point ofTemperature")
elif temp ==100:
	print("At Boiling point of Temperature")
elif temp> 100:
	print("Above boiling point") 
