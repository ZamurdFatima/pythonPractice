a=int(input("Enter number: "))

match a:
    case 1:
        print("Case is 1")
    case 2:
        print("Case is 2")
    case 5:
        print("Case is 5")
    case _:
        print("No match found")

# Problems
#...1
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()  # Blank line for better readability




