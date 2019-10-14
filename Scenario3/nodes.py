import pygame
from numpy import loadtxt
from stacks import Stack
from defMoves import *


class Node(object):
    def __init__(self, column, row, width, height):
        self.row, self.col = row, column
        self.neighbors = {UP:None, DOWN:None, LEFT:None, RIGHT:None}
        self.target = None
        self.position = movement(self.col * width, self.row * height)
        self.visited = False
        self.portalNode = None
        
    def render(self, screen):

        for n in self.neighbors.keys():
            if self.neighbors[n] is not None:
                pygame.draw.line(screen,(100,100,100), self.position.toTuple(), self.neighbors[n].position.toTuple(), 1)
        pygame.draw.circle(screen, (100,100,100), self.position.toTuple(), 20)


class NodeGroup(object):
    def __init__(self, width, height):

        self.nodeList = []
        self.width = width
        self.height = height
        self.grid = None
        self.nodeStack = Stack()
        self.fRows = 0
        self.fCols = 0
        
    def getNode(self, row, col):

        for node in self.nodeList:
            if node.row == row and node.col == col:
                return node
        return None

    def getNodeFromNode(self, node):

        if node is not None:
            for inode in self.nodeList:
                if node.row == inode.row and node.col == inode.col:
                    return inode
        return node
    
    def initNodes(self, rows, cols):

        nodeFound = False
        for row in range(rows):
            for col in range(cols):
                if self.grid[row][col] == "+":
                    return Node(col, row, self.width, self.height)
        return None

    def addNode(self, node):

        nodeInList = self.listedNode(node)
        if not nodeInList:
            self.nodeList.append(node)

    def listedNode(self, node):

        for inode in self.nodeList:
            if node.row == inode.row and node.col == inode.col:
                return True
        return False
    
    def setBoardNodes(self, filename):

        self.grid = loadtxt(filename, dtype=str)
        self.fRows, self.fCols = self.grid.shape
        startNode = self.initNodes(self.fRows, self.fCols)
        self.nodeStack.push(startNode)
        # print self.grid.shape
        while not self.nodeStack.isEmpty():
            node = self.nodeStack.pop()
            self.addNode(node)
            leftNode = self.folDirect(LEFT, node.row, node.col)
            rightNode = self.folDirect(RIGHT, node.row, node.col)
            upNode = self.folDirect(UP, node.row, node.col)
            downNode = self.folDirect(DOWN, node.row, node.col)
            leftNode = self.getNodeFromNode(leftNode)
            rightNode = self.getNodeFromNode(rightNode)
            upNode = self.getNodeFromNode(upNode)
            downNode = self.getNodeFromNode(downNode)
            node.neighbors[LEFT] = leftNode
            node.neighbors[RIGHT] = rightNode
            node.neighbors[UP] = upNode
            node.neighbors[DOWN] = downNode
            if leftNode is not None and not self.listedNode(leftNode):
                self.nodeStack.push(leftNode)
            if rightNode is not None and not self.listedNode(rightNode):
                self.nodeStack.push(rightNode)
            if upNode is not None and not self.listedNode(upNode):
                self.nodeStack.push(upNode)
            if downNode is not None and not self.listedNode(downNode):
                self.nodeStack.push(downNode)

    def folDirect(self, direction, row, col):
        if direction == LEFT and col-1 >= 0:
            if self.grid[row][col-1] == "-" or self.grid[row][col-1] == "+":
                while self.grid[row][col-1] != "+":
                    col -= 1
                return Node(col-1, row, self.width, self.height)
            else:
                return None
        elif direction == RIGHT and col+1 < self.fCols:
            if self.grid[row][col+1] == "-" or self.grid[row][col+1] == "+":
                while self.grid[row][col+1] != "+":
                    col += 1
                return Node(col+1, row, self.width, self.height)
            else:
                return None
        elif direction == UP and row-1 >= 0:
            if self.grid[row-1][col] == "|" or self.grid[row-1][col] == "+":
                while self.grid[row-1][col] != "+":
                    row -= 1
                return Node(col, row-1, self.width, self.height)
            else:
                return None
        elif direction == DOWN and row+1 < self.fRows:
            if self.grid[row+1][col] == "|" or self.grid[row+1][col] == "+":
                while self.grid[row+1][col] != "+":
                    row += 1
                return Node(col, row+1, self.width, self.height)
            else:
                return None
        else:
            return None    

    def render(self, screen):
        for node in self.nodeList:
            node.render(screen)
