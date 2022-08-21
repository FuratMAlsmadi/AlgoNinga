'''
Describe a non recursive method for finding, by link hopping, the middle
node of a doubly linked list with header and trailer sentinels. In the case
of an even number of nodes, report the node slightly left of center as the
“middle.” (Note: This method must only use link hopping; it cannot use a
counter.) What is the running time of this method?
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
        successor._prev = predecessor
        self._size -= 1
        element = node._element                             # record deleted element
        node._prev = node._next = node._element = None      # deprecate node
        return element                                      # return deleted element

    def find_middle(self, start, end):
        if (start == end) or (start == end._prev):
            return start._element
        else:
            return self.find_middle(start._next, end._prev)


var = _DoublyLinkedBase()
var1 = var._insert_between(1, var._header, var._trailer)
var2 = var._insert_between(2, var1, var._trailer)
var3 = var._insert_between(3, var2, var._trailer)
var4 = var._insert_between(4, var3, var._trailer)
var5 = var._insert_between(5, var4, var._trailer)
print(var.find_middle(var._header, var._trailer))
