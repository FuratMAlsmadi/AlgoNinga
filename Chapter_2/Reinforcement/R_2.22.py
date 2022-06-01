"""
The collections.Sequence abstract base class does not provide support for
comparing two sequences to each other. Modify our Sequence class from
Code Fragment 2.14 to include a deﬁnition for the eq method, so
that expression seq1 == seq2 will return True precisely when the two
sequences are element by element equivalent.

In similar spirit to the previous problem, augment the Sequence class with
method lt , to support lexicographic comparison seq1 < seq2.
"""
from abc import ABCMeta, abstractmethod

class Sequence(metaclass=ABCMeta):
	"""Our own version of collections.Sequence abstract base class"""

	@abstractmethod
	def __len__(self):
		"""return the length of the sequence"""

	@abstractmethod
	def __getitem__(self,j):
		"""Return the element at index j of the sequence"""

	def __contains__(self, val):
		for j in range(len(self)):
			if self[j] == val:
				return True
		return False

	def __eq__(self, other):
		"""checks if two sequences are equivalent"""
		if len(self) != len(other):
			return False
		for j in range(len(self)):
				if self[j] == other[j]:
					pass
				else:
					return False
		return True

	def __lt__(self, other):
		"""Checks if one sequence is lexigraphically less than the other sequence"""
		for j in range(len(self)):
			if self[j] > other[j]:
				return False
		return True

	def index(self, val):
		"""Return leftmost index at which val is found (or raise ValueError)"""
		for j in range(len(self)):
			if self[j] == val:
				return j
		raise ValueError('value not in sequence')

	def count(self, val):
		"""Return the number of elements equal to given value"""
		k = 0
		for j in range(len(self)):
			if self[j] == val:
				k += 1
		return k