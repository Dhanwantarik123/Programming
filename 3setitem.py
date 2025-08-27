a={"199.99","150","160","170","299.99","298","293"}
b={"199.99","150","360","180","399.99","298","293"}
c={"170","160","360","150","180","299.99","399.99"}
x=a.union(b)
y=x.union(c)
print("No item sold today\n",y)
z=a.intersection(b)
print(z.intersection(c))
