# Store client names
Name = []
n = int(input("Enter number of clients: "))

print("Enter Name of clients:")
for i in range(n):
    ele = input(f"Client {i+1} name: ")
    Name.append(ele)

print("\nThe Names of clients:")
print(Name)

# Store hours worked for each client
c = []
print("\nEnter hours worked for each client:")
for i in range(n):
    ele = int(input(f"Hours worked by {Name[i]}: "))
    c.append(ele)

print("\nThe work hours of all clients:")
print(c)

# Store hourly rate for each client
r = []
print("\nEnter hourly rate for each client:")
for i in range(n):
    ele = int(input(f"Hourly rate for {Name[i]}: "))
    r.append(ele)

print("\nThe Hourly rate for each client:")
print(r)

# Calculate total income
t = []
total = 0
for i in range(n):
    income = c[i] * r[i]
    t.append(income)
    total += income

print("\nIncome from each client:", t)
print("Total income for the month:", total)
