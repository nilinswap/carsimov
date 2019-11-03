"""
for all utility functions
"""
from typing import List, Optional


class Cord:
	"""
	A Cord represents co-ordinate in 2d board
	:param x: x co-ordiante
	:param y: y co-ordingate
	
	"""
	def __init__(self, x: Optional[int] = None, y : Optional[int] = None):
		self.x = x
		self.y = y
		
		
	
	
class Block:
	"""
		A Block represents a building in the map. It is rectuangular
		and is represented by two cords: left top and right bottom corners
		:param lt:
		:param rb:

	"""
	def __init__(self, lt: Optional[Cord] = None, rb : Optional[Cord] = None):
		self.lt = lt
		self.rb = rb
		

def get_random_map(map: List[Block] ,width: int, length: int, level: int) -> List:
	"""
	
	:param map: List of Blocks(Buildings)
	:param width: width of board
	:param height: length of board
	:param level: level to the depth of map
	:return: map itself
	"""
	if not level:
		return map
	if map == []:
	
	return []
