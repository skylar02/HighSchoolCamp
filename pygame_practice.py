"""
title: pygame_practice
author: Skylar
date: 2019-06-14 09:48
"""

import pygame

pygame.init()

size = (400, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("First Pygame")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

# Loop as long as done == False
while not done:

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    PI = 3.141592653

    pygame.draw.circle(screen, GREEN, [200, 100], 50)

    pygame.draw.ellipse(screen, BLACK, [170, 80, 14, 17])
    pygame.draw.ellipse(screen, BLACK, [210, 80, 14, 17])

    pygame.draw.arc(screen, BLACK, [160, 75, 75, 62], PI, 0, 2)
    pygame.draw.arc(screen, BLACK, [160, 75, 75, 62], PI, PI, 2)

    pygame.draw.line(screen, GREEN, [200, 150], [200, 300], 2)
    pygame.draw.line(screen, GREEN, [200, 300], [150, 340], 2)
    pygame.draw.line(screen, GREEN, [200, 300], [250, 340], 2)
    pygame.draw.line(screen, GREEN, [200, 200], [150, 150], 2)
    pygame.draw.line(screen, GREEN, [200, 200], [250, 150], 2)

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()

    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)

# Be IDLE friendly
pygame.quit()
