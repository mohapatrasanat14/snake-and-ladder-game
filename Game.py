from collections import deque
import random
from Player import Player
from Board import Board
from Dice import Dice


class Game:
    def __init__(self):
        self.board = None
        self.dice = None
        self.playersList = deque()
        self.winner = None
        self.initializeGame()

    def initializeGame(self):
        self.board = Board(10, 5, 4)
        self.dice = Dice(1)
        self.winner = None
        self.addPlayers()

    def addPlayers(self):
        player1 = Player("p1", 0)
        player2 = Player("p2", 0)
        self.playersList.append(player1)
        self.playersList.append(player2)

    def startGame(self):
        while self.winner is None:
            playerTurn = self.findPlayerTurn()
            print("player turn is:", playerTurn.id, "current position is:", playerTurn.currentPosition)

            diceNumbers = self.dice.rollDice()

            playerNewPosition = playerTurn.currentPosition + diceNumbers
            playerNewPosition = self.jumpCheck(playerNewPosition)
            playerTurn.currentPosition = playerNewPosition

            print("player turn is:", playerTurn.id, "new Position is:", playerNewPosition)

            if playerNewPosition >= self.board.boardSize() * self.board.boardSize() - 1:
                self.winner = playerTurn

        print("WINNER IS:", self.winner.id)

    def findPlayerTurn(self):
        playerTurn = self.playersList.popleft()
        self.playersList.append(playerTurn)
        return playerTurn

    def jumpCheck(self, playerNewPosition):
        if playerNewPosition > self.board.boardSize() * self.board.boardSize() - 1:
            return playerNewPosition

        cell = self.board.getCell(playerNewPosition)
        if cell.jump is not None and cell.jump.start == playerNewPosition:
            return cell.jump.end

        return playerNewPosition