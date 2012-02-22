import unittest
import random

class Grid:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.cells = []
  
  def initialiseRandomly(self):
    for rowIndex in range(self.width):
      self.cells.append([])
      for columnIndex in range(self.height):
        if random.randint(1,4) == 1:
          cell = Cell(True)
        else:
          cell = Cell(False)
        self.cells[rowIndex].append(cell)

  def initialiseWithCells(self, someCells):
    for rowIndex in range(self.width):
      self.cells.append([])
      for columnIndex in range(self.height):
        self.cells[rowIndex].append(Cell(someCells[rowIndex][columnIndex].alive))
  
  def isCellInitialised(self, rowIndex, columnIndex):
    return self.cells[rowIndex][columnIndex] != None
  
  def isCellAlive(self, rowIndex, columnIndex):
    return self.cells[rowIndex][columnIndex].alive == True

class Cell:
  
  def __init__(self, alive):
    self.alive = alive

class GridTests(unittest.TestCase):

  def testCanRunTestingFramework(self):
    self.assertTrue(True)

  def testCanCreateGridOfSpecifiedWidth(self):
    width = 20
    grid = Grid(width, 30)
    self.assertEqual(grid.width, width)

  def testCanCreateGridOfSpecifiedHeight(self):
    height = 20
    grid = Grid(30, height)
    self.assertEqual(grid.height, height)

  def testCanInitialiseGrid(self):
    grid = Grid(20,30)
    grid.initialiseRandomly()
    self.assertEqual(grid.isCellInitialised(10,10), True)

  def testCanInitialiseGridWithCells(self):
    grid = Grid(2,2)
    cells = [[Cell(False), Cell(True)], [Cell(False), Cell(False)]]
    grid.initialiseWithCells(cells)
    self.assertEqual(grid.isCellAlive(0,1), True)

if __name__ == '__main__':
  unittest.main()
