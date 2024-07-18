try:
    a=int(input("Enter your number: "))
    print(a+3)
except Exception as ex:
    print("Some error occured",ex)