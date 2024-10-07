import pygame
import random
import time 
import sys

pygame.init()

#Spillvindu 
bredde = 800 
høyde = 600
grønn = (0, 255, 0)
svart = (0, 0, 0)
hvit = (255, 255, 255)
rød = (255, 0, 0)
blå = (0, 0, 255)

spillvindu = pygame.display.set_mode((bredde, høyde))

snake_pos = [100, 60]
snake_kropp = [[100, 60], [100-20, 60], [100-(2*20), 60]]

mat_pos = [random.randrange(1, (bredde//20)-1)*20, random.randrange(1, (høyde//20)-1)*20]
søppel_pos = [random.randrange(1, (bredde//20)-1)*20, random.randrange(1, (høyde//20)-1)*20]

retning = "HØYRE"
ny_retning = retning

fps = pygame.time.Clock()

score = 0

bakgrunn = pygame.image.load('stein.jpg')
bakgrunn = pygame.transform.scale(bakgrunn, (bredde, høyde))

snake_hode_bilde = pygame.image.load('snake_hode.png')
snake_hode_bilde = pygame.transform.scale(snake_hode_bilde, (20, 20))

snake_kropp_bilde = pygame.image.load('snake_kropp.png')
snake_kropp_bilde = pygame.transform.scale(snake_kropp_bilde, (20, 20))

mat_bilde = pygame.image.load('eple.png')
mat_bilde = pygame.transform.scale(mat_bilde, (20, 20))

søppel_bilde = pygame.image.load('epleskrott.png')
søppel_bilde = pygame.transform.scale(søppel_bilde, (20, 20))


def vis_score(pos): 
    score_font = pygame.font.Font(None, 36)
    score_text = score_font.render("Score: {}".format(score), True, hvit)
    spillvindu.blit(score_text, pos)

def game_over(): 
    game_over_font = pygame.font.SysFont('time new roman', 90)
    game_over_text = game_over_font.render('GAME OVER', True, blå)

    spillvindu.blit(bakgrunn, (0, 0))
    spillvindu.blit(game_over_text, (200, 200))
    vis_score((350, 290))
    pygame.display.flip()

    time.sleep(3)
    spill_meny()

def spill_meny(): 
    start_meny_font = pygame.font.SysFont('time new roman', 70)
    start_meny_text = start_meny_font.render('Joanna sitt snake-spill!', True, hvit)

    start_knapp_font = pygame.font.SysFont('time new roman', 50)
    start_knapp_text = start_knapp_font.render('START SPILLET', True, grønn)
    start_knapp = start_knapp_text.get_rect(center=(390, 380))

    regler_font = pygame.font.SysFont('time new roman', 30)
    regler_tekst = regler_font.render("Spis så mye mat du kan og unngå søppelet!", True, hvit)


    spillvindu.blit(bakgrunn, (0, 0))

    spillvindu.blit(start_meny_text, (120, 200))
    spillvindu.blit(regler_tekst, (170, 500))

    pygame.draw.rect(spillvindu, svart, start_knapp)
    spillvindu.blit(start_knapp_text, start_knapp)
    pygame.display.flip()

    vente = True 
    while vente: 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN: 
                mouse_pos = pygame.mouse.get_pos()
                if start_knapp.collidepoint(mouse_pos): 
                    vente  = False

    global snake_pos, snake_kropp, mat_pos, søppel_pos, retning, ny_retning, score
    snake_pos = [100, 60]
    snake_kropp = [[100, 60], [100-20, 60], [100-(2*20), 60]]

    mat_pos = [random.randrange(1, (bredde//20)-1)*20, random.randrange(1, (høyde//20)-1)*20]
    søppel_pos = [random.randrange(1, (bredde//20)-1)*20, random.randrange(1, (høyde//20)-1)*20]

    retning = "HØYRE"
    ny_retning = retning 

    score = 0



spill_meny()
#Spill-løkke
kjør = True
while kjør: 

    spillvindu.blit(bakgrunn, (0, 0))
    pygame.display.update()

    #Hendelseshåndtering 
    for hendelse in pygame.event.get():
        if hendelse.type == pygame.QUIT:
            kjør = False

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]: 
        ny_retning = "VENSTRE"
    if key[pygame.K_RIGHT]: 
        ny_retning = "HØYRE"
    if key[pygame.K_UP]: 
        ny_retning = "OPP"
    if key[pygame.K_DOWN]: 
        ny_retning = "NED"

    if ny_retning == "OPP" and retning != "NED": 
        retning = "OPP"
    if ny_retning == "NED" and retning != "OPP": 
        retning = "NED"
    if ny_retning == "VENSTRE" and retning != "HØYRE": 
        retning = "VENSTRE"
    if ny_retning == "HØYRE" and retning != "VENSTRE": 
        retning = "HØYRE"

    if retning == "OPP": 
        snake_pos[1] -= 20
    if retning == "NED": 
        snake_pos[1] += 20 
    if retning == "VENSTRE": 
        snake_pos[0] -= 20 
    if retning == "HØYRE": 
        snake_pos[0] += 20 

    snake_kropp.insert(0, list(snake_pos))

    # Tegner slangen, inkludert hode og kropp 
    spillvindu.blit(snake_hode_bilde, (snake_pos[0], snake_pos[1]))
    
    for pos in snake_kropp[1:]: 
        spillvindu.blit(snake_kropp_bilde, (pos[0], pos[1]))

    if snake_pos[0] == mat_pos[0] and snake_pos[1] == mat_pos[1]: 
        mat_pos = [random.randrange(1, (bredde//20)-1)*20, random.randrange(1, (høyde//20)-1)*20]
        score += 1
    elif snake_pos[0] == søppel_pos[0] and snake_pos[1] == søppel_pos[1]: 
        søppel_pos = [random.randrange(1, (bredde//20)-1)*20, random.randrange(1, (høyde//20)-1)*20]
        score -= 1
        snake_kropp.pop()
    else: 
        snake_kropp.pop()

    # Tegner maten og søppelet 
    spillvindu.blit(mat_bilde, (mat_pos[0], mat_pos[1]))
    spillvindu.blit(søppel_bilde, (søppel_pos[0], søppel_pos[1]))

    if snake_pos[0] < 0 or snake_pos[0] > bredde -20: 
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > høyde -20: 
        game_over()

    for rute in snake_kropp[1:]: 
        if snake_pos[0] == rute[0] and snake_pos[1] == rute[1]: 
            game_over()

    vis_score((10, 10))

    pygame.display.update()

    fps.tick(10)

pygame.quit()
