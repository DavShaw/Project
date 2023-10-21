import pygame
import random
import sys
import threading
import time
import os
import json
from clases.Personajes import Enemigos, Heroe, Entidades


# Variables para acceder a rutas del src
script_dir = os.path.dirname(__file__)
next_dir = os.path.join(script_dir, 'resources', 'background_5.png')

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

lista_enemigos = []
jugador = Heroe()
jugador.cambiar_x(valores_predeterminados["pantalla_tamano"][0] // 2)
jugador.cambiar_y(valores_predeterminados["pantalla_tamano"][1] - 50)
jugador.cambiar_radio(valores_predeterminados["radio_jugador"])
jugador.cambiar_velocidad(valores_predeterminados["velocidad_jugador"])
fondo = pygame.image.load(next_dir)
fondo = pygame.transform.scale(fondo, valores_predeterminados["pantalla_tamano"])

puntos_obtenidos = 0
coordenadas_jugador = [(valores_predeterminados["pantalla_tamano"][0] // 2), valores_predeterminados["pantalla_tamano"][1] - 50]




reloj = pygame.time.Clock()

def jugador_sobre_enemigo(jugador: Heroe, enemigo: Enemigos):
    
    distancia = ((jugador.x - enemigo.x) ** 2 + (jugador.y - enemigo.y) ** 2) ** 0.5
    return distancia <= (jugador.radio + enemigo.radio)

def generar_enemigos():
    x = random.randint(0, valores_predeterminados["pantalla_tamano"][0])
    y = random.randint(0, valores_predeterminados["pantalla_tamano"][1])
    
    enemigo = Enemigos()
    enemigo.cambiar_velocidad(valores_predeterminados["velocidad_enemigo"])
    enemigo.cambiar_x(x)
    enemigo.cambiar_y(y)

    lista_enemigos.append(enemigo)
    return enemigo

def supero_limites(personaje: Entidades):
    return personaje.y > valores_predeterminados["pantalla_tamano"][1]

def reiniciar_enemigo(enemigo: Enemigos):
    enemigo.x = random.randint(0, valores_predeterminados["pantalla_tamano"][0])
    enemigo.y = 0

def mover_enemigo(enemigo: Enemigos):
    enemigo.mover()

def aparecer_enemigo():
    for enemigo in lista_enemigos:

        enemigo.cambiar_imagen("enemigo_5.png")
        enemigo.cambiar_radio(valores_predeterminados["radio_enemigo"])
        enemigo.transformar_imagen(3*enemigo.radio, 3*enemigo.radio)
        enemigo.cambiar_pantalla(pantalla)
        enemigo.aparecer()

        mover_enemigo(enemigo)
        if supero_limites(enemigo):
            reiniciar_enemigo(enemigo)

def aparecer_jugador():
    jugador.cambiar_imagen("warrior_2.png")
    jugador.transformar_imagen(3*jugador.radio, 3*jugador.radio)
    jugador.cambiar_x(jugador.x)
    jugador.cambiar_y(jugador.y)
    jugador.cambiar_pantalla(pantalla)
    jugador.cambiar_pantalla_tamano(1000, 800)
    jugador.aparecer()

def evento_tocar_enemigo():
    cerrar()
    
def x_pulsada(evento):
    return evento.type == pygame.QUIT

def mover_jugador_izquierda(jugador: Heroe):
    jugador.mover_jugador_izquierda()

def mover_jugador_derecha(jugador: Heroe):
    jugador.mover_jugador_derecha()

def sumar_puntos(multiplicador = valores_predeterminados["multiplicador_puntos"], segundos = valores_predeterminados["ticks_puntos"]):
    global puntos_obtenidos
    while True:
        puntos_obtenidos += 1 * multiplicador
        time.sleep(segundos)

def hilo_sumar_puntos(multiplicador_puntos = valores_predeterminados["multiplicador_puntos"], ticks_puntos = valores_predeterminados["ticks_puntos"]):
    t = threading.Thread(target=sumar_puntos, args=(multiplicador_puntos, ticks_puntos))
    t.daemon = True
    t.start()
    
def cerrar():
    if(supero_el_maximo):
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
            mover_jugador_izquierda(jugador)

        # Si la tecla derecha está presionada, mover el jugador a la derecha
        if keys[pygame.K_RIGHT]:
            mover_jugador_derecha(jugador)
            

        pantalla.blit(fondo, (0, 0))

        if len(lista_enemigos) < valores_predeterminados["cantidad_enemigos"]:
            generar_enemigos()

        for enemigo in lista_enemigos:
            if jugador_sobre_enemigo(jugador, enemigo):
                evento_tocar_enemigo()

        aparecer_enemigo()
        aparecer_jugador()
        pygame.display.flip()

        reloj.tick(30)


jugar()