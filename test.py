def palindrom(s):
    if len(s) <= 1:
        return True
    else:
        
        return ((s[0] == s[-1]) and palindrom(s[1:-1]))
        
        


print(palindrom("WOW"))