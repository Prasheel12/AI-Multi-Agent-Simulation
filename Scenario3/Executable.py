import pygame
from pygame.locals import *
from defMoves import *
from Environment import World
import numpy as np
import csv

print "Scenario 3 Begin\n"
pygame.init() # Initialize the pygame board

SCREENSIZE = (100*gridUnit, 100*gridUnit)
screen = pygame.display.set_mode(SCREENSIZE, 0, 32)
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))

world = World()
world.returnNodes()
clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    if world.checkScenarioGoal():

        print "Scenario 3 Complete"

        Data = \
            [
                ["Scenario", "Iteration", "Agent Number", "Targets Collected", "Total Moves", "Agent Happiness", "Max Happiness", "Min Happiness", "Avg Happiness", "Standard Deviation Happiness", "Agent Competitiveness"],
                ["1", "10", "1", world.agentRed.targetsFound, world.agentRed.moves, float(world.agentRed.targetsFound/(world.agentRed.moves + 1)), np.max(world.agentRed.happiness), np.min(world.agentRed.happiness), np.mean(world.agentRed.happiness), np.std(world.agentRed.happiness), ((float(world.agentRed.targetsFound / (world.agentRed.moves + 1))) - np.min(world.agentRed.happiness))/(np.max(world.agentRed.happiness) - np.min(world.agentRed.happiness))],
                ["1", "10", "2", world.agentWhite.targetsFound, world.agentWhite.moves, float(world.agentWhite.targetsFound/(world.agentWhite.moves + 1)), np.max(world.agentWhite.happiness), np.min(world.agentWhite.happiness), np.mean(world.agentWhite.happiness), np.std(world.agentWhite.happiness), ((float(world.agentWhite.targetsFound / (world.agentWhite.moves + 1))) - np.min(world.agentWhite.happiness))/(np.max(world.agentWhite.happiness) - np.min(world.agentWhite.happiness))],
                ["1", "10", "3", world.agentTeal.targetsFound, world.agentTeal.moves, float(world.agentTeal.targetsFound/(world.agentTeal.moves + 1)), np.max(world.agentTeal.happiness), np.min(world.agentTeal.happiness), np.mean(world.agentTeal.happiness), np.std(world.agentTeal.happiness), ((float(world.agentTeal.targetsFound / (world.agentTeal.moves + 1))) - np.min(world.agentTeal.happiness))/(np.max(world.agentTeal.happiness) - np.min(world.agentTeal.happiness))],
                ["1", "10", "4", world.agentPurple.targetsFound, world.agentPurple.moves, float(world.agentPurple.targetsFound/(world.agentPurple.moves + 1)), np.max(world.agentPurple.happiness), np.min(world.agentPurple.happiness), np.mean(world.agentPurple.happiness), np.std(world.agentPurple.happiness), ((float(world.agentPurple.targetsFound / (world.agentPurple.moves + 1))) - np.min(world.agentPurple.happiness))/(np.max(world.agentPurple.happiness) - np.min(world.agentPurple.happiness))],
                ["1", "10", "5", world.agentGrey.targetsFound, world.agentGrey.moves, float(world.agentGrey.targetsFound/(world.agentGrey.moves + 1)), np.max(world.agentGrey.happiness), np.min(world.agentGrey.happiness), np.mean(world.agentGrey.happiness), np.std(world.agentGrey.happiness), ((float(world.agentGrey.targetsFound / (world.agentGrey.moves + 1))) - np.min(world.agentGrey.happiness))/(np.max(world.agentGrey.happiness) - np.min(world.agentGrey.happiness))]
            ]
        myFile = open("scenario_3_iter_11.csv", "w")
        with myFile:
            writer = csv.writer(myFile)
            writer.writerows(Data)

        exit()

    elapsedTime = clock.tick(30) / 1000.0

    screen.blit(background, (0, 0))
    world.nodes.render(screen)
    world.update(elapsedTime, screen)
    pygame.display.update()
