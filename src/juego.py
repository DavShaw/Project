from button import Button
import pygame
import random
import sys
import threading
import time
import os
import json

from button import Button


# Variables para acceder a rutas del src
script_dir = os.path.dirname(__file__)
next_dir = os.path.join(script_dir, 'resources', 'background_4.png')

def cargar_json(nombre_archivo, datos_default = None):
    if not os.path.exists(nombre_archivo):
        if datos_default is not None:
            return datos_default
        else:
            return valores_predeterminados
    else:
        with open(nombre_archivo, 'r') as archivo:
            return json.load(archivo)


# Variables a persistir
valores_predeterminados = {
    "pantalla_tamano": (1000, 800),
    "racha_maxima": 0,
    "velocidad_enemigo": 5,
    "velocidad_jugador": 10,
    "radio_enemigo": 10,
    "radio_jugador": 20,
    "cantidad_enemigos": 15,
    "multiplicador_puntos": 0.1,
    "ticks_puntos": 0.1
}

valores_predeterminados = cargar_json("database", valores_predeterminados)

# Variables de PyGame
pantalla = pygame.display.set_mode(valores_predeterminados["pantalla_tamano"])
pygame.display.set_caption("Don't Touch the Bones")

icono = os.path.join(script_dir, 'resources', 'enemigo.png')
icono = pygame.image.load(icono)
pygame.display.set_icon(icono)

coordenadas_enemigos = []
fondo = pygame.image.load(next_dir)
fondo = pygame.transform.scale(fondo, valores_predeterminados["pantalla_tamano"])

puntos_obtenidos = 0
coordenadas_jugador = [(valores_predeterminados["pantalla_tamano"][0] // 2), valores_predeterminados["pantalla_tamano"][1] - 50]


reloj = pygame.time.Clock()

def jugador_sobre_enemigo(jugador_coords, enemigo_coords):
    distancia = ((jugador_coords[0] - enemigo_coords[0]) ** 2 + (jugador_coords[1] - enemigo_coords[1]) ** 2) ** 0.5
    return distancia <= (valores_predeterminados["radio_jugador"] + valores_predeterminados["radio_enemigo"])

def generar_posiciones_enemigo():
    x = random.randint(0, valores_predeterminados["pantalla_tamano"][0])
    y = random.randint(0, valores_predeterminados["pantalla_tamano"][1])
    coordenadas_enemigos.append([x, y])
    return [x, y]

def supero_limites(coordenadas):
    return coordenadas[1] > valores_predeterminados["pantalla_tamano"][1]

def reiniciar_enemigo(coordenadas):
    coordenadas[0] = random.randint(0, valores_predeterminados["pantalla_tamano"][0])
    coordenadas[1] = 0

def mover_enemigo(coordenadas):
    coordenadas[1] += valores_predeterminados["velocidad_enemigo"]

def aparecer_enemigo():
    for coords in coordenadas_enemigos:
        next_dir = os.path.join(script_dir, 'resources', 'enemigo.png')
        imagen_enemigo = pygame.image.load(next_dir)
        ancho = 3 * valores_predeterminados["radio_enemigo"]
        alto = 3 * valores_predeterminados["radio_enemigo"]
        imagen_enemigo = pygame.transform.scale(imagen_enemigo, (ancho, alto))
        pantalla.blit(imagen_enemigo, (coords[0] - valores_predeterminados["radio_enemigo"], coords[1] - valores_predeterminados["radio_enemigo"]))



        mover_enemigo(coords)
        if supero_limites(coords):
            reiniciar_enemigo(coords)

def aparecer_jugador():
    ancho = 3 * valores_predeterminados["radio_jugador"]
    alto = 3 * valores_predeterminados["radio_jugador"]
    jugador_imagen = os.path.join(script_dir, 'resources', 'warrior_2.png')
    jugador_imagen = pygame.image.load(jugador_imagen)
    jugador_imagen = pygame.transform.scale(jugador_imagen, (ancho, alto))
    pantalla.blit(jugador_imagen, (coordenadas_jugador[0] - valores_predeterminados["radio_jugador"], coordenadas_jugador[1] - valores_predeterminados["radio_jugador"]))

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
    if coordenadas_jugador[0] - valores_predeterminados["velocidad_jugador"] >= 0:
        coordenadas_jugador[0] -= valores_predeterminados["velocidad_jugador"]

def mover_jugador_derecha():
    if coordenadas_jugador[0] + valores_predeterminados["radio_jugador"] * 2 + valores_predeterminados["velocidad_jugador"] <= valores_predeterminados["pantalla_tamano"][0]:
        coordenadas_jugador[0] += valores_predeterminados["velocidad_jugador"]

def sumar_puntos(multiplicador = valores_predeterminados["multiplicador_puntos"], segundos = valores_predeterminados["ticks_puntos"]):
    global puntos_obtenidos
    while True:
        puntos_obtenidos += 1 * multiplicador
        time.sleep(segundos)
        print(round(puntos_obtenidos, 1))

def hilo_sumar_puntos(multiplicador_puntos = valores_predeterminados["multiplicador_puntos"], ticks_puntos = valores_predeterminados["ticks_puntos"]):
    t = threading.Thread(target=sumar_puntos, args=(multiplicador_puntos, ticks_puntos))
    t.daemon = True
    t.start()
    
def cerrar():
    if(supero_el_maximo()):
        cambiar_maximo()
    pygame.quit()
    sys.exit(0)

def guardar_json(nombre_archivo, datos):
    with open(nombre_archivo, 'w') as archivo:
        json.dump(datos, archivo, indent=4)

def supero_el_maximo():
    data = cargar_json("database", valores_predeterminados)
    if data["racha_maxima"] < puntos_obtenidos:
        return True
    return False

def cambiar_maximo():
    datos = cargar_json("database", valores_predeterminados)
    datos["racha_maxima"] = puntos_obtenidos
    guardar_json("database", datos)

def jugar():
    valores_predeterminados = cargar_json("database")
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

        if len(coordenadas_enemigos) < valores_predeterminados["cantidad_enemigos"]:
            generar_posiciones_enemigo()

        for enemigo_coords in coordenadas_enemigos:
            if jugador_sobre_enemigo(coordenadas_jugador, enemigo_coords):
                evento_tocar_enemigo()

        aparecer_enemigo()
        aparecer_jugador()

        pygame.display.flip()
        reloj.tick(30)

        print(puntos_obtenidos)
        print(supero_el_maximo())


jugar()