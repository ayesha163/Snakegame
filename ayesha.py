# Main Menu
def main_menu():
    pygame.mixer.music.play(-1)

    m = True
    while m:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()

        # mouse position
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        game_layout_display.blit(menu_background, (0, 0))
        button("Play", mouse[0], mouse[1], (width_screen / 2 - 100), height_screen / 2, 200, 50, green_color,
               blue_green_color, 60, 1)
        button("Pause", mouse[0], mouse[1], (width_screen / 2 - 100), height_screen / 2+100, 200, 50, green_color,
               blue_green_color, 60, 0)

        button("Quit", mouse[0], mouse[1], (width_screen / 2 - 100), (height_screen / 2) + 200, 200, 50, red_color,
               blue_red_color, 60, 0)

        mouse = pygame.mouse.get_pos()
        if button2("Mute Music", mouse[0], mouse[1], 1166, 0, 200, 50, purple_color, blue_purple_color, 25):
            pygame.mixer.music.pause()
        if button2("Play Music", mouse[0], mouse[1], 1166, 75, 200, 50, purple_color, blue_purple_color, 25):
            pygame.mixer.music.unpause()


        pygame.display.update()


# Options Menu:
def choice():
    f = True
    while f == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()

        # mouse position
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        best1 = best2 = best3 = best4 = best5 = -1
        game_layout_display.blit(menu_background, (0, 0))
        # Single player button
        best1 = button("Single Player", mouse[0], mouse[1], (width_screen / 2 - 150), 250, 300, 50, green_color,
                       blue_green_color, 30, "s")
        # 2 player button
        best2 = button("2 Players", mouse[0], mouse[1], (width_screen / 2) - 150, 350, 300, 50, green_color,
                       blue_green_color, 30, 2)
        # 3 player
        best3 = button("3 Players", mouse[0], mouse[1], (width_screen / 2) - 150, 450, 300, 50, green_color,
                       blue_green_color, 30, 3)
        # 4 player
        best4 = button("4 Players", mouse[0], mouse[1], (width_screen / 2) - 150, 550, 300, 50, green_color,
                       blue_green_color, 30, 4)
        # Back button
        best5 = button("Back", mouse[0], mouse[1], 0, 650, 200, 50, red_color, blue_red_color, 30, 5)
        if best5 == 5:
            main_menu()



        pygame.display.update()


def playing(best):
    best6 = -1
    time = 3000
    if best6 == 7:
        choice()
    game_layout_display.blit(post, (0, 0))
    game_layout_display.blit(mother_board, (width_screen / 2 - 250, height_screen / 2 - 250))
    xcr = xcy = xcg = xcb = 406 - 25
    ycr = ycy = ycg = ycb = 606 - 25
    game_layout_display.blit(red_c, (xcy, ycy))
    if 5 > best > 1 or best == 21:
        game_layout_display.blit(yellow_c, (xcy, ycy))

    if 5 > best > 2 or best == 21:
        game_layout_display.blit(green_c, (xcg, ycg))

    if 5 > best > 2:
        game_layout_display.blit(blue_c, (xcb, ycb))
    gamer1 = "Player 1"
    gamer1score = 0
    if best == 21:
        gamer2 = "Computer"
        gamer2score = 0
    if 5 > best > 1:
        gamer2 = "Player 2"
        gamer2score = 0
    if 5 > best > 2:
        gamer3 = "Player 3"
        gamer3score = 0
    if 5 > best > 3:

        gamer4 = "Player 4"
        gamer4score = 0
    tips = 1
    play = True
    while True:
        less = False
        set = False
        time = 3000
        game_layout_display.blit(post, (0, 0))
        game_layout_display.blit(mother_board, (width_screen / 2 - 250, height_screen / 2 - 250))
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()

        if best == 21:
            quit()
        pygame.display.update()


introduction()
main_menu()
