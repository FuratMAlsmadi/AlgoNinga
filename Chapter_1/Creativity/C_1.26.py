"""
Write a short program that takes as input three integers, a, b, and c, from
the console and determines if they can be used in a correct arithmetic
formula (in the given order), like “a + b = c,” “a = b − c,” or “a ∗ b = c.”
"""

def can_be_used():
    a = int(input("a:"))
    b = int(input("b:"))
    c = int(input("c:"))
    result = []
    if a+b == c:
        result.append("a + b = c")
    if a == b-c:
        result.append("a = b - c")
    if a*b == c:
        result.append("a * b = c")
    return result



print(can_be_used())         
    
    
    
    
    