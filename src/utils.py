"""
for all utility functions
"""
from typing import List, Optional
import random

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
	
		

def get_random_map(map: List[Block] ,width: int, length: int, level: int) -> List[Block]:
	"""
	
	:param map: List of Blocks(Buildings)
	:param width: width of board
	:param height: length of board
	:param level: level to the depth of map
	:return: map itself
	"""
	if length < 3 or width < 3:
		print("length and width must be greater than 2")
		return None
	
	if not level:
		return map
	
	if map == []:
		
		#initial cord
		lt = Cord(1,1)
		rb = Cord(width-2, length - 2)
		parent_block = Block(lt, rb)
		map.append(parent_block)
		map = get_random_map(map, width, length, level - 1)
		return map
	
	
	
	
	return map
