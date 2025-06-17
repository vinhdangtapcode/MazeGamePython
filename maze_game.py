import pygame
import sys
import time
from maze import *

# Colors    # Màu cho các nút kích thước
black=(0,0,0)
white=(255,255,255)
green=(0,255,0)
red=(255,0,0)
yellow=(255,255,153)
blue=(0,191,255)
light_gray=(200,200,200)

# Create game
pygame.init()
size = width, height = 800,600
screen = pygame.display.set_mode(size)

# Fonts
smallFont = pygame.font.SysFont('arial', 20)
mediumFont = pygame.font.SysFont('arial', 28)
largeFont = pygame.font.SysFont('arial', 40)

# Maze
N=10  # Kích thước mặc định 10x10
M=10
P0=(0,0)
P1=(N-1,M-1)
matrix=[['██' for i in range(M)] for i in range(N)]
maze=Maze(N,M,P0,P1)

# Biến lưu kích thước mê cung được chọn
selected_size = "10x10"  # Kích thước mặc định

# Board size
BOARD_PADDING = 40  # Increase padding for better spacing
BUTTON_HEIGHT = 50
BUTTON_WIDTH = int(width * 0.22)
BUTTON_SPACING = 20

# Calculate area for maze board (left side)
board_area_width = int(width * 0.62) - BOARD_PADDING * 2
board_area_height = height - BOARD_PADDING * 2
cell_size = int(min(board_area_width / N, board_area_height / M))
board_width = cell_size * N
board_height = cell_size * M
board_origin = (BOARD_PADDING, (height - board_height) // 2)

# Calculate area for buttons and result box (right side)
right_panel_left = board_origin[0] + board_width + 2 * BOARD_PADDING
right_panel_width = width - right_panel_left - BOARD_PADDING

# Buttons for maze size selection
SIZE_BUTTON_HEIGHT = 30
SIZE_BUTTON_WIDTH = 80
SIZE_BUTTON_SPACING = 10
size_buttons_top = BOARD_PADDING - 20  # Moved 10 pixels higher
size_button_10x10 = pygame.Rect(right_panel_left, size_buttons_top, SIZE_BUTTON_WIDTH, SIZE_BUTTON_HEIGHT)
size_button_20x20 = pygame.Rect(right_panel_left + SIZE_BUTTON_WIDTH + SIZE_BUTTON_SPACING, size_buttons_top, SIZE_BUTTON_WIDTH, SIZE_BUTTON_HEIGHT)
size_button_50x50 = pygame.Rect(right_panel_left + 2 * (SIZE_BUTTON_WIDTH + SIZE_BUTTON_SPACING), size_buttons_top, SIZE_BUTTON_WIDTH, SIZE_BUTTON_HEIGHT)

# Button positions (stacked vertically, centered in right panel)
first_button_top = (height - (BUTTON_HEIGHT * 5 + BUTTON_SPACING * 4 + 120 + 20)) // 2
AstarButton = pygame.Rect(right_panel_left, first_button_top, BUTTON_WIDTH, BUTTON_HEIGHT)
GreedyButton = pygame.Rect(right_panel_left, first_button_top + (BUTTON_HEIGHT + BUTTON_SPACING), BUTTON_WIDTH, BUTTON_HEIGHT)
DFSButton = pygame.Rect(right_panel_left, first_button_top + 2 * (BUTTON_HEIGHT + BUTTON_SPACING), BUTTON_WIDTH, BUTTON_HEIGHT)
BFSButton = pygame.Rect(right_panel_left, first_button_top + 3 * (BUTTON_HEIGHT + BUTTON_SPACING), BUTTON_WIDTH, BUTTON_HEIGHT)
resetButton = pygame.Rect(right_panel_left, first_button_top + 4 * (BUTTON_HEIGHT + BUTTON_SPACING), BUTTON_WIDTH, BUTTON_HEIGHT)

# Result box (below buttons)
result_box_top = resetButton.bottom + 30
result_box_height = 120
result_box_rect = pygame.Rect(right_panel_left, result_box_top, BUTTON_WIDTH, result_box_height)

# Thêm biến lưu kết quả các thuật toán đã chạy
algo_results = []

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
                maze.explore = []
                maze.solution = []
                instructions = False
                time.sleep(0.3)
        pygame.display.flip()
        continue

    # Maze
    # maze.generate()
    # Vẽ lại mê cung chỉ với màu trắng (path), không vẽ explore/solution nếu chưa có
    for point in maze.path:
        rect = pygame.Rect(
            board_origin[0] + point[0] * cell_size,
            board_origin[1] + point[1] * cell_size,
            cell_size, cell_size
        )
        pygame.draw.rect(screen, white, rect)
    # Chỉ vẽ explore nếu đang có (sau khi giải)
    if maze.explore:
        for cell in maze.explore:
            rect = pygame.Rect(
                board_origin[0] + cell[0] * cell_size,
                board_origin[1] + cell[1] * cell_size,
                cell_size, cell_size
            )
            pygame.draw.rect(screen, blue, rect)
    # Chỉ vẽ solution nếu đang có (sau khi giải)
    if maze.solution:
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

    # Vẽ các nút chọn kích thước mê cung
    # Nút 10x10
    button_color = light_gray if selected_size == "10x10" else white
    pygame.draw.rect(screen, button_color, size_button_10x10)
    buttonText = smallFont.render("10x10", True, black)
    buttonRect = buttonText.get_rect()
    buttonRect.center = size_button_10x10.center
    screen.blit(buttonText, buttonRect)

    # Nút 20x20
    button_color = light_gray if selected_size == "20x20" else white
    pygame.draw.rect(screen, button_color, size_button_20x20)
    buttonText = smallFont.render("20x20", True, black)
    buttonRect = buttonText.get_rect()
    buttonRect.center = size_button_20x20.center
    screen.blit(buttonText, buttonRect)

    # Nút 50x50
    button_color = light_gray if selected_size == "50x50" else white
    pygame.draw.rect(screen, button_color, size_button_50x50)
    buttonText = smallFont.render("50x50", True, black)
    buttonRect = buttonText.get_rect()
    buttonRect.center = size_button_50x50.center
    screen.blit(buttonText, buttonRect)

    # Astar button
    pygame.draw.rect(screen, white, AstarButton)
    buttonText = smallFont.render("Astar Solve", True, black)
    buttonRect = buttonText.get_rect()
    buttonRect.center = AstarButton.center
    screen.blit(buttonText, buttonRect)

    # Greedy button
    pygame.draw.rect(screen, white, GreedyButton)
    buttonText = smallFont.render("Greedy Solve", True, black)
    buttonRect = buttonText.get_rect()
    buttonRect.center = GreedyButton.center
    screen.blit(buttonText, buttonRect)

    # DFS button
    pygame.draw.rect(screen, white, DFSButton)
    buttonText = smallFont.render("DFS Solve", True, black)
    buttonRect = buttonText.get_rect()
    buttonRect.center = DFSButton.center
    screen.blit(buttonText, buttonRect)

    # BFS button
    pygame.draw.rect(screen, white, BFSButton)
    buttonText = smallFont.render("BFS Solve", True, black)
    buttonRect = buttonText.get_rect()
    buttonRect.center = BFSButton.center
    screen.blit(buttonText, buttonRect)

    # Reset button
    pygame.draw.rect(screen, white, resetButton)
    buttonText = mediumFont.render("Reset", True, black)
    buttonRect = buttonText.get_rect()
    buttonRect.center = resetButton.center
    screen.blit(buttonText, buttonRect)

    # Display text
    text = f"Path = {len(maze.solution)} | Explored = {len(maze.explore)}" if end else ''
    text = smallFont.render(text, True, white)
    textRect = text.get_rect()
    textRect.center = ((5 / 6) * width, (9 / 10) * height)
    screen.blit(text, textRect)

    # Hiển thị ô kết quả các thuật toán đã chạy (luôn hiển thị, không phụ thuộc end)
    pygame.draw.rect(screen, (30,30,30), result_box_rect, border_radius=8)
    pygame.draw.rect(screen, white, result_box_rect, 2, border_radius=8)
    for idx, result in enumerate(algo_results[-5:]):
        result_text = smallFont.render(result, True, white)
        result_text_rect = result_text.get_rect()
        result_text_rect.topleft = (result_box_rect.left + 10, result_box_rect.top + 10 + idx*24)
        screen.blit(result_text, result_text_rect)

    click, _, _ = pygame.mouse.get_pressed()
    if click==1:
        mouse=pygame.mouse.get_pos()

        def animate_solution():
            # Vẽ từng bước explore
            for cell in maze.explore:
                rect = pygame.Rect(
                    board_origin[0] + cell[0] * cell_size,
                    board_origin[1] + cell[1] * cell_size,
                    cell_size, cell_size
                )
                pygame.draw.rect(screen, blue, rect)
                # Vẽ lại start và end
                rect_end = pygame.Rect(
                    board_origin[0] + maze.end[0] * cell_size,
                    board_origin[1] + maze.end[1] * cell_size,
                    cell_size, cell_size
                )
                pygame.draw.rect(screen, green, rect_end)
                rect_start = pygame.Rect(
                    board_origin[0] + maze.start[0] * cell_size,
                    board_origin[1] + maze.start[1] * cell_size,
                    cell_size, cell_size
                )
                pygame.draw.rect(screen, red, rect_start)
                pygame.display.flip()
                pygame.time.delay(10)
            # Vẽ từng bước solution
            for cell in maze.solution:
                rect = pygame.Rect(
                    board_origin[0] + cell[0] * cell_size,
                    board_origin[1] + cell[1] * cell_size,
                    cell_size, cell_size
                )
                pygame.draw.rect(screen, yellow, rect)
                rect_end = pygame.Rect(
                    board_origin[0] + maze.end[0] * cell_size,
                    board_origin[1] + maze.end[1] * cell_size,
                    cell_size, cell_size
                )
                pygame.draw.rect(screen, green, rect_end)
                rect_start = pygame.Rect(
                    board_origin[0] + maze.start[0] * cell_size,
                    board_origin[1] + maze.start[1] * cell_size,
                    cell_size, cell_size
                )
                pygame.draw.rect(screen, red, rect_start)
                pygame.display.flip()
                pygame.time.delay(30)

        def redraw_maze_only_path():
            screen.fill(black)
            for point in maze.path:
                rect = pygame.Rect(
                    board_origin[0] + point[0] * cell_size,
                    board_origin[1] + point[1] * cell_size,
                    cell_size, cell_size
                )
                pygame.draw.rect(screen, white, rect)
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
            # Vẽ lại các nút với text căn giữa
            pygame.draw.rect(screen, white, AstarButton)
            buttonText = smallFont.render("Astar Solve", True, black)
            buttonTextRect = buttonText.get_rect()
            buttonTextRect.center = AstarButton.center
            screen.blit(buttonText, buttonTextRect)

            pygame.draw.rect(screen, white, GreedyButton)
            buttonText = smallFont.render("Greedy Solve", True, black)
            buttonTextRect = buttonText.get_rect()
            buttonTextRect.center = GreedyButton.center
            screen.blit(buttonText, buttonTextRect)

            pygame.draw.rect(screen, white, DFSButton)
            buttonText = smallFont.render("DFS Solve", True, black)
            buttonTextRect = buttonText.get_rect()
            buttonTextRect.center = DFSButton.center
            screen.blit(buttonText, buttonTextRect)

            pygame.draw.rect(screen, white, BFSButton)
            buttonText = smallFont.render("BFS Solve", True, black)
            buttonTextRect = buttonText.get_rect()
            buttonTextRect.center = BFSButton.center
            screen.blit(buttonText, buttonTextRect)

            pygame.draw.rect(screen, white, resetButton)
            buttonText = mediumFont.render("Reset", True, black)
            buttonTextRect = buttonText.get_rect()
            buttonTextRect.center = resetButton.center
            screen.blit(buttonText, buttonTextRect)
            # Vẽ lại ô kết quả các thuật toán đã chạy (dùng lại result_box_rect)
            pygame.draw.rect(screen, (30,30,30), result_box_rect, border_radius=8)
            pygame.draw.rect(screen, white, result_box_rect, 2, border_radius=8)
            for idx, result in enumerate(algo_results[-5:]):
                result_text = smallFont.render(result, True, white)
                result_text_rect = result_text.get_rect()
                result_text_rect.topleft = (result_box_rect.left + 10, result_box_rect.top + 10 + idx*24)
                screen.blit(result_text, result_text_rect)
            pygame.display.flip()

        # If Astar button clicked
        if AstarButton.collidepoint(mouse):
            maze.explore = []
            maze.solution = []
            redraw_maze_only_path()
            maze.Astar()
            algo_results.append(f"Astar: {len(maze.solution)}({len(maze.explore)})")
            animate_solution()
        # If Greedy button clicked
        elif GreedyButton.collidepoint(mouse):
            maze.explore = []
            maze.solution = []
            redraw_maze_only_path()
            maze.Greedy()
            algo_results.append(f"Greedy: {len(maze.solution)}({len(maze.explore)})")
            animate_solution()
        # If DFS button clicked
        elif DFSButton.collidepoint(mouse):
            maze.explore = []
            maze.solution = []
            redraw_maze_only_path()
            maze.DFS()
            algo_results.append(f"DFS: {len(maze.solution)}({len(maze.explore)})")
            animate_solution()
        # If BFS button clicked
        elif BFSButton.collidepoint(mouse):
            maze.explore = []
            maze.solution = []
            redraw_maze_only_path()
            maze.BFS()
            algo_results.append(f"BFS: {len(maze.solution)}({len(maze.explore)})")
            animate_solution()
        # If reset button clicked
        elif resetButton.collidepoint(mouse):
            maze=Maze(N,M,P0,P1)
            maze.generate()
            maze.explore = []
            maze.solution = []
            algo_results.clear()
            end=False
        # Nếu nhấp vào nút kích thước 10x10
        elif size_button_10x10.collidepoint(mouse):
            if selected_size != "10x10":
                selected_size = "10x10"
                N = M = 10
                P0 = (0, 0)
                P1 = (N-1, M-1)
                # Tạo mê cung mới với kích thước 10x10
                maze = Maze(N, M, P0, P1)
                maze.generate()
                maze.explore = []
                maze.solution = []
                algo_results.clear()
                # Tính toán lại kích thước hiển thị
                cell_size = int(min(board_area_width / N, board_area_height / M))
                board_width = cell_size * N
                board_height = cell_size * M
                board_origin = (BOARD_PADDING, (height - board_height) // 2)
                # Cập nhật vị trí các nút bên phải
                right_panel_left = board_origin[0] + board_width + 2 * BOARD_PADDING
                # Cập nhật vị trí các nút kích thước
                size_button_10x10 = pygame.Rect(right_panel_left, size_buttons_top, SIZE_BUTTON_WIDTH, SIZE_BUTTON_HEIGHT)
                size_button_20x20 = pygame.Rect(right_panel_left + SIZE_BUTTON_WIDTH + SIZE_BUTTON_SPACING, size_buttons_top, SIZE_BUTTON_WIDTH, SIZE_BUTTON_HEIGHT)
                size_button_50x50 = pygame.Rect(right_panel_left + 2 * (SIZE_BUTTON_WIDTH + SIZE_BUTTON_SPACING), size_buttons_top, SIZE_BUTTON_WIDTH, SIZE_BUTTON_HEIGHT)
        # Nếu nhấp vào nút kích thước 20x20
        elif size_button_20x20.collidepoint(mouse):
            if selected_size != "20x20":
                selected_size = "20x20"
                N = M = 20
                P0 = (0, 0)
                P1 = (N-1, M-1)
                # Tạo mê cung mới với kích thước 20x20
                maze = Maze(N, M, P0, P1)
                maze.generate()
                maze.explore = []
                maze.solution = []
                algo_results.clear()
                # Tính toán lại kích thước hiển thị
                cell_size = int(min(board_area_width / N, board_area_height / M))
                board_width = cell_size * N
                board_height = cell_size * M
                board_origin = (BOARD_PADDING, (height - board_height) // 2)
                # Cập nhật vị trí các nút bên phải
                right_panel_left = board_origin[0] + board_width + 2 * BOARD_PADDING
                # Cập nhật vị trí các nút kích thước
                size_button_10x10 = pygame.Rect(right_panel_left, size_buttons_top, SIZE_BUTTON_WIDTH, SIZE_BUTTON_HEIGHT)
                size_button_20x20 = pygame.Rect(right_panel_left + SIZE_BUTTON_WIDTH + SIZE_BUTTON_SPACING, size_buttons_top, SIZE_BUTTON_WIDTH, SIZE_BUTTON_HEIGHT)
                size_button_50x50 = pygame.Rect(right_panel_left + 2 * (SIZE_BUTTON_WIDTH + SIZE_BUTTON_SPACING), size_buttons_top, SIZE_BUTTON_WIDTH, SIZE_BUTTON_HEIGHT)
        # Nếu nhấp vào nút kích thước 50x50
        elif size_button_50x50.collidepoint(mouse):
            if selected_size != "50x50":
                selected_size = "50x50"
                N = M = 50
                P0 = (0, 0)
                P1 = (N-1, M-1)
                # Tạo mê cung mới với kích thước 50x50
                maze = Maze(N, M, P0, P1)
                maze.generate()
                maze.explore = []
                maze.solution = []
                algo_results.clear()
                # Tính toán lại kích thước hiển thị
                cell_size = int(min(board_area_width / N, board_area_height / M))
                board_width = cell_size * N
                board_height = cell_size * M
                board_origin = (BOARD_PADDING, (height - board_height) // 2)
                # Cập nhật vị trí các nút bên phải
                right_panel_left = board_origin[0] + board_width + 2 * BOARD_PADDING
                # Cập nhật vị trí các nút kích thước
                size_button_10x10 = pygame.Rect(right_panel_left, size_buttons_top, SIZE_BUTTON_WIDTH, SIZE_BUTTON_HEIGHT)
                size_button_20x20 = pygame.Rect(right_panel_left + SIZE_BUTTON_WIDTH + SIZE_BUTTON_SPACING, size_buttons_top, SIZE_BUTTON_WIDTH, SIZE_BUTTON_HEIGHT)
                size_button_50x50 = pygame.Rect(right_panel_left + 2 * (SIZE_BUTTON_WIDTH + SIZE_BUTTON_SPACING), size_buttons_top, SIZE_BUTTON_WIDTH, SIZE_BUTTON_HEIGHT)
        else:
            if any([
                AstarButton.collidepoint(mouse),
                GreedyButton.collidepoint(mouse),
                DFSButton.collidepoint(mouse),
                BFSButton.collidepoint(mouse)
            ]):
                end=True

    pygame.display.flip()
