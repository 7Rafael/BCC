import pygame, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")
confirmSound = pygame.mixer.Sound('assets/8bit_kill_vo_01.ogg')
confirmSound.set_volume(0.01)

pygame.mixer.music.load("assets/Night_Shade.mp3")
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play()
def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)


def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")


        PLAY_TEXT = get_font(45).render("Escolha o jogo", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 50))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 640),
                           text_input="Voltar", font=get_font(45), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)


        PLAY_GAME = Button(image=None, pos=(300, 160),
                           text_input="GAME", font=get_font(45), base_color="White", hovering_color="Green")

        PLAY_GAME.changeColor(PLAY_MOUSE_POS)
        PLAY_GAME.update(SCREEN)

        PLAY_GAME2 = Button(image=None, pos=(600, 160),
                           text_input="GAME", font=get_font(45), base_color="White", hovering_color="Green")

        PLAY_GAME2.changeColor(PLAY_MOUSE_POS)
        PLAY_GAME2.update(SCREEN)

        PLAY_GAME3 = Button(image=None, pos=(900, 160),
                           text_input="GAME", font=get_font(45), base_color="White", hovering_color="Green")

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
                    import tictactoe
                if PLAY_GAME2.checkForInput(PLAY_MOUSE_POS):
                    pygame.mixer.music.stop()
                    confirmSound.play()
                    main_menu() #aqui vai rodar o .py do jogo
                if PLAY_GAME3.checkForInput(PLAY_MOUSE_POS):
                    pygame.mixer.music.stop()
                    confirmSound.play()
                    main_menu() #aqui vai rodar o .py do jogo

        pygame.display.update()


def extra():
    while True:
        EXTRA_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        EXTRA_TEXT = get_font(45).render("extra.", True, "white")
        EXTRA_RECT = EXTRA_TEXT.get_rect(center=(640, 50))
        SCREEN.blit(EXTRA_TEXT, EXTRA_RECT)

        EXTRA_BACK = Button(image=None, pos=(640, 640),
                              text_input="Voltar", font=get_font(45), base_color="white", hovering_color="Green")

        EXTRA_BACK.changeColor(EXTRA_MOUSE_POS)
        EXTRA_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if EXTRA_BACK.checkForInput(EXTRA_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:

        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="#b68f40")
        EXTRA_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400),
                                text_input="EXTRA", font=get_font(75), base_color="#d7fcd4", hovering_color="#b68f40")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="#b68f40")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, EXTRA_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if EXTRA_BUTTON.checkForInput(MENU_MOUSE_POS):
                    extra()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()