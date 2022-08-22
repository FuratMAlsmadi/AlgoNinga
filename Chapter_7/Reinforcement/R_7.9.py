'''
Give a fast algorithm for concatenating two doubly linked lists L and M,
with header and trailer sentinel nodes, into a single list L.
'''


class _DoublyLinkedBase:
    """A base class providing a doubly linked list representation."""

    # -------------------------- nested _Node class --------------------------
    # nested _Node class
    class _Node:
        """Lightweight, nonpublic class for storing a doubly linked node."""
        __slots__ = '_element', '_prev', '_next'            # streamline memory

        def __init__(self, element, prev, next):            # initialize node's fields
            self._element = element                           # user's element
            self._prev = prev                                 # previous node reference
            self._next = next                                 # next node reference

    # -------------------------- list constructor --------------------------

    def __init__(self):
        """Create an empty list."""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer                  # trailer is after header
        self._trailer._prev = self._header                  # header is before trailer
        self._size = 0                                      # number of elements

    # -------------------------- public accessors --------------------------

    def __len__(self):
        """Return the number of elements in the list."""
        return self._size

    def is_empty(self):
        """Return True if list is empty."""
        return self._size == 0

    # -------------------------- nonpublic utilities --------------------------

    def _insert_between(self, e, predecessor, successor):
        """Add element e between two existing nodes and return new node."""
        newest = self._Node(
            e, predecessor, successor)      # linked to neighbors
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        """Delete nonsentinel node from the list and return its element."""
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predeself._header._nextcessor
        self._size -= 1
        element = node._element                             # record deleted element
        node._prev = node._next = node._element = None      # deprecate node
        return element                                      # return deleted element

    def find_middle(self, start, end):
        if (start == end) or (start == end._prev):
            return start._element
        else:
            return self.find_middle(start._next, end._prev)

    def concatenate(self, other):
        if isinstance(other, _DoublyLinkedBase):
            self._trailer._prev._next = other._header._next
            other._header._next._prev = self._trailer._prev
            self._trailer._next = other._trailer._next
            self._trailer._prev = other._trailer._prev
            other._header._next = None
            other._header._prev = None
            self._size = self.__len__() + other.__len__()
        else:
            return TypeError


var = _DoublyLinkedBase()
var1 = var._insert_between(1, var._header, var._trailer)
var2 = var._insert_between(2, var1, var._trailer)
var3 = var._insert_between(3, var2, var._trailer)
var4 = var._insert_between(4, var3, var._trailer)
var5 = var._insert_between(5, var4, var._trailer)
print(var.find_middle(var._header, var._trailer))

foo = _DoublyLinkedBase()
foo1 = foo._insert_between(6, foo._header, foo._trailer)
foo2 = foo._insert_between(7, foo1, foo._trailer)
foo3 = foo._insert_between(8, foo2, foo._trailer)
foo4 = foo._insert_between(9, foo3, foo._trailer)
foo5 = foo._insert_between(10, foo4, foo._trailer)

var.concatenate(foo)
print(var.find_middle(var._header, var._trailer))

print(len(var))
