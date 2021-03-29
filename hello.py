def calculator():
    num = input('enter the input to add, muliply, divide, reminder: ')
    a = int(input('first number \n'))
    b = int(input('second number \n'))
    if (num == 'add'):
        add(a,b)
    elif(num == 'multiply'):
        multiply(a,b)
    elif(num == 'divide'):
        divide(a,b)
    elif(num == 'reminder'):
        reminder(a,b)
    else:
        print('Enter the suitable option')
    return 0

def add(a,b):
    return a + b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

def reminder(a,b):
    return  a % b
    
calculator()


