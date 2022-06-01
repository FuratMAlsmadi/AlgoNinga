"""Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution"""

def minmax(data):
    mn = data[0]
    mx = data[0]
    for i in range(len(data)):
        if data[i] <= mn:
            mn =  data[i]
        if data[i] >= mx:
            mx = data[i]
    return mn,mx


print(minmax([2,3,1,70])) #(1, 70)


    