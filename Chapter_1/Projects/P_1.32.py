"""
Write a Python program that can simulate a simple calculator, using the
console as the exclusive input and output device. That is, each input to the
calculator, be it a number, like 12.34 or 1034, or an operator, like + or =,
can be done on a separate line. After each such input, you should output
to the Python console what would be displayed on your calculator.
"""

def simple_calculator():
    storage = []
    calc = [] #to store the calculated value
    numop = input("Enter a number or operator:") #numop varaible to store the provided number or operator 
    while numop != "=":
        storage.append(numop)
    for i in storage:
        if i=="*" or "/":
            index = storage.index(i)
            if i == "*":
                one = storage[index-1]
                storage[index]=((storage[index-1]*storage[index+1]))
            else:
                storage[index]=((storage[index-1]//storage[index+1]))
        else:
            if i == "+":
                storage[index]=((storage[index-1]+storage[index+1]))
            else:
                storage[index]=((storage[index-1]-storage[index+1]))