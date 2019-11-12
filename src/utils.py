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
	
	def __add__(self, other):
		return Cord(x = self.x + other.x, y = self.y + other.y)
		
	def car_valid(self, board):
		
		for block in board.map:
			if block.encloses(self):
				return False
		
		return True
	
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
	
	def encloses(self, cord):
		
		# if self.lt <= cord <= self.rb
		return self.lt.x <= cord.x and self.lt.y <= cord.y and cord.x <= self.rb.x and cord.y <= self.rb.y
		

class Map:
	"""
	
	:param block_list:
	"""
	current_choice = None
	def __init__(self, block_list: List[Block] = []):
		self.block_list = block_list
		
	
	def __str__(self):
		st = 'map: \n'
		st += "block_list_length: %d"% len(self.block_list)
		for b in self.block_list:
			st += str(b)
			
		return st
	
	def add(self, block):
		self.block_list.append(block)
		
	def is_empty(self):
		return len(self.block_list) == 0
	
	def blind_pick(self):
		current_choice = random.choice(self.block_list)
		return current_choice

class Board:
	"""
	:param map:
	:param carPos:
	"""
	def __init__(self, map: Map = Map(), carPos = Cord(0, 0)):
		self.map = map
		self.carPos = carPos
	
def get_random_map(map: Map ,width: int, length: int, level: int) -> Map:
	"""
	
	:param map: List of Blocks(Buildings)
	:param width: width of board
	:param height: length of board
	:param level: level to the depth of map
	:return: map itself
	"""
	print(map)
	if length < 3 or width < 3:
		print("length and width must be greater than 2")
		return None
	
	if not level:
		return map
	
	if map.is_empty():
		
		#initial cord
		lt = Cord(1, 1)
		rb = Cord(width-2, length - 2)
		parent_block = Block(lt, rb)
		map.add(parent_block)
		map = get_random_map(map = map, width =  width, length= length, level = level - 1)
		return map
	
	s_length = 0
	s_width = 0
	for i in range(MaxTries):
		slaughter_block = map.blind_pick()
		s_length = slaughter_block.rb.x - slaughter_block.lt.x + 1
		s_width = slaughter_block.rb.y - slaughter_block.lt.y + 1
		if s_length >= 5 or s_width >= 5:
			break
	if s_length < 5 or s_width < 5:
		return map
	cut_point_x = slaughter_block.lt.x + random.randint(2, s_length - 2)
	cut_point_y = slaughter_block.lt.y + random.randint(2, s_width - 2)
	print("slaughter_block", slaughter_block)
	
	child1_block = Block(Cord(cut_point_x+1, cut_point_y+1), slaughter_block.rb)
	map.add(child1_block)
	
	child2_block = Block(
		Cord(slaughter_block.lt.x, cut_point_y + 1, ),
		Cord(cut_point_x-1, slaughter_block.rb.y)
	)
	map.add(child2_block)
	
	child3_block = Block(
		Cord( cut_point_x + 1,slaughter_block.lt.y),
		Cord(slaughter_block.rb.x, cut_point_y - 1),
	)
	map.add(child3_block)
	
	
	
	slaughter_block.rb = Cord(cut_point_x - 1, cut_point_y - 1)
	map.add(child3_block)
	
	
	
	map = get_random_map(map = map, length = length, width = width, level= level-1)
	
	return map

def get_next_random_pos(board):
	"""
	
	:param board:
	:return:
	"""
	
	curr_pos = board.carPos
	
	lis_dir = [Cord(1, 1), Cord(1, -1), Cord(-1, 1), Cord(-1, -1)]
	new_pos = curr_pos
	for dir in lis_dir:
		new_pos = curr_pos + dir
		if new_pos.car_valid(board):
			break
			
	board.carPos = new_pos
	
	return new_pos
	
	
	
def test():
	map = get_random_map(
		map = Map(),
		length = 20,
		width = 20,
		level = 4
		
	)
	print(map)
if __name__ == '__main__':
	test()
	