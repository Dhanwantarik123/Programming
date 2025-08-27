marks=[]
print("Enter the marks obtained in 5 course ")
for i in range(5):
	course=int(input())
	marks.append(course)
print("The marks obtained in 5 course are as follows:")
total=0
for i in range(5):
	total=total+marks[i]
per=total/5.0
print("the Marks are:")  
print(marks)
print(total)
print(per)
