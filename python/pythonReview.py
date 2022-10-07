
#//*-------Q1 and Q4------------*//
#//* Write a Python program to create a Vehicle class with max_speed and mileage instance attributes
#//* Define a property that must have the same value for every class instance (object) --Define a class attribute ”color” with a default value white. I.e., Every Vehicle should be white.


class Vehicle:

    color = 'White'
    def __init__(self):
        self.max_speed = 60
        self.mileage = 50
        print(__class__.__name__) # Q6 Helped by Omkar Sir

hello = Vehicle()

#//*-------Q2------------*//
# //*Write a Program to create an empty valid class by name Students, with no properties

class Students:
    pass 


#//*-------Q3 ------------*//
# //* Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

class Bus(Vehicle):

    def show(self):
        print('max_speed',self.max_speed)
        print('milage',self.mileage)
        print('Color',Vehicle.color)

ko = Bus()
ko.show()



#//*-------Q5------------*//
#//*Write a Program in Python to implement a Stack Data Structure using Class and Objects, with push, pop, and traversal method.
#//* Stack is work last in last out
sample_list = [1,2,3,4]

class Stack():
    def __init__(self,list):
        self.list = list

    def push(self,p):
        self.list.append(p)
        return print( 'After Push : ',self.list)

    def pop(self):
        self.list.pop()
        return print('After Pop : ',self.list)

    def traverse(self):
        print('Traverse the Stack')
        for i in self.list:
            print(i)
        

# Example
obj1 = Stack(sample_list)
obj1.push(3)
obj1.push(10)
obj1.pop()


obj1.traverse()


#//*-------Q6 (Helped By Omkar sir)------------*//

class sample:
    def __init__(self):
        print('Name of the Class is : ',__class__.__name__)
        
class_Name = sample()


        
    

#//*-------Q7------------*//

'''Write an Example for Method Overloading and Method Overriding
-- Create New Class
-- Add Methods for Method Overloading
-- Add Methods for Method Overriding
-- Call parent class method inside the child class method.
'''


#//*-----Method Overriding------*//
'''Method overriding is done in class with Inheritance as the child method gets overrided to the parent method of same name and same parameter '''
#Example
#//* 1.-- Create New Class
#//*2.-- Add Methods for Method Overriding
class parent():
    def show(self):
        return print('Hello I am Parent Class')

class Child(parent):
    def show(self):
        return print('Hello I am Child Class')

print('\n Method Overriding')

obj1 = Child()
obj1.show() 

#Child method is overrided

#//*-----Method Overloading------*//
# //*-Python does not support method overloading. When there is two method of same name 
# but of different parameter in same block and we call the previous method it will 
# considered as method overloading.

class parent_1():
    
    def add(self,a,b):
        return print(a+b)
    
    def add(self,a,b,c):
        return print(a+b+c)

try:
    obj2 = parent_1()
    obj2.add(2,3)
except TypeError:
    print('\nit will give TypeError: add() missing 1 required positional argument: error')


#//*-Hence it will give TypeError: add() missing 1 required positional argument: error

obj3 = parent_1()
obj3.add(2,3,4)

#//*---The latest method will override the previous one.



#//*-----Calling Parent method------*//
class parent_2():
    def show(self):
        return print('Hello I am Parent Class')

class Child_2(parent_2):
    def show(self):

        return super().show()
        

obj4 = Child_2()
obj4.show() 


#//*-------Q8 (Polymorphisom)------------*//
'''when an interface(method) act different according to the given parameter is considered as polymorphism'''

#Example

x = 1
y = 10

x_1 = 'hello'
x_2 = 'world'

print(x+y)
#//*-For Integer the (+) operator act as a additin

print(x_1+x_2)
#//*-For String the (+) operator act as a Concatination



def intadd(*args):
    res = 0
    for i in args:
        if isinstance(i,int):
            res+=i

def stradd(*args):
    res = ''
    for i in args:
        if isinstance(i,str):
            res+=i
