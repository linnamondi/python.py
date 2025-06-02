class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sound(self):
        print(f"{self.name} {self.age} and says wooof!")

class Animal:
    def __init__(self,species):
        self.species=species
    def sound(self):
        print("some generic sound")
class Cat(Animal):
    def __init__(self,name,age):

        self.name=name
        self.age=age
    def sound(self):
        print("wolf!")
# Define a class Car with attributes make, model, and year. Add a method to display the car details.

class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def info(self):
        print(f"Linn bought a new {self.make},{self.model},{self.year}")

# Create a class BankAccount with methods to deposit and withdraw money, and check balance.

class  BankAccount:
    def __init__(self):
        self.balance=0
    def deposit(self,amount):
        if amount<0:
            print("you cant deposit less than zero")
        else:

            self.balance +=amount
    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficient balance")
        else:
            self.balance -= amount
    def get_balance(self):
        return self.balance

#  Write a class Rectangle with methods to calculate area and perimeter.

class Rectangle:
    def __init__(self,height,width):
        self.height=height
        self.width=width
    def Area(self):
        return self.height * self.width
    def perimeter(self):
        return (self.height + self.width)*2

# Define a class Student with name and grades attributes. Add a method to calculate average grade.
class Student:
    def __init__(self,name,grades):
        self.name=name
        self.grades=grades
    def Avaragegrade(self):
        return sum(self.grades)/ len(self.grades)
# Write a class Book with attributes for title, author, and pages. Add a method to check if the book is a long read (more than 300 pages).

class Book:
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
    def longRead(self):
        if self.pages >300:
            print("It is a long read")

# Create a class Employee with name, position, and salary. Add a method to give a raise by a percentage.
class Employee:
    def __init__(self,name,position,salary):
        self.name=name
        self.position=position
        self.salary=salary
    def give_raise(self,percentage):
        self.salary +=self.salary * (percentage/100)

# Define a class Circle with an attribute radius and methods to calculate area and circumference.
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.142 * (self.radius)**2
    def circumference(self):

        return 3.412* 2*(self.radius)
# . Create a class Temperature that converts Celsius to Fahrenheit.

class Temperature:
    def __init__(self,celcius):
        self.celcius=celcius
    def to_Fahrenheit(self):
        return (self.celcius *0.45) + 32
#  Write a class Light with a method to turn on and off (print “Light On” or “Light Off”).
class Light:
    def __init__(self):
        self.is_on=False
    def  turn_on(self):
        print("light is on")
    def  turn_off(self):
        print("Light is off")
# Define a class Counter with a method to increment and return the current count. 
class Counter:
    def __init__(self):
        self.count=0
    def increment(self):
       self.count +=1
       return self.count

# Q11. Create a class Car with a class variable wheels set to 4. Add a method to display wheels.

class Car:
    wheel=4
    def display_wheel(self):
        print(f"this car has {Car.wheel}")

# . Write a class Person with a private attribute __age. Add getter and setter methods for age.
class Person:
    def __init__(self,age):
        self._age=age
    def getter_age(self):
        return self._age
    def setter_age(self,age):
        if age>0:
            self._age=age
        else:
            print("invalid age")
# Q13. Implement a class Student with a class method to change the school name (a class attribute).
class Student:

    school = "ABC High School"


    def change_school(cls, new_school):
        cls.school = new_school
# Write a class Calculator with static methods for addition and multiplication.
class Calculator:
    
    def addition(a,b):
        return a + b
    def multiplication(a,b):
        return a*b


        
    



        
    

    
    


        



