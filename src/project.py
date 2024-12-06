import pygame
from pygame.locals import *


# Global resolution constant, since it is needed throughout the project.
RESOLUTION = (1280, 720)

class Player:
    player_color = (0, 0, 0)
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.speed = speed

    def movement(self, player_input, walls):
        # Store players x and y movement in order to make changes in case of a collision
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

        # Updates the players collision shape based on above inputs
        self.rect.x += x_movement
        self.rect.y += y_movement

        # Handles collision with game walls
        for wall in walls:
            if self.rect.colliderect(wall):
                self.rect.x -= x_movement
                self.rect.y -= y_movement

        # Ensure player stays within the bounds of the game window
        self.rect.x = max(0, min(self.rect.x, RESOLUTION[0] - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, RESOLUTION[1] - self.rect.height))

    def draw(self, surface):
        pygame.draw.rect(surface, self.player_color, self.rect)

class Wall:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, surface):
        pygame.draw.rect(surface, (88, 15, 15), self.rect)

class TextDisplay:
    def __init__(self, x, y, font_size, color):
        self.x = x
        self.y = y
        self.font = pygame.font.Font(None, font_size)
        self.color = color
        self.text = ""

    def change_text(self, text):
        self.text = text

    def draw(self, surface):
        display_text = self.font.render(self.text, True, self.color)
        surface.blit(display_text, (self.x, self.y))


def main():
    pygame.init()

    background_color = (5, 158, 41)
    location1_color = (112, 42, 42)
    location2_color = (108, 108, 108)
    location3_color = (158, 158, 158)

    clock = pygame.time.Clock()

    # Game Rendering
    screen = pygame.display.set_mode(RESOLUTION)
    pygame.display.flip()

    pygame.display.set_caption("Forest Adventure")

    player = Player(5, RESOLUTION[1] // 2, 25, 25, 5)

    display_text = TextDisplay(font_size=30, color=(255, 255, 255), x=player.x + 20, y=player.y)

    # Location 3 uses a new text display since the first one would result in text being off-screen
    display_text2 = TextDisplay(font_size=30, color=(255, 255, 255), x=player.x + 20, y=player.y)

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

    # Creation of locations that the player interacts with
    location1 = pygame.Rect(600, 0, 80, 20)
    location2 = pygame.Rect(600, 720-20, 80, 20)
    location3 = pygame.Rect(1280-20, 330, 80, 90)

    running = True

    while running:

        # Handles game quitting via ESCAPE
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        player_input = pygame.key.get_pressed()

        screen.fill(background_color)

        # Sets up player movement and drawing
        player.movement(player_input, walls)
        player.draw(screen)

        # Offsets text displayed based off of player
        display_text.x = player.rect.x + 25
        display_text.y = player.rect.y

        display_text2.x = display_text.x - 750
        display_text2.y = display_text.y

        # Draw the walls seen in the level
        for wall in walls:
            wall.draw(screen)

        # Draws the locations created above
        pygame.draw.rect(screen, location1_color, location1)
        pygame.draw.rect(screen, location2_color, location2)
        pygame.draw.rect(screen, location3_color, location3)

        # Handles displaying, or not displaying text based on what the player is colliding with
        if player.rect.colliderect(location1):
            display_text.text = "Looks like an old decrepit cabin, nothing interesting this way..."
        elif player.rect.colliderect(location2):
            display_text.text = "I can't go this way, the path is blocked by large boulders "
        elif player.rect.colliderect(location3):
            display_text2.text = "Finally! A way through (You've found the way through, press Esc to quit!)"
        else:
            display_text.text = ""

        display_text.draw(screen)
        display_text2.draw(screen)

        clock.tick(30)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()