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
#my_list.append(6)
#print(my_list) #[1,2,3,4,5,6]
#my_list.extend([10,11,12,13,14])
#print(my_list)
#add 500 more numbers to the list 
#my_list.extend(list(range(15,515)))
#print(my_list)
#my_list.extend(list(range(515,1115)))
#print(my_list)

new_list = ['a','b','c']
print(new_list) #['a','b','c']
new_list.append('d')
print(new_list) #['a','b','c','d']
#removing an item from the list 
removed_item = new_list.pop()
#removes the last item by default 
print(removed_item) #d 
print(new_list) #['a','b','c','d']
remove_second_item = new_list.pop(1)
# removes the item at index 1 
print(remove_second_item) #b 
print(new_list) # ['a','c']

#sorting the list 
numbers = [4,2,5,1,3]
numbers.sort()
print(numbers) #[1,2,3,4,5]
#inerting an item at a specific position 
numbers.insert (2,10)
print(numbers) # [ 5, 4, 10, 3, 2, 1]
third_list = [7, 8, 9]
third_list [0] = 6 
print(third_list) # [6, 8, 9]
third_list[-1] = 10 
print(third_list) #[6, 8, 10]

import random
random_list = random.sample(range(1,1000), 100)
print(random_list)
# this will create a list of 10 unique random numbers 
# between 1 and 99 
print(random_list)
print(sorted(random_list))
sorted_list = sorted(random_list)
print(sorted_list)
#reverse the list 
#remove every 3rd item from the list

#summary of list functions 
# .append(item) - adds an item ot the end of the list 
# .pop(index) - removes and returns the item at the specified index 
# .sort() - sorts the list in ascending order 
# .reverse() - reverses the order of the list 



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