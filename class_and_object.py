rno = 1
class student:
    rno = 123                  # instance variable: presents within class but outside the method
    name = "shivani"
    branch = "cse"

    def __init__(self, cn):     # no need of calling this method explicitly using object.
        college_name = cn
        print("college name is: ", college_name)

    def read(self):
        rno = 345                      # local variable: presents with in the method and with in same class
        print("rollno=", rno)
        print("Instance variable=", self.rno)
        print("reading")

    def write(self):
        global rno
        print("writing")
        rno = 1000
        print("rollno=", rno)

abc = student('xyz')
print("rno=", student.rno)
print("rno=", abc.rno)
print("name=", abc.name)
print("branch=", abc.branch)
abc.read()
abc.write()
print(rno)
print(abc.rno)

"""
instance variable can be accessable by using the class name and the object from outside of the class.
instance variable can access by using self with in the function of a same class.
in my point of view instance variable is a class variable in python.
"""