"""
Write a short Python function that takes a string s, representing a sentence,
and returns a copy of the string with all punctuation removed. For exam-
ple, if given the string "Let's try, Mike.", this function would return
"Lets try Mike".
"""

def punctuation_remove(sentence):
    new_sentence = []
    for i in sentence:
        if i in "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~":
            continue
        new_sentence.append(i)
    return "".join([i for i in new_sentence])


print((punctuation_remove("Let's try, Mike.")))
