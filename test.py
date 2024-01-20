import pygame

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((618, 359))
pygame.display.set_caption("Ernisov1x game")


bg = pygame.image.load('images/screen.jpg').convert_alpha()

walk_left = [
    pygame.image.load('images/player_left/left1.png').convert_alpha(),
    pygame.image.load('images/player_left/left2.png').convert_alpha(),
    pygame.image.load('images/player_left/left3.png').convert_alpha(),
    pygame.image.load('images/player_left/left4.png').convert_alpha(),
]

walk_right = [
    pygame.image.load('images/player_right/right1.png').convert_alpha(),
    pygame.image.load('images/player_right/right2.png').convert_alpha(),
    pygame.image.load('images/player_right/right3.png').convert_alpha(),
    pygame.image.load('images/player_right/right4.png').convert_alpha(),
]

player_anim_count = 0
bg_x = 0

player_speed = 5
player_x = 150



# переменный для прыжка 
player_y = 250
is_jump = False
jump_count = 7

#переиенный врага
ghost = pygame.image.load('images/bad.png').convert_alpha()
# ghost_x = 620
ghost_list_in_game = [

]

ghost_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ghost_timer, 3000)



label = pygame.font.Font(None, 40)
lose_label = label.render('Game Over!', False, (193, 196, 199))
restart_label = label.render('Restart', False, (115, 132, 148))



                            # Цикл


running = True
while running:


    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x  + 618, 0))
    # screen.blit(walk_right[player_anim_count], (player_x, 250))
    # screen.blit(ghost, (ghost_x, 250))

    #неведимка 
    player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))
     
    if ghost_list_in_game:
        for el in ghost_list_in_game:
            screen.blit(ghost, el)
            el.x -= 10
    
        if player_rect.colliderect(el):
            print('game over')
  
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        screen.blit(walk_left[player_anim_count], (player_x, player_y))
    else:
        screen.blit(walk_right[player_anim_count], (player_x, player_y))

    if keys[pygame.K_LEFT] and player_x > 50:
        player_x -= player_speed
    elif keys[pygame.K_RIGHT] and player_x < 200:
        player_x += player_speed


    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -7:
            if jump_count > 0:
                player_y -= (jump_count ** 2) / 2
            else:
                player_y += (jump_count ** 2) / 2
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 7
    

    if player_anim_count == 3:
        player_anim_count = 0
    else:
        player_anim_count += 1

    

    bg_x -= 2
    if bg_x == -618:
        bg_x = 0

    # передвижение врага 
    # ghost_x -= 10

    
    

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit

    #   
        if event.type == ghost_timer:
            ghost_list_in_game.append(ghost.get_rect(topleft=(620, 250)))

        

        
    clock.tick(20)

