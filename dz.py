import pygame as pg


pg.init()

screen_width, screen_height = 1280, 720

FPS = 24    # frame per second
clock = pg.time.Clock()

display = pg.display.set_mode((screen_width, screen_height))
display.fill('gray', (0, 0, screen_width, screen_height))

sys_font = pg.font.SysFont('Arial Black', 34)
text_img = sys_font.render('Тимофей', True, 'white')
test = sys_font.render('ЭЫВЦВЦ', True, 'red')
display.blit(text_img, (110, 570))

appear = True
running = True
while running:
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                running = False
            if event.key == pg.K_SPACE or event.key == pg.K_n:
                if appear:
                    appear = False
                    display.fill('gray', (0, 0, screen_width, screen_height))
                else:
                    appear = True
                    display.blit(text_img, (110, 570))


    clock.tick(FPS)
pg.quit()