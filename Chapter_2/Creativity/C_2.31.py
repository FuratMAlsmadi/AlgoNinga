"""Write a Python class that extends the Progression class so that each value
in the progression is the absolute value of the difference between the 
previous two values. You should include a constructor that accepts a pair of
numbers as the first two values, using 2 and 200 as the defaults."""

"""
Write a Python class that extends the Progression class so that each value
in the progression is the square root of the previous value. (Note that
you can no longer represent each value with an integer.) Your constructor 
should accept an optional parameter specifying the start value, using
65, 536 as a default.
"""

class Progression:
	"""Iterator producing a generic progression.
	Default iterator  produces the whole numbers 0, 1, 2..."""

	def __init__(self, start=0):
		"""Initialize current to the first value of the progression"""
		self._current = start

	def _advance(self):
		"""Update self._current to a new val.
		This should be overriden by a subclass to customize progression.
		By convention, if current is set to None, this designates the
		end of a finite progression"""

		self._current += 1

	def __next__(self):
		"""Return the next element, or else raise StopIteration error."""
		if self._current is None:			#our convention to end a progression
			raise StopIteration()
		else:
			answer = self._current		#record current value to return
			self._advance()				#advance to prepare for next time
			return answer				#return the answer

	def __iter__(self):
		"""By convention, an iterator must return itself as an iterator"""
		return self

	def print_progression(self, n):
		"""print next n values of the progression"""
		print(" ".join(str(next(self)) for i in range(n)))
  



class AbsValueDiff(Progression):
    def __init__(self, start=2,stop = 200):
        super().__init__(start)
        self._prev = abs(stop - start)

    def _advance(self):
        self._prev , self._current = self._current , abs(self._current - self._prev)



class SqrRt(Progression):
	def __init__(self, start = 65536):
		super().__init__(start)

	def _advance(self):
		self._current = self._current**(0.5)

