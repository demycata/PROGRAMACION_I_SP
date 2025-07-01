import pygame
import pygame.mixer as mixer

mixer.init()
#FONDO
background = pygame.image.load("assets\Frame_00_delay-0.05s.png")
background = pygame.transform.scale(background, (820, 600))

cell = pygame.image.load("assets\Greentoken.png")
#VISUAL AGUA
agua = pygame.image.load("assets\Bluetoken.png")
#VISUAL BARCO
ship = pygame.image.load("assets\Redtoken.png")
#BOTON START
boton_start_img = pygame.image.load("assets\Botonplay.png")
boton_start_img = pygame.transform.scale(boton_start_img, (140, 60))
boton_start_hover_img = pygame.image.load("assets\Botonplayanimado.png")
boton_start_hover_img = pygame.transform.scale(boton_start_hover_img, (140, 60))
#BOTON LEVELS
boton_levels_img = pygame.image.load("assets\Botonlevels.png")
boton_levels_img = pygame.transform.scale(boton_levels_img, (140, 60))
boton_levels_hover_img = pygame.image.load("assets\Botonlevelsanimado.png")
boton_levels_hover_img = pygame.transform.scale(boton_levels_hover_img, (140, 60))
#BOTON SCORES
boton_scores_img = pygame.image.load("assets\Botonscores.png")
boton_scores_img = pygame.transform.scale(boton_scores_img, (140, 60))
boton_scores_hover_img = pygame.image.load("assets\Botonscoresanimado.png")
boton_scores_hover_img = pygame.transform.scale(boton_scores_hover_img, (140, 60))
#BOTON EXIT
boton_exit_img = pygame.image.load("assets\Botonexit.png")
boton_exit_img = pygame.transform.scale(boton_exit_img, (140, 60))
boton_exit_hover_img = pygame.image.load("assets\Botonexitanimado.png")
boton_exit_hover_img = pygame.transform.scale(boton_exit_hover_img, (140, 60))

# Botones dificultad
boton_easy_img = pygame.image.load("assets\Botoneasy.png")
boton_easy_img = pygame.transform.scale(boton_easy_img, (200, 60))
boton_easy_hover_img = pygame.image.load("assets\Botoneasyanimado.png")
boton_easy_hover_img = pygame.transform.scale(boton_easy_hover_img, (200, 60))

boton_medium_img = pygame.image.load("assets\Botonmedium.png")
boton_medium_img = pygame.transform.scale(boton_medium_img, (200, 60))
boton_medium_hover_img = pygame.image.load("assets\Botonmediumanimado.png")
boton_medium_hover_img = pygame.transform.scale(boton_medium_hover_img, (200, 60))

boton_hard_img = pygame.image.load("assets\Botonhard.png")
boton_hard_img = pygame.transform.scale(boton_hard_img, (200, 60))
boton_hard_hover_img = pygame.image.load("assets\Botonhardanimado.png")
boton_hard_hover_img = pygame.transform.scale(boton_hard_hover_img, (200, 60))

#
sonido_agua = mixer.Sound("assets\Agua.mp3")
sonido_barco = mixer.Sound("assets\Disparo.mp3")
#ICONO SONIDO
logo_sonidosi = pygame.image.load("assets/sonidosi.png")
logo_sonidosi = pygame.transform.scale(logo_sonidosi, (40, 40))
logo_sonidono = pygame.image.load("assets/sonidono.png")
logo_sonidono = pygame.transform.scale(logo_sonidono, (40, 40))

# Icono
icon = pygame.image.load("assets\icono.png")