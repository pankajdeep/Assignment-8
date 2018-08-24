#Q.1- Create a circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class.
import math
class circle:
    def __init__(self,r):
        self.radius=r
    def getArea(self):
        self.area=math.pi*(self.radius**2)
    def getCircumference(self):
        self.circum=2*math.pi*self.radius
r=int(input("Enter Radius"))
c=circle(r)
c.getArea()
c.getCircumference()
print("Area is:",c.area,"Volume is:",c.circum)


#Q.2- Create a Student class and initialize it with name and roll number. Make methods to : 
#1. Display - It should display all informations of the student. 
#2. setAge - It should assign age to student 3. setMarks - It should assign marks to the student.
class student:
    __name=''
    __rno=0
    __age=0
    __marks=0
    def __init__(self,name,rno):
        self.__name=name
        self.__rno=rno
    def setAge(self,age):
        self.__age=age
    def setMarks(self,marks):
        self.__marks=marks
    def display(self):
        print("Name:",self.__name,"\nRoll No.",self.__rno,"\nAge:",self.__age,"\nMarks:",self.__marks)
name=input("Enter Name")
rno=int(input("Enter Roll No."))
s1=student(name,rno)
age=int(input("Enter Age"))
s1.setAge(age)
marks=int(input("Enter Marks"))
s1.setMarks(marks)
s1.display()


#Q.3- Create a Temperature class and create two methods: 
#1. convertFahrenheit - It will take celsius and will print it into Fahrenheit. 
#2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.
class Temperature:
    def convertFahrenheit(self,c):
        self.f=((c*9)/5)+32
        print("Temperature in Fahrenheit :",self.f)
    def convertCelsius(self,f):
        self.c=(f-32)*5/9
        print("Temperature in Celsius :",self.c)
temp=Temperature()
c=float(input("Enter temperature in Celsius"))
temp.convertFahrenheit(c)
f=float(input("Enter temperature in Fahrenheit"))
temp.convertCelsius(f)


#Q.4- Create a class MovieDetails and initialize it with artistname,Year of release and ratings . 
#Make methods to 
#1. Display-Display the details. 
#2. Add- Add the movie details.
class MovieDetails:
    __artistname=''
    __year=0
    __rating=0
    def Add(self,name,year,rating):
        self.__artistname=name
        self.__year=year
        self.__rating=rating
    def Display(self):
        print("The Artist Name is:",self.__artistname,"\nMovie is Released in year:",self.__year,"\nThe movie has rating:",self.__rating)
M=MovieDetails()
name=input("Enter the name of Artist")
year=int(input("Enter the year of movie release"))
rating=int(input("Enter ratings of movie"))
M.Add(name,year,rating)
M.Display()


#Q.5- Create a class Animal as a base class and define method animal_attribute.
#Create another class Tiger which is inheriting Animal and access the base class method.
class Animal:
    def animal_attribute(self):
        print("Name of animal is Tiger")
class Tiger(Animal):
    pass
t=Tiger()
t.animal_attribute()


#Q.6- What will be the output of following code.
#class A:
#       def f(self):
#            return self.g()
#
#       def g(self):
#            return 'A'
#
#class B(A):
#       def g(self):
#            return 'B'
#
#a = A()
#b = B()
#print a.f(), b.f()
#print a.g(), b.g()
OUTPUT IS :
'A' 'B'
'A' 'B'
The output is like this because a.f() calls function f() in class A which calls g() in class A which returns 'A' and
b.f() calls f() in class A which calls self.g() in class B so this means g() of class B will be called.
a.g() and b.g() will call g() of class A and B respectively. Here, method overriding is done.


#Q.7- Create a class Shape.Initialize it with length and breadth Create the method Area.
#Create class rectangle and square which inherits shape and access the method Area.
class Shape:
    def __init__(self):
        self.length=0
        self.breadth=0
    def Area(self):
        self.area=self.length*self.breadth
        return self.area
class rectangle(Shape):
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
class square(Shape):
    def __init__(self,s):
        self.length=s
        self.breadth=s
r=rectangle(5,4)
s=square(4)
print("Area of Square is:",s.Area(),"Area of Rectangle is:",r.Area())


    
