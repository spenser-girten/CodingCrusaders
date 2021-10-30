import pygame
import os
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hack-A-Thon")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

FPS = 60

def generateGarbages(x):
    x = x

def traggleGarbageToBin(x):
    x = x

def draw_window():
    pygame.draw.rect(WIN, BLACK, BORDER)
    pygame.display.update()

def draw_notes(note, posX, posY):
    draw_note = WINNER_FONT.render(note, 1, WHITE)
    WIN.blit(draw_note, (posX, posY))
    pygame.display.update()
    pygame.time.delay(5000)


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)

        # Event handlers
        for event in pygame.event.get():
            #Fetch the key pressed
            keys_pressed = pygame.key.get_pressed()

            # Handle quit event
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            # Handle mouse lick
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                #Fetch mouse position
                pos = pygame.mouse.get_pos()
                x = pos[0]
                y = pos[1]

                # Mouse middle key clicked
                if event.button == 3:
                    x = x

                # Mouse left key clicked
                if event.button == 2:
                    x = x

                # Mouse right key clicked
                if event.button == 1:
                    x = x

                # Trigger custom functions
                draw_notes("Sample Note", x, y)    
        
        #Trigger general handing fucntions
        draw_window()

    main()


if __name__ == "__main__":
    main()
