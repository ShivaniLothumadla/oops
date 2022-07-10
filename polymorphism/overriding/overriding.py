# method name and signatures must be same
# inheritance is always required
# overriding is performed between base class and derived class.
# overriding is used in order to change the behaviour of the existing method
# Atleast 2 classes should be there for overriding.


class grandFather:
    def Transportation(self):
        print("Walk")


class grandFather1:
    def Transportation(self):
        print("watching tv")

class father(grandFather, grandFather1):
    def Transportation(self):
        print("cycle")


class child1:
    def Transportation(self):
        print("sleeping")

class child2:
    def Transportation(self):
        print("dancing")

class child3(child1, child2):
    def Transportation(self):
        print("hungry")

class son(father, child3):

    def __init__(self):
        super().Transportation()

    def Transportation(self):
        print("Bike")

obj = son()
obj.Transportation()


