import pygame
import sys
from button import Button

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 800
LINE_WIDTH = 15

BG = pygame.image.load("assets/Background.png")
# Colors
BLACK = (0, 0, 0)
WHITE = (111, 111, 111)
RED = (255, 0, 0)
# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
run = True
boardSize = 9

# Variable to keep track of the current player
current_player = "X"
gameHasStarted = False
SQUARE_SIZE = WIDTH // boardSize
# Initialize the game board
board = [[None] * boardSize for _ in range(boardSize)]

def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

# Function to draw the game board
def draw_board():
    global SQUARE_SIZE  # Declare SQUARE_SIZE as a global variable
    screen.fill(BLACK)
    SQUARE_SIZE = WIDTH // boardSize
    for row in range(boardSize):
        for col in range(boardSize):
            pygame.draw.rect(screen, WHITE, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), LINE_WIDTH)
            if board[row][col] is not None:
                font = pygame.font.Font(None, 150)
                text = font.render(board[row][col], True, WHITE)
                text_rect = text.get_rect(center=(col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2))
                screen.blit(text, text_rect)


# Function to handle player's move
def make_move(row, col):
    if gameHasStarted and board[row][col] is None:
        board[row][col] = current_player
        draw_board()
        check_winner()
        toggle_player()

# Function to toggle the current player
def toggle_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

# Function to check if there's a winner or a draw
def check_winner():
    # Check rows
    for row in range(boardSize):
        if all(board[row][col] == current_player for col in range(boardSize)):
            show_winner(current_player)

    # Check columns
    for col in range(boardSize):
        if all(board[row][col] == current_player for row in range(boardSize)):
            show_winner(current_player)

    # Check diagonals
    if all(board[i][i] == current_player for i in range(boardSize)):
        show_winner(current_player)
    if all(board[i][boardSize - i - 1] == current_player for i in range(boardSize)):
        show_winner(current_player)

    # Check for a draw
    if all(board[row][col] is not None for row in range(boardSize) for col in range(boardSize)):
        show_winner(None, is_draw=True)

# Function to display the winner or a draw
def show_winner(player, is_draw=False):
    if is_draw:
        message = "It's a draw!"
    else:
        message = f"Player {player} wins!"
    font = pygame.font.Font(None, 80)
    text = font.render(message, True, RED)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(3000)
    reset_game()

# Function to reset the game
def reset_game():
    global board, current_player
    board = [[None] * boardSize for _ in range(boardSize)]
    current_player = "X"
    draw_board()

while run:
    if gameHasStarted == False:
        TIC_MOUSE_POS = pygame.mouse.get_pos()
        screen.fill("black")
        EXTRA_TEXT = get_font(40).render("board size", True, "white")
        EXTRA_RECT = EXTRA_TEXT.get_rect(center=(400, 50))
        screen.blit(EXTRA_TEXT, EXTRA_RECT)
        SIZE3 = Button(image=None, pos=(100, 160),
                       text_input="size 3", font=get_font(12), base_color="White", hovering_color="Green")
        SIZE3.changeColor(TIC_MOUSE_POS)
        SIZE3.update(screen)
        SIZE5 = Button(image=None, pos=(200, 160),
                       text_input="size 5", font=get_font(12), base_color="White", hovering_color="Green")
        SIZE5.changeColor(TIC_MOUSE_POS)
        SIZE5.update(screen)
        SIZE7 = Button(image=None, pos=(300, 160),
                       text_input="size 7", font=get_font(12), base_color="White", hovering_color="Green")
        SIZE7.changeColor(TIC_MOUSE_POS)
        SIZE7.update(screen)
        SIZE9 = Button(image=None, pos=(400, 160),
                       text_input="size 9", font=get_font(12), base_color="White", hovering_color="Green")
        SIZE9.changeColor(TIC_MOUSE_POS)
        SIZE9.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.type == pygame.QUIT:
                    gameHasStarted = True
                    pygame.quit()
                    sys.exit()
                elif SIZE3.checkForInput(TIC_MOUSE_POS):
                    gameHasStarted = True
                    boardSize = 3
                    SQUARE_SIZE = WIDTH // boardSize
                    draw_board()
                elif SIZE5.checkForInput(TIC_MOUSE_POS):
                    gameHasStarted = True
                    boardSize = 5
                    draw_board()
                elif SIZE7.checkForInput(TIC_MOUSE_POS):
                    gameHasStarted = True
                    boardSize = 7
                    SQUARE_SIZE = WIDTH // boardSize
                    draw_board()
                elif SIZE9.checkForInput(TIC_MOUSE_POS):
                    gameHasStarted = True
                    boardSize = 9
                    SQUARE_SIZE = WIDTH // boardSize
                    draw_board()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            clicked_row = mouse_pos[1] // SQUARE_SIZE
            clicked_col = mouse_pos[0] // SQUARE_SIZE

            make_move(clicked_row, clicked_col)

    pygame.display.update()
