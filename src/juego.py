import tkinter
import tkinter as tk
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
"ticks_puntos": 0.1,
"velocidad_enemigo_incrementar_en_intervalo": 60,
"velocidad_enemigo_incremento": 0.2
}


# Variables de PyGame
pantalla = None
icono = None
lista_enemigos = None
jugador = None
fondo = None
puntos_obtenidos = None
coordenadas_jugador = None
reloj = None

def variables_de_inicio():

    global valores_predeterminados
    global pantalla
    global icono
    global lista_enemigos
    global jugador
    global fondo
    global puntos_obtenidos
    global coordenadas_jugador
    global reloj

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
        "ticks_puntos": 0.1,
        "velocidad_enemigo_incrementar_en_intervalo": 60,
        "velocidad_enemigo_incremento": 0.2
    }

    valores_predeterminados = cargar_json("database", valores_predeterminados)

    # Variables de PyGame
    pygame.font.init()  # Inicializa el módulo de fuentes de Pygame

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

def cargar_json(nombre_archivo, datos_default = None):
    if not os.path.exists(nombre_archivo):
        if datos_default is not None:
            return datos_default
        else:
            return valores_predeterminados
    else:
        with open(nombre_archivo, 'r') as archivo:
            return json.load(archivo)

def jugador_sobre_enemigo(jugador: Heroe, enemigo: Enemigos):
    
    distancia = ((jugador.x - enemigo.x) ** 2 + (jugador.y - enemigo.y) ** 2) ** 0.5
    return distancia <= (jugador.radio + enemigo.radio)

def generar_enemigos():
    x = random.randint(0, valores_predeterminados["pantalla_tamano"][0])
    y = random.randint(0, valores_predeterminados["pantalla_tamano"][1])
    
    if generacion_valida(x,y,600):
        enemigo = Enemigos()
        enemigo.cambiar_velocidad(valores_predeterminados["velocidad_enemigo"])
        enemigo.cambiar_x(x)
        enemigo.cambiar_y(y)

        lista_enemigos.append(enemigo)

def generacion_valida(x_enemigo, y_enemigo, distancia_minima = 5):
    distancia_x = abs(jugador.x - x_enemigo)
    distancia_y = abs(jugador.y - y_enemigo)
    if distancia_x <= distancia_minima and distancia_y <= distancia_minima:
        return False
    return True

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

def mostrar_puntuacion():
    texto = f"Puntos: {round(puntos_obtenidos,1)} - Record: {round(valores_predeterminados['racha_maxima'],1)}"
    fuente = pygame.font.Font(None, 36)
    texto_surface = fuente.render(texto, True, (255, 255, 255))
    coordenadas = (10,10)
    pantalla.blit(texto_surface, coordenadas)

def mostrar_ventana_emergente():
    ventana_emergente = tk.Tk()
    ventana_emergente.title("Mensaje")

    label = tk.Label(ventana_emergente, text="Has perdido... ¡Inténtalo nuevamente!")
    label.pack(pady=20)

    ok_button = tk.Button(ventana_emergente, text="OK", command=ventana_emergente.destroy)
    ok_button.pack()

    ventana_emergente.geometry("300x150+400+200")  # Ajusta el tamaño y la posición
    ventana_emergente.mainloop()

def evento_tocar_enemigo():
    detener_juego()
    mostrar_ventana_emergente()
    actualizar_racha()
    cerrar()
    
def x_pulsada(evento):
    return evento.type == pygame.QUIT

def actualizar_racha():
    if supero_el_maximo():
            cambiar_maximo()

def mover_jugador_izquierda(jugador: Heroe):
    jugador.mover_jugador_izquierda()

def mover_jugador_derecha(jugador: Heroe):
    jugador.mover_jugador_derecha()

def sumar_puntos():
    global puntos_obtenidos
    while True:
        puntos_obtenidos += 1 * valores_predeterminados["multiplicador_puntos"]
        time.sleep(valores_predeterminados["ticks_puntos"])

def hilo_sumar_puntos():
    t = threading.Thread(target=sumar_puntos)
    t.daemon = True
    t.start()

def incrementar_velocidad_enemigo(ticks, incremento):
    while True:
        time.sleep(ticks)
        valores_predeterminados["velocidad_enemigo"] += incremento
        velocidad = valores_predeterminados["velocidad_enemigo"]
        for enemigo in lista_enemigos:
            enemigo.cambiar_velocidad(velocidad)

def hilo_incrementar_velocidad_enemigo():
    segundos = valores_predeterminados["velocidad_enemigo_incrementar_en_intervalo"]
    incremento = valores_predeterminados["velocidad_enemigo_incremento"]

    t = threading.Thread(target=incrementar_velocidad_enemigo, args=(segundos, incremento))
    t.daemon = True
    t.start()
    
def cerrar():
    sys.exit(0)

def detener_juego():
    valores_predeterminados["multiplicador_puntos"] = 0
    pygame.quit()

def guardar_json(nombre_archivo, datos):
    with open(nombre_archivo, 'w') as archivo:
        json.dump(datos, archivo, indent=4)

def invisible():
    pantalla = pygame.display.set_mode((0,0))

def visible():
    pantalla = pygame.display.set_mode(valores_predeterminados["pantalla_tamano"])

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
    variables_de_inicio()
    hilo_sumar_puntos()
    hilo_incrementar_velocidad_enemigo()

    while True:
        for evento in pygame.event.get():
            if x_pulsada(evento):
                cerrar()

        # Funciones lógicas (No gráficas)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            mover_jugador_izquierda(jugador)

        if keys[pygame.K_RIGHT]:
            mover_jugador_derecha(jugador)

        if len(lista_enemigos) < valores_predeterminados["cantidad_enemigos"]:
            generar_enemigos()

        for enemigo in lista_enemigos:
            if jugador_sobre_enemigo(jugador, enemigo):
                evento_tocar_enemigo()

        # Funciones no lógicas (Gráficas)
        pantalla.blit(fondo, (0, 0))

        aparecer_enemigo()
        aparecer_jugador()
        mostrar_puntuacion()
        pygame.display.flip()

        reloj.tick(30)
