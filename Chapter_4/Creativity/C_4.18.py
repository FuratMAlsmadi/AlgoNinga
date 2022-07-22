'''
Use recursion to write a Python function for determining if a string s has
more vowels than consonants
'''
def if_more_vowels(S,l,acc =0):
    if S == "":
        if acc > l/2:
            return True
        else:
            return False
    else:
        if S[0] in ["a","e","o","i","u"]:
            acc += 1
        return if_more_vowels(S[1:],l,acc)
        
        
        
        
print(if_more_vowels("anaui",5))