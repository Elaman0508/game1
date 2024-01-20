import pygame

clock = pygame.time.Clock()


pygame.init()
screen = pygame.display.set_mode((618, 359))
pygame.display.set_caption('Pygame Ernisov1x game')
icon = pygame.image.load('images/MonkeydLuffy.jpeg')
pygame.display.set_icon(icon)


bg = pygame.image.load('images/screen.jpg').convert()

brag = pygame.image.load('images/bad1.png').convert_alpha()
brag_list = [
    # pygame.image.load('images/bad1.png').convert_alpha(),
    # pygame.image.load('images/bad2.png').convert_alpha(),
    # pygame.image.load('images/bad.png').convert_alpha(),
]


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

# # координаты играка/
player_x = 150
player_y = 250



is_jump = False
jum_count = 8


# # Добовление звука
# bg_sound = pygame.mixer.Sound('music/Glichery - Sea Of Problems (Slowed + Reverb).mp3')
# bg_sound.play()

#  # таймер врага
brag_timer = pygame.USEREVENT + 1
pygame.time.set_timer(brag_timer, 3000)

logica = False

# #рисовка рестарта и проигрыша
label = pygame.font.Font(None, 40)
lose_label = label.render('Game Over!', logica, (193, 196, 199))
restart_label = label.render('Restart', logica, (115, 132, 148))
restart_label_rect = restart_label.get_rect(topleft=(180, 200))


# #Орграничение патрона
bullets_left = 5

# # картинка патрона
bullet = pygame.image.load('images/bullet.png').convert_alpha()
bullets = []

gameplay = True




#                             # ЦИКЛ

dis = True
while dis:



    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 618, 0))
    



    if gameplay:
        """логика невидемного квадрата и врага"""
        player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))
        if brag_list:
            for (el, i) in enumerate(brag_list):
                screen.blit(brag, i)
                i.x -= 10

                if i.x < -10:
                    brag_list.pop(el)


                if player_rect.colliderect(i):
                    gameplay = False

        keys = pygame.key.get_pressed()

        # логика движение
        if keys[pygame.K_LEFT] and player_x > 50:
            screen.blit(walk_left[player_anim_count], (player_x, player_y))
        else:
            screen.blit(walk_right[player_anim_count], (player_x, player_y))
        if keys[pygame.K_LEFT] and player_x > 50:
            player_x -= player_speed

        elif keys[pygame.K_RIGHT] and player_x < 200:
            player_x += player_speed




#         # логика прыжка
        if not is_jump:
            if keys[pygame.K_SPACE]:
                is_jump = True
        else:
            if jum_count > -9:
                if jum_count > 0:
                    player_y -= (jum_count ** 2) / 2
                else:
                    player_y += (jum_count ** 2) / 2
                jum_count -= 1
            else:
                is_jump = False
                jum_count = 8

        if player_anim_count == 3:
            player_anim_count = 0
        else:
            player_anim_count += 1


        bg_x -= 2
        if bg_x == -618:
            bg_x = 0


        
#         # логика патрона 
        if bullets:
            for (el, i) in enumerate(bullets):
                screen.blit(bullet, (i.x, i.y))
                i.x += 4

                if i.x >630:
                    bullets.pop(el)

                if brag_list:
                    for (index, brag_el) in enumerate(brag_list):
                        if i.colliderect(brag_el):
                            brag_list.pop(index)
                            bullets.pop(el)
    else:
        screen.fill((72, 0, 120 ))
        screen.blit(lose_label, (180, 100))
        screen.blit(restart_label, restart_label_rect)


        mouse = pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            player_x = 150
            brag_list.clear()
            bullets.clear()
            bullets_left = 5

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dis = False
            pygame.quit()
        if event.type == brag_timer:
            brag_list.append(brag.get_rect(topleft=(620, 250)))

            #Рисовка патрона
        if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_b \
            and bullets_left > 0:
            bullets.append(bullet.get_rect(topleft=(player_x + 30, player_y + 10)))
            bullets_left -= 1




    clock.tick(20)