# -*- coding: utf-8 -*-
"""Untitled11.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19Xgchyd5LxvNNs9jra8ZJzLVrL70M3go
"""

# Slicing on a string
my_str ='PORTION'
print('characters 1 to 3 is' my_str[1:3])
print('characters 2 to end is' my_str[2:])
print('charcters 1 to -1 is' my_str[1:-1])

# ACCESS ELEMENTS IN LIST
a = [10, 20, 30 , 40, 50]

# Access first element
print(a[0])

# Access last element
print(a[-1])

# MODIFY ELEMENTS IN LIST
a = [10, 20, 30, 40, 50]

#Change the second element
a[1] = 25

print(a)

a =[10, 25, 30, 40, 50]

# DELETE ELEMENTS IN LIST

a = [10, 20, 30, 40, 50]
a.remove[30]
print(a)

# TUPLES AND LIST
# IN CASE OF LIST, WE USE SQUARE
# BRACKETS[] HERE WE USE ROUND BRACKETS()

a = [1, 'apple', 3.14, [5, 6]]
print(a)
print(type(a))

[1, 'apple', 3.14, [5, 6]]

t = (10, 20, 30, 40, 50)
print(t)
print(type(t))

(10, 20, 30)
<class 'tuple>'

# ADD ITEMS IN DICTIONARY
# BY USING THE ASSIGNMENT OPRATOR
# The assignment operator (=) sets a value to a dictionary key:

dictionary_name[key] = value

#The assignment operator adds a new key-value pair if the key does not exist.

my_dictionary = {
  "one": 1,
  "two": 2
}
my_dictionary["three"] = 3
# ADD ITEMS IN DICTIONARY
# BY USING THE ASSIGNMENT OPRATOR
# The assignment operator (=) sets a value to a dictionary key:

dictionary_name[key] = value

#The assignment operator adds a new key-value pair if the key does not exist.

my_dictionary = {
  "one": 1,
  "two": 2
}
my_dictionary["three"] = 3
print(my_dictionary)

#The code shows the updated dictionary contents after adding a new item.

#{'one': 1, 'two': 2, 'three': 3}

# MODIFY ITEMS IN DICTIONARY
# Updating the dictionary using the dict() constructor
# Assuming main_dict is defined elsewhere
# Example:
main_dict = {"a": 1, "b": 2}
updated_dict = dict(main_dict, c=3, d=4)

print(updated_dict)

# DELETE ITEMS IN DICTIONARY
test_dict = {"Arushi": 22, "Mani": 21, "Haritha": 21}

# using del to Delete element
del test_dict["Mani"]

print(test_dict)

#The dictionary before performing remove is :  {'Arushi': 22, 'Mani': 21, 'Haritha': 21}
#The dictionary after remove is :  {'Arushi': 22, 'Haritha': 21}

# MODIFY ITEMS IN DICTIONARY
# Updating the dictionary using the dict() constructor
updated_dict = dict(main_dict, c=3, d=4)

print(updated_dict)

# DELETE ITEMS IN DICTIONARY
#test_dict = {"Arushi": 22, "Mani": 21, "Haritha": 21}

# using del to Delete element
del test_dict["Mani"]

print(test_dict)

The dictionary before performing remove is :  {'Arushi': 22, 'Mani': 21, 'Haritha': 21}
The dictionary after remove is :  {'Arushi': 22, 'Haritha': 21}

# DICTIONARY KEYS IS IMMUTABLE....

d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d)
{1: 'Geeks', 2: 'For', 3: 'Geeks'}

# Creating a List
mylist = ["Jacob", "Harry", "Mark", "Anthony"]

# Displaying the List
print("List = ",mylist)

# Convert List to Tuple
res = tuple(mylist)
print("Tuple = ",res)