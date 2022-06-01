"""
In Section 2.3.5, we note that our version of the Range class has implicit 
support for iteration, due to its explicit support of both __len__
and __getitem__. The class also receives implicit support of the Boolean
test, “k in r” for Range r. This test is evaluated based on a forward iteration 
through the range, as evidenced by the relative quickness of the test
2 in Range(10000000) versus 9999999 in Range(10000000). Provide a
more efﬁcient implementation of the __contains__ method to determine
whether a particular value lies within a given range. The running time of
your method should be independent of the length of the range.
"""


class Range():
    def __init__(self,start,stop=None,step=1):
        if step == 0:
            raise ValueError("Step Can't Be Zero")
        if stop == None:
            stop , start = start, 0 
        self._length = max(0,(stop-start+step-1)//step)
        self._start = start
        self._step = step
        self._stop = stop
    def __len__(self):
        return self._length
    def __getitem__(self,k):
        if k< 0:
            k += len(self)
        if not 0<= k <self._length:
            raise IndexError("Index Out Of Range")
        return self._start + k*self._step
    def __contains__(self,item):
        if ( (item >= self._stop) or item< self._start):
            raise IndexError("Index Out Of Range")
        if (item+self._start)%self._step == 0:
            return True
        else:
            return False
    
    
    
    
# print(4 in Range(0,9,3)) #False
print(2 in Range(0,10000000,3))
print(9999999 in Range(10000000))
