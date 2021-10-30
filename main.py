import pygame
import os
import random

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

GARBAGE_WIDTH, GARABGE_HEIGHT = 55, 40
MAX_GARBAGE = 5

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

RECYCLING_TYPE = ["plastic", "paper", "glass"]
GARBAGE_COLLECTION = [
    {
        "item_name": "water_bottle",
        "item_type": "plastic",
        "item_image": ""
    },
    {
        "item_name": "milk_jug",
        "item_type": "plastic",
        "item_image": ""
    },
    {
        "item_name": "laundry_soap_bottle",
        "item_type": "plastic",
        "item_image": ""
    },
    {
        "item_name": "carboard_box",
        "item_type": "paper",
        "item_image": ""
    },
    {
        "item_name": "newspaper",
        "item_type": "paper",
        "item_image": ""
    },
    {
        "item_name": "brown_bag",
        "item_type": "paper",
        "item_image": ""
    },
    {
        "item_name": "soda_bottle",
        "item_type": "glass",
        "item_image": ""
    },
    {
        "item_name": "beer_bottle",
        "item_type": "glass",
        "item_image": ""
    },
    {
        "item_name": "soda_can",
        "item_type": "metal",
        "item_image": ""
    }
]

FPS = 60

def generateGarbages():
    garbages = []
    offsetBetweenGarbageItems = 30
    while(len(garbages) < MAX_GARBAGE):
        locationX = 10 + (GARBAGE_WIDTH + offsetBetweenGarbageItems) * len(garbages)
        locationY = 10 + GARABGE_HEIGHT
        garbage = random.choice(GARBAGE_COLLECTION)
        garbage['item'] = pygame.Rect(locationX, locationY, GARBAGE_WIDTH, GARABGE_HEIGHT)
        garbages.append(garbage)

    return garbages

def traggleGarbageToBin(x):
    x = x

def draw_window(current_garbages):
    pygame.draw.rect(WIN, BLACK, BORDER)

    for garbage in current_garbages:
        image = pygame.image.load(os.path.join(IMAGE_PATH, garbage['item_image']))
        WIN.blit(image, (garbage['item'].x, garbage['item'].y))

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
    current_garbages = []
    while run:
        clock.tick(FPS)

        if not current_garbages:
            current_garbages = generateGarbages()

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
        
        #Trigger general handing fucntions
        draw_window(current_garbages)

    main()


if __name__ == "__main__":
    main()
