import pygame as pg


pg.init()

screen_width, screen_height = 800, 600

FPS = 24    # frame per second
clock = pg.time.Clock()

bg_img = pg.image.load('src/dz.png')
icon_img = pg.image.load('src/ufo.png')

display = pg.display.set_mode((screen_width, screen_height))
pg.display.set_icon(icon_img)
pg.display.set_caption('Космическое вторжение')

sys_font = pg.font.SysFont('arial', 34)
font = pg.font.Font('src/04B_19.TTF', 48)
display.blit(bg_img, (0, 0))

text_img = sys_font.render('Score 123', True, 'white')
display.blit(text_img, (100, 50))

game_over_text = font.render('Game Over', True, 'red')
w, h = game_over_text.get_size()
display.blit(game_over_text, (screen_width/2 - w/2, screen_height / 2 - h/2))

player_img = pg.image.load('src/player.png')
player_width, player_height = player_img.get_size()


running = True
while running:
    pg.display.update()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                running = False
            if event.key == pg.K_SPACE:
                display.blit(bg_img, (0, 0))
    clock.tick(FPS)
pg.quit()