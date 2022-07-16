'''
Describe a recursive function for computing the n th Harmonic number
'''
def harmonic_number(start,end,acc):
    if end == start:
        return acc
    else:
        return harmonic_number(start+1,end,(1/start)+acc)
        
        

print(harmonic_number(1,5,1/5))
