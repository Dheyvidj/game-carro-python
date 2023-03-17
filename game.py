import pygame
from random import randint

pygame.init()

x = 360  #min 140  #max 520
y = 350
pos_y_azul = 300
pos_y_laranja = 800
pos_y_verde = 2000

velocidade = 10
velocidade_obstaculos = 20

timer = 0
tempo_segundo = 0

pista = pygame.image.load('pista.png')
car_azul = pygame.image.load('car_azul.png')
car_laranja = pygame.image.load('car_laranja.png')
car_verde = pygame.image.load('car_verde.png')
car_vermelho = pygame.image.load('car_vermelho.png')

font = pygame.font.SysFont('arial black',30)
texto = font.render("Tempo:",True,(255,255,255),(0,0,0))
pos_texto = texto.get_rect()
pos_texto.center = 40,20

janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Novo Jogo do Dheyvid")

janela_aberta = True

while janela_aberta:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y -= velocidade
    if comandos[pygame.K_w]:
        y -= velocidade
    if comandos[pygame.K_DOWN]:
        y += velocidade
    if comandos[pygame.K_s]:
        y += velocidade
    if comandos[pygame.K_RIGHT] and x <= 520:
        x += velocidade
    if comandos[pygame.K_d]:
        x += velocidade
    if comandos[pygame.K_LEFT] and x > 140:
        x -= velocidade
    if comandos[pygame.K_a]:
        x -= velocidade

    if (pos_y_azul >= 800):
        pos_y_azul = -randint(300, 1000)

    if (pos_y_laranja >= 800):
        pos_y_laranja = -randint(300, 1000)

    if (pos_y_verde >= 800):
        pos_y_verde = -randint(700, 2000)

    if(timer < 20):
        timer += 1
    else:
        tempo_segundo +=1
        texto = font.render("Tempo:"+str(tempo_segundo),True,(255,255,255),(0,0,0))
        timer = 0

    pos_y_azul += velocidade_obstaculos
    pos_y_laranja += velocidade_obstaculos+2
    pos_y_verde += velocidade_obstaculos+5

    janela.blit(pista, (0, 0))
    janela.blit(car_vermelho, (x, y))
    janela.blit(car_azul, (160, pos_y_azul))
    janela.blit(car_verde, (350, pos_y_verde))
    janela.blit(car_laranja, (520, pos_y_laranja))
    janela.blit(texto,pos_texto)

    pygame.display.update()

pygame.quit()
