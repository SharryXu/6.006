#!/usr/bin/env python3

from rc_2_array_seq import ArraySeq


def set_from_seq(seq):
	class SetFromSeq:
		def __init__(self) -> None:
			self.S: ArraySeq = seq()
		def __len__(self):
			return len(self.S)
		def __iter__(self):
			yield from self.S

		def build(self, x):
			self.S.build(x)

		def find(self, k):
			for x in self:
				if x.key == k:
					return x
			return None

		def insert(self, x):
			for i in range(len(self.S)):
				if self.S.get_at(i).key == x.key:
					self.S.set_at(i, x)
			self.S.insert_last(x)
			return True

		def delete(self, k):
			for i in range(len(self.S)):
				if self.S.get_at(i).key == k:
					return self.S.delete_at(i)

		def find_min(self):
			min = None
			for x in self:
				if min == None or x.key < min.key:
					min = x
			return min

		def find_max(self):
			max = None
			for x in self:
				if max == None or x.key > max.key:
					max = x
			return max

		def find_next(self, k):
			next = None
			for x in self:
				if x.key > k and (next == None or x.key < next.key):
					next = x
			return next

		def find_prev(self, k):
			prev = None
			for x in self:
				if x.key < k and (prev == None or x.key > prev.key):
					prev = x
			return prev

		def iter_ord(self):
			x = self.find_min()
			while x:
				yield x
				x = self.find_next(x.key)
	
	return SetFromSeq

