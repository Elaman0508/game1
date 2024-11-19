import pygame
pygame.init()

clock = pygame.time.Clock()


screen = pygame.display.set_mode((618, 359))
pygame.display.set_caption("My Game Bir balee")
icon = pygame.image.load("images/ICO.png")
pygame.display.set_icon(icon)

label = pygame.font.Font(None, 40)
lose_label = label.render('Game Over!', False, (255, 0, 0))
restart = label.render('Restart', False, (255, 255, 255))


bg = pygame.image.load("images/screen.jpg")
bg_x = 0

walk_left = [
    pygame.image.load("images/player_left/left1.png").convert_alpha(),
    pygame.image.load("images/player_left//left2.png").convert_alpha(),
    pygame.image.load("images/player_left//left3.png").convert_alpha(),
    pygame.image.load("images/player_left//left4.png").convert_alpha(),
]

walk_right = [
    pygame.image.load("images/player_right/right1.png"),
    pygame.image.load("images/player_right/right2.png"),
    pygame.image.load("images/player_right/right3.png"),
    pygame.image.load("images/player_right/right4.png"),
]

brag = pygame.image.load('images/bad1.png')
brag_x = 630

player_x = 200
player_y = 250
player_speed = 5
player_amin_count = 0
game = True

while True:
    
    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 618, 0))
    screen.blit(walk_right[player_amin_count], (player_x, player_y))
    screen.blit(brag, (brag_x, 230))
    if game:
        player_kvadrat = walk_left[0].get_rect(topleft = (player_x, player_y))
        brag_kvadrat = brag.get_rect(topleft = (brag_x, 230))

        if player_kvadrat.colliderect(brag_kvadrat):
            game = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 50:
            player_x -= player_speed
        elif keys[pygame.K_RIGHT] and player_x < 300:
            player_x += player_speed
            


        if player_amin_count == 3:
            player_amin_count = 0
        else: 
            player_amin_count += 1
        
        bg_x -= 2
        if bg_x <= -618:
            bg_x = 0
        
        brag_x -= 10
    else: 
        screen.fill((56, 57, 58))
        screen.blit(lose_label, (200, 200))
        screen.blit(restart, (200, 250))

    pygame.display.update()


    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    clock.tick(15)