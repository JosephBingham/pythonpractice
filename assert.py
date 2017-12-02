#!/usr/bin/python

class Base:
	def food(self):
		return 'foo'

class Derived(Base):
	def bar(self):
		return self.foo()


assert hasattr(Base, 'foo'), "you broke it"







