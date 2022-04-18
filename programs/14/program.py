# To write a python program simulate bouncing ball in Pygame.

import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Bouncing Ball")
    ball = pygame.image.load("ball.png")
    x = 50
    y = 50
    x_speed = 5
    y_speed = 5
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill((255, 255, 255))
        screen.blit(ball, (x, y))
        x += x_speed
        y += y_speed
        if x > screen.get_width() - ball.get_width() or x < 0:
            x_speed = -x_speed
        if y > screen.get_height() - ball.get_height() or y < 0:
            y_speed = -y_speed
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()