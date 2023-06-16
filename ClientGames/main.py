import pygame, sys, os
from button import Button
from pathlib import Path

pygame.init()
clock = pygame.time.Clock()
def get_file_path(name):
    currentPath = os.getcwd()
    absolutePath = os.path.join(currentPath, "assets/", name)
    absolutePath = Path(absolutePath)
    return absolutePath
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")
BG = pygame.image.load(get_file_path("Background.png"))
confirmSound = pygame.mixer.Sound(get_file_path("8bit_kill_vo_01.ogg"))
confirmSound.set_volume(.5)

pygame.mixer.music.load(get_file_path("Night_Shade.mp3"))
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
class boardSize:
    sizeBoard = 0

    def tictacSize(self):
        while True:
            TIC_MOUSE_POS = pygame.mouse.get_pos()
            SCREEN.fill("black")

            EXTRA_TEXT = get_font(45).render("board size.", True, "white")
            EXTRA_RECT = EXTRA_TEXT.get_rect(center=(640, 50))
            SCREEN.blit(EXTRA_TEXT, EXTRA_RECT)

            SIZE3 = Button(image=None, pos=(300, 160),
                           text_input="size 3", font=get_font(30), base_color="White", hovering_color="Green")

            SIZE3.changeColor(TIC_MOUSE_POS)
            SIZE3.update(SCREEN)

            SIZE5 = Button(image=None, pos=(600, 160),
                           text_input="size 5", font=get_font(30), base_color="White", hovering_color="Green")

            SIZE5.changeColor(TIC_MOUSE_POS)
            SIZE5.update(SCREEN)

            SIZE7 = Button(image=None, pos=(900, 160),
                           text_input="size 7", font=get_font(30), base_color="White", hovering_color="Green")
            SIZE7.changeColor(TIC_MOUSE_POS)
            SIZE7.update(SCREEN)

            SIZE9 = Button(image=None, pos=(1200, 160),
                           text_input="size 9", font=get_font(30), base_color="White", hovering_color="Green")
            SIZE9.changeColor(TIC_MOUSE_POS)
            SIZE9.update(SCREEN)

            EXTRA_BACK = Button(image=None, pos=(640, 640),
                                text_input="Voltar", font=get_font(45), base_color="white", hovering_color="Green")

            EXTRA_BACK.changeColor(TIC_MOUSE_POS)
            EXTRA_BACK.update(SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if SIZE3.checkForInput(TIC_MOUSE_POS):
                        sizeBoard = 3
                        print(boardSize)
                    if SIZE5.checkForInput(TIC_MOUSE_POS):
                        sizeBoard = 5
                        print(boardSize)
                    if SIZE7.checkForInput(TIC_MOUSE_POS):
                        sizeBoard = 7
                        print(boardSize)
                    if SIZE9.checkForInput(TIC_MOUSE_POS):
                        sizeBoard = 9
                        print(boardSize)

            pygame.display.update()


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font(get_file_path("font.ttf"), size)




def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(BG, (0, 0))

        PLAY_TEXT = get_font(45).render("Escolha o jogo", True, "Red")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 50))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 640),
                           text_input="Voltar", font=get_font(30), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        PLAY_GAME = Button(image=None, pos=(300, 160),
                           text_input="TicTac", font=get_font(30), base_color="White", hovering_color="Green")

        PLAY_GAME.changeColor(PLAY_MOUSE_POS)
        PLAY_GAME.update(SCREEN)

        PLAY_GAME2 = Button(image=None, pos=(600, 160),
                           text_input="Frogger", font=get_font(30), base_color="White", hovering_color="Green")

        PLAY_GAME2.changeColor(PLAY_MOUSE_POS)
        PLAY_GAME2.update(SCREEN)

        PLAY_GAME3 = Button(image=None, pos=(900, 160),
                           text_input="WordZapper", font=get_font(30), base_color="White", hovering_color="Green")

        PLAY_GAME3.changeColor(PLAY_MOUSE_POS)
        PLAY_GAME3.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu() #aqui vai rodar o .py do jogo
                if PLAY_GAME.checkForInput(PLAY_MOUSE_POS):
                    pygame.mixer.music.stop()
                    confirmSound.play()
                    tictactoe()
                if PLAY_GAME2.checkForInput(PLAY_MOUSE_POS):
                    pygame.mixer.music.stop()
                    confirmSound.play()
                    import frogger
                if PLAY_GAME3.checkForInput(PLAY_MOUSE_POS):
                    pygame.mixer.music.stop()
                    confirmSound.play()
                    import wordZapper

        pygame.display.update()

def help():
    helptext = ""
    while True:

        HELP_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        game1 = Button(image=None, pos=(300, 60),
                       text_input="Tictac", font=get_font(20), base_color="White", hovering_color="Green")

        game1.changeColor(HELP_MOUSE_POS)
        game1.update(SCREEN)

        game2 = Button(image=None, pos=(600, 60),
                       text_input="Frogger", font=get_font(20), base_color="White", hovering_color="Green")

        game2.changeColor(HELP_MOUSE_POS)
        game2.update(SCREEN)

        game3 = Button(image=None, pos=(900, 60),
                       text_input="WordZapper", font=get_font(20), base_color="White", hovering_color="Green")
        game3.changeColor(HELP_MOUSE_POS)
        game3.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if game1.checkForInput(HELP_MOUSE_POS):
                    helptext = "Como jogar jogo da velha"
                if game2.checkForInput(HELP_MOUSE_POS):
                    helptext = "O objetico do frogger é fazer \n galinha atravessar a rua"
                if game3.checkForInput(HELP_MOUSE_POS):
                    helptext = "Como jogar wordZapper"

        HELP_TEXT = get_font(25).render(f"{helptext}", True, "green")
        HELP_RECT = HELP_TEXT.get_rect(center=(640, 320))
        SCREEN.blit(HELP_TEXT, HELP_RECT)

        HELP_BACK = Button(image=None, pos=(640, 640),
                              text_input="Voltar", font=get_font(45), base_color="white", hovering_color="Green")

        HELP_BACK.changeColor(HELP_MOUSE_POS)
        HELP_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if HELP_BACK.checkForInput(HELP_MOUSE_POS):
                    main_menu()
        clock.tick(60)
        pygame.display.update()

def main_menu():
    while True:

        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load(get_file_path("Play Rect.png")), pos=(640, 250),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="#b68f40")
        HELP_BUTTON = Button(image=pygame.image.load(get_file_path("Options Rect.png")), pos=(640, 400),
                                text_input="HELP", font=get_font(75), base_color="#d7fcd4", hovering_color="#b68f40")
        QUIT_BUTTON = Button(image=pygame.image.load(get_file_path("Quit Rect.png")), pos=(640, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="#b68f40")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, HELP_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if HELP_BUTTON.checkForInput(MENU_MOUSE_POS):
                    help()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        clock.tick(60)
        pygame.display.update()


main_menu()
