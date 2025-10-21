'''n=[1,2,3,4,5,6,7,8,9,10]
print(n[2:7:2])

print(n[4:100])
i=0
while i<len(n):
    print(n[i])
    i=i+1

for n1 in n:
    print(n1)
n=[1,5,1,1,4,4,4,5,4,5]
print(n.count(1))
print(n.count(4))
print(n.count(5))
print(n.count(9))

n=[1,2,2,2,2,2,3,3]
print(n.index(1))
print(n.index(2))
print(n.index(3))
#print(n.index(4))

n=[1,2,3,4,5]
n.insert(1,1998)
print(n)b;
n.insert(-10,4656)
print(n)

order1=["chicken",'"Prawns","Fish"]
order2=["RC","KF","FO"]
order1.extend(order2)
print(order1)
order1.extend("Mushroom")
print(order1

n=[10,20,30,40]
n.remove(10)
print(n)

n=[10,20,30,40,50]
print(n.pop())
print(n.pop())
print(n)
n.reverse()
print(n)
n.sort()
print(n)

s=["sindhu","saranti"]
s.sort()
print(s)

n1=[10,20,30,40]
n2=[55,44,33,22]
print(n1+n2)

n=[1,2,3,4,5]
print(n*3)

n=[10,20,30,40]
print(10 in n)
print(50 not in n)
n.clear()
print(n)

#NESTED LITS
n=[[1,2,3],[4,5,6],[7,8,9]]
print(n)
for r in n:
    print(r)

print("Elements by matrix style:")
for i in range(len(n)):
    for j in range(len(n[i])):
        print(n[i][j],end=' ')
    print()

t=(10)
print(t)
print(type(t))
t1=(10,20,60,40,50)
print(t1)
t=(10,)
print(t)
print(type(t))
t2=sorted(t1)
t3=sorted(t2,reverse=True)
print(t3)

s={10,20,30}
i=[40,50,60,10]
s.update(i,range(5))
print(s)

s={40,10,20,30}
print(s)
print(s.pop())
print(s)
print(s.pop())
s.discard(20)
s.discard(50)
print(s)

s1={1,2,3,4}
s2={7,8,9,3,4}
print(s1.union(s2))  #print(s1|s2))
print(s1.intersection(s2))
#symmetric difference
print(s1^s2)
d=dict()
d[100]="sai"
d[200]="saindhu"
d[300]="saranti"
print(d)

d=dict()
d[1]="harini"
d[2]="sindhu"
d[3]="divya"
d[4]="manisha"
print(d)
d[4]="Monisha"
print(d)'''

#Functions
def display():
    print("Hello")
def sum_dif(a,b):
    c=a+b
    d=a-b
    return c,d

display()
a,b=sum_dif(10,82)
print(a)
print(b)
