"""
for all utility functions
"""
from typing import List, Optional
import random
random.seed(0)

MaxTries = 5

class Cord:
	"""
	A Cord represents co-ordinate in 2d board
	:param x: x co-ordiante
	:param y: y co-ordingate
	
	"""
	def __init__(self, x: Optional[int] = None, y : Optional[int] = None):
		self.x = x
		self.y = y
	
	def __str__(self):
		return "\n\t\tx: %d\n\t\ty: %d\n"%(self.x, self.y)
		
		
	
	
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
	
	def __str__(self):
		return "\n\tlt: %s\n\t\trb: %s\n" % (self.lt, self.rb)
		
def get_random_map(map: List[Block] ,width: int, length: int, level: int) -> List[Block]:
	"""
	
	:param map: List of Blocks(Buildings)
	:param width: width of board
	:param height: length of board
	:param level: level to the depth of map
	:return: map itself
	"""
	print("map")
	for b in map:
		print(b)
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
		map = get_random_map(map = map, width =  width, length= length, level = level - 1)
		return map
	
	s_length = 0
	s_width = 0
	for i in range(MaxTries):
		slaughter_block = random.choice(map)
		s_length = slaughter_block.rb.x - slaughter_block.lt.x + 1
		s_width = slaughter_block.rb.y - slaughter_block.lt.y + 1
		if s_length >= 5 or s_width >= 5:
			break
	if s_length < 5 or s_width < 5:
		return map
	cut_point_x = slaughter_block.lt.x + random.randint(2, s_length - 2)
	cut_point_y = slaughter_block.lt.y + random.randint(2, s_width - 2)
	
	child_block = Block(Cord(cut_point_x+1, cut_point_y+1), slaughter_block.rb)
	print("slaughter_block", slaughter_block)
	slaughter_block.rb = Cord(cut_point_x, cut_point_y)
	
	map.append(child_block)
	
	map = get_random_map(map = map, length = length, width = width, level= level-1)
	
	
	
	
	
	return map

def test():
	map = get_random_map(
		map = [],
		length = 20,
		width = 20,
		level = 4
		
	)
	print(len(map))

if __name__ == '__main__':
	test()
	