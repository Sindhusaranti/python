'''#INSTANCE CLASS
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print('Hi',self.name)
        print('Your Marks are:',self.marks)
    def grade(self):
        if self.marks>=60:
            print('You got first grade')
        elif self.marks>=50:
            print('You got second Grade')
        elif self.marks>=35:
            print('You got third Grade')
        else:
            print('You failed')
n=int(input('Enter number of students:'))
for i in range(n):
    name=input('Enter name:')
    marks=int(input('Enter marks:'))
    s=student(name,marks)
    s.display()
    s.grade()
    print()

#CLASS METHODS
class test:
    count=0
    def __init__(self):
        test.count=test.count+1
    @classmethod
    def noofobjects(cls):
        print('The no.of objects created for test class:',cls.count)

t1=test()
t2=test()
test.noofobjects()
t3=test()
t4=test()
t5=test()
test.noofobjects()

#STATIC CLASS
class aditya:
    @staticmethod
    def add(x,y):
        print('The sum value is:',(x+y))

    @staticmethod
    def sub(x,y):
        print('The subtraction value is:',(x-y))

    @staticmethod
    def avg(x,y):
        print('The average value is:',(x+y)/2)
aditya.add(200,100)
aditya.sub(200,100)
aditya.avg(200,100)'''

#Single Inheritance

class Animal:
    def sound(self):
        print('Animal Sound')
class Dog(Animal):
    def bark(self):
        print('Bark')
d=Dog()
d.sound()
d.bark()

#MULTPIPLE INHERITANCE

class A:
    def methodA(self):
        print("Method A")
class B:
    def methodB(self):
        print('method B')
class C(A,B):
    def methodC(self):
        print('Method C')
c=C()
c.methodA()
c.methodB()
c.methodC()

#HYBRID INHERITANCE

class A:
    def methodA(self):
        print("A")
class B(A):
    def methodB(self):
        print('B')
class C:
    def methodC(self):
        print('C')
class D(B,C):
    pass

d=D()
d.methodA()
d.methodB()
d.methodC()


