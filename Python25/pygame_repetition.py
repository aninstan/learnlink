# Det opprettes en startknapp som heter STARTKNAPP
# Deretter ... 
import pygame
import time

#1
waiting = True
while waiting:
    for event in pygame.event.get():

        if STARTKNAPP.collidepoint(mouse_pos): 
            waiting = False 
        elif event.type == pygame.MOUSEBUTTONDOWN: 
            mouse_pos = pygame.mouse.get_pos()




#2
hvit = (255, 255, 255)
start_meny_font = pygame.font.SysFont('time new roman', 70)
start_meny_text = start_meny_font.render('Velkommen til mitt spill! ', True, hvit)
spillvindu.blit(start_meny_text, (120, 200))


#3
global tall1, tall2 
tall1 = 345
tall2 = 122


#4
tekst = "Nå har du ventet lenge!"
time.sleep(10)
print(tekst)


#5
hvit = (255, 255, 255)
font = pygame.font.SysFont('time new roman', 70)
text = start_meny_font.render('Heisann! ', True, hvit)


