# a = [1, 2, 3, 'shiva']
# b = sorted(a)
# print(a)
# print(b)

#copy list
# a = [1, 2, 3, 4, 5]
# a_copy = a
# # a_copy = list(a)
# # a_copy = a.copy()
# print(a)
# print(a_copy)
# a_copy.append(6)
# print(a)
# print(a_copy)

# Tuple unpacking:

# a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 9)
# print(a)
# i1, *i2, i3 = a
# print(i1)
# print(i3)
# print(i2)


# tuple is more efficient than list
# import timeit
# print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1))
# print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1))

#Dictionary
# mydict = {"name": "Shivani", "worksat": "ivy"}
# print(mydict)
# mydict["email"] = "shivani.l@gmail.com"
# print(mydict)
# mydict.popitem()
# mydict.pop("name")
# print(mydict)

# copy dictionary
# mydict = {"name": "Shivani", "worksat": "ivy"}
# print(mydict)
#
# mydict_copy = mydict
# # mydict_copy = mydict.copy()
# # mydict_copy = dict(mydict)
# print(mydict_copy)
# mydict_copy["email"] = "lsg@gmail.com"
# print(mydict)
# print(mydict_copy)

# updating 2 dictiories into 1
# dict1 = {"name": "xyz", "email": "xyz@gmail.com", "id": 10007371}
# dict2 = {"name": "Shivani", "email": "lsg@gmail.com", "city": "Hyd"}
# dict1.update(dict2)
# print(dict1)

# String: ordered, immutable, text representation
my_string = 'how are you doing'
my_list = my_string.split()
print(my_list)
new_string = ''.join(my_list)
print(new_string)
