import pygame 
pygame.init() 
clock = pygame.time.Clock() 

screen = pygame.display.set_mode((600, 400)) 
pygame.display.set_caption("My Game") 
icon = pygame.image.load("images/MonkeydLuffy.jpeg") 
pygame.display.set_icon(icon) 
bagraund = pygame.image.load('images/fon.jpg')
bg_x = 0

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

player_x = 200
player_y = 250
player_speed = 5
player_amin_count = 0

running = True 
while running: 
    
    screen.blit(bagraund, (bg_x, 0)) 
    screen.blit(bagraund, (bg_x + 600, 0))
    screen.blit(walk_right[player_amin_count], (player_x, player_y))

    keys = pygame.key.get_pressed() 
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    elif keys[pygame.K_RIGHT]:
        player_x += player_speed

    if player_amin_count == 3:
        player_amin_count = 0
    else:
        player_amin_count += 1

    bg_x -= 2
    if bg_x == -600:
         bg_x = 0

    
    
    
    pygame.display.update()


    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 

    
    clock.tick(10) 
