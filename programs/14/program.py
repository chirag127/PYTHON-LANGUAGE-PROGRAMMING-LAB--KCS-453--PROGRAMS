# To write a python program simulate bouncing ball in Pygame.

import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Bouncing Ball")

x = 30
y = 30
x_speed = 5
y_speed = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 30)
    x += x_speed
    y += y_speed
    if x > screen.get_width() - 30 or x < 0:
        x_speed *= -1
    if y > screen.get_height() - 30 or y < 0:
        y_speed *= -1
    pygame.display.update()
pygame.quit()
quit()
