# def greetHello(name, ending):
#     print("Hello "+ name)
#     print("You are awesome")
#     print(ending)
# def letterGenerator(name, date):
#     st=f"Hi mam,\nThis is {name} and i'll not come to {date}"
#     print(st)
# def average(a, b):                      #returning values
#     return (a+b)/2
#
# print("Executing function...")
# greetHello("Zara", "Thank u")
# letterGenerator("Zara","23rd Octuber")
# print(average(2,3))
#
# # Practice
# #...1
# def greet(name="stranger"):
#     print(f"Heloo,{name}")
# greet("Alice")
#,,,2
# def great(num1 ,num2  ,num3):
#   largest= max(num1 ,num2 ,num3)
#   return largest
# num1=float(input("Enter number1: "))
# num2=float(input("Enter number2: "))
# num3=float(input("Enter number3: "))
# large= great(num1 ,num2 ,num3)
# print(large)
#...3
# def remove_and_strip_word(my_list, word_to_remove):
#   """Removes a given word from a list and strips the remaining words."""
#   new_list = [word.strip() for word in my_list if word.strip() != word_to_remove]
#   return new_list
# my_list = ["  apple  ", " banana ", " cherry ", " apple  "]
# word_to_remove = "apple"
# result = remove_and_strip_word(my_list, word_to_remove)
# print(result)
#...4
def print_inverted_triangle(n):
  for i in range(n, 0, -1):
    print("* " * i)
n = 5
print_inverted_triangle(n)
