import pygame
from pygame.locals import *

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

width = 800
height = 600
speed = 0.6
playerSpeed = 0.6

red = (255, 0, 0)
select_color = (60, 130, 210)
color_hover = (255, 255, 0)

player = pygame.image.load("assets/chicken.png")
player = pygame.transform.scale(player, (50, 50))
colliderPlayer = player.get_rect()

car = pygame.image.load("assets/car.png")
car = pygame.transform.scale(car, (62, 96))
car = pygame.transform.rotate(car, (-90))
colliderCar = car.get_rect()

car1 = pygame.image.load("assets/car.png")
car1 = pygame.transform.scale(car1, (62, 96))
car1 = pygame.transform.rotate(car1, (90))
colliderCar1 = car.get_rect()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Frogger")

bg = pygame.image.load("assets/BackgroundFrogger.png")
bg = pygame.transform.scale(bg, (width, height))

#pygame.draw.rect(car, (0, 0, 0), colliderCar, 4)
#pygame.draw.rect(car1, (0, 0, 0), colliderCar1, 4)
#pygame.draw.rect(player, (255, 0, 0), colliderPlayer, 4)
class Button:
    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
        self.rect = pygame.Rect(pos[0] - 75, pos[1] - 25, 150, 50)
        self.select = False

    def draw(self):
        if self.select:
            pygame.draw.rect(screen, select_color, self.rect)
        else:
            pygame.draw.rect(screen, red, self.rect)

        font = self.font = pygame.font.Font("assets/font.ttf", 24)
        text_render = self.font.render(self.text, True, (255, 255, 255))
        text_pos = text_render.get_rect(center=self.pos)
        screen.blit(text_render, text_pos)

button_start = Button("Start", (width // 2, height // 2 - 50))
button_exit = Button("Exit", (width // 2, height // 2 + 50))
pygame.display.update()

def start_game(carX, carX2):
    global colliderCar1,colliderPlayer,colliderCar
    Run = True

    width_element = 50
    height_element = 50
    carX2 = 690

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

        screen.fill((0, 0, 0))
        screen.blit(bg, (0, 0))

        # Limitar a posição horizontal do avatar

        if colliderPlayer.x < 0:
            colliderPlayer.x = 0
        elif colliderPlayer.x > width - width_element:
            colliderPlayer.x = width - width_element

        # Limitar a posição vertical do avatar
        if colliderPlayer.y < 0:
            colliderPlayer.y= 0
        elif colliderPlayer.y > height - height_element:
            colliderPlayer.y = height - height_element

        screen.blit(player, colliderPlayer)
        screen.blit(car, (colliderCar.x , 60))
        colliderCar.x += speed

        carz = screen.blit(car1, colliderCar1)
        colliderCar1.x -= speed
        #screen.blit(car, (carX, 400))
        #screen.blit(car, (carX, 475))
        #screen.blit(car, (carX, 330))
        #screen.blit(car1, (carX2, 210))
        #screen.blit(car1, (carX2, 135))
        #screen.blit(car1, (carX2, 60))
        if colliderPlayer.colliderect(colliderCar):
           print("Bateu")
        if colliderCar.x == width:
            colliderCar.x = 0
        if colliderCar1.x == 0:
            colliderCar1.x = 800

        carX += speed
        carX2 -= speed
        pygame.draw.rect(screen, (0, 0, 0), colliderCar, 4)
        pygame.display.update()
def exit_game():
    pygame.quit()
    exit()

def main():
    menuOn = True
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                exit_game()
            elif event.type == MOUSEBUTTONDOWN:
                if menuOn:
                    if button_start.rect.collidepoint(event.pos):
                        menuOn = False
                        pygame.mixer.music.stop()
                        start_game(speed, speed)

                    elif button_exit.rect.collidepoint(event.pos):
                        exit_game()
            if event.type == MOUSEMOTION:
                if button_start.rect.collidepoint(event.pos):
                    button_start.select = True
                else:
                    button_start.select = False

                if button_exit.rect.collidepoint(event.pos):
                    button_exit.select = True
                else:
                    button_exit.select = False
        screen.fill((0, 0, 0))
        if menuOn:
            button_start.draw()
            button_exit.draw()
        pygame.display.update()
main()
pygame.quit()
exit()
