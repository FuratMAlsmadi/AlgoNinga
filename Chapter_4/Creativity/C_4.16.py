'''
Write a short recursive Python function that takes a character string s and
outputs its reverse. For example, the reverse of pots&pans would be
snap&stop .
'''
def reverse(s,acc=""):
    if s == "":
        return acc
    else:
       return reverse(s[:-1],acc = acc + s[-1])
        
        
               
print(reverse("pots&pans"))