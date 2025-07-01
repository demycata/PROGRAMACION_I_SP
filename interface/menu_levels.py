import pygame as pg
import data.assets as assets

def menu_levels(screen, clock):
    dificult = None
    running = True
    while running:
        screen.blit(assets.background, (0, 0))
        mouse_pos = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                if 300 <= mouse_pos[0] <= 500 and 180 <= mouse_pos[1] <= 240:
                    print("Easy selected")
                    dificult = 1
                    running = False
                if 300 <= mouse_pos[0] <= 500 and 250 <= mouse_pos[1] <= 310:
                    print("Medium selected")
                    dificult = 2
                    running = False
                if 300 <= mouse_pos[0] <= 500 and 320 <= mouse_pos[1] <= 380:
                    print("Hard selected")
                    dificult = 4
                    running = False

        # Hover para cada botón de dificultad
        if 300 <= mouse_pos[0] <= 500 and 180 <= mouse_pos[1] <= 240:
            screen.blit(assets.boton_easy_hover_img, (300, 180))
        else:
            screen.blit(assets.boton_easy_img, (300, 180))

        if 300 <= mouse_pos[0] <= 500 and 250 <= mouse_pos[1] <= 310:
            screen.blit(assets.boton_medium_hover_img, (300, 250))
        else:
            screen.blit(assets.boton_medium_img, (300, 250))

        if 300 <= mouse_pos[0] <= 500 and 320 <= mouse_pos[1] <= 380:
            screen.blit(assets.boton_hard_hover_img, (300, 320))
        else:
            screen.blit(assets.boton_hard_img, (300, 320))

        pg.display.flip()
        clock.tick(60)
    return dificult

