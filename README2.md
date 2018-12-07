Name: Tizeta Fantaye
Roles: Research,Outline,Write
Project: Cloud 9 Project
Type: Building A Calculator In python

Step 1.-Provide a detailed description of the app’s function(*Calculator)
Step 2.-Provide a user experience story to your audience(*Classmates)
Step 3.- Design the view layout of the calculator(*Provide the HTML,CSS,& Python Input[Numbers & Double],output[Amount],Click Event Listener[Add Button])
Example Input:  		number_1 = input('Enter your first number: ')
				number_2 = input('Enter your second number: ')

Example Output:			Enter your first number: 5
				Enter your second number: 7

		
Step 4.- Adding conditional statements.
With our calculator.py program, we want the user to be able to choose among the different operators.
	Example:    Please type in the math operation you would like to complete:
‘’’
+ for addition
- for subtraction
* for multiplication
/ for division
‘''
Step 5.Defining functions
Example
# Define our function
def calculate():
    operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

    number_1 = int(input('Please enter the first number: '))
    number_2 = int(input('Please enter the second number: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('You have not typed a valid operator, please run the program again.')

# Call calculate() outside of the function
calculate()



Step 6. -Improving the code
Example
-def welcome():
    print('''
Welcome to Calculator
''')
...
# Don’t forget to call the function
welcome()
calculate()
We limited ourselves to 4 operators, but you can add additional operators, as in:
operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
** for power
% for modulo
''')
___________________________________________________________________________
Source List:
1.https://www.digitalocean.com/community/tutorials/how-to-make-a-simple-calculator-program-in-python-3



