import pygame
from random import randint

time_clocks = pygame.time.Clock()

# Initialize
pygame.init()
width_screen = 1366
height_screen = 768

ic = pygame.image.load("resources/icon.png")
game_layout_display = pygame.display.set_mode((width_screen, height_screen), pygame.FULLSCREEN)
pygame.display.set_caption("Snakes and Ladders Game ")
pygame.display.set_icon(ic)
pygame.display.update()

# Graphics:
black_color = (10, 10, 10)
white_color = (250, 250, 250)
red_color = (200, 0, 0)
blue_red_color = (240, 0, 0)
green_color = (0, 200, 0)
blue_green_color = (0, 230, 0)
blue_color = (0, 0, 200)
grey_color = (50, 50, 50)
yellow_color = (150, 150, 0)
purple_color = (43, 3, 132)
blue_purple_color = (60, 0, 190)

mother_board = pygame.image.load("resources/Snakes_ladders_big_image.png")
d1 = pygame.image.load("resources/dice_image1.png")
d2 = pygame.image.load("resources/dice_image2.png")
d3 = pygame.image.load("resources/dice_image3.png")
d4 = pygame.image.load("resources/dice_image4.png")
d5 = pygame.image.load("resources/dice_image5.png")
d6 = pygame.image.load("resources/dice_image6.png")

red_c = pygame.image.load("resources/red_c.png")
yellow_c = pygame.image.load("resources/yellow_c.png")
green_c = pygame.image.load("resources/green_c.png")
blue_c = pygame.image.load("resources/blue_c.png")
menu_background = pygame.image.load("resources/menu.jpg")
post = pygame.image.load("resources/game_background.jpg")

initial_background = pygame.image.load("resources/introduction_image.png")
initial_background2 = pygame.image.load("resources/introduction_image2.jpg")
initial_background3 = pygame.image.load("resources/introduction_image3.jpg")
initial_background4 = pygame.image.load("resources/introduction_image4.jpg")
initial_background5 = pygame.image.load("resources/introduction_image5.jpg")

pygame.mixer.music.load("sound/music.wav")
snake_sound = pygame.mixer.Sound("sound/snake.wav")
win = pygame.mixer.Sound("sound/win.wav")
lose = pygame.mixer.Sound("sound/lose.wav")
ladder = pygame.mixer.Sound("sound/ladder.wav")

# mouse position
mouse = pygame.mouse.get_pos()
click = pygame.mouse.get_pressed()


# Message displaying for buttons
def message_display_screen(text, x, y, fs):
    largeText = pygame.font.Font('freesansbold.ttf', fs)
    TextSurf, TextRect = text_objects_screen(text, largeText)
    TextRect.center = (x, y)
    game_layout_display.blit(TextSurf, TextRect)


def text_objects_screen(text, font):
    textSurface = font.render(text, True, white_color)
    return textSurface, textSurface.get_rect()





# Goti movement function
def movement(a):
    l1 = [[406, 606], [456, 606], [506, 606], [556, 606], [606, 606], [656, 606], [706, 606], [756, 606], [806, 606],
          [856, 606], [906, 606], [906, 560], [856, 560], [806, 560], [756, 560], [706, 560], [656, 560], [606, 560],
          [556, 560], [506, 560], [456, 560], [456, 506], [506, 506], [556, 506], [606, 506], [656, 506], [706, 506],
          [756, 506], [806, 506], [856, 506], [906, 506], [906, 460], [856, 460], [806, 460], [756, 460], [706, 460],
          [656, 460], [606, 460], [556, 460], [506, 460], [456, 460], [456, 406], [506, 406], [556, 406], [606, 406],
          [656, 406], [706, 406], [756, 406], [806, 406], [856, 406], [906, 406], [906, 360], [856, 360], [806, 360],
          [756, 360], [706, 360], [656, 360], [606, 360], [556, 360], [506, 360], [456, 360], [456, 306], [506, 306],
          [556, 306], [606, 306], [656, 306], [706, 306], [756, 306], [806, 306], [856, 306], [906, 306], [906, 260],
          [856, 260], [806, 260], [756, 260], [706, 260], [656, 260], [606, 260], [556, 260], [506, 260], [456, 260],
          [456, 206], [506, 206], [556, 206], [606, 206], [656, 206], [706, 206], [756, 206], [806, 206], [856, 206],
          [906, 206], [906, 160], [856, 160], [806, 160], [756, 160], [706, 160], [656, 160], [606, 160], [556, 160],
          [506, 160], [456, 160]]
    l2 = l1[a]
    x = l2[0] - 25
    y = l2[1] - 25
    return x, y


def text_objects1(text, font):
    textSurface = font.render(text, True, blue_color)
    return textSurface, textSurface.get_rect()


# Ladder check
def ladders(x):
    if x == 1:
        return 38
    elif x == 4:
        return 14
    elif x == 9:
        return 31
    elif x == 28:
        return 84
    elif x == 21:
        return 42
    elif x == 51:
        return 67
    elif x == 80:
        return 99
    elif x == 72:
        return 91
    else:
        return x
