import pygame
from pygame.locals import *


# Global resolution constant since it is needed throughout the project
RESOLUTION = (1280, 720)

class Player:
    player_color = (0, 0, 0)
    # TODO: Refactor player class to work better with collision logic
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.speed = speed

    def movement(self, player_input, walls):
        x_movement = 0
        y_movement = 0

        # Handle player Movement using W, A, S, D
        if player_input[K_w]:
            y_movement -= self.speed
        if player_input[K_s]:
            y_movement += self.speed
        if player_input[K_a]:
            x_movement -= self.speed
        if player_input[K_d]:
            x_movement += self.speed

        self.rect.x += x_movement
        self.rect.y += y_movement

        for wall in walls:
            if self.rect.colliderect(wall):
                self.rect.x -= x_movement
                self.rect.y -= y_movement

        # Ensure player stays within the bounds of the game window
        self.rect.x = max(0, min(self.rect.x, RESOLUTION[0] - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, RESOLUTION[1] - self.rect.height))

        # TODO: Check for collision against walls

    def draw(self, surface):
        pygame.draw.rect(surface, self.player_color, self.rect)

class Wall:
    # TODO: Implement Walls with collision
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, surface):
        pygame.draw.rect(surface, (149, 37, 37), self.rect)


def main():

    background_color = (5, 158, 41)

    clock = pygame.time.Clock()

    # Game Rendering
    screen = pygame.display.set_mode(RESOLUTION)
    pygame.display.flip()
    pygame.init()
    pygame.display.set_caption("Forest Adventure")

    player = Player(5, RESOLUTION[1] // 2, 25, 25, 5)

    walls = [
        # Top Left Wall
        Wall(0, 0, 600, 330),
        # Top Right Wall
        Wall(1280 - 600, 0, 600, 330),
        # Bottom Left Wall
        Wall(0, 720 - 300, 600, 300),
        # Bottom Right Wall
        Wall(1280 - 600, 720 - 300, 600, 300)
    ]

    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

        player_input = pygame.key.get_pressed()

        screen.fill(background_color)

        player.movement(player_input, walls)
        player.draw(screen)

        for wall in walls:
            wall.draw(screen)

        clock.tick(30)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()