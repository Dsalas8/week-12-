list1 = [1, 2, 3]
list2 = [4, 5, 6]
nested_list = [list1, list2]
print(nested_list) #output: is the lists
print(nested_list[1][2])

fruits = ["apple", "orange", "banana", "coconut"] 
veggies = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "Turkey"]
groceries = [fruits, veggies, meats]
print(groceries[1][2])  #potatoes
print(groceries[0][2]) #Banana
for collection in groceries :  
    for food in collection:
        print(food,end=" ")             #" "makes the items inside be spaced out, and not in 3 seperate lists, or row.
    print()

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))
for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()


# Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.

# List comprehensions provide a concise way to create lists.

# Examples:

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])    # 6
print(matrix[0][2]) #3
print(matrix[0][0]) #1 

# List comprehension
example_list = [row[0]for row in matrix]
#for row in matrix
#   print(row[0])
print(example_list)
    #[1,4,7]

first_col = [row[0] for row in matrix]
print(first_col)       # [1, 4, 7]



# Practice Problems:

# Build a matrix variable containing 3 lists of 3 numbers each.
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
# Print the first list.
print(matrix)
# Print the second item from the third list.
print(matrix[2][1])
# Use a list comprehension to extract the last item from each sub-list.
comprehension_list = [row[-1]for row in matrix]
print(comprehension_list)
# Challenge: Create a new list containing squares of numbers from 1–10 using a comprehension.
squared_numbers = [x**2 for x in range(1,11)]
#for x in range (1,11): 
#    squared =x**2
#    print(squared)
print(squared_numbers)