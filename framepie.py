import pygame
import functools
import os

# Check if being run internally
if __name__ == '__main__':
    raise ValueError("Do not run this directly please.")

# Initialize Pygame
pygame.init()

# Set initial values
screen = 0
clock = pygame.time.Clock()
background_color = (0, 0, 0)
dt = 0

# Values you can change easily
FPS = 60

# Set up the screen
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('FramePie')

# Get the window size
w, h = pygame.display.get_surface().get_size()

# Set the window icon
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# Set the window resolution
def set_window_resolution(res=(800, 600)):
    global screen, w, h
    w, h = res[0], res[1]
    screen = pygame.display.set_mode((w, h))

# Update the screen
def update(clear_screen=True):
    global dt
    pygame.display.flip()
    if clear_screen:
        pygame.draw.rect(screen, background_color, (0, 0, 20000, 20000))

    dt = clock.tick_busy_loop(FPS) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit("Application terminated by user")

# Set the window background color
def set_window_background_color(color=(0, 0, 0)):
    global background_color
    if len(color) != 3:
        raise ValueError('Color (value 3) in "set_window_background_color" must have 3 values exactly')
    background_color = color

# Set the window name
def set_window_name(name="FramePie"):
    if not isinstance(name, str):
        raise TypeError('name in "set_window_name (value 1)" is not a string')
    pygame.display.set_caption(name)

# Draw a polygon
def draw_polygon(poly=[(0, 0), (10, 20), (20, 0)], colors=(100, 0, 0), offsets=(0, 0), outline_width=0):
    pygame.draw.polygon(screen, colors, poly+offsets, outline_width)

# Draw a rectangle
def draw_rect(size=(100, 100), position=(0, 0), color=(100, 0, 0), type=0):
    # Check for errors
    if len(color) != 3:
        raise ValueError('Color (value 3) in "draw_rect" must have 3 values exactly')
    elif len(position) != 2:
        raise ValueError('Position (value 2) in "draw_rect" must have 2 values exactly')
    elif len(size) != 2:
        raise ValueError('Size (value 1) in "draw_rect" must have 2 values exactly')
    pygame.draw.rect(screen, color, pygame.Rect(position[0], position[1], size[0], size[1]), type)

# Get a draw image
@functools.lru_cache(maxsize=512)
def transform_image(image, transform=None, flip=(False, False)):
    if transform:
        image = pygame.transform.scale(image, transform)
    return pygame.transform.flip(image, *flip)

# Draw a surface
def draw_surface(surface, position=(0, 0), main_surface=screen):
    pygame.Surface.blit(main_surface, surface, position)

# Draw an image
def draw_image(image, position=(0,0),transform=None,flip=(False,False),surface=screen):
    image = transform_image(image, transform, flip)
    surface.blit(image, position)

# Get some input
def get_input(input):
    keys = pygame.key.get_pressed() 
    if keys[input]: 
        return True

def to_delta(number):
    return number * dt

def load_image(path_to_file='icon.png', transparent=True):
    if not os.path.exists(path_to_file):
        raise FileNotFoundError('The requested file location "'+path_to_file+'" was not found in active directory "'+os.getcwd()+'"')

    surface = pygame.image.load(path_to_file)
    if transparent == True:
        return surface
    else:
        return surface.convert_alpha()

def get_mouse_position():
    return pygame.mouse.get_pos()

def get_index(Array:list,index:int):
    if index >= Array.__len__() or index <=-1:
        return None
    else:
        return Array[index]
