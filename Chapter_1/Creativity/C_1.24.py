"""
Write a short Python function that counts the number of vowels in a given
character string.
"""
def vowels_count(word):
    word.lower()
    count = 0
    for i in word:
        if i in "aeiou":
            count += 1
    return count
    
    
    
    
print(vowels_count("Mani")) 
            
            