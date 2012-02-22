import unittest

class GameOfLifeTests(unittest.TestCase):
	
	def testCanSpecifyMaximumIterationsForGame(self):
		game = Game(100)
		self.assertEqual(100, game.maximum_iterations)

	def testCanAddPoint(self):
		game = Game(100)
		game += (1, 1)
		self.assertTrue((1, 1) in game)
	
	def testCanFindNeighboursOfACell(self):
		game = Game(100)
		game += (1,1)
		game += (1,2)
		game += (2,1)
		game += (2,2)
		cell_neighbours = game.getCellNeighbours(1,1)
		self.assertTrue((1,2) in cell_neighbours and (2,1) in cell_neighbours and (2,2) in cell_neighbours)

	def testCountLiveNeighbours(self):
		game = Game(100)
		game += (1,1)
		game += (1,2)
		game += (2,1)
		game += (2,2)
		self.assertEqual(3, game.countLiveNeighbours(1,1))
	
	def testAliveCellWithOneAliveNeighbourWillDie(self):
		game = Game(100)
		game += (1,1)
		game += (1,2)
		game.evolve()
		self.assertFalse((1,1) in game)

class Game(object):
	def __init__(self, max_itter):
		self.maximum_iterations = max_itter
		self.points = []
	
	def __add__(self, new_point):
		self.points.append(new_point)
		return self

	def __sub__(self, point):
		self.points = list(i for i in self.points if i != point)
		return self
	
	def __contains__(self, point):
		return point in self.points

	def getCellNeighbours(self, *point):
		return list(i for i in self._getCellNeighbours(*point) if i != point)

	def _getCellNeighbours(self, *point):
		if len(point) == 1:
			for i in (-1, 0, 1):
				yield point[0]+i
		else:
			for n in self._getCellNeighbours(*point[1:]):
				for i in (-1, 0, 1):
					yield (point[0]+i, n)

	def countLiveNeighbours(self, *point):
		return sum(1 for neighbour in self.getCellNeighbours(*point) if neighbour in self.points)

	def evolve(self):
		for point in self.points:
			if (self.countLiveNeighbours(*point) not in (2, 3)):
				self -= point

	
if __name__ == '__main__':
	unittest.main()
