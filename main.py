import pygame
#from pygame.locals import mixer
from fighter import Fighter

#mixer.init()
pygame.init()

# creacion de ventana de juego
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Talana Kombat JRPG")

# razon de cuadros por segundo
clock = pygame.time.Clock()
FPS = 40

# definicion de colores
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# cargar imagen de fondo
bg_image = pygame.image.load("assets/images/Background/la-portada-de-antofagasta-B.png").convert_alpha()

# carga de sprietesheets
warrrior1_sheet = pygame.image.load("assets/images/Fighters/warrior1.png").convert_alpha()
warrrior2_sheet = pygame.image.load("assets/images/Fighters/warrior2.jpg").convert_alpha()

# definir el numero de pasoos para cada animacion
WARRIOR1_ANIMATION_STEPS = [10,8,1,7,7,3,7]
WARRIOR2_ANIMATION_STEPS = [8,8,1,8,8,3,7]

# f(x) de renderizacion de imagen de fondo

def draw_background(screen):
    scale_background = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scale_background, (0, 0))


# dibujar barra de salud de figthers
def draw_health_bar(health, x, y):
    ratio = health / 6
    pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 402, 34))
    pygame.draw.rect(screen, RED, (x, y, 400, 30))
    pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))


# creacion de instancias de jugador
fighter1 = Fighter(200, 310, warrrior1_sheet, WARRIOR1_ANIMATION_STEPS)
fighter2 = Fighter(700, 310, warrrior2_sheet, WARRIOR2_ANIMATION_STEPS)

# loop de juego
run = True
while run:

    clock.tick(FPS)

    # dibujar imagen de fondo
    draw_background(screen)

    # dibujar barra de salud de figthers
    draw_health_bar(fighter1.health, 20, 20)
    draw_health_bar(fighter2.health, 580, 20)

    # movimiento de fighter
    fighter1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter2)
    # fighter2.move()

    # dibujar peleadores (fighter y fighter2)
    fighter1.draw(screen)
    fighter2.draw(screen)

    # eventos de teclado
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # actualizar pantalla
    pygame.display.update()

pygame.quit()
