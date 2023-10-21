import os
import pygame

class Entidades:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.image = None
        self.radio = 0
        self.velocidad = 0
        self.pantalla = None
        self.pantalla_tamano = [0,0]
    
    def cambiar_imagen(self, new_image_path):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        resources_dir = os.path.join(script_dir, '..', 'resources')
        img_path = os.path.join(resources_dir, new_image_path)
        img = pygame.image.load(img_path)
        self.image = img

    def transformar_imagen(self, ancho, alto):
        if self.image is not None:
            self.image = pygame.transform.scale(self.image, (ancho, alto))

    def cambiar_x(self, x):
        self.x = x

    def cambiar_y(self, y):
        self.y = y
    
    def cambiar_radio(self, radio):
        self.radio = radio
    
    def cambiar_velocidad(self, velocidad):
            self.velocidad = velocidad

    def cambiar_pantalla(self, pantalla: pygame.display):
        self.pantalla = pantalla
    
    def cambiar_pantalla_tamano(self, width, height):
        self.pantalla_tamano[0] = width
        self.pantalla_tamano[1] = height

    def aparecer(self):
        if self.image is not None:
            self.pantalla.blit(self.image, (self.x - self.radio, self.y - self.radio))


    
class Enemigos(Entidades):
    
    def __init__(self) -> None:
        super().__init__()

    def mover(self):
        self.y += self.velocidad    

class Heroe(Entidades):
    
    def __init__(self) -> None:
        super().__init__()

    def mover(self, eventos):
        for evento in eventos:

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    self.mover_jugador_izquierda()

                elif evento.key == pygame.K_RIGHT:
                    self.mover_jugador_derecha()

    def mover_jugador_izquierda(self):
        if (self.x - self.velocidad) >= 0:
            self.x -= self.velocidad

    def mover_jugador_derecha(self):
        if (self.x + self.radio * 2 + self.velocidad <= self.pantalla_tamano[0]):
            self.x += self.velocidad

    def aparecer(self):
        if self.image is not None:
            self.pantalla.blit(self.image, (self.x - self.radio, self.y - self.radio))