"""
The SequenceIterator class of Section 2.3.4 provides what is known as a
forward iterator. Implement a class named ReversedSequenceIterator that
serves as a reverse iterator for any Python sequence type. The first call to
next should return the last element of the sequence, the second call to next
should return the second-to-last element, and so forth.
"""
class SequenceIterator():
    def __init__(self,sequence):
        self._seq = sequence
        self.k = 0
    def __next__(self):
        self.k -= 1
        if -(self.k) <= len(self._seq):
            return self._seq[self.k]
        else:
            raise StopIteration()
    def __iter__(self):
        return self
        

for i in SequenceIterator([1,2,3,4,5]):
    print(i)
         
         
