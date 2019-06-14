"""
title: pygame_practice
author: Skylar
date: 2019-06-14 09:48
"""

import pygame


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

PI = 3.141592653
pygame.init()

size = (400, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("First Pygame")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()


x_speed = 0
y_speed = 0

x_cord = 10
y_cord = 10


ball_pos = 0
ball_change = 1


def draw_stick_man(screen, x, y):
    pygame.draw.ellipse(screen, RED, [120 + x, 150 + ball_pos + y, 40, 40])
    pygame.draw.circle(screen, GREEN, [200 + x, 100 + y], 50)

    pygame.draw.ellipse(screen, BLACK, [170 + x, 80 + y, 14, 17])
    pygame.draw.ellipse(screen, BLACK, [210 + x, 80 + y, 14, 17])

    pygame.draw.arc(screen, BLACK, [160 + x, 75 + y, 75, 62], PI, 0, 2)
    pygame.draw.arc(screen, BLACK, [160 + x, 75 + y, 75, 62], PI, PI, 2)

    pygame.draw.line(screen, GREEN, [200 + x, 150 + y], [200 + x, 300 + y], 2)
    pygame.draw.line(screen, GREEN, [200 + x, 300 + y], [150 + x, 340 + y], 2)
    pygame.draw.line(screen, GREEN, [200 + x, 300 + y], [250 + x, 340 + y], 2)
    pygame.draw.line(screen, GREEN, [200 + x, 200 + y], [150 + x, 150 + y], 2)
    pygame.draw.line(screen, GREEN, [200 + x, 200 + y], [250 + x, 150 + y], 2)


# Loop as long as done == False
while not done:
    ball_pos += ball_change

    if ball_pos > 150:
        ball_change -= 1
    elif ball_pos < 20:
        ball_change += 1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x_speed = -3
    if keys[pygame.K_RIGHT]:
        x_speed = 3
    if keys[pygame.K_UP]:
        y_speed = -3
    if keys[pygame.K_DOWN]:
        y_speed = 3

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    x_cord += x_speed
    y_cord += y_speed

    x_speed = 0
    y_speed = 0

    screen.fill(BLACK)

    draw_stick_man(screen, x_cord, y_cord)

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)

# Be IDLE friendly
pygame.quit()
