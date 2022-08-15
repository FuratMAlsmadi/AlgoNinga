'''
escribe a good algorithm for concatenating two singly linked lists L and
M, given only references to the first node of each list, into a single list L
that contains all the nodes of L followed by all the nodes of M.
'''
class SinglyList:
    class _Node:
        def __init__(self,data,next):
            self._data = data 
            self._next = next
    def __init__(self):
        self._head = None 
    def add(self,data):
        if self._head == None:
            self._head = self._Node(data,None)
        else:
            oldhead = self._head
            self._head = self._Node(data,oldhead)
    def second_to_last(self):
        temp = self._head
        while temp != None:
            if temp._next._next == None:
                return temp._data
            else:
                temp = temp._next
            
    def concatenate(self,other):
        if isinstance(other,SinglyList):
            tail_one = self._head
            while tail_one._next != None:
                tail_one = tail_one._next
            tail_one._next = other._head
            
            
                
                
            
            
linkedlist = SinglyList()
linkedlist.add(1)
linkedlist.add(2)
linkedlist.add(3)
foo = SinglyList()
foo.add(4)
foo.add(5)
foo.add(6)
linkedlist.concatenate(foo)