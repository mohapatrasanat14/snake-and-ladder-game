import random
from Cell import Cell
from Jump import Jump

class Board:
    def __init__(self, boardSize, numberOfSnakes, numberOfLadders):
        self.cells = []
        self.initializeCells(boardSize)
        self.addSnakesLadders(numberOfSnakes, numberOfLadders)

    def initializeCells(self, boardSize):
        for i in range(boardSize):
            row = []
            for j in range(boardSize):
                cellObj = Cell()
                row.append(cellObj)
            self.cells.append(row)

    def addSnakesLadders(self, numberOfSnakes, numberOfLadders):
        while numberOfSnakes > 0:
            snakeHead = random.randint(1, len(self.cells) * len(self.cells) - 1)
            snakeTail = random.randint(1, len(self.cells) * len(self.cells) - 1)
            if snakeTail >= snakeHead:
                continue

            snakeObj = Jump()
            snakeObj.start = snakeHead
            snakeObj.end = snakeTail

            cell = self.getCell(snakeHead)
            cell.jump = snakeObj

            numberOfSnakes -= 1

        while numberOfLadders > 0:
            ladderStart = random.randint(1, len(self.cells) * len(self.cells) - 1)
            ladderEnd = random.randint(1, len(self.cells) * len(self.cells) - 1)
            if ladderStart >= ladderEnd:
                continue

            ladderObj = Jump()
            ladderObj.start = ladderStart
            ladderObj.end = ladderEnd

            cell = self.getCell(ladderStart)
            cell.jump = ladderObj

            numberOfLadders -= 1

    def getCell(self, playerPosition):
        boardRow = playerPosition // len(self.cells)
        boardColumn = playerPosition % len(self.cells)
        return self.cells[boardRow][boardColumn]


