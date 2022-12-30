import pygame
import sys
from maze import *


size = width, height = 500,500
N=10
M=10
P0=(0,0)
P1=(9,9)
matrix=[['██' for i in range(M)] for i in range(N)]
maze=Maze(N,M,P0,P1)
black=(0,0,0)
white=(255,255,255)
green=(0,255,0)
red=(255,0,0)
yellow=(255,255,153)
blue=(0,191,255)
pygame.init()
screen = pygame.display.set_mode(size)
FPS=100
fpsClock = pygame.time.Clock()
screen.fill(black)

cell=min(width//N,width//M)

maze.generate()
for point in maze.path:
    rect = pygame.Rect(
        point[0] * cell,
        point[1] * cell,
        cell, cell
    )
    pygame.draw.rect(screen, white, rect)
    rect = pygame.Rect(
        maze.end[0] * cell,
        maze.end[1] * cell,
        cell, cell
    )
    pygame.draw.rect(screen, green, rect)
    rect = pygame.Rect(
        maze.start[0] * cell,
        maze.start[1] * cell,
        cell, cell
    )
    pygame.draw.rect(screen, red, rect)
    fpsClock.tick(100)
    pygame.display.update()

maze.Astar()

for point in maze.explore:
    rect = pygame.Rect(
        point[0] * cell,
        point[1] * cell,
        cell, cell
    )
    pygame.draw.rect(screen, blue, rect)
    rect = pygame.Rect(
        maze.end[0] * cell,
        maze.end[1] * cell,
        cell, cell
    )
    pygame.draw.rect(screen, green, rect)
    rect = pygame.Rect(
        maze.start[0] * cell,
        maze.start[1] * cell,
        cell, cell
    )
    pygame.draw.rect(screen, red, rect)
    fpsClock.tick(20)
    pygame.display.update()
for point in maze.solution:
    rect = pygame.Rect(
        point[0] * cell,
        point[1] * cell,
        cell, cell
    )
    pygame.draw.rect(screen, yellow, rect)
    rect = pygame.Rect(
        maze.end[0] * cell,
        maze.end[1] * cell,
        cell, cell
    )
    pygame.draw.rect(screen, green, rect)
    rect = pygame.Rect(
        maze.start[0] * cell,
        maze.start[1] * cell,
        cell, cell
    )
    pygame.draw.rect(screen, red, rect)
    fpsClock.tick(20)
    pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    fpsClock.tick(100)
    pygame.display.update()
    