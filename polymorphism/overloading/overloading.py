# implementing the same thing in different ways
# + operater is the best example of operator overloading
# Methods have same name and different signatures.
# inheritance may or may not required.
# overloading is performed with in the class.
# It is used in order to add more to the behaviour of the methods
# There is no need of more than one class.
# we can achieve method overloading with default arguments and keyword arguments in python.


# class A:
#
#     def show(self):
#         print("show method")
#
#     def show(self, a):
#         print(a)
#
#     def show(self, a, b):
#         c = a + b
#         print(c)
#     def show(self, d, e):
#         c = d + e
#         print(c)
#
# obj = A()
# # obj.show()
# # obj.show(10)
# obj.show(10, 20)
# obj.show('Hello ', 'Python')


class A:

    def show(self, a=None, b=None, *args):
        # c = a + b
        print(a, b)
        print(type(a), type(b))
        for i in args:
            a = a + i
obj = A()
obj.show()
obj.show(10)
obj.show(10, '20')
obj.show('hello', 'python', 'shivani', 'shravani')


# class A:
#     def add(self, datatype, *args):
#         global a
#         if datatype == 'int':
#             a = 0
#         if datatype == 'str':
#             a = ''
#         for x in args:
#             a = a + x
#         print(a)
# obj = A()
# obj.add('int', 5, 6, 6)
# obj.add('str', 'Hi ', 'Hello ', 'Namaste')


# class A:
#
#     def show(self, a=0, b=0):
#         c = a + b
#         print(c)
# obj = A()
# obj.show()
# obj.show(10)
# obj.show(10, 20)


# class A:
#     def add(self, *args):
#         a=0
#         # if datatype == 'int':
#         #     a = 0
#         # if datatype == 'str':
#         #     a = ''
#         for x in args:
#             a = a + x
#         print(a)
# obj = A()
# obj.add(5, 6, 6)
# obj.add('str', 'Hi ', 'Hello ', 'Namaste')

