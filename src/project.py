import pygame
from pygame.locals import *



resolution = (1280, 720)

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
        if player_input[K_s]:
            self.y += self.speed
        if player_input[K_a]:
            self.x -= self.speed
        if player_input[K_d]:
            self.x += self.speed

        self.x = max(0, min(self.x, resolution[0]//2 - self.width))
        self.y = max(0, min(self.y, resolution[1]//2 - self.height))

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 0, 0), (self.x, self.y, self.width, self.height))

class Wall:
    def __init__(self):
        pass
# TODO: Implement Walls with collision

def main():

    background_color = (5, 158, 41)

    clock = pygame.time.Clock()

    # Game Rendering
    screen = pygame.display.set_mode(resolution)
    pygame.display.flip()
    pygame.init()
    pygame.display.set_caption("Forest Adventure")

    player = Player(5, resolution[1]//2, 25, 25, 5)

    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # TODO: Player Input
        player_input = pygame.key.get_pressed()

        screen.fill(background_color)

        player.movement(player_input)
        player.draw(screen)

        clock.tick(30)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()