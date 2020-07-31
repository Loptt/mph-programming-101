import pygame
pygame.init()

SCREENWIDTH = 500

win = pygame.display.set_mode((SCREENWIDTH,SCREENWIDTH))
pygame.display.set_caption("First Game")

cabezaX = 50
cabezaY = 50
width = 10
height = 10
vel = 10
serpiente = [(cabezaX,cabezaY),(cabezaX-10,cabezaY),(cabezaX-20,cabezaY),(cabezaX-30,cabezaY),(cabezaX-40,cabezaY),(cabezaX-50,cabezaY),(cabezaX-60,cabezaY),(cabezaX-70,cabezaY)]
running = True

direccion = "DERECHA"


def moverSerpiente(direccion, serpiente):
    nuevaCabezaX = serpiente[0][0]
    nuevaCabezaY = serpiente[0][1]
    serpiente.pop(len(serpiente) - 1)

    if direccion == "ARRIBA":
        nuevaCabezaY -= vel
    if direccion == "ABAJO":
        nuevaCabezaY += vel
    if direccion == "DERECHA":
        nuevaCabezaX += vel
    if direccion == "IZQUIERDA":
        nuevaCabezaX -= vel

    serpiente.insert(0, (nuevaCabezaX,nuevaCabezaY))


def main():
    global cabezaX
    global cabezaY
    global width 
    global height
    global vel
    global serpiente
    global direccion
    global running
    global win
    global SCREENWIDTH
    while running:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        
        
        
        if keys[pygame.K_LEFT]:
            direccion = "IZQUIERDA"
            cabezaX -= vel

        elif keys[pygame.K_RIGHT]:
            direccion = "DERECHA"
            cabezaX += vel

        elif keys[pygame.K_UP]:
            direccion = "ARRIBA"
            cabezaY -= vel

        elif keys[pygame.K_DOWN]:
            direccion = "ABAJO"
            cabezaY += vel
        
        win.fill((0,0,0))

        moverSerpiente(direccion,serpiente)
        # dibujar a la serpiente  
        for piece in serpiente:
            pygame.draw.rect(win, (255,0,0), (piece[0],piece[1], width, height))
        pygame.display.update() 
        
    pygame.quit()

main()