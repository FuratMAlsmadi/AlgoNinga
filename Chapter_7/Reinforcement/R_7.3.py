'''
Describe a recursive algorithm that counts the number of nodes in a singly
linked list.
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

    def count(self):
        temp = self._head
        num = 0
        def counter(head):
            if head._next  == None:
                return 1
            else:
                return 1 + counter(head._next)
        return counter(temp)
        
            
            
                
                
            
            
linkedlist = SinglyList()
linkedlist.add(1)
linkedlist.add(2)
linkedlist.add(3)
foo = SinglyList()
foo.add(4)
foo.add(5)
foo.add(6)
linkedlist.concatenate(foo)
print(linkedlist.count())