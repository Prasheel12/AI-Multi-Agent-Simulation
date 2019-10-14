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

    def getTarget(self, direction):
        # Gets location of next target in relation to location
        key = direction
        if self.node.neighbors[key] is not None:
            self.nextNode = self.node.neighbors[key]
        else:
            self.stopNode()

    def overshotTarget(self):
        # Will return true if the agent has moved further away from its target than at its previous location
        v1 = self.nextNode.position - self.node.position
        v2 = self.position - self.node.position
        nodeToTarget = v1.magnitudeSquared()
        nodeToSelf = v2.magnitudeSquared()
        return nodeToSelf > nodeToTarget

    def stopNode(self):
        # Will stop the agent on the current node
        self.setPosition()
        self.direction = STOP

    def render(self, screen):
        # Render agents
        px = int(self.position.x)
        py = int(self.position.y)
        pygame.draw.circle(screen, self.color, (px, py), 25)

    def render2(self, screen):
        # Render targets
        px = int(self.position.x)
        py = int(self.position.y)
        pygame.draw.circle(screen, self.color, (px, py), 20)