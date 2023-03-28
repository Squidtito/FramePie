#This is a kinda bad example for optimization whoops ¯\_(ツ)_/¯
#Still looks cool tho lol

import framepie as fp
import random
import pygame
block = [fp.load_image("blocks/grass.png", True),fp.load_image("blocks/stone.png", True)]
x:int=0
z:int=1
camera_x:int=0
camera_y:int=0
current:int
block_size=50
fp.FPS = 6000
world=[]
premath=[]
update = True
maths:int = 0
while not z==100:
    x=0
    current=0
    while not x==100:
         x+=1
         rand = random.randint(30,80)
         world.append((x,z,random.randint(0,1),random.randint(0,1)))
    z+=1
print(len(world))
fp.set_window_background_color((31,31,51))
fp.set_window_resolution((1280/2,720/2))

def generate_premath(blocksize): #This prevents the game from doing a extra pointless amount of math for the block size/camera
        premath.append(0.47*blocksize)
        premath.append(0.45*blocksize)
        premath.append(0.242*blocksize)
        premath.append(0.26*blocksize)

generate_premath(block_size)

while True:
    maths = 0

    camera_x_old = camera_x
    camera_y_old = camera_y

    speed = fp.to_delta(50)
    if fp.get_input(pygame.K_w):
        if not block_size <= 3:
            block_size-=speed
            premath=[]
            maths+=4
            generate_premath(block_size)
    elif fp.get_input(pygame.K_s):
        block_size+=speed
        premath=[]
        maths+=4
        generate_premath(block_size)


    speed = fp.to_delta(500)
    if fp.get_input(pygame.K_RIGHT):
        camera_x-=speed
    elif fp.get_input(pygame.K_LEFT):
        camera_x+=speed
    if fp.get_input(pygame.K_UP):
        camera_y-=speed
    elif fp.get_input(pygame.K_DOWN):
        camera_y+=speed


    current=0
    drawn=0
    z=0



    fp.update()
    for i in world:
            current+=1
            meth = (
            i[0]*premath[0]+camera_x-premath[1]*
            i[1],
            i[0]*premath[2]+premath[3]*
            i[1]-camera_y+
            i[2]*premath[1])
            
            if meth[0] >= -15 and meth[0] <= 590 and meth[1] >= -15 and meth[1] <= 330:
                    fp.draw_image(block[i[3]],meth,(block_size,block_size))
                    drawn+=1
            maths+=12
            

    fp.set_window_name(str(drawn)+" drawn blocks, " +str(maths)+" math calculations and operations total."+"   FPS: "+str(round(fp.clock.get_fps())))
