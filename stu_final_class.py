class student_details:

    """This class i.e Student Details get the name and age of the student
    and keep track of the attandence and marks score by the student
    Following Methods
    1. __init__ = Initilize the name and age for each object with the
                  help of self(alias of the calling object),
                  which must be the first arguments of each methods
    2. attand = Keep track of the attandance. Increase the attandance when
                this method is call

    3. marks = Keep tracks of the marks of student. Initiall it is empty
               list and append as we call this method with mark

    4. avg_mark = Show the average mark of the student, when it call

    5. __str__ = Show details of the object, when call inside the print function

    6. __del__ = Delete the unused object, object as the argument of the del
                 method"""

    #__init__ Method
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.attandance = 0
        self.marks = []
        print("Welcome, {} to the school".format(self.name))

    #Keep track of the Attandance of the student
    def stu_attand(self):
        self.attandance += 1


    #Keep track of the marks of the student
    def stu_marks(self, mark):
        self.marks.append(mark)

    #Display the Average marks of the Student
    def avg_mark(self):
        return sum(self.marks) / len(self.marks)

    # Display the object details in the print function
    def __str__(self):
        return("Name: {}.\nAge: {}.\nAttandance: {}.\nMarks: {}".format(self.name,self.age, self.attandance, self.marks))

    # Delete the Object
    def __del__(self):
        print("Now the Object: {} is free from the Matrix".format(self.name))


s1 = student_details("Peter", 22)
s1.stu_marks(99)
s1.stu_attand()
s1.stu_attand()
s1.stu_marks(97)
s1.stu_marks(98)
print(s1)
print("Your average mark is {}".format(s1.avg_mark()))
del(s1)
    

                 
