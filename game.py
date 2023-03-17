import pygame

pygame.init()
x = 360
y = 350
velocidade = 10
pista = pygame.image.load('pista.png')
car = pygame.image.load('car.png')
janela = pygame.display.set_mode((800,600))
pygame.display.set_caption("Novo Jogo do Dheyvid")

janela_aberta = True

while janela_aberta :
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y-= velocidade
    if comandos[pygame.K_w]:
        y-= velocidade
    if comandos[pygame.K_DOWN]:
        y+= velocidade
    if comandos[pygame.K_s]:
        y+= velocidade    
    if comandos[pygame.K_RIGHT]:
        x+= velocidade   
    if comandos[pygame.K_d]:
        x+= velocidade 
    if comandos[pygame.K_LEFT]:
        x-= velocidade
    if comandos[pygame.K_a]:
        x-= velocidade   

    janela.blit(pista, (0,0))
    janela.blit(car, (x,y))
    pygame.display.update()        

pygame.quit()