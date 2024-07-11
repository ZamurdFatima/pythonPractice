# List
a=[2,4,62,42,1,3,'MA']               #list is mutable and represent by []
print(type(a))

a.remove('MA')
print(a)
print(a.count(3))
a.sort()
print(a)
a.reverse()
print(a)
a.pop(3)                  #if there is only pop it'll del last value
print(a)
a.append(6)
print(a)
a.extend([9,8,7])
print(a)
print(a.index(4))
a[0]='MA'
print(a)
a.insert(3,1)
print(a)
a.clear()
print(a)

# Tuples
n=[1,]                                   #these can be empty and if there is onl one element it'll need comma
b=(3,3,5,2,88)                           # Tuples are immutable and represent by ()
print(b.count(2))
print(b.index(2))
# a.__add__(6,55)
# print(b)

# Sets
c={5,1,7}                               # No repetition here
d={1,24,1,2}
e=set()                                  # method to make empt set

# print(c.pop())
# c.add(3)
print(c.union(d))
print(c.intersection( d))

print(c)
print(d)
print(e,type(e))

# Practice set
#...1
fruits = []                              # Initialize an empty list to store the fruits
for i in range(7):                       # Loop to get seven fruits from the user
    fruit = input(f"Enter fruit {i + 1}: ")
    fruits.append(fruit)
print("The list of fruits entered is:", fruits)     # Print the list of fruits
#...2

