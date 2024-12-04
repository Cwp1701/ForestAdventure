import pygame
from pygame.locals import *

class Player:
    # TODO: Implement Character Class
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

    def movement(self, player_input):
        if player_input[K_w]:
            self.y -= self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y, self.width, self.height))


def main():

    clock = pygame.time.Clock()

    # Game Rendering
    resolution = (1280, 720)
    screen = pygame.display.set_mode(resolution)
    screen.fill((0, 0, 0))
    pygame.display.flip()
    pygame.init()
    pygame.display.set_caption("Forest Adventure")

    player = Player(resolution[0]//2, resolution[1]//2, 25, 25, 5)

    running = True

    while running:

        screen.fill((255, 125, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # TODO: Player Input
        player_input = pygame.key.get_pressed()

        player.movement(player_input)
        player.draw(screen)

        clock.tick(30)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()