'''Importación de librerías'''
import pygame

'''Declaración de variables'''
SCREENSIZE = 500
running = True
cabezaX = 50
cabezaY = 50
anchoDePixel = 10
altoDePixel = 10
vel = 10
direccion = "DERECHA"

serpiente = [(cabezaX, cabezaY), (60, 50), (70, 50), (80, 50), (90, 50), (100, 50), (110, 50)]

"""
Función para mover Serpiente
    direccion: Dirección a la que se va moviendo la serpiente
    serpiente: Arreglo de tuplas
"""
def moverSerpiente(direccion, serpiente):
    global vel
    nuevaCabezaX = serpiente[0][0]
    nuevaCabezaY = serpiente[0][1]
    serpiente.pop()

    if direccion == "ARRIBA":
        nuevaCabezaY -= vel
    elif direccion == "ABAJO":
        nuevaCabezaY += vel
    elif direccion == "DERECHA":
        nuevaCabezaX += vel
    elif direccion == "IZQUIERDA":
        nuevaCabezaX -= vel
    
    serpiente.insert(0, (nuevaCabezaX,nuevaCabezaY))

"""
Función para dibujar en la pantalla 
    win: Ventana de juego
    serpiente: Arreglo de tuplas que contiene la serpiente
"""
def dibujar(win, serpiente):
    global anchoDePixel
    global altoDePixel
    
    win.fill((0,0,0))

    for pixel in serpiente:
        pygame.draw.rect(win, (255,0,0), (pixel[0],pixel[1],anchoDePixel,altoDePixel))
    pygame.display.update()


"""
Función para principal del juego
"""
def main():
    global SCREENSIZE
    global running
    global cabezaX
    global cabezaY
    global anchoDePixel
    global altoDePixel
    global serpiente
    global vel
    global direccion

    pygame.init()
    win = pygame.display.set_mode((SCREENSIZE,SCREENSIZE))
    pygame.display.set_caption("SnakeGame")
    '''Ciclo de vida del juego'''
    while running: 
        pygame.time.delay(100)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            direccion = "DERECHA"
        elif keys[pygame.K_LEFT]:
            direccion = "IZQUIERDA"
        elif keys[pygame.K_UP]:
            direccion = "ARRIBA"
        elif keys[pygame.K_DOWN]:
            direccion = "ABAJO"
           

        moverSerpiente(direccion,serpiente)
        dibujar(win, serpiente)

    pygame.quit()
'''Ejecutar el juego'''
main()