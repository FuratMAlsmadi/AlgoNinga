""" 
Write a Python program that inputs a document and then outputs a bar-
chart plot of the frequencies of each alphabet character that appears in
that document.
"""
import matplotlib.pyplot as plt 
class bar_chart():
    def __init__(self,file):
        self._file = file
    def plot(self):
        _letter_list = []
        with open(self._file) as f:
            for line in f :
                for L in line:
                    if L.isalpha():
                        _letter_list.append(L)
            _letter = list(set(_letter_list))
            _occurrence = []
            for l in _letter:
                count = _letter_list.count(l)
                _occurrence.append(count)
            plt.bar(_letter,_occurrence)
            plt.show()


draw = bar_chart("alphabet.txt")
draw.plot()
