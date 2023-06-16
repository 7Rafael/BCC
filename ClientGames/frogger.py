import pygame, sys, os
from pygame.locals import *
from button import Button
from pathlib import Path


pygame.init()
def get_file_path(name):
    currentPath = os.getcwd()
    absolutePath = os.path.join(currentPath, "assets/", name)
    absolutePath = Path(absolutePath)
    return absolutePath
pygame.mixer.init()
clock = pygame.time.Clock()

pygame.time.wait(1000)
#1280, 720
width =1280 #800
height =720 #600
speed = 0.6
playerSpeed = 5
win = 0
red = (255, 0, 0)
select_color = (60, 130, 210)
color_hover = (255, 255, 0)

BG = pygame.image.load(get_file_path("Background.png"))

confirmSound = pygame.mixer.Sound(get_file_path('8bit_kill_vo_01.ogg'))
confirmSound.set_volume(0.01)

pygame.mixer.music.load(get_file_path("Eric Skiff- Underclocked.mp3"))
pygame.mixer.music.set_volume(0)
pygame.mixer.music.play(-1)

player = pygame.image.load(get_file_path("chicken.png"))
player = pygame.transform.scale(player, (62, 50))
colliderPlayer = player.get_rect()

car = pygame.image.load(get_file_path("car.png"))
car = pygame.transform.scale(car, (62, 96))
car = pygame.transform.rotate(car, (-90))
colliderCar = car.get_rect()

car2 = pygame.image.load(get_file_path("car.png"))
car2 = pygame.transform.scale(car2, (62, 96))
car2 = pygame.transform.rotate(car2, (-90))
colliderCar2 = car2.get_rect()

car3 = pygame.image.load(get_file_path("car.png"))
car3 = pygame.transform.scale(car3, (62, 96))
car3 = pygame.transform.rotate(car3, (-90))
colliderCar3 = car3.get_rect()

carR = pygame.image.load(get_file_path("car.png"))
carR = pygame.transform.scale(carR, (62, 96))
carR = pygame.transform.rotate(carR, (90))
colliderCarR = carR.get_rect()

carR2 = pygame.image.load(get_file_path("car.png"))
carR2 = pygame.transform.scale(carR2, (62, 96))
carR2 = pygame.transform.rotate(carR2, (90))
colliderCarR2 = carR2.get_rect()

carR3 = pygame.image.load(get_file_path("car.png"))
carR3 = pygame.transform.scale(carR3, (62, 96))
carR3 = pygame.transform.rotate(carR3, (90))
colliderCarR3 = carR3.get_rect()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Frogger")

bg = pygame.image.load(get_file_path("BackgroundFrogger.png"))
bg = pygame.transform.scale(bg, (width, height))

def check_win():
    global playerSpeed, win
    if colliderPlayer.y == 0:
        win += 1
        start_game()
def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font(get_file_path("font.ttf"), size)
def start_game():
    global colliderPlayer,colliderCar, colliderCar2, playerSpeed, win
    Run = True
    width_element = 50
    height_element = 50
    colliderPlayer.y = height
    colliderPlayer.x = width/2
    while Run:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            colliderPlayer.y -= playerSpeed
        if keys[pygame.K_DOWN]:
            colliderPlayer.y += playerSpeed
        if keys[pygame.K_LEFT]:
            colliderPlayer.x -= playerSpeed
        if keys[pygame.K_RIGHT]:
            colliderPlayer.x += playerSpeed
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                exit()
        screen.blit(bg, (0, 0))
        # Limitar a posição horizontal do avatar
        if colliderPlayer.x < 0:
            colliderPlayer.x = 0
        elif colliderPlayer.x > width - width_element:
            colliderPlayer.x = width - width_element
        # Limitar a posição vertical do avatar
        if colliderPlayer.y < 0:
            colliderPlayer.y = 0
        elif colliderPlayer.y > height - height_element:
            colliderPlayer.y = height - height_element
        screen.blit(player, colliderPlayer)
        screen.blit(car, colliderCar)
        screen.blit(car2, colliderCar2)
        screen.blit(car3, colliderCar3)
        screen.blit(carR, colliderCarR)
        screen.blit(carR2, colliderCarR2)
        screen.blit(carR3, colliderCarR3)

        #set values y of each car
        colliderCarR.y = 85
        colliderCarR2.y = 170
        colliderCarR3.y = 255

        colliderCar.y = 400
        colliderCar2.y = 485
        colliderCar3.y = 570

        #set speed for each car
        colliderCarR.x -= 8
        colliderCarR3.x -= 10
        colliderCarR2.x -= 5
        colliderCar.x += 6
        colliderCar2.x += 10
        colliderCar3.x += 12

        if colliderPlayer.colliderect(colliderCar) or colliderPlayer.colliderect(colliderCar2)  or colliderPlayer.colliderect(colliderCar3) or colliderPlayer.colliderect(colliderCarR) or colliderPlayer.colliderect(colliderCarR2) or colliderPlayer.colliderect(colliderCarR3):
            win = 0
            main()
        if colliderCar.x >= width:
            colliderCar.x = 0
        if colliderCar2.x >= width:
            colliderCar2.x = 0
        if colliderCar3.x >= width:
            colliderCar3.x = 0
        if colliderCarR.x <= 0:
            colliderCarR.x = 1280
        if colliderCarR2.x <= 0:
            colliderCarR2.x = 1280
        if colliderCarR3.x <= 0:
            colliderCarR3.x = 1280
        win_text = get_font(20).render(f"{win}", True, "Red")
        win_rect = win_text.get_rect(center=(20, 20))
        screen.blit(win_text, win_rect)
        check_win()
        pygame.display.update()
        clock.tick(60)
def exit_game():
    pygame.quit()
    exit()
def main():
    while True:

        screen.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("Frogger", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load(get_file_path("Play Rect.png")), pos=(640, 250),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="#b68f40")
        QUIT_BUTTON = Button(image=pygame.image.load(get_file_path("Quit Rect.png")), pos=(640, 400),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="#b68f40")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    start_game()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
main()
pygame.quit()
exit()
