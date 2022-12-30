import pygame
import sys
import time
from maze import *

# Colors
black=(0,0,0)
white=(255,255,255)
green=(0,255,0)
red=(255,0,0)
yellow=(255,255,153)
blue=(0,191,255)

# Create game
pygame.init()
size = width, height = 600,400
screen = pygame.display.set_mode(size)

# Fonts

smallFont = pygame.font.SysFont('arial', 20)
mediumFont = pygame.font.SysFont('arial', 28)
largeFont = pygame.font.SysFont('arial', 40)

# Maze
N=40
M=40
P0=(0,0)
P1=(39,39)
matrix=[['██' for i in range(M)] for i in range(N)]
maze=Maze(N,M,P0,P1)

# Board size
BOARD_PADDING = 20
board_width = ((2 / 3) * width) - (BOARD_PADDING * 2)
board_height = height - (BOARD_PADDING * 2)
cell_size = int(min(board_width / N, board_height / M))
board_origin = (BOARD_PADDING, BOARD_PADDING)


instructions = True
end=False

while True:

    # Check if game quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)

    if instructions:

        # Title
        title = largeFont.render("Solve Maze", True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 50)
        screen.blit(title, titleRect)

        # Generate maze button
        buttonRect = pygame.Rect((width / 4), (3 / 4) * height, width / 2, 50)
        buttonText = mediumFont.render("Generate Maze", True, black)
        buttonTextRect = buttonText.get_rect()
        buttonTextRect.center = buttonRect.center
        pygame.draw.rect(screen, white, buttonRect)
        screen.blit(buttonText, buttonTextRect)

        # Check if generate button clicked
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
            if buttonRect.collidepoint(mouse):
                maze.generate()
                instructions = False
                time.sleep(0.3)
        pygame.display.flip()
        continue

    # Maze
    # maze.generate()
    for point in maze.path:
        rect = pygame.Rect(
            board_origin[0] + point[0] * cell_size,
            board_origin[1] + point[1] * cell_size,
            cell_size, cell_size
        )
        pygame.draw.rect(screen, white, rect)
    for cell in maze.explore:
        rect = pygame.Rect(
            board_origin[0] + cell[0] * cell_size,
            board_origin[1] + cell[1] * cell_size,
            cell_size, cell_size
        )
        pygame.draw.rect(screen, blue, rect)
    for cell in maze.solution:
        rect = pygame.Rect(
            board_origin[0] + cell[0] * cell_size,
            board_origin[1] + cell[1] * cell_size,
            cell_size, cell_size
        )
        pygame.draw.rect(screen, yellow, rect)
    
    rect = pygame.Rect(
        board_origin[0] + maze.end[0] * cell_size,
        board_origin[1] + maze.end[1] * cell_size,
        cell_size, cell_size
    )
    pygame.draw.rect(screen, green, rect)

    rect = pygame.Rect(
        board_origin[0] + maze.start[0] * cell_size,
        board_origin[1] + maze.start[1] * cell_size,
        cell_size, cell_size
    )
    pygame.draw.rect(screen, red, rect)

    # Astar button
    AstarButton = pygame.Rect(
        (2 / 3) * width + BOARD_PADDING, (1 / 3) * height - 120,
        (width / 3) - BOARD_PADDING * 2, 50
    )
    buttonText = smallFont.render("Astar Solve", True, black)
    buttonRect = buttonText.get_rect()
    buttonRect.center = AstarButton.center
    pygame.draw.rect(screen, white, AstarButton)
    screen.blit(buttonText, buttonRect)

    # DFS button
    DFSButton = pygame.Rect(
        (2 / 3) * width + BOARD_PADDING, (1 / 3) * height -50,
        (width / 3) - BOARD_PADDING * 2, 50
    )
    buttonText = smallFont.render("DFS Solve", True, black)
    buttonRect = buttonText.get_rect()
    buttonRect.center = DFSButton.center
    pygame.draw.rect(screen, white, DFSButton)
    screen.blit(buttonText, buttonRect)

    # BFS button
    BFSButton = pygame.Rect(
        (2 / 3) * width + BOARD_PADDING, (1 / 3) * height +20,
        (width / 3) - BOARD_PADDING * 2, 50
    )
    buttonText = smallFont.render("BFS Solve", True, black)
    buttonRect = buttonText.get_rect()
    buttonRect.center = BFSButton.center
    pygame.draw.rect(screen, white, BFSButton)
    screen.blit(buttonText, buttonRect)

    # Greedy button
    GreedyButton = pygame.Rect(
        (2 / 3) * width + BOARD_PADDING, (1 / 3) * height + 90,
        (width / 3) - BOARD_PADDING * 2, 50
    )
    buttonText = smallFont.render("Greedy Solve", True, black)
    buttonRect = buttonText.get_rect()
    buttonRect.center = GreedyButton.center
    pygame.draw.rect(screen, white, GreedyButton)
    screen.blit(buttonText, buttonRect)

    # Reset button
    resetButton = pygame.Rect(
        (2 / 3) * width + BOARD_PADDING, (1 / 3) * height + 160,
        (width / 3) - BOARD_PADDING * 2, 50
    )
    buttonText = mediumFont.render("Reset", True, black)
    buttonRect = buttonText.get_rect()
    buttonRect.center = resetButton.center
    pygame.draw.rect(screen, white, resetButton)
    screen.blit(buttonText, buttonRect)

    # Display text
    text = f"Path = {len(maze.solution)}" if end else ''
    text = smallFont.render(text, True, white)
    textRect = text.get_rect()
    textRect.center = ((5 / 6) * width, (9 / 10) * height)
    screen.blit(text, textRect)

    click, _, _ = pygame.mouse.get_pressed()
    if click==1:
        mouse=pygame.mouse.get_pos()

        # If Astar button clicked
        if AstarButton.collidepoint(mouse):
            maze.Astar()
        
        # If DFS button clicked
        if DFSButton.collidepoint(mouse):
            maze.DFS()
            
        # If BFS button clicked
        if BFSButton.collidepoint(mouse):
            maze.BFS()

        # If Greedy button clicked
        if GreedyButton.collidepoint(mouse):
            maze.Greedy()

        end=True

         # If reset button clicked
        if resetButton.collidepoint(mouse):
            maze=Maze(N,M,P0,P1)
            maze.generate()
            end=False

    pygame.display.flip()
