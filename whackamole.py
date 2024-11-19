import pygame
import random


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        mole_coordinates = [0, 0]
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            screen.fill("light green")
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_coordinates[0], mole_coordinates[1])))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    click_coordinates = event.pos
                    if int(click_coordinates[0] / 32) == int(mole_coordinates[0] / 32) and int(click_coordinates[1] / 32) == int(mole_coordinates[1] / 32):
                        mole_coordinates[0] = random.randrange(0, 20) * 32
                        mole_coordinates[1] = random.randrange(0, 16) * 32
                        screen.blit(mole_image, mole_image.get_rect(topleft=(mole_coordinates[0], mole_coordinates[1])))
            for i in range(16*32):
                pygame.draw.line(screen, "black", (i * 32, 0), (i * 32, 16*32))
            for i in range(20*32):
                pygame.draw.line(screen, "black", (0, i * 32), (20*32, i * 32))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
