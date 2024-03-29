'''
Implement a clear() method for the FavoritesList class that returns the list
to empty.

Implement a reset_counts( ) method for the FavoritesList class that resets
all elements access counts to zero (while leaving the order of the list
unchanged).
'''
from positional_list import PositionalList

class FavoritesList:
  """List of elements ordered from most frequently accessed to least."""

  #------------------------------ nested _Item class ------------------------------
  class _Item:
    __slots__ = '_value', '_count'             # streamline memory usage
    def __init__(self, e):
      self._value = e                          # the user's element
      self._count = 0                          # access count initially zero

  #------------------------------- nonpublic utilities -------------------------------
  def _find_position(self, e):
    """Search for element e and return its Position (or None if not found)."""
    walk = self._data.first()
    while walk is not None and walk.element()._value != e:
      walk = self._data.after(walk)
    return walk

  def _move_up(self, p):
    """Move item at Position p earlier in the list based on access count."""
    if p != self._data.first():                      # consider moving...
      cnt = p.element()._count
      walk = self._data.before(p)
      if cnt > walk.element()._count:                # must shift forward
        while (walk != self._data.first() and
               cnt > self._data.before(walk).element()._count):
          walk = self._data.before(walk)
        self._data.add_before(walk, self._data.delete(p))   # delete/reinsert
  
  #------------------------------- public methods -------------------------------
  def __init__(self):
    """Create an empty list of favorites."""
    self._data = PositionalList()                 # will be list of _Item instances

  def __len__(self):
    """Return number of entries on favorites list."""
    return len(self._data)

  def is_empty(self):
    """Return True if list is empty."""
    return len(self._data) == 0

  def access(self, e):
    """Access element e, thereby increasing its access count."""
    p = self._find_position(e)                    # try to locate existing element
    if p is None:
      p = self._data.add_last(self._Item(e))      # if new, place at end
    p.element()._count += 1                       # always increment count
    self._move_up(p)                              # consider moving forward

  def remove(self, e):
    """Remove element e from the list of favorites."""
    p = self._find_position(e)                    # try to locate existing element
    if p is not None:
      self._data.delete(p)                        # delete, if found 

  def top(self, k):
    """Generate sequence of top k elements in terms of access count."""
    if not 1 <= k <= len(self):
      raise ValueError('Illegal value for k')
    walk = self._data.first()
    for j in range(k):
      item = walk.element()                       # element of list is _Item
      yield item._value                           # report user's element
      walk = self._data.after(walk)

  def __repr__(self):
    """Create string representation of the favorites list."""
    return ', '.join('({0}:{1})'.format(i._value, i._count) for i in self._data)
  def clear(self):
      list1 = [i for i in self._data] 
      for j in list1:
          self.remove(j._value)
  def reset_counts(self):
      for i in self._data:
          i._count = 0
          
     

if __name__ == '__main__':
  fav = FavoritesList()
  fav.access(1)
  fav.access(2)
  fav.access(3)
  fav.access(5)
  fav.access(4)
  fav.access(4)
  print(fav.is_empty())
  print(fav)
  fav.reset_counts()
  print(fav)
  fav.clear()
  print(fav.is_empty())
  

  