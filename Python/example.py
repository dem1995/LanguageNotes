"""Example reference for Python for personal use.

A general example for Python for personal use. This isn't intended to be comprehensive; the only intent here is to provide a refresher should I ever need one.
Dawn McKnight, 11 Feb 2019
"""

#Standard library imports, then third-party imports, then local imports
import sys
from collections import namedtuple
import numpy as np

class ClassName:
	class_variable = None
	#Self is automatically passed in when called on an instance of the class
	def __init__(self, name):
		#An instance variable; created at runtime
		self.name = name
	def instance_method(self):
		pass
	def class_method():
		pass
#Runs when this program is called. Is not called when this is imported as a module.
if __name__ == "__main__":
	print("You've run example.py")
