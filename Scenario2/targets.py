from agentInfo import agentControls


class Targets(agentControls):
    def __init__(self, node, ownerID):
        agentControls.__init__(self, node)
        self.color = (255, 255, 0)
        self.owner = ownerID
        self.isFound = False
        self.isInCheckList = False
        self.setPosition()
