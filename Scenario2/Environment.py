from targets import Targets
from Agent import Agent
from random import randint
from nodes import NodeGroup
from defMoves import *


class environment(object):
    def __init__(self):
        self.nodes = NodeGroup(gridUnit, gridUnit)
        self.nodes.getBoardNodes("field.txt")

        # initialize agents
        self.agentRed = Agent(self.nodes.nodeList[randint(0, 2000)])
        self.agentRed.color = (255, 0, 0)
        # print self.clyde1.id
        self.agentWhite = Agent(self.nodes.nodeList[randint(0, 2000)])
        self.agentWhite.color = (255, 255, 255)
        # print self.clyde2.id
        self.agentTeal = Agent(self.nodes.nodeList[randint(0, 2000)])
        self.agentTeal.color = (0, 255, 255)
        # print self.clyde3.id
        self.agentPurple = Agent(self.nodes.nodeList[randint(0, 2000)])
        self.agentPurple.color = (100, 100, 200)
        # print self.clyde4.id
        self.agentGrey = Agent(self.nodes.nodeList[randint(0, 2000)])
        self.agentGrey.color = (150, 150, 150)
        #print self.clyde5.id

        # initialize targets
        self.targetRed1 = Targets(self.nodes.nodeList[randint(0, 2000)], self.agentRed.id)
        self.targetRed1.color = (250, 1, 1)
        self.targetRed2 = Targets(self.nodes.nodeList[randint(0, 2000)], self.agentRed.id)
        self.targetRed2.color = (250, 2, 2)
        self.targetRed3 = Targets(self.nodes.nodeList[randint(0, 2000)], self.agentRed.id)
        self.targetRed3.color = (250, 3, 3)
        self.targetRed4 = Targets(self.nodes.nodeList[randint(0, 2000)], self.agentRed.id)
        self.targetRed4.color = (250, 4, 4)
        self.targetRed5 = Targets(self.nodes.nodeList[randint(0, 2000)], self.agentRed.id)
        self.targetRed5.color = (250, 5, 5)

        self.targetWhite1 = Targets(self.nodes.nodeList[randint(0, 2000)], self.agentWhite.id)
        self.targetWhite1.color = (255, 255, 255)
        self.targetWhite2 = Targets(self.nodes.nodeList[randint(0, 2000)], self.agentWhite.id)
        self.targetWhite2.color = (255, 255, 255)
        self.targetWhite3 = Targets(self.nodes.nodeList[randint(0, 2000)], self.agentWhite.id)
        self.targetWhite3.color = (255, 255, 255)
        self.targetWhite4 = Targets(self.nodes.nodeList[randint(0, 2000)], self.agentWhite.id)
        self.targetWhite4.color = (255, 255, 255)
        self.targetWhite5 = Targets(self.nodes.nodeList[randint(0, 2000)], self.agentWhite.id)
        self.targetWhite5.color = (255, 255, 255)

        self.targetTeal1 = Targets(self.nodes.nodeList[randint(0, 2000)], self.agentTeal.id)
        self.targetTeal1.color = (0, 255, 255)
        self.targetTeal2 = Targets(self.nodes.nodeList[randint(0, 2000)], self.agentTeal.id)
        self.targetTeal2.color = (0, 255, 255)
        self.targetTeal3 = Targets(self.nodes.nodeList[randint(0, 2000)], self.agentTeal.id)
        self.targetTeal3.color = (0, 255, 255)
        self.targetTeal4 = Targets(self.nodes.nodeList[randint(0, 2000)], self.agentTeal.id)
        self.targetTeal4.color = (0, 255, 255)
        self.targetTeal5 = Targets(self.nodes.nodeList[randint(0, 2000)], self.agentTeal.id)
        self.targetTeal5.color = (0, 255, 255)

        self.targetPurple1 = Targets(self.nodes.nodeList[randint(0, 2000)], self.agentPurple.id)
        self.targetPurple1.color = (100, 100, 200)
        self.targetPurple2 = Targets(self.nodes.nodeList[randint(0, 2000)], self.agentPurple.id)
        self.targetPurple2.color = (100, 100, 200)
        self.targetPurple3 = Targets(self.nodes.nodeList[randint(0, 2000)], self.agentPurple.id)
        self.targetPurple3.color = (100, 100, 200)
        self.targetPurple4 = Targets(self.nodes.nodeList[randint(0, 2000)], self.agentPurple.id)
        self.targetPurple4.color = (100, 100, 200)
        self.targetPurple5 = Targets(self.nodes.nodeList[randint(0, 2000)], self.agentPurple.id)
        self.targetPurple5.color = (100, 100, 200)

        self.targetGrey1 = Targets(self.nodes.nodeList[randint(0, 2000)], self.agentGrey.id)
        self.targetGrey1.color = (150, 150, 150)
        self.targetGrey2 = Targets(self.nodes.nodeList[randint(0, 2000)], self.agentGrey.id)
        self.targetGrey2.color = (150, 150, 150)
        self.targetGrey3 = Targets(self.nodes.nodeList[randint(0, 2000)], self.agentGrey.id)
        self.targetGrey3.color = (150, 150, 150)
        self.targetGrey4 = Targets(self.nodes.nodeList[randint(0, 2000)], self.agentGrey.id)
        self.targetGrey4.color = (150, 150, 150)
        self.targetGrey5 = Targets(self.nodes.nodeList[randint(0, 2000)], self.agentGrey.id)
        self.targetGrey5.color = (150, 150, 150)

        self.Agents = [self.agentRed, self.agentWhite, self.agentTeal, self.agentPurple, self.agentGrey]

        self.Targets = [self.targetRed1, self.targetRed2, self.targetRed3, self.targetRed4, self.targetRed5,
                        self.targetWhite1, self.targetWhite2, self.targetWhite3, self.targetWhite4, self.targetWhite5,
                        self.targetTeal1, self.targetTeal2, self.targetTeal3, self.targetTeal4, self.targetTeal5,
                        self.targetPurple1, self.targetPurple2, self.targetPurple3, self.targetPurple4,
                        self.targetPurple5,
                        self.targetGrey1, self.targetGrey2, self.targetGrey3, self.targetGrey4, self.targetGrey5]


        self.checkList = []

    def update(self, time_passed, screen):
        self.checkScenarioGoal()

        for target in self.Targets:
            if target.isInCheckList:
                if target not in self.checkList:
                    self.checkList.append(target)
                    #print self.checkList

            if target.isFound:
                if target in self.checkList:
                    self.checkList.remove(target)
                    #print self.checkList
                self.Targets.remove(target)
            #target.update()

        self.agentRed.update(time_passed, self.Targets, self.checkList)
        self.agentWhite.update(time_passed, self.Targets, self.checkList)
        self.agentTeal.update(time_passed, self.Targets, self.checkList)
        self.agentPurple.update(time_passed, self.Targets, self.checkList)
        self.agentGrey.update(time_passed, self.Targets, self.checkList)

        # render targets
        for target in self.Targets:
            target.render2(screen)

        # render agents
        self.agentRed.render(screen)
        self.agentWhite.render(screen)
        self.agentTeal.render(screen)
        self.agentPurple.render(screen)
        self.agentGrey.render(screen)

    def returnNodes(self):
        return self.nodes

    def checkScenarioGoal(self):
        if self.agentRed.targetsFound == 5 \
                and self.agentWhite.targetsFound == 5 \
                and self.agentTeal.targetsFound == 5 \
                and self.agentGrey.targetsFound == 5 \
                and self.agentPurple.targetsFound == 5:
            return True
