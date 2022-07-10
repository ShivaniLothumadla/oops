"""
By using inheritance we can create one object to the derived class and access the all methods from base classes  instead of creating object to every class.
we can reduce the code
reusability can achieve
"""


class grandparent:
    def disp(self):
        print("GrandParent class")


class parent(grandparent):
    def display(self):
        print("Parent class")


class child(parent):
    def show(self):
        print("child class")


class somex():
    def fun(self):
        print("Somex class")


class grandchild(child, somex):
    def gshow(self):
        print("grandchild class")

    def fun(self):
        print("grandchild class")


c = child()
c.display()
c.show()

gc = grandchild()
gc.disp()
gc.fun()
gc.gshow()
