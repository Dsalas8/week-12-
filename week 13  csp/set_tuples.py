#sets and tuples examples:
# sets examples 
set1 ={1, 2, 3, 4, 5}
print(set1) #{1, 2, 3, 4, 5}
print(type(set1))# <class 'set'>
set1.add(6)
print(set1) #{1, 2, 3, 4, 5,}
set1.remove(2)
print(set1)

#sets drope duplicate items 
set2 = {"apple", "bannana", "cherry", "cherry"}
print(set2) #{"apple", "bannana", "cherry", "cherry"}

# tuples examples 
tuple1 = (1, 2, 3, 4, 5)
print(tuple1) # (1, 2, 3, 4, 5)
print(type(tuple1)) #<class 'tuple'>
#tuples are immutable, meaning they cannot be changed after creation
#this makes tuples useful for storing data that cannot be modified
social_secutiry_number = (12344,444445, 567890)
print(social_security_number) # (12344,444445, 567890)