# Inheritance and the Overload Concept

class person:

    """In this Example I am going to show the Inheritance concept.
       person is the base class and teacher, student are classes
       which inherit the basic properties(person) from the base class."""
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Name is: {} and age is {}".format(self.name, self.age))


# Teacher Class, To inherit the Base class i.e person, we have to pass person
# as argument to the teacher class 
class teacher(person):
    def print(self, name, age):
        person.__init__(self,name,age)

# Student Class, To inherit the Base class i.e person, we have to pass person
# as argument to the student class 
class student(person):
    #To print the Name and Age of the Student
    def print(self, name, age):
        #To Call the print class of the Base class i.e person.
        # We have to call like this
        # base_class_name.(dot)method_name(arguments)
        # Since it is the constructor class so we are calling the
        # __init__ class
        person.__init__(self, name, age)


        

        
       
    
    
