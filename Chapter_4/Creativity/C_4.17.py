'''
Write a short recursive Python function that determines if a string s is a
palindrome, that is, it is equal to its reverse. For example, "racecar" and
"gohangasalamiimalasagnahog" are palindromes.
'''
def is_palindrome(s):
    if s == "":
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False
        
        
        
print(is_palindrome("racecar"))
print(is_palindrome("gohangasalamiimalasagnahog"))

        