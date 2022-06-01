"""
Write a Python program that repeatedly reads lines from standard input
until an EOFError is raised, and then outputs those lines in reverse order
(a user can indicate end of input by typing ctrl-D).
"""

def take_input_write_reverse():
    lines_list = []
    while True:
        try:
            line = input("Enter Your line: ")
            lines_list.append(line)
        except EOFError:
            lines_list.reverse()
            for i in lines_list:
                print(i)
            break
        
        

take_input_write_reverse()