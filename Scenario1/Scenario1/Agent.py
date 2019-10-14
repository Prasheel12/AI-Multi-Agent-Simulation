from defMoves import *
from agentInfo import agentControls
from random import randint


class Agent(agentControls):
    id_count = 1

    def __init__(self, node):
        agentControls.__init__(self, node)
        self.id = Agent.id_count
        Agent.id_count += 1
        self.color = (0, 0, 255)
        self.direction = RIGHT
        self.nextNode = self.node.neighbors[self.direction]
        self.poi = movement()
        self.radiusSquared = (gridUnit * 22)**2
        self.closestCheck = None

        self.moves = 0.0
        self.movesToComplete = None
        self.targetsFound = 0.0
        self.happiness = []
        self.maxHappiness = 0.0
        self.minHappiness = 0.0

    def update(self, dt, targetList, checkList):
        self.position += self.direction*self.speed*dt

        if self.happiness:
            happiness = self.happiness[-1]
        else:
            happiness = 0.0

        overshot = self.overshotTarget()
        if overshot:
            self.node = self.nextNode
            self.position = self.node.position

            validDirections = self.getValidDirections()
            self.checkList = []
            dummyCheckList = []
            self.falseCheckList = []
            dummyTargetList = []

            for check in checkList:
                self.checkList.append(check)
            if self.checkList:
                for check in self.checkList:
                    for false in self.falseCheckList:
                        if false.position != check.position:
                            check.distanceVector = check.position - self.position
                            check.distanceSquared = check.distanceVector.magnitudeSquared()
                            dummyCheckList.append(check.distanceSquared)
                if dummyCheckList:
                    closestCheckIndex = dummyCheckList.index(min(dummyCheckList))
                    self.closestCheck = self.checkList[closestCheckIndex]

            for target in targetList:
                target.distanceVector = target.position - self.position
                target.distanceSquared = target.distanceVector.magnitudeSquared()
                dummyTargetList.append(target.distanceSquared)
            closestTargetIndex = dummyTargetList.index(min(dummyTargetList))
            closestTarget = targetList[closestTargetIndex]

            if dummyCheckList:
                index = self.getClosestNode(validDirections)
                self.poi = self.closestCheck.position
                if self.closestCheck.distanceSquared < self.radiusSquared:
                    if self.id == self.closestCheck.owner:
                        self.poi = self.closestCheck.position
                        if self.position == self.closestCheck.position:
                            self.setFound(self.closestCheck)
                    else:
                        self.falseCheckList.append(self.closestCheck)
                        index = randint(0, len(validDirections) - 1)
            elif closestTarget.distanceSquared < self.radiusSquared:
                index = self.getClosestNode(validDirections)
                if self.id == closestTarget.owner:
                    self.poi = closestTarget.position
                    if self.position == closestTarget.position:
                        if not closestTarget.isFound:
                            self.setFound(closestTarget)
                        index = randint(0, len(validDirections) - 1)
                else:
                    if not closestTarget.isInCheckList and (happiness > 0.002):
                        self.setIsInCheckList(closestTarget)
                    index = randint(0, len(validDirections) - 1)
            else:
                index = randint(0, len(validDirections) - 1)
            self.direction = validDirections[index]
            self.nextNode = self.node.neighbors[self.direction]
            self.moves += 1.0
            currentHappiness = self.targetsFound/(self.moves + 1)
            self.happiness.append(currentHappiness)

    def getClosestNode(self, validDirections):
        distances = []
        for key in validDirections:
            diffVec = self.node.neighbors[key].position - self.poi
            distances.append(diffVec.magnitudeSquared())
        return distances.index(min(distances))

    def getValidDirections(self):
        validDirections = []
        for key in self.node.neighbors.keys():
            if self.node.neighbors[key] is not None:
                if not key == self.direction * -1:
                    validDirections.append(key)
        return validDirections

    def setFound(self, target):
        target.isFound = True
        self.targetsFound += 1.0
        if self.targetsFound == 5.0:
            self.movesToComplete = self.moves

    def setIsInCheckList(self, target):
        target.isInCheckList = True
