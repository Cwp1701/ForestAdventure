import pygame


class Player:
    # TODO: Implement Character Class
    pass

def main():

    pygame.init()
    pygame.display.set_caption("Forest Adventure")

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # TODO: Player Input

        # Game Rendering
        resolution = (1280, 720)
        screen = pygame.display.set_mode(resolution)
        screen.fill((0, 0, 0))
        pygame.display.flip()

if __name__ == "__main__":
    main()