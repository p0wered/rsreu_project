import pygame as pg
import random

pg.init()

screen_width, screen_height = 800, 600

FPS = 60
clock = pg.time.Clock()

bg_img = pg.image.load('src/background.png')
icon_img = pg.image.load('src/ufo.png')

display = pg.display.set_mode((screen_width, screen_height))
pg.display.set_icon(icon_img)
pg.display.set_caption('Космическое вторжение')

sys_font = pg.font.SysFont('arial', 34)
font = pg.font.Font('src/04B_19.TTF', 48)
display.blit(bg_img, (0, 0))

game_over_text = font.render('Game Over', True, 'red')
w, h = game_over_text.get_size()
align_center = screen_width / 2 - w / 2, screen_height / 2 - h / 2
game_over = False

player_img = pg.image.load('src/player.png')
player_width, player_height = player_img.get_size()
player_gap = 10
player_velocity = 10
player_dx = 0
player_x = screen_width / 2 - player_width / 2
player_y = screen_height - player_height - player_gap

bullet_img = pg.image.load('src/projectile.png')
bullet_width, bullet_height = bullet_img.get_size()
bullet_dy = -10
bullet_x = 0
bullet_y = 0
bullet_alive = False

enemy_img = pg.image.load('src/enemy.png')
enemy_width, enemy_height = enemy_img.get_size()
enemy_dx = 0
enemy_dy = 2
enemy_x = 0
enemy_y = 0


def enemy_create():
    global enemy_y, enemy_x
    enemy_x = random.randint(0, screen_width - enemy_width)
    enemy_y = 0
    print(f'CREATE: {enemy_x=}')


def model_update():
    player_model()
    bullet_model()
    enemy_model()


def player_model():
    global player_x, game_over
    player_x += player_dx
    if player_x < 0:
        player_x = 0
    elif player_x > screen_width - player_width:
        player_x = screen_width - player_width


def bullet_model():
    global bullet_y, bullet_alive
    bullet_y += bullet_dy
    if bullet_y < 0:
        bullet_alive = False


def bullet_create():
    global bullet_y, bullet_x, bullet_alive
    bullet_alive = True
    bullet_x = player_x + bullet_width / 2
    bullet_y = player_y - bullet_height


def enemy_model():
    global enemy_y, enemy_x, bullet_alive, enemy_alive, game_over
    enemy_x += enemy_dx
    enemy_y += enemy_dy
    if not game_over:
        re = pg.Rect(enemy_x, enemy_y, enemy_width, enemy_height)
        rb = pg.Rect(bullet_x, bullet_y, bullet_width, bullet_height)
        rp = pg.Rect(player_x, player_y, player_width, player_height)
        is_touched = rp.colliderect(re)
        if enemy_y > screen_height:
            enemy_create()
        if bullet_alive:
            is_crossed = re.colliderect(rb)
            if is_crossed:
                print('BANG!')
                enemy_create()
                bullet_alive = False
        if is_touched:
            game_over = True


def display_redraw():
    if not game_over:
        display.blit(bg_img, (0, 0))
        display.blit(player_img, (player_x, player_y))
        display.blit(enemy_img, (enemy_x, enemy_y))
        if bullet_alive:
            display.blit(bullet_img, (bullet_x, bullet_y))
    else:
        display.blit(game_over_text, align_center)
    pg.display.update()


def event_processing():
    global player_dx, game_over
    running = True
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_a or event.key == pg.K_LEFT:
                player_dx = -player_velocity
            if event.key == pg.K_d or event.key == pg.K_RIGHT:
                player_dx = player_velocity
        if event.type == pg.KEYUP:
            player_dx = 0

        if event.type == pg.MOUSEBUTTONDOWN:
            key = pg.mouse.get_pressed()
            print(f'{key[0]=} {bullet_alive=}')
            if not bullet_alive:
                bullet_create()

    clock.tick(FPS)
    return running


enemy_create()
running = True
while running:
    model_update()
    display_redraw()
    running = event_processing()

pg.quit()
