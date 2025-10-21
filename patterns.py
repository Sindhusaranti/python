'''n=int(input("enter any number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,end=" ")
    print()

print()
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end=" ")
    print()

print()
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

print()
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()'''


#Accessing elements into matrix
r=int(input("Enter no.of rows:"))
c=int(input("Enter no.of colomuns:"))
x=[]
for i in range(r):
    val=[]
    for j in range(c):
        element=int(input(f"Enter element at position [{i}{j}]:"))
        val.append(element)
    x.append(val)

print("Matrix is:")
for rows in x:
    print(rows)
