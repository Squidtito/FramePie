import pygame
import functools
screen = 0
clock = pygame.time.Clock()
background_color = (0,0,0)
#Values you can change easily
FPS = 60


pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('FramePie')
dt = clock
w, h = pygame.display.get_surface().get_size()

icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)


def set_window_resolution(res=(800,600)):
    w, h = res[0], res[1]
    screen = pygame.display.set_mode((w, h))


#Reset the screen!
def update(clear_screen=True):
    pygame.display.update()
    if clear_screen==True:
        pygame.draw.rect(screen,background_color,(0,0,20000,20000))
    dt = clock.tick(FPS) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    #print(clock.get_fps())

def set_window_background_color(color=(0,0,0)):
    background_color = color

def set_window_name(name="FramePie"):
    if not type(name) == str:
        print('------name from "set_window_name (value 1) is not a string')
        quit()
    pygame.display.set_caption(name)


def draw_polygon(poly=[(0,0),(10,20),(20,0)],colors=(100,0,0),offsets=(0,0),outline_width=0):
    pygame.draw.polygon(screen,colors,poly+offsets,outline_width)


#Draw the rect
def draw_rect(Width_And_Length=(100,100),position=(0,0),color=(100,0,0),type=0):
    #Checking for errors
    if not len(color)==3:
        print('------Color (value 3) in "draw_rect" must have 3 values exactly')
        quit()
    elif not len(position)==2:
        print('------Position (value 2) in "draw_rect" must have 2 values exactly')
        quit()
    elif not len(Width_And_Length)==2:
        print('------Width_And_Length (value 1) in "draw_rect" must have 2 values exactly')
        quit()


    pygame.draw.rect(screen, (color), pygame.Rect(position[0], position[1], Width_And_Length[0], Width_And_Length[1]),type)


@functools.lru_cache(maxsize=512)
def get_draw_image(image, transform=None, flip=(False, False)):
    if transform is not None:
        image = pygame.transform.scale(image, transform)
    return pygame.transform.flip(image, *flip)

def draw_surface(surface,position=(0,0),main_surface=screen):
    pygame.Surface.blit(main_surface,surface,position)

def draw_image(image, position=(0,0),transform=None,flip=(False,False),surface=screen):
    image = get_draw_image(image, transform, flip)
    surface.blit(image, position)

def get_input(input):
    keys = pygame.key.get_pressed() 
    if keys[input]: 
        return True

#SHOULD NOT BE USED, NOT WORKING CORRECTLY
def to_delta(number):
    return number*dt.get_fps()

def load_image(image='icon.png', transparent=True):
    if transparent == True:
        return pygame.image.load(image)
    else:
        return pygame.image.load(image).convert()
def get_mouse_position():
    pygame.sprite
    return pygame.mouse.get_pos()
def get_index(Array:list,index:int):
    if index >= Array.__len__() or index <=-1:
        return None
    else:
        return Array[index]
