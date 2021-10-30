import pygame
import os
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 960, 540#half the size of 1080p
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hack-A-Thon")

#defined RGB colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

IMAGE_PATH = os.path.join(os.getcwd(), 'assets\images')#concates working dir with image location

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

#loads image files as objects, will probably be in classes later

#bin = pygame.image.load(os.path.join(IMAGE_PATH, 'bin.png'))
#sorting_table = pygame.image.load(os.path.join(IMAGE_PATH, 'foreground_table.png'))
#aerosol_can = pygame.image.load(os.path.join(IMAGE_PATH, 'aerosol_can.png'))
#alum_soda_can = pygame.image.load(os.path.join(IMAGE_PATH, 'alum_soda_can.png'))
#brown_glass_bottle = pygame.image.load(os.path.join(IMAGE_PATH, 'brown_glass_bottle.png'))
#brown_paper_bag = pygame.image.load(os.path.join(IMAGE_PATH, 'brown_paper_bag.png'))
#cardboard_box = pygame.image.load(os.path.join(IMAGE_PATH, 'cardboard_box.png'))
#dirty_pizza_box = pygame.image.load(os.path.join(IMAGE_PATH, 'dirty_pizza_box.png'))
#glass_bottle = pygame.image.load(os.path.join(IMAGE_PATH, 'glass_bottle.png'))
#glass_jar = pygame.image.load(os.path.join(IMAGE_PATH, 'glass_jar.png'))
#laundry_det_bottle = pygame.image.load(os.path.join(IMAGE_PATH, 'laundry_det_bottle.png'))
#metal_can = pygame.image.load(os.path.join(IMAGE_PATH, 'metal_can.png'))
#newspaper = pygame.image.load(os.path.join(IMAGE_PATH, 'newspaper.png'))
#plastic_gallon_jug = pygame.image.load(os.path.join(IMAGE_PATH, 'plastic_gallon_jug.png'))
#short_metal_can = pygame.image.load(os.path.join(IMAGE_PATH, 'short_metal_can.png'))
#styrofoam_cup = pygame.image.load(os.path.join(IMAGE_PATH, 'styrofoam_cup.png'))
#water_bottle = pygame.image.load(os.path.join(IMAGE_PATH, 'water_bottle.png'))




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
