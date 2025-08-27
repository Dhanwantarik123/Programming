score=[]
n=int(input("Enter number of players :"))
for i in range(n):
	print("Enter Score for player -",(i+1))
	ele=int(input())
	score.append(ele)
print("The Scores:")
print(score)

lowest=score[0]
highest=score[0]
for i in range(1,n):
	if score[i]<lowest:
		lowest=score[i]
	if score[i]>highest:
		highest=score[i]
print("Highest:",highest)
print("Lowest :",lowest)

