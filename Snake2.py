import pygame as pg
from random import randrange
import sys

RES = 700
SIZE = 20

x,y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
dirs = {'W': True, 'S': True, 'A': True, 'D': True, }
length = 1
snake = [(x, y)]
dx,dy = 0,0
score = 0
fps = 10

apple = randrange(0,RES, SIZE), randrange(0, RES, SIZE)
while apple in snake:
    apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)


pg.init()
screen = pg.display.set_mode([RES,RES])
clock = pg.time.Clock()

font_score = pg.font.SysFont('Arial', 20, True)
font_end = pg.font.Font('typo_pixel.ttf', 50)
font_retry = pg.font.Font('typo_pixel.ttf', 20)
render_end = font_end.render("GAME OVER", True, pg.Color('orange'), pg.Color('blue'))
render_retry = font_retry.render("PRESS u TO RETRY", True, pg.Color('orange'), pg.Color('blue'))


while True:
    screen.fill(pg.Color('blue'))

    # drawing snake, apple
    [ (pg.draw.rect(screen, pg.Color('white'), (i, j, SIZE-2, SIZE-2))) for i, j in snake ]
    pg.draw.rect(screen, pg.Color('red'), (*apple, SIZE, SIZE) )
    render_score = font_score.render(f'SCORE: {score}', True, pg.Color('orange'))
    screen.blit(render_score, (5,5) )

    pg.display.flip()
    clock.tick(fps)

    # snake movement
    x += dx * SIZE
    y += dy * SIZE
    # moving through the walls
    if x > RES - SIZE:
        x = 0
    if x < 0:
            x = RES
    if y > RES - SIZE:
        y = 0
    if y < 0:
            y = RES
    snake.append((x, y))
    snake = snake[-length:]

    # eating an apple
    if snake[-1] == apple:
        while apple in snake:
            apple = randrange(0,RES, SIZE), randrange(0, RES, SIZE)
        length += 1
        score += 1
        if not score % 5:
            fps += 1

    # game over
    if len(snake) != len(set(snake)):
        over = True
        while over:
            screen.blit(render_end, (RES // 2 - 220, RES // 4))
            screen.blit(render_retry, (RES // 2 - 150, RES // 2))
            pg.display.flip()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
                if event.type == pg.KEYDOWN and event.key == pg.K_u:
                    x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
                    dirs = {'W': True, 'S': True, 'A': True, 'D': True, }
                    length = 1
                    snake = [(x, y)]
                    dx, dy = 0, 0
                    score = 0
                    fps = 10
                    over = False


    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w and dirs['W']:
                dx, dy = 0, -1
                dirs = {'W': True, 'S': False, 'A': True, 'D': True, }
            if event.key == pg.K_s and dirs['S']:
                dx, dy = 0, 1
                dirs = {'W': False, 'S': True, 'A': True, 'D': True, }
            if event.key == pg.K_a and dirs['A']:
                dx, dy = -1, 0
                dirs = {'W': True, 'S': True, 'A': True, 'D': False, }
            if event.key == pg.K_d and dirs['D']:
                dx, dy = 1, 0
                dirs = {'W': True, 'S': True, 'A': False, 'D': True, }
            if event.key == pg.K_UP:
                fps += 20
        if event.type == pg.KEYUP:
            if event.key == pg.K_UP:
                fps -= 20




