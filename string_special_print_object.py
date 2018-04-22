class person:
    """ This class suit store the name and age of the person.
        __init__ method = initilized the object and
        __str__ method = print the object
        __del__ method = Delete the object, when it is not necessary """
    #Initilized the special Constructor Method
    def __init__(self, name, age):
        # Note self must be the first argument of the __init__ method
        # Self is just like the place holder for the object created
        # self is call each time when the an object is created
        self.name = name
        self.age = age
        print("Welcome, {}".format(self.name))

    #Initilize the Special Method called as string function which is useful to pring the object details
    def __str__(self):
        return("name: {}\n age: {}".format(self.name, self.age))

    #Initlize the Special method name as del, use to delete the unused object
    def __del__(self):
        print("Object name: {} is now deleted".format(self.name))


p1 = person("Peter", 29)
p2 = person("Vel", 35)
print(p1)
print(p2)
del(p1)
del(p2)




    

    
