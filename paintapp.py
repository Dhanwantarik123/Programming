inte=int(input("Enter number of interior wall:\n"))
if inte!=0:

	intarea=int(input("Enter surface area of interior wall:\n"))
	interiorp=18*intarea*inte
	print("Interior Price:\n",((int)(interiorp)))
	
ext=int(input("Enter number of exterior wall:\n"))
if ext!=0:

	extarea=int(input("Enter surface area of exterior wall:\n"))
	exteriorp=12*extarea*ext
	print("Exterior Price:\n",((int)(exteriorp)))
	
print("Estimated cost of painting \t:\n",(interiorp+exteriorp))
