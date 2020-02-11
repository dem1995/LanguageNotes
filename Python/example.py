"""Example reference for Python for personal use.

A general example for Python for personal use. This isn't intended to be comprehensive; the only intent here is to provide a refresher should I ever need one.
Dawn McKnight, 11 Feb 2019
"""

#Standard library imports, then third-party imports, then local imports
import sys
from collections import namedtuple
import numpy as np

class ClassName:
	instance_variable = None
	def __init__(self, name):	#Self is automatically passed in when called on an instance of the class
		self.name = name		#Another instance variable; created at runtime
	def instance_method(self):
		pass
	def class_method():
		pass

if __name__ == "__main__":		#Runs when this program is called. Is not called when this is imported as a module.
	print("You've run example.py")
