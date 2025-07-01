import pygame 
import random
import time
import pygame.mixer as mixer
mixer.init()
clock = pygame.time.Clock()

# Inicializar Pygame
pygame.init()

# Titulo 
pygame.display.set_caption("BATTLESHIP PRO MAX")

# Icono
icon = pygame.image.load("C:/Users/santi/OneDrive/Escritorio/TRABAJOS PYTHON/2do Parcial/icono.png")
pygame.display.set_icon(icon)

# Musica
muted = False
logo_sonidosi = pygame.image.load("C:/Users/santi/OneDrive/Escritorio/TRABAJOS PYTHON/2do Parcial/sonidosi.png")
logo_sonidosi = pygame.transform.scale(logo_sonidosi, (40, 40))
logo_sonidono = pygame.image.load("C:/Users/santi/OneDrive/Escritorio/TRABAJOS PYTHON/2do Parcial/sonidono.png")
logo_sonidono = pygame.transform.scale(logo_sonidono, (40, 40))
mixer.music.load("C:/Users/santi/OneDrive/Escritorio/TRABAJOS PYTHON/2do Parcial/musicamenu.mp3")
mixer.music.play(-1)
mixer.music.set_volume(0.2)

# Creando la ventana
screen_resolution = (800, 600)
screen = pygame.display.set_mode((screen_resolution))

# FONDO
frame_actual = 0
N = 83
fondo_frames = []
for i in range(0, N+1):  # Empieza en 0
    num = str(i).zfill(2)  # '00', '01', ..., '83'
    frame = pygame.image.load(f"C:/Users/santi/OneDrive/Escritorio/TRABAJOS PYTHON/2do Parcial/frame_{num}_delay-0.05s.png")
    frame = pygame.transform.scale(frame, (800, 600))
    fondo_frames.append(frame)





#FUENTE
font = pygame.font.Font("C:/Users/santi/OneDrive/Escritorio/TRABAJOS PYTHON/2do Parcial/Michroma.ttf", 50)







def draw_button(text, x, y, w, h, text_color, font_name, font_size, hover=False):
    oval_margin = 0  
    ellipse_surface = pygame.Surface((w, h), pygame.SRCALPHA)
    pygame.draw.ellipse(
        ellipse_surface,
        (50, 50, 50), 
        (oval_margin, oval_margin, w - 2 * oval_margin, h - 2 * oval_margin)
    )

    if hover:
        pygame.draw.ellipse(
            ellipse_surface,
            (255, 255, 255, 80),  # Blanco semitransparente
            (oval_margin, oval_margin, w - 2 * oval_margin, h - 2 * oval_margin)
        )
    screen.blit(ellipse_surface, (x, y))
    # Fuente
    if font_name.lower() == "michroma":
        font = pygame.font.Font("C:/Users/santi/OneDrive/Escritorio/TRABAJOS PYTHON/2do Parcial/Michroma.ttf", font_size)
    else:
        font = pygame.font.SysFont(font_name, font_size, bold=True)
    label = font.render(text, True, text_color)
    label_rect = label.get_rect(center=(x + w // 2, y + h // 2))
    screen.blit(label, label_rect)



# Bucle principal del juego-----------------------------------------------------------------------------
while True:
    clock.tick(83)
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            # Nuevo área de clic para el icono en (0, 560) de 40x40
            if 0 <= mouse_pos[0] <= 40 and 560 <= mouse_pos[1] <= 600:
                muted = not muted
                if muted:
                    mixer.music.set_volume(0)
                else:
                    mixer.music.set_volume(0.2)

    frame_actual = (frame_actual + 1) % len(fondo_frames)
    screen.blit(fondo_frames[frame_actual], (0, 0))

    if muted:
        screen.blit(logo_sonidono, (0, 560))
    else:
        screen.blit(logo_sonidosi, (0, 560))

    draw_button("Level", 5, 100, 140, 60, (255, 255, 255), "Michroma", 28,
            5 <= mouse_pos[0] <= 5+140 and 100 <= mouse_pos[1] <= 100+60)
    draw_button("Start", 5, 175, 140, 60, (255, 255, 255), "Michroma", 28,
            5 <= mouse_pos[0] <= 5+140 and 175 <= mouse_pos[1] <= 175+60)
    draw_button("Scores", 5, 250, 140, 60, (255, 255, 255), "Michroma", 28,
            5 <= mouse_pos[0] <= 5+140 and 250 <= mouse_pos[1] <= 250+60)
    draw_button("Exit", 5, 325, 140, 60, (255, 255, 255), "Michroma", 28,
            5 <= mouse_pos[0] <= 5+140 and 325 <= mouse_pos[1] <= 325+60)

    pygame.display.flip()