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
BIN_WIDTH, BIN_HEIGHT = 55, 40
TABLE_WIDTH, TABLE_HEIGHT = 478, 237
MAX_GARBAGE = 5
TABLE_LOCATIONX = (WIDTH - TABLE_WIDTH) // 2
TABLE_LOCATIONY = HEIGHT - (TABLE_HEIGHT + 10)

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)
RECYCLING_TYPE = ["plastic", "paper", "glass", "metal", "NA"]#NA placeholder for future types i.e. hazmat

BIN_COLLECTION = []
for i in RECYCLING_TYPE:
    bin = {
        "bin_name": ("recycle_bin_" + str(RECYCLING_TYPE.index(i))), 
        "bin_image": "bin.png"}
    BIN_COLLECTION.append(bin)
trash = {
    "bin_name": "trash_bin", 
    "bin_image": "bin.png"}
BIN_COLLECTION.append(trash)

GARBAGE_COLLECTION = [
    {
        "item_name": "plastic_gallon_jug",
        "item_type": "plastic",
        "item_image": "plastic_gallon_jug.png"
    },
    {
        "item_name": "water_bottle",
        "item_type": "plastic",
        "item_image": "water_bottle.png"
    },
    {
        "item_name": "laundry_det_bottle",
        "item_type": "plastic",
        "item_image": "laundry_det_bottle.png"
    },
    {
        "item_name": "carboard_box",
        "item_type": "paper",
        "item_image": "cardboard_box.png"
    },
    {
        "item_name": "newspaper",
        "item_type": "paper",
        "item_image": "newspaper.png"
    },
    {
        "item_name": "brown_paper_bag",
        "item_type": "paper",
        "item_image": "brown_paper_bag.png"
    },
    {
        "item_name": "green_glass_bottle",
        "item_type": "glass",
        "item_image": "green_glass_bottle.png"
    },
    {
        "item_name": "brown_glass_bottle",
        "item_type": "glass",
        "item_image": "brown_glass_bottle.png"
    },
    {
        "item_name": "glass_jar",
        "item_type": "glass",
        "item_image": "glass_jar.png"
    },
    {
        "item_name": "alum_soda_can",
        "item_type": "metal",
        "item_image": "alum_soda_can.png"
    },
    {
        "item_name": "short_metal_can",
        "item_type": "metal",
        "item_image": "short_metal_can.png"
    },
    {
        "item_name": "metal_can.png",
        "item_type": "metal",
        "item_image": "metal_can.png"
    },  
    {
        "item_name": "aerosol_can",
        "item_type": "NA",
        "item_image": "aerosol_can.png"
    },
    {
        "item_name": "dirty_pizza_box",
        "item_type": "NA",
        "item_image": "dirty_pizza_box.png"
    },
    # {
    #     "item_name": "dirty_pizza_box",
    #     "item_type": "NA",
    #     "item_image": "dirty_pizza_box.png"
    # }
]

SCENE_COLLECTION = [
    {
        "item_name": "foreground_table",
        "item_image": "foreground_table.png",
        "location_x": TABLE_LOCATIONX,
        "location_y": TABLE_LOCATIONY
    },
#    {
#        "item_name": "wall",
#        "item_image": ""
#    },
#    {
#        "item_name": "floor",
#        "item_image": ""
#    }
]



FPS = 60
#bar hovering on the top of the screen
def temperatureBar():
    pygame.draw.rect(surface, (255,255,255), pygame.Rect(10,10,940,10),1)

#not completed bin drop detection
def binDrop():
    if garbage.rect.colliderect(binrect, garbagerect):
        x = 0
      #delete garbage sprite
        #check bin type and garbage type
        #increase temp bar if mismatched types

def drag():
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        x = pos[0]
        y = pos[1]
        if event.button == 1:
            for garbage in garbages:
                if garbage.rect.collidepoint(pos):
                    garbage.clicked == True
    if event.type == pygame.MOUSEBUTTONUP:
        garbage.clicked = False

def garbageClicked():
    for garbage in garbages:
        if garbage.clicked == True:
            pos = pygame.mouse.get_pos()
            garbage.rect.x = pos[0] - (garbage.rect.width/2)
            garbage.rect.y = pos[1] - (garbage.rect.width/2)

def generateGarbages():
    garbages = []
    offsetBetweenGarbageItems = 30
    randomGarbages = random.sample(GARBAGE_COLLECTION, MAX_GARBAGE)
    for garbage in randomGarbages:
        locationX = TABLE_LOCATIONX + 40 + (GARBAGE_WIDTH + offsetBetweenGarbageItems) * len(garbages)
        locationY = TABLE_LOCATIONY + 50
        garbage['item'] = pygame.Rect(locationX, locationY, GARBAGE_WIDTH, GARABGE_HEIGHT)
        garbages.append(garbage)
        print(garbage['item_name'])

    return garbages

def generateBins():
    bins = []
    offsetBetweenBins = 250
    for bin in BIN_COLLECTION:
        locationX = WIDTH // 2 - 200 + (BIN_WIDTH + offsetBetweenBins) * len(bins)
        locationY = 10 + BIN_HEIGHT
        bin['bin'] = pygame.Rect(locationX, locationY, BIN_WIDTH, BIN_HEIGHT)
        bins.append(bin)

    return bins

def draw_window(current_garbages, bins):
    pygame.draw.rect(WIN, BLACK, BORDER)

    for scene in SCENE_COLLECTION:
        image = pygame.image.load(os.path.join(IMAGE_PATH, scene['item_image']))
        WIN.blit(image, (scene['location_x'], scene['location_y']))

    for garbage in current_garbages:
        image = pygame.image.load(os.path.join(IMAGE_PATH, garbage['item_image']))
        pygame.transform.scale(image, (GARBAGE_WIDTH, GARABGE_HEIGHT))
        WIN.blit(image, (garbage['item'].x, garbage['item'].y))

    for bin in bins:
        image = pygame.image.load(os.path.join(IMAGE_PATH, bin['bin_image']))
        pygame.transform.scale(image, (BIN_WIDTH, BIN_HEIGHT))
        WIN.blit(image, (bin['bin'].x, bin['bin'].y))

    pygame.display.update()

def draw_notes(note, posX, posY):
    draw_note = WINNER_FONT.render(note, 1, WHITE)
    WIN.blit(draw_note, (posX, posY))
    pygame.display.update()
    pygame.time.delay(5000)


def main():
    clock = pygame.time.Clock()
    run = True
    current_garbages = []
    bins = []
    while run:
        clock.tick(FPS)

        if not current_garbages:
            current_garbages = generateGarbages()
        
        if not bins:
            bins = generateBins()

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
        draw_window(current_garbages, bins)

    main()


if __name__ == "__main__":
    main()
