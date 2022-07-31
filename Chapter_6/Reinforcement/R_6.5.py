'''
Implement a function that reverses a list of elements by pushing them onto
a stack in one order, and writing them back to the list in reversed order.
'''


def reverse(S):
    stack = []
    for i in range(len(S)):
        stack.append(S.pop())
    for i in range(len(stack)):
        S.append(stack[i])
        stack[i] = None


S = [1, 2, 3, 4, 5]
reverse(S)
print(S)
