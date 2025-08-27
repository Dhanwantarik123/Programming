mydict={
	"Name":"Dhanno",
	"Usn":"44",
	"Department":"sales"
}
print("------------------------------------")
print("Printing the Items in dictionary")
print(mydict)
print("Accessing the individual item in dictionary")
print(mydict["Name"])
print(mydict["Usn"])
print(mydict["Department"])
print("------------------------------------")
print("Printing the keys in dictionary")
print(mydict.keys())
print("------------------------------------")
print("Printing the values in dictionary")
print(mydict.values())
print("------------------------------------")
print("Printing the keys in dictionary")
for x in mydict:
	print(x)
print("------------------------------------")
print("Printing the keys in dictionary")
for x in mydict.keys():
	print(x)
print("------------------------------------")	
print("Printing the values in dictionary")
for x in mydict.values():
	print(x)
print("------------------------------------")
print("Searching the value")
if "Dhanno" in mydict.values():
	print("Available")
print("------------------------------------")	
print("Searching the key")
if "Name" in mydict.keys():
	print("Available")

print(mydict.items())
	
	
