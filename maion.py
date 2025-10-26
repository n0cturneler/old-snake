import pygame
import time
import random


pygame.init()
pygame.font.init()

font1 = pygame.font.SysFont('monospace', 30)

length_color = None

move_x = 0
move_y = 0

rand_x = 0
rand_y = 0

snake_length = 5

fruit_pos = { 'x' : 0,
              'y' : 0
               }

length_x = []
length_y = []

move_list_x = []
move_list_y = []

screen_res = { 'x' : 720,
               'y' : 720
               }

snake_pos = { 'x' : 360,
              'y' : 360
              }

snake_size = { 'x' : 20,
               'y' : 20
               }

spawn_fruit = False

screen = pygame.display.set_mode((screen_res['x'], screen_res['y']))
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    while not spawn_fruit:
        rand_x = random.randrange(0, 720, 20)
        rand_y = random.randrange(0, 720, 20)
        if any(a == rand_x and b == rand_y for a, b in zip(length_x, length_y)) == False:
            if rand_x != snake_pos['x'] and rand_y != snake_pos['y']:
                spawn_fruit = True
                fruit_pos['x'] = rand_x
                fruit_pos['y'] = rand_y

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and move_y != 20:
        move_y = -20
        move_x = 0
    if keys[pygame.K_s] and move_y != -20:
        move_y = 20
        move_x = 0
    if keys[pygame.K_a] and move_x != 20:
        move_y = 0
        move_x = -20
    if keys[pygame.K_d] and move_x != -20:
        move_y = 0
        move_x = 20

    screen.fill('black')

    text_surface1 = font1.render(f'Length : {snake_length}', 1, (255,255,0))

    screen.blit(text_surface1, (0, 0))

    snake_pos['x'] += move_x
    snake_pos['y'] += move_y

    if spawn_fruit:
        pygame.draw.rect(screen, 'red', pygame.Rect(fruit_pos['x'], fruit_pos['y'], 20, 20), 6)
    if snake_pos == fruit_pos:
        snake_length += 1
        spawn_fruit = False
    if snake_pos['x'] > screen_res['x'] or snake_pos['x'] < 0 or snake_pos['y'] < 0 or snake_pos['y'] > screen_res['y']:
        running = False

    pygame.draw.rect(screen, 'green', pygame.Rect(snake_pos['x'], snake_pos['y'], 20, 20), 6)

    move_list_x.insert(0, move_x)
    move_list_y.insert(0, move_y)

    for length_num in range(snake_length):
        length_color = 'black'
        sum_x = sum(move_list_x[0:length_num + 1])
        sum_y = sum(move_list_y[0:length_num + 1])
        if length_num % 2 == 0:
            length_color = 'yellow'
        else:
            length_color = 'green'
        pygame.draw.rect(screen, length_color, pygame.Rect(snake_pos['x'] - sum_x, snake_pos['y'] - sum_y, 20, 20), 0)
        length_x.insert(0, (snake_pos['x'] - sum_x))
        length_y.insert(0, (snake_pos['y'] - sum_y))


    if move_x != 0 or move_y != 0:
        if (snake_pos['x'] in length_x) and (snake_pos['y'] in length_y):
            if any(a == snake_pos['x'] and b == snake_pos['y'] for a, b in zip(length_x, length_y)):
                running = False

    del length_x[:]
    del length_y[:]

    try:
        del move_list_x[snake_length]
        del move_list_y[snake_length]
    except IndexError:
        continue

    pygame.display.flip()

    time.sleep(.1)

    clock.tick(60)

time.sleep(1)
pygame.quit()