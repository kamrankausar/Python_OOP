

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return("Name : {}\nAge: {}".format(self.name, self.age))


class teacher(person):
    def __init__(self, name, age, sub):
        person.__init__(self, name, age)
        self.sub = sub

    def __str__(self):
        return(person.__str__(self)+"\nSubject: {}".format(self.sub))
    
    
class student(person):
    def __init__(self, name, age):
        person.__init__(self, name, age)
        self.marks = []
        self.attendance = 0

    def stu_mark(self, mark):
        self.marks.append(mark)

    def stu_attendance(self):
        self.attendance += 1
    def __str__(self):
        return(person.__str__(self)+"\n Student Marks: {}\n Student Attendance: {}".format(self.marks,self.attendance))


print("\nFollowing are Student Details")
s1 = student('Kamran', 29)
s1.stu_mark(99)
s1.stu_mark(99)
s1.stu_mark(97)
s1.stu_attendance()
s1.stu_attendance()
s1.stu_attendance()
s1.stu_attendance()
print(s1)

print("\nFollowing are Teacher Details")
t1 = teacher('Pash', 37, "Maths")
print(t1)

print("\nFollowing are Person Details")
p1 = person('Linda', 34)
print(p1)



        
        
        
