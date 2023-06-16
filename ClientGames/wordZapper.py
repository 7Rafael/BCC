import string
import pygame
from pygame import *
from sys import exit
import os
from pathlib import Path
import random
import time


countdown_duration = 99

def restartGame():
    global playing, chosenWord, wordLength, wordLetters, countdown_duration, countingLetter
    player.return_to_start()
    playing = False
    countingLetter = True
    chosenWord = choose_word()
    wordLength = 0
    width = (wordLettersFontWidth + 10) * len(chosenWord)
    xCurrentLetterRectangle = int(400 - width / 2)
    wordLetters.clear()
    for i in range(len(chosenWord)):
        wordLetters.append(Letter(chosenWord[i], wordLettersFont, xCurrentLetterRectangle, 500,
                                 wordLettersFontWidth, wordLettersFontHeight))
        xCurrentLetterRectangle += (wordLettersFontWidth + 10)


class Player(pygame.sprite.Sprite):
    def __init__(self, initial_position_x, initial_position_y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.ship = pygame.image.load(get_file_path("Ship1.png"))
        self.rect = pygame.Rect(initial_position_x, initial_position_y, self.ship.get_width(), self.ship.get_height())
        self.rect.topleft = initial_position_x, initial_position_y
        self.speed = speed
        self.shot_fired = False

    def move(self):
        window.blit(self.ship, self.rect)

        if pygame.key.get_pressed()[K_a]:
            self.rect.x -= self.speed
            if self.rect.x < -5:
                self.rect.x += self.speed

        if pygame.key.get_pressed()[K_d]:
            self.rect.x += self.speed
            if self.rect.x >= 760:
                self.rect.x -= self.speed

        if pygame.key.get_pressed()[K_s]:
            self.rect.y += self.speed
            if self.rect.y >= 425:
                self.rect.y -= self.speed

        if pygame.key.get_pressed()[K_w]:
            self.rect.y -= self.speed
            if self.rect.y < 150:
                self.rect.y += self.speed
    def return_to_start(self):
        self.rect.x = 380
        self.rect.y = 400
    def shoot(self):
        if pygame.key.get_pressed()[K_SPACE] and not self.shot_fired:
            shot = Shot(self.rect.center[0], self.rect.top)
            shotGroup.add(shot)
            self.shot_fired = True
        elif not pygame.key.get_pressed()[K_SPACE]:
            self.shot_fired = False
class Shot(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.image.load(get_file_path("tiro.png"))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
    def update(self):
        global options_list, chosenWord, wordLength, wordLetters, play
        self.rect.y -= 10
        for i in range(26):

            if self.rect.colliderect(options_list[i].rectangle) and not options_list[i].collided:
                self.kill()
                options_list[i].color = (48, 32, 152)

                options_list[i].collided = True
                if options_list[i].letter == chosenWord[wordLength].capitalize():

                    for letter in range(len(chosenWord)):
                        if chosenWord[letter] == options_list[i].letter:

                            wordLetters[letter].letter = options_list[i].letter
                    wordLength += 1
                    if len(chosenWord) == wordLength:
                        restartGame()

        if self.rect.y < 0:
            self.kill()

class Button():
    def __init__(self, text, x, y, width, height, function):
        self.clicked = False

        self.container_rectangle = pygame.Rect(x, y, width, height)
        self.button_color = (100, 100, 100)

        self.text = textFont.render(text, True, (255, 255, 255))
        self.text_rectangle = self.text.get_rect(
            center=(self.container_rectangle.centerx, self.container_rectangle.centery))

        self.function = function
    def draw_button(self):
        pygame.draw.rect(window, self.button_color, self.container_rectangle, border_radius=10)
        window.blit(self.text, self.text_rectangle)
    def click(self):
        mouse = pygame.mouse.get_pos()

        if self.container_rectangle.collidepoint(mouse):

            self.buttonColor = (55, 55, 55)

        # Check if left mouse button is pressed
        if pygame.mouse.get_pressed()[0]:
            # Indicates that the button is clicked, and a boolean value is assigned to this variable
            self.clicked = True
        # When the above condition is no longer true, i.e., the player has released the button, then the boolean value is set to false by default, and the action is executed
        else:
            # This is done to prevent the action from being executed multiple times if there are a large number of frames in the game, which can impact the performance on certain devices
            if self.clicked == True:
                self.clicked = False
                self.function()
            else:
                self.buttonColor = (100, 100, 100)
class Alphabet():
    def __init__(self, letter, fontLetter, rectangle, speed, fontWidth, fontHeight):
        self.letter = letter
        self.fontLetter = fontLetter
        self.rectangle = rectangle
        self.speed = speed
        self.fontWidth = fontWidth
        self.fontHeight = fontHeight
        self.color = (255, 255, 255)
        self.collided = False

    def draw_moving_list(self):
        letterSurface = self.fontLetter.render(self.letter, True, self.color)
        window.blit(letterSurface, self.rectangle)
        self.rectangle.x -= self.speed*0.7
        if self.rectangle.x < 0:
            self.rectangle.x = 1700
            self.color = (255, 255, 255)
            self.collided = False
class Letter():
    def __init__(self, letter, usedFont, x, y, fontWidth, fontHeight):
        self.letter = letter
        self.usedFont = usedFont
        self.x = x
        self.y = y
        self.fontWidth = fontWidth
        self.fontHeight = fontHeight
        self.color = (255, 255, 255)
    def draw_letters(self):
        rectangle = pygame.draw.rect(window, (255, 0, 0), (self.x, 500, self.fontWidth, self.fontHeight))
        letterSurface = self.usedFont.render(self.letter, True, self.color)
        xLetter = rectangle.centerx - letterSurface.get_width() // 2
        yLetter = rectangle.centery - letterSurface.get_height() // 2

        # Draw the letter at the correct position
        window.blit(letterSurface, (xLetter, yLetter))
def draw_container_rectangle():
    pygame.draw.rect(window, (21, 0, 80), (25, 475, 750, 100), border_radius=90)
def get_file_path(name):
    currentPath = os.getcwd()
    absolutePath = os.path.join(currentPath, "assets/", name)
    absolutePath = Path(absolutePath)
    return absolutePath

def write_text(text, font, textColor, positionX, positionY):
    writtenText = font.render(text, True, textColor)
    window.blit(writtenText, (positionX, positionY))

def play_game():
    global playing
    playing = True

def choose_word():
    with open(get_file_path("words.txt"), encoding="utf-8") as file:  # Read the file in "utf-8" format
        words = file.readlines()  # Read each line of the file and store them in a list
        words = list(map(str.strip, words))  # Remove possible leading and trailing whitespaces from the list
        chosenWord = random.choice(words).upper()  # Standardize the chosen word to have all uppercase letters
        print(chosenWord)
    return chosenWord

if __name__ == "__main__":

    pygame.init()
    pygame.font.init()
    window = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Word Zapper")
    clock = pygame.time.Clock()

    titleFont = pygame.font.SysFont("arialblack", 30)
    textFont = pygame.font.SysFont("arialblack", 20)

    alphabetFont = pygame.font.SysFont("arialblack", 40)
    wordLettersFont = pygame.font.SysFont("arialblack", 40)

    alphabetFontWidth = alphabetFont.size("Tg")[0]
    alphabetFontHeight = alphabetFont.size("Tg")[1]

    wordLettersFontWidth = wordLettersFont.size("Tg")[0]
    wordLettersFontHeight = wordLettersFont.size("Tg")[1]

    scenario = pygame.image.load(get_file_path("Background.png"))
    scenario = pygame.transform.scale(scenario, (800, 600))

    playButton = Button("play", 250, 150, 300, 50, play_game)

    shotGroup = pygame.sprite.Group()
    alphabetList = list(string.ascii_uppercase)
    rectangleList = []
    xContainerRectangles = 100

    for i in range(26):
        rectangleList.append(pygame.Rect(xContainerRectangles, 100, alphabetFontWidth, alphabetFontHeight))
        xContainerRectangles += 65

    options_list = []
    wordLength = 0

    for i in range(26):
        options_list.append(
            Alphabet(alphabetList[i], alphabetFont, rectangleList[i], 5, alphabetFontWidth, alphabetFontHeight))

    player = Player(370, 400, 5)
    play = True
    playing = False
    chosenWord = choose_word()
    width = (wordLettersFontWidth + 10) * len(chosenWord)
    xCurrentLetterRectangle = int(400 - width / 2)
    backup = xCurrentLetterRectangle
    wordLetters = []

    for i in range(len(chosenWord)):
        wordLetters.append(Letter(chosenWord[i], wordLettersFont, xCurrentLetterRectangle, 500,
                                 wordLettersFontWidth, wordLettersFontHeight))
        xCurrentLetterRectangle += (wordLettersFontWidth + 10)
    countingLetter = True
    while play:
        clock.tick(100)
        window.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
                exit()

        if playing:
            time = pygame.time.get_ticks()
            if countingLetter:
                if time > 3000:
                    for i in range(len(chosenWord)):
                        wordLetters[i].letter = "_"
                        countingLetter = False


            time_elapsed = pygame.time.get_ticks()  # Get the time elapsed in milliseconds
            countdown = int((countdown_duration - time_elapsed / 1000) + 1)  # Calculate the countdown in seconds
            if countdown <= 0:
                restartGame()
            else:
                # Display the countdown on the screen
                countdown_text = f"Time left: {countdown}"
                write_text("countdown_text", textFont, (255, 255, 255), 100, 100)
            window.fill((48, 32, 152))
            for i in range(26):
                options_list [i].draw_moving_list()

            draw_container_rectangle()

            for i in range(len(chosenWord)):
                wordLetters[i].draw_letters()
            player.move()
            player.shoot()
            shotGroup.draw(window)
            shotGroup.update()

        else:
            play_game()

        pygame.display.update()

    pygame.quit()
