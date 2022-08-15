'''
Give an algorithm for finding the second-to-last node in a singly linked
list in which the last node is indicated by a next reference of None.
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
            
            
            
            
linkedlist = SinglyList()
linkedlist.add(1)
linkedlist.add(2)
linkedlist.add(3)
print(linkedlist.second_to_last())