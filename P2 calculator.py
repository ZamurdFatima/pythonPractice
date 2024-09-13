from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self,master):
        master.title("Calculator")
        master.geometry('356x420+0+0')
        master.config(bg='gray')
        master.resizable(False,False)

        self.equation = StringVar()
        self.entry_value = ''
        Entry(width=17,bg='#ccddff',font=('Arial Bold',28),textvariable=self.equation).place(x=0,y=0)

        Button(width=11,height=4, text='(',relief='flat',bg='white', command=lambda:self.show('(')).place(x= 0,y=50)
        Button(width=11, height=4, text=')', relief='flat', bg='white', command=lambda: self.show(')')).place(x=90, y=50)
        Button(width=11, height=4, text='%', relief='flat', bg='white', command=lambda: self.show('%')).place(x=180, y=50)
        Button(width=11, height=4, text='1', relief='flat', bg='pink', command=lambda: self.show(1)).place(x=0, y=125)
        Button(width=11, height=4, text='2', relief='flat', bg='pink', command=lambda: self.show(2)).place(x=90, y=125)
        Button(width=11, height=4, text='3', relief='flat', bg='pink', command=lambda: self.show(3)).place(x=180, y=125)
        Button(width=11, height=4, text='4', relief='flat', bg='pink', command=lambda: self.show(4)).place(x=0, y=200)
        Button(width=11, height=4, text='5', relief='flat', bg='pink', command=lambda: self.show(5)).place(x=90, y=200)
        Button(width=11, height=4, text='6', relief='flat', bg='pink', command=lambda: self.show(6)).place(x=180, y=200)
        Button(width=11, height=4, text='7', relief='flat', bg='pink', command=lambda: self.show(7)).place(x=0, y=275)
        Button(width=11, height=4, text='8', relief='flat', bg='pink', command=lambda: self.show(8)).place(x=180, y=275)
        Button(width=11, height=4, text='9', relief='flat', bg='pink', command=lambda: self.show(9)).place(x=90, y=275)
        Button(width=11, height=4, text='0', relief='flat', bg='pink', command=lambda: self.show(0)).place(x=90, y=350)
        Button(width=11, height=4, text='.', relief='flat', bg='white', command=lambda: self.show('.')).place(x=180 ,y=350)
        Button(width=11, height=4, text='+', relief='flat', bg='white',command=lambda:self.show('+')).place(x=270 ,y=275)
        Button(width=11, height=4, text='-', relief='flat', bg='white', command=lambda: self.show('-')).place(x=270, y=200)
        Button(width=11, height=4, text='/', relief='flat', bg='white', command=lambda: self.show('/')).place(x=270, y=50)
        Button(width=11, height=4, text='x', relief='flat', bg='white', command=lambda: self.show('*')).place(x=270, y=125)
        Button(width=11, height=4, text='=', relief='flat', bg='lightblue', command= self.solve).place(x=270, y=350)
        Button(width=11, height=4, text='C', relief='flat', command=self.clear).place(x=0, y=350)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        result = eval(self.entry_value)
        self.equation.set(result)



root = Tk()
calculator = Calculator(root)
root.mainloop()


# '''
# Calculator
# -------------------------------------------------------------
# '''
#
#
# import os
#
#
# def addition():
#    os.system('cls' if os.name == 'nt' else 'clear')
#    print('Addition')
#
#    continue_calc = 'y'
#
#    num_1 = float(input('Enter a number: '))
#    num_2 = float(input('Enter another number: '))
#    ans = num_1 + num_2
#    values_entered = 2
#    print(f'Current result: {ans}')
#
#    while continue_calc.lower() == 'y':
#        continue_calc = (input('Enter more (y/n): '))
#        while continue_calc.lower() not in ['y', 'n']:
#            print('Please enter \'y\' or \'n\'')
#            continue_calc = (input('Enter more (y/n): '))
#
#        if continue_calc.lower() == 'n':
#            break
#        num = float(input('Enter another number: '))
#        ans += num
#        print(f'Current result: {ans}')
#        values_entered += 1
#    return [ans, values_entered]
#
#
# def subtraction():
#    os.system('cls' if os.name == 'nt' else 'clear')
#    print('Subtraction')
#
#    continue_calc = 'y'
#
#    num_1 = float(input('Enter a number: '))
#    num_2 = float(input('Enter another number: '))
#    ans = num_1 - num_2
#    values_entered = 2
#    print(f'Current result: {ans}')
#
#    while continue_calc.lower() == 'y':
#        continue_calc = (input('Enter more (y/n): '))
#        while continue_calc.lower() not in ['y', 'n']:
#            print('Please enter \'y\' or \'n\'')
#            continue_calc = (input('Enter more (y/n): '))
#
#        if continue_calc.lower() == 'n':
#            break
#        num = float(input('Enter another number: '))
#        ans -= num
#        print(f'Current result: {ans}')
#        values_entered += 1
#    return [ans, values_entered]
#
#
# def multiplication():
#    os.system('cls' if os.name == 'nt' else 'clear')
#    print('Multiplication')
#
#    continue_calc = 'y'
#
#    num_1 = float(input('Enter a number: '))
#    num_2 = float(input('Enter another number: '))
#    ans = num_1 * num_2
#    values_entered = 2
#    print(f'Current result: {ans}')
#
#    while continue_calc.lower() == 'y':
#        continue_calc = (input('Enter more (y/n): '))
#        while continue_calc.lower() not in ['y', 'n']:
#            print('Please enter \'y\' or \'n\'')
#            continue_calc = (input('Enter more (y/n): '))
#
#        if continue_calc.lower() == 'n':
#            break
#        num = float(input('Enter another number: '))
#        ans *= num
#        print(f'Current result: {ans}')
#        values_entered += 1
#    return [ans, values_entered]
#
#
# def division():
#    os.system('cls' if os.name == 'nt' else 'clear')
#    print('Division')
#
#    continue_calc = 'y'
#
#    num_1 = float(input('Enter a number: '))
#    num_2 = float(input('Enter another number: '))
#    while num_2 == 0.0:
#        print('Please enter a second number > 0')
#        num_2 = float(input('Enter another number: '))
#
#    ans = num_1 / num_2
#    values_entered = 2
#    print(f'Current result: {ans}')
#
#    while continue_calc.lower() == 'y':
#        continue_calc = (input('Enter more (y/n): '))
#        while continue_calc.lower() not in ['y', 'n']:
#            print('Please enter \'y\' or \'n\'')
#            continue_calc = (input('Enter more (y/n): '))
#
#        if continue_calc.lower() == 'n':
#            break
#        num = float(input('Enter another number: '))
#        while num == 0.0:
#            print('Please enter a number > 0')
#            num = float(input('Enter another number: '))
#        ans /= num
#        print(f'Current result: {ans}')
#        values_entered += 1
#    return [ans, values_entered]
#
#
# def calculator():
#    quit = False
#    while not quit:
#        results = []
#        print('Simple Calculator in Python!')
#        print('Enter \'a\' for addition')
#        print('Enter \'s\' for substraction')
#        print('Enter \'m\' for multiplication')
#        print('Enter \'d\' for division')
#        print('Enter \'q\' to quit')
#
#        choice = input('Selection: ')
#
#        if choice == 'q':
#            quit = True
#            continue
#
#        if choice == 'a':
#            results = addition()
#            print('Ans = ', results[0], ' total inputs: ', results[1])
#        elif choice == 's':
#            results = subtraction()
#            print('Ans = ', results[0], ' total inputs: ', results[1])
#        elif choice == 'm':
#            results = multiplication()
#            print('Ans = ', results[0], ' total inputs: ', results[1])
#        elif choice == 'd':
#            results = division()
#            print('Ans = ', results[0], ' total inputs: ', results[1])
#        else:
#            print('Sorry, invalid character')
#
#
# if __name__ == '__main__':
#    calculator()