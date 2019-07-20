class Student:
    #init = constructor ของ class นี้
    def __init__(self, fname, lname, gpa):
        self.fname = fname
        self.lname = lname
        self.gpa = gpa
    
    def printInfo(self):
        print("First name: " + self.fname)
        print("Last name: " + self.lname)
        print("GPA: " + str(self.gpa))

student1 = Student("Tharathep","Klinla-or",3.33)
print(student1.fname)
student1.printInfo()