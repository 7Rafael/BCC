import pygame, sys
from button import Button

print("Rodou")
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tic Tac Toe")
run = True
line_width = 6
lines = 9
def draw_Grid():
    bg =(255, 255, 200)
    grid = (50, 50, 50)
    screen.fill(bg)
    for x in range(1,lines):
        pygame.draw.line(screen, grid, (0, x*(screen_height/lines)), (screen_width, x*screen_height/lines),line_width)
        pygame.draw.line(screen, grid, ( x * (screen_width/lines), 0), (x * (screen_width/lines), screen_height),line_width)
while run:
    draw_Grid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            import main
            run = False

    pygame.display.update()