import pygame, sys, random, os


# - - - Definición de variables - - - #

# Variables globales (Generales)
coordenadas_enemigos = []
diccionario_colores = {
    "negro": (0, 0, 0),
    "blanco": (255, 255, 255),
    "rojo": (255, 0, 0),
    "verde": (0, 255, 0),
    "azul": (0, 0, 255),
    "yellow": (255, 255, 0),
    "cian": (0, 255, 255),
    "magenta": (255, 0, 255),
    "naranja": (255, 165, 0),
    "morado": (128, 0, 128),
    "gris": (128, 128, 128),
    "marron": (165, 42, 42),
    "rosa": (255, 182, 193),
    "lima": (50, 205, 50),
    "dorado": (255, 215, 0),
    "SILVER": (192, 192, 192)
    }

# Variables globales (Juego)
velocidad_enemigo = 5
radio_enemigo = 10
color_enemigo = diccionario_colores["rojo"]
cantidad_enemigos = 30

# Variables globales (PyGame)
pantalla_tamano = (1000, 800)
pantalla = pygame.display.set_mode(pantalla_tamano)
reloj = pygame.time.Clock()


def jugador_sobre_enemigo(jugador_coords, enemigo_coords) -> bool:

    # Fórmula matemática de la distancia entre dos puntos 
    x_distancia_al_enemigo = abs(jugador_coords[0] - enemigo_coords[0])
    y_distancia_al_enemigo = abs(jugador_coords[1] - enemigo_coords[1])
    
    # ¿El jugador está sobre algún enemigo?
    return x_distancia_al_enemigo < radio_enemigo and y_distancia_al_enemigo < radio_enemigo

def generar_posiciones_enemigo() -> list:
    # Asignar x,y como componentes de un punto (generados en el intervalo de la pantalla)
    x = random.randint(0, pantalla_tamano[0])
    y = random.randint(0, pantalla_tamano[1])

    # Agregar coordenadas del enemigo en la lista
    coordenadas_enemigos.append([x,y])

    # Retornar nuevas coordenadas del spawn de un enemigo
    return [x,y]
    
def generar_enemigos():

    for coords in coordenadas_enemigos:

        # Spawnear enemigos
        pygame.draw.circle(pantalla, color_enemigo, coords, radio_enemigo)

        # Mover enemigos
        coords[1] += velocidad_enemigo

        # Obtener coordenadas del jugador
        (x,y) = pygame.mouse.get_pos()
        player_coords = [x,y]

        if coords[1] > pantalla_tamano[1]:
             coords[1] = 0

        if jugador_sobre_enemigo(player_coords, coords):
            print("Graveee")
            coords[0] = 0
            coords[1] = 0
    
def evento_tocar_enemigo():
    pass 

def aparecer_enemigos():
    for i in range(cantidad_enemigos):
        generar_posiciones_enemigo()
    
def x_pulsada(evento):
    return evento.type in [pygame.QUIT]

def cerrar():
    sys.exit(0)

aparecer_enemigos()

# Iniciar ciclo de refresco de pantalla
while True:
    for evento in pygame.event.get():
        if x_pulsada(evento):
            cerrar()
        
    # Nivel de indentación para tener los eventos
    pantalla.fill(diccionario_colores["cian"])

    generar_enemigos()
        
    pygame.display.flip()
    reloj.tick(30)

