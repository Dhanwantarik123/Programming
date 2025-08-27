L = []
terms = int(input("Enter number of terms: "))
n1=0
n2 = 1
L.append(n1)
L.append(n2)

i = 2
while i < terms:
    next = n1 + n2
    L.append(next)
    n1=n2 
    n2=next
    i += 1

print("Fibonacci sequence:", L)

fibo = []
for L in L[:terms]:  
    if L % 2 != 0:
        fibo.append(L)

print("Printing the odd series of Fibonacci:", fibo)

