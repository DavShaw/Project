import pygame
import random
import sys
import threading
import time

# Definición de variables
pantalla_tamano = (1000, 800)
coordenadas_enemigos = []
coordenadas_jugador = [(pantalla_tamano[0] // 2), pantalla_tamano[1] - 50]
diccionario_colores = {
    "negro": (0, 0, 0),
    "blanco": (255, 255, 255),
    "rojo": (255, 0, 0),
    "verde": (0, 255, 0),
    "azul": (0, 0, 255),
    }

# Variables de juego
fondo = pygame.image.load('background.jpg')
fondo = pygame.transform.scale(fondo, pantalla_tamano)
tecla_izquierda_presionada = False
tecla_derecha_presionada = False
puntos_obtenidos = 0
velocidad_enemigo = 5
velocidad_jugador = 10
radio_enemigo = 10
radio_jugador = 10
cantidad_enemigos = 15
multiplicador_puntos = 0.1
ticks_puntos = 0.1

# Variables de PyGame
pantalla = pygame.display.set_mode(pantalla_tamano)
reloj = pygame.time.Clock()

def jugador_sobre_enemigo(jugador_coords, enemigo_coords):
    distancia = ((jugador_coords[0] - enemigo_coords[0]) ** 2 + (jugador_coords[1] - enemigo_coords[1]) ** 2) ** 0.5
    return distancia <= (radio_jugador + radio_enemigo)

def generar_posiciones_enemigo():
    x = random.randint(0, pantalla_tamano[0])
    y = random.randint(0, pantalla_tamano[1])
    coordenadas_enemigos.append([x, y])
    return [x, y]

def supero_limites(coordenadas):
    return coordenadas[1] > pantalla_tamano[1]

def reiniciar_enemigo(coordenadas):
    coordenadas[0] = random.randint(0, pantalla_tamano[0])
    coordenadas[1] = 0

def mover_enemigo(coordenadas):
    coordenadas[1] += velocidad_enemigo

def aparecer_enemigo():
    for coords in coordenadas_enemigos:
        imagen_enemigo = pygame.image.load('enemigo.png')
        ancho = 3 * radio_enemigo
        alto = 3 * radio_enemigo
        imagen_enemigo = pygame.transform.scale(imagen_enemigo, (ancho, alto))
        pantalla.blit(imagen_enemigo, (coords[0] - radio_enemigo, coords[1] - radio_enemigo))
        mover_enemigo(coords)
        if supero_limites(coords):
            reiniciar_enemigo(coords)

def aparecer_jugador():
    pygame.draw.circle(pantalla, diccionario_colores["verde"], coordenadas_jugador, radio_jugador)

def evento_tocar_enemigo():
    print("Hola xd")

def x_pulsada(evento):
    return evento.type == pygame.QUIT

def mover_jugador(evento):
    global tecla_izquierda_presionada, tecla_derecha_presionada

    if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_LEFT:
            tecla_izquierda_presionada = True
        elif evento.key == pygame.K_RIGHT:
            tecla_derecha_presionada = True

    elif evento.type == pygame.KEYUP:
        if evento.key == pygame.K_LEFT:
            tecla_izquierda_presionada = False
        elif evento.key == pygame.K_RIGHT:
            tecla_derecha_presionada = False
            
    if tecla_izquierda_presionada:
        mover_jugador_izquierda()
    if tecla_derecha_presionada:
        mover_jugador_derecha()

def mover_jugador_izquierda():
    coordenadas_jugador[0] -= velocidad_jugador

def mover_jugador_derecha():
    coordenadas_jugador[0] += velocidad_jugador 

def sumar_puntos(multiplicador = multiplicador_puntos, segundos = ticks_puntos):
    global puntos_obtenidos
    while True:
        puntos_obtenidos += 1 * multiplicador
        time.sleep(segundos)
        print(round(puntos_obtenidos, 1))

def hilo_sumar_puntos(multiplicador_puntos = multiplicador_puntos, ticks_puntos = ticks_puntos):
    t = threading.Thread(target=sumar_puntos, args=(multiplicador_puntos, ticks_puntos))
    t.daemon = True
    t.start()
    
def cerrar():
    sys.exit(0)

# Iniciar ciclo de reinicio de pantalla
hilo_sumar_puntos()


while True:
    for evento in pygame.event.get():
        if x_pulsada(evento):
            cerrar()

    # Obtener el estado de las teclas
    keys = pygame.key.get_pressed()

    # Si la tecla izquierda está presionada, mover el jugador a la izquierda
    if keys[pygame.K_LEFT]:
        mover_jugador_izquierda()

    # Si la tecla derecha está presionada, mover el jugador a la derecha
    if keys[pygame.K_RIGHT]:
        mover_jugador_derecha()

    pantalla.blit(fondo, (0, 0))

    if len(coordenadas_enemigos) < cantidad_enemigos:
        generar_posiciones_enemigo()

    for enemigo_coords in coordenadas_enemigos:
        if jugador_sobre_enemigo(coordenadas_jugador, enemigo_coords):
            evento_tocar_enemigo()

    aparecer_enemigo()
    aparecer_jugador()

    pygame.display.flip()
    reloj.tick(30)
