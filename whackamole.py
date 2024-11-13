import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        mole_x = 0
        mole_y = 0
        while running:


            screen.fill("light green")
            for i in range(0, 20):
                pygame.draw.line(screen, "forest green", (32 * i, 0), (32 * i, 512))
            for i in range(0, 16):
                pygame.draw.line(screen, "forest green", (0, 32 * i), (640, i * 32))
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x, mole_y)))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if x // 32 == mole_x // 32 and y // 32 == mole_y // 32:
                        mole_x = random.randrange(0, 21) * 32
                        mole_y = random.randrange(0, 17) * 32
            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
