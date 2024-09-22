import pygame

def update_screen():
    pygame.display.flip()

# Constants
BG_COLOR = pygame.Color(255, 255, 255, 255)
black = (0, 0, 0)
WIDTH = 480
HEIGHT = 480
block_size = 160

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")
screen.fill(BG_COLOR)

def drawGrid():
    for x in range(block_size, WIDTH, block_size):
        pygame.draw.line(screen, black, (x, 0), (x, HEIGHT), 2)
    for y in range(block_size, HEIGHT, block_size):
        pygame.draw.line(screen, black, (0, y), (WIDTH, y), 2)

def draw_marker(marker, row, col):
    font = pygame.font.Font(None, 120)  
    text = font.render(marker, True, black)
    text_rect = text.get_rect(center=((col * block_size + block_size // 2), (row * block_size + block_size // 2)))
    screen.blit(text, text_rect)

def get_grid_pos(mouse_pos):
    x, y = mouse_pos
    row = y // block_size
    col = x // block_size
    return row, col

def check_winner():
    for row in range(3):
        if grid[row][0] == grid[row][1] == grid[row][2] != "":
            return grid[row][0]  # Row winner
    for col in range(3):
        if grid[0][col] == grid[1][col] == grid[2][col] != "":
            return grid[0][col]  # Column winner
    if grid[0][0] == grid[1][1] == grid[2][2] != "":
        return grid[0][0]  # Diagonal winner
    if grid[0][2] == grid[1][1] == grid[2][0] != "":
        return grid[0][2]  # Diagonal winner
    return None

def reset_game():
    global grid, current_turn
    screen.fill(BG_COLOR) 
    drawGrid()  
    grid = [["" for _ in range(3)] for _ in range(3)]  
    current_turn = "X"  

grid = [["" for _ in range(3)] for _ in range(3)]  
current_turn = "X"  

drawGrid()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            row, col = get_grid_pos(mouse_pos)

            if grid[row][col] == "":
                grid[row][col] = current_turn
                draw_marker(current_turn, row, col)

                winner = check_winner()
                if winner:
                    print(f"{winner} wins!")
                    pygame.time.wait(2000) 
                    reset_game()
                    
                current_turn = "O" if current_turn == "X" else "X"

    update_screen()
