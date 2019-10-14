import pygame
from defMoves import *
from Movement import movement


class agentControls(object):
    def __init__(self, node):
        self.node = node
        self.nextNode = node
        self.speed = 1000
        self.setPosition()
        self.color = (255, 255, 255)
        
    def setPosition(self):
        self.position = movement(self.node.position.x, self.node.position.y)

    #Next target by direction
    def getNextTarget(self, direction):
        key = direction
        if self.node.neighbors[key] is not None:
            self.nextNode = self.node.neighbors[key]
        else:
            self.stopNode()

    #Returns true if moved past target
    def overshotTarget(self):
        vec1 = self.nextNode.position - self.node.position
        vec2 = self.position - self.node.position
        nodeToTarget = vec1.magnitudeSquared()
        nodeToSelf = vec2.magnitudeSquared()
        return nodeToSelf > nodeToTarget

    #Function to stop
    def stopNode(self):
        self.setPosition()
        self.direction = STOP

    #Agents
    def render(self, screen):
        px = int(self.position.x)
        py = int(self.position.y)
        pygame.draw.circle(screen, self.color, (px, py), 25)

    #Targets
    def render2(self, screen):
        px = int(self.position.x)
        py = int(self.position.y)
        pygame.draw.circle(screen, self.color, (px, py), 20)
