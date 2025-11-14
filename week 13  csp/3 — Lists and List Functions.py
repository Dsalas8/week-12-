# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.
#creating lists are part of the collections family in python.
#collections are used to store multiple items in one variable 
#lists are ordered collections of items 
#lists are mutable, meaning you can change their content 
#lists are created using square brackets 
# Examples:
#Mr.Evins notes 
#instead of c reating seperate variabhles we can store them into a list.
#This makes our job easier, 
#when we need to manage multiple items. 
#performance task answer
my_list = [1,2,3,4,5]
print(my_list) # [1,2,3,4,5]
print(type(my_list)) # <class 'list'>
#Access elements:
print(my_list[0]) #1
print(my_list[1:4]) # [2,3,4]
print(my_list[0:])

# Modifiying lists 
#adding an item to the end of the list 
my_list.append(6)
print(my_list) #[1,2,3,4,5,6]
my_list.extend([10,11,12,13,14])
print(my_list)
#add 500 more numbers to the list 
my_list.extend(list(range(15,515)))
print(my_list)
my_list.extend(list(range(515,1115)))
print(my_list)

my_list = ['apple', 'banana', 'cherry']
print(my_list[0])         # apple
print(my_list[1:])        # ['banana', 'cherry']

my_list.append('grape')
print(my_list)

my_list.pop(1)
print(my_list)

numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)


# Practice Problems:

# Create a list with 5 of your favorite foods.

# Print the second and last item.

# Add a new item using .append().

# Remove the first item using .pop(0).

# Reverse your list using .reverse().

# Create a list of 3 lists (matrix), and access the middle element.