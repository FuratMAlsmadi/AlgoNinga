'''
Implement a function that counts the number of nodes in a circularly
linked list.
'''


class CircularList:
    class _Node:
        def __init__(self, data, next):
            self._data = data
            self._next = next

    def __init__(self):
        self._head = None

    def add(self, data):
        if self._head == None:
            self._head = self._Node(data, None)
            self._head._next = self._head
        else:
            if self._head._next == self._head:
                self._head._next = self._Node(data, self._head)
            else:
                temp = self._head
                while temp._next != self._head:
                    temp = temp._next
                temp._next = self._Node(data, self._head)

    def count(self):
        temp = self._head
        count = 1
        while temp._next != self._head:
            count += 1
            temp = temp._next
        return count


var = CircularList()
var.add(1)
var.add(2)
var.add(3)
print(var.count())
