# n='zamurd is a gem'
# print(n)
# # string Slicing
# print(n[0:3])   #start from 0 & go all the wa till 2(3-1)
#
# print(n.capitalize())
# print(n.upper())
# print(n.isupper())
# print(n.isalnum())
# print(n.isnumeric())
# print(n.count('m'))
# print(n.endswith("rd"))
# print(n.find('g'))
# # '\\' or'\b'--> it stands for backslash
#
# # Practice set
# #...1
# a=input('Enter name:')
# print('Good Afternoon',a)
#
# #...2
# a=input('enter string: ')
# if "  " in a:
#     print("The string contains double spaces.")
# else:
#     print("The string does not contain double spaces.")

#...3
a=input('enter string: ')
if "  " in a:
    print(a.replace("  ",' '))